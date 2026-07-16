"""
ces_gdp_loss.py
───────────────────────────────────────────────────────────────────────────────
Endogenous GDP loss per commodity from the ToyModelSOEMC CES production function.

MECHANISM (five steps):
  1. Gross shortfall   = m * ED_c_bar               (m = fraction of annual supply)
  2. Reserve draw      = min(phi_R * gross, R_bar)   (drawdown policy rule)
  3. Net shortfall     = gross − draw                (residual after reserves)
  4. E_crisis          = E_ss − net_shortfall        (total CES energy input)
  5. GDP loss%         = (1 − Y_crisis / Y_ss) × 100 (CES output loss)

CES production:
  Y = A × (α_K × K^ρ + α_L × L^ρ + α_E × E^ρ)^(1/ρ)
  ρ = (η−1)/η = 1/3  (η = 1.5, elasticity of substitution between K, L, E)

Capital fixed at K_ss (short-run: capital cannot be reallocated during a crisis).
Labour fixed at Lbar (exogenous endowment).

STANDALONE USAGE:
  from ces_gdp_loss import CESModel, add_model_columns, model_section_md
  m = CESModel()
  r = m.compute_avoided_loss('oil', shock_fraction=0.20, rbar_days=30)
  print(r)

OPTIONAL MATLAB CSV INPUT:
  If toy_model_gdp_loss.csv exists in the same directory this module will
  read it and use those values; otherwise computes analytically.

All hardcoded defaults are taken directly from ToyModelSOEMC.mod.
───────────────────────────────────────────────────────────────────────────────
"""

from __future__ import annotations
import csv
import math
from pathlib import Path
from typing import Optional

# ── ToyModelSOEMC.mod calibration parameters ─────────────────────────────────
_ALPHA_K     = 0.38
_ALPHA_L     = 0.47
_ALPHA_E     = 0.15
_ETA         = 1.5
_RHO         = (_ETA - 1) / _ETA   # = 1/3
_BETA        = 0.95
_DELTA_K     = 0.065
_LBAR        = 10.0
_EC_BAR      = 0.25          # clean energy (exogenous, unaffected by disruptions)
_ED_OIL_BAR  = 0.30          # annual dirty energy from oil/products (model units)
_ED_COAL_BAR = 0.45          # annual dirty energy from coal (model units)
_PHI_R       = 0.5           # reserve drawdown fraction (policy rule parameter)
_A_TFP       = 1.0           # TFP normalised to 1 by calibration

# Approximations for LNG and LPG (not separately modelled in ToyModelSOEMC)
# LNG competes with coal for power generation; proxy = ~8% of total dirty energy
# LPG is a small refined-products fraction; proxy = ~1.3% of dirty energy
_ED_LNG_PROXY = 0.06
_ED_LPG_PROXY = 0.01

# Steady-state total energy (= 1.0 by construction)
_E_SS = _ED_OIL_BAR + _ED_COAL_BAR + _EC_BAR

# ── Benchmark shock scenarios ──────────────────────────────────────────────
# Consistent with ToyModelSOEMC crisis calibration: e_c_shock ~ U(0.20,0.50)×ED_c
SHOCK_MOD = 0.20   # moderate: 20% of annual supply disrupted
SHOCK_SEV = 0.50   # severe:   50% of annual supply disrupted


def _bisect(f, a: float, b: float, tol: float = 1e-12, maxiter: int = 300) -> float:
    """Bisection root-finder; no external dependencies required."""
    fa = f(a)
    for _ in range(maxiter):
        m = (a + b) / 2
        if (b - a) < tol:
            break
        fm = f(m)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return (a + b) / 2


class CESModel:
    """
    Wraps the ToyModelSOEMC CES production function for GDP loss calculations.

    Parameters can be overridden at construction to test sensitivity:
        m = CESModel(alpha_E=0.12)   # re-run with lower energy share
    """

    def __init__(
        self,
        alpha_K:     float = _ALPHA_K,
        alpha_L:     float = _ALPHA_L,
        alpha_E:     float = _ALPHA_E,
        eta:         float = _ETA,
        beta:        float = _BETA,
        delta_K:     float = _DELTA_K,
        lbar:        float = _LBAR,
        ec_bar:      float = _EC_BAR,
        ed_oil_bar:  float = _ED_OIL_BAR,
        ed_coal_bar: float = _ED_COAL_BAR,
        phi_r:       float = _PHI_R,
        a_tfp:       float = _A_TFP,
    ):
        self.alpha_K     = alpha_K
        self.alpha_L     = alpha_L
        self.alpha_E     = alpha_E
        self.rho         = (eta - 1) / eta
        self.beta        = beta
        self.delta_K     = delta_K
        self.lbar        = lbar
        self.ec_bar      = ec_bar
        self.ed_oil_bar  = ed_oil_bar
        self.ed_coal_bar = ed_coal_bar
        self.phi_r       = phi_r
        self.a_tfp       = a_tfp

        self.e_ss: float = ed_oil_bar + ed_coal_bar + ec_bar
        self.r_ss: float = 1 / beta - 1 + delta_K

        # Solve for K_ss and pre-compute Y_ss
        self.K_ss: float = self._solve_K_ss()
        self._sum_ss     = self._ces_sum(self.K_ss, self.e_ss)
        self.Y_ss: float = self.a_tfp * self._sum_ss ** (1 / self.rho)

        # Energy revenue share at SS (for linearisation check)
        self.s_E: float  = (
            self.alpha_E * self.e_ss**self.rho / self._sum_ss
        )

    # ── CES building blocks ───────────────────────────────────────────────────

    def _ces_sum(self, K: float, E: float) -> float:
        return (
            self.alpha_K * K**self.rho
            + self.alpha_L * self.lbar**self.rho
            + self.alpha_E * E**self.rho
        )

    def _solve_K_ss(self) -> float:
        """Bisection on capital Euler: MPK(K) = r_ss."""
        def foc(K: float) -> float:
            s = self._ces_sum(K, self.e_ss)
            mpk = (
                self.alpha_K
                * self.a_tfp
                * K ** (self.rho - 1)
                * s ** (1 / self.rho - 1)
            )
            return mpk - self.r_ss

        return _bisect(foc, 1e-4, 1e4)

    def gdp_loss_pct(self, E_crisis: float) -> float:
        """
        GDP loss (% of Y_ss) when total energy input is E_crisis.
        K and L are held at steady-state values (short-run fixed factors).
        """
        E_c   = max(E_crisis, 0.0)
        sum_c = self._ces_sum(self.K_ss, E_c)
        Y_c   = self.a_tfp * sum_c ** (1 / self.rho)
        return max(0.0, (1 - Y_c / self.Y_ss) * 100)

    def gdp_loss_linear(self, dE: float) -> float:
        """First-order (linearised) GDP loss for small energy shortfall dE."""
        return self.s_E * (dE / self.e_ss) * 100

    # ── Main computation ──────────────────────────────────────────────────────

    def compute_avoided_loss(
        self,
        ed_bar:         float,
        shock_fraction: float,
        rbar_days:      float,
        phi_r:          Optional[float] = None,
    ) -> dict:
        """
        Compute GDP loss WITH and WITHOUT a reserve for one (shock, reserve) pair.

        Parameters
        ----------
        ed_bar          Annual supply of the disrupted commodity in CES model units.
                        Use self.ed_oil_bar, self.ed_coal_bar, or a proxy.
        shock_fraction  Fraction of annual supply disrupted  ∈ [0, 1].
        rbar_days       Reserve size expressed as days of daily-supply coverage.
        phi_r           Drawdown fraction (defaults to self.phi_r = 0.5).

        Returns
        -------
        dict with keys:
          shock_units     gross shortfall in model energy units
          rbar_units      reserve stock in model energy units
          draw            reserve actually drawn
          residual_no_r   net shortfall without reserve
          residual_with_r net shortfall with reserve
          loss_no_r       GDP loss% without reserve
          loss_with_r     GDP loss% with reserve
          avoided_loss    difference (what the reserve "buys")
        """
        if phi_r is None:
            phi_r = self.phi_r

        shock_u = shock_fraction * ed_bar
        rbar_u  = (rbar_days / 365.0) * ed_bar

        resid_no_r   = shock_u
        draw         = min(phi_r * shock_u, rbar_u)
        resid_with_r = shock_u - draw

        loss_no_r   = self.gdp_loss_pct(self.e_ss - resid_no_r)
        loss_with_r = self.gdp_loss_pct(self.e_ss - resid_with_r)

        return {
            "shock_units":       shock_u,
            "rbar_units":        rbar_u,
            "draw":              draw,
            "residual_no_r":     resid_no_r,
            "residual_with_r":   resid_with_r,
            "loss_no_r":         loss_no_r,
            "loss_with_r":       loss_with_r,
            "avoided_loss":      loss_no_r - loss_with_r,
        }

    def print_summary(self) -> None:
        """Print ToyModel steady-state diagnostics."""
        print(f"\nToyModelSOEMC CES -- Steady State")
        print(f"  Parameters:  a_K={self.alpha_K}  a_L={self.alpha_L}  a_E={self.alpha_E}")
        print(f"               rho={self.rho:.4f}  beta={self.beta}  delta={self.delta_K}")
        print(f"  Solved K_ss: {self.K_ss:.4f}")
        print(f"  Y_ss:        {self.Y_ss:.4f}  (normalised; A=1)")
        print(f"  E_ss:        {self.e_ss:.4f}  (oil={self.ed_oil_bar} coal={self.ed_coal_bar} clean={self.ec_bar})")
        print(f"  r_ss:        {self.r_ss:.4f}")
        print(f"  s_E:         {self.s_E:.4f}  (energy revenue share at SS)")
        print(f"  Linearised:  1% energy disruption ~= {self.s_E:.4f}% GDP loss\n")


# ── Carrier → ED parameter mapping ───────────────────────────────────────────

def _ed_for_carrier(carrier_label: str, model: CESModel) -> Optional[float]:
    """
    Map a carrier label from compute_reserve_breakeven.py to a CES ED parameter.
    Returns None for carriers that cannot be mapped (PSHP, BESS).
    """
    lbl = carrier_label.lower()
    if lbl.startswith("crude oil") or lbl.startswith("ref. products"):
        return model.ed_oil_bar
    if lbl.startswith("coal"):
        return model.ed_coal_bar
    if lbl.startswith("lng"):
        return _ED_LNG_PROXY
    if lbl.startswith("lpg"):
        return _ED_LPG_PROXY
    return None


def _carrier_note(carrier_label: str) -> str:
    lbl = carrier_label.lower()
    if lbl.startswith("lng"):
        return "(LNG proxy: approx. as small coal-type, ED=0.06)"
    if lbl.startswith("lpg"):
        return "(LPG proxy: refined-products fraction, ED=0.01)"
    return ""


# ── Optional: read MATLAB-generated CSV for cross-validation ─────────────────

def _load_matlab_csv(path: Path) -> Optional[dict]:
    """
    Load toy_model_gdp_loss.csv written by toy_model_gdp_loss.m.
    Returns nested dict: [commodity][shock_frac][rbar_days] -> avoided_loss_pct
    """
    if not path.exists():
        return None
    try:
        data: dict = {}
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                c   = row["commodity"]
                s   = round(float(row["shock_frac"]), 4)
                d   = int(row["rbar_days"])
                av  = float(row["avoided_loss_pct"])
                data.setdefault(c, {}).setdefault(s, {})[d] = av
        return data
    except Exception as exc:
        print(f"[WARN] ces_gdp_loss: could not read MATLAB CSV ({exc})")
        return None


# ── Main entry point for compute_reserve_breakeven.py ────────────────────────

def add_model_columns(rows: list[dict], script_dir: Optional[Path] = None) -> None:
    """
    Augment each row dict in-place with CES GDP loss model columns.

    New keys added to each row:
      model_ed           : ED_bar used in CES (model units), or None
      model_avoid_mod    : avoided GDP loss% at SHOCK_MOD (20% annual supply)
      model_avoid_sev    : avoided GDP loss% at SHOCK_SEV (50% annual supply)
      model_status_mod   : 'justified' / 'marginal' / 'not justified' (20% shock)
      model_status_sev   : same for 50% shock
      model_note         : caveat string (e.g. for LNG proxy)
    """
    model = CESModel()

    # Optionally load MATLAB CSV for cross-check (uses Python calc if absent)
    matlab_data = None
    if script_dir is not None:
        matlab_data = _load_matlab_csv(script_dir / "toy_model_gdp_loss.csv")

    for row in rows:
        # Grid storage assets address grid frequency (minutes/hours), not multi-month
        # supply disruptions — the annual CES model is the wrong tool for these.
        if row["section"] == "Grid Storage":
            row["model_ed"]         = None
            row["model_avoid_mod"]  = None
            row["model_avoid_sev"]  = None
            row["model_status_mod"] = "grid stability (sub-annual)"
            row["model_status_sev"] = "grid stability (sub-annual)"
            row["model_note"]       = "PSHP/BESS address frequency/inertia events; CES annual model does not apply"
            continue

        ed = _ed_for_carrier(row["carrier"], model)
        if ed is None:
            row["model_ed"]         = None
            row["model_avoid_mod"]  = None
            row["model_avoid_sev"]  = None
            row["model_status_mod"] = "not mapped"
            row["model_status_sev"] = "not mapped"
            row["model_note"]       = ""
            continue

        row["model_ed"]   = ed
        row["model_note"] = _carrier_note(row["carrier"])
        coverage_days     = row["coverage"]  # days (float)

        for tag, frac in [("mod", SHOCK_MOD), ("sev", SHOCK_SEV)]:
            # Try MATLAB CSV first; fall back to Python CES
            avoided = None
            if matlab_data is not None:
                comm = "oil" if ed == model.ed_oil_bar else "coal"
                sfrac = round(frac, 4)
                rdays = int(round(coverage_days))
                try:
                    avoided = matlab_data[comm][sfrac][rdays]
                except KeyError:
                    pass

            if avoided is None:
                result = model.compute_avoided_loss(ed, frac, coverage_days)
                avoided = result["avoided_loss"]

            be = row["be_gdp"]
            if avoided >= be:
                status = "justified"
            elif avoided >= 0.70 * be:
                status = "marginal"
            else:
                status = "not justified"

            row[f"model_avoid_{tag}"] = avoided
            row[f"model_status_{tag}"] = status


def model_section_md(rows: list[dict]) -> str:
    """
    Return a markdown section comparing model GDP loss to break-even thresholds.
    Appended to the existing markdown output.
    """
    model = CESModel()

    lines = [
        "---",
        "",
        "### Model Validation — Endogenous GDP Loss vs Break-Even Threshold",
        "",
        (
            f"**ToyModelSOEMC CES parameters:** "
            f"α_E={model.alpha_E}, α_K={model.alpha_K}, α_L={model.alpha_L}, "
            f"ρ={model.rho:.4f} (η={_ETA}),  "
            f"K_ss={model.K_ss:.3f}, Y_ss={model.Y_ss:.3f} (normalised),  "
            f"energy revenue share s_E={model.s_E:.4f}."
        ),
        "",
        (
            "> **Reading the table:**  "
            "*Avoided GDP%* is how much GDP loss (% of GDP, in the crisis year) "
            "the reserve prevents, computed from the CES function with K and L fixed at "
            "steady-state values.  "
            "*BE: GDP%* is the minimum avoided loss needed for the reserve to break even "
            "under MC = MB.  "
            "**Justified** = avoided loss ≥ break-even.  "
            "**Marginal** = within 30% below break-even.  "
            "**Not justified** = avoided loss < 70% of break-even.  "
            "Shock scenarios: **20%** = 20% of annual commodity supply disrupted; "
            "**50%** = 50% disrupted (tail event)."
        ),
        "",
        (
            "| Carrier | Coverage | BE: GDP% "
            "| Avoided GDP% (20% shock) | Status (20%) "
            "| Avoided GDP% (50% shock) | Status (50%) | Note |"
        ),
        "| --- | --- | ---: | ---: | :---: | ---: | :---: | --- |",
    ]

    for r in rows:
        be_str = f"{r['be_gdp']:.3f}%"

        av_mod = r.get("model_avoid_mod")
        av_sev = r.get("model_avoid_sev")
        st_mod = r.get("model_status_mod", "")
        st_sev = r.get("model_status_sev", "")
        note   = r.get("model_note", "")

        if av_mod is not None:
            av_mod_str = f"{av_mod:.3f}%"
            av_sev_str = f"{av_sev:.3f}%"
        else:
            av_mod_str = st_mod
            av_sev_str = st_sev
            st_mod = ""
            st_sev = ""

        lines.append(
            f"| {r['carrier']} | {r['cov_label']} | {be_str} "
            f"| {av_mod_str} | {st_mod} "
            f"| {av_sev_str} | {st_sev} | {note} |"
        )

    lines += [
        "",
        (
            "**Interpretation notes:**  "
            "(1) The CES model treats the shock as an *annual* supply shortfall — "
            "a 20% shock means 20% of the commodity's yearly import never arrives. "
            "Real crises are shorter but more severe per day; the annual framing is "
            "conservative for short reserves (30 d).  "
            "(2) LNG/LPG estimates use proxy ED values (not separately calibrated in "
            "ToyModelSOEMC); treat them as order-of-magnitude.  "
            "(3) PSHP and BESS address grid inertia and frequency events (timescale: "
            "seconds to hours) — the annual CES model is not the relevant tool; "
            "their benefit is better measured by avoided blackout cost per MWh.  "
            "(4) To run with Dynare's solved K_ss, call "
            "`toy_model_gdp_loss(M_, oo_)` in MATLAB after `steady`, then re-run "
            "this Python script — it will read `toy_model_gdp_loss.csv` automatically."
        ),
        "",
    ]

    return "\n".join(lines)


def model_csv_columns(rows: list[dict]) -> tuple[str, list[str]]:
    """
    Return (header_suffix, row_value_strings) for the new CSV columns.
    """
    header = "ModelED,AvoidedGDP_20pct,Status_20pct,AvoidedGDP_50pct,Status_50pct"

    vals = []
    for r in rows:
        ed   = f"{r['model_ed']:.4f}" if r.get("model_ed") is not None else ""
        av20 = f"{r['model_avoid_mod']:.4f}" if r.get("model_avoid_mod") is not None else ""
        st20 = r.get("model_status_mod", "")
        av50 = f"{r['model_avoid_sev']:.4f}" if r.get("model_avoid_sev") is not None else ""
        st50 = r.get("model_status_sev", "")
        vals.append(f"{ed},{av20},{st20},{av50},{st50}")

    return header, vals


# ── Quick self-test ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    m = CESModel()
    m.print_summary()

    SEP = "-" * 72
    print(SEP)
    print(f"  {'Commodity':<12} {'Shock':>7} {'R(days)':>9} "
          f"{'No-R loss%':>12} {'With-R loss%':>14} {'Avoided%':>10}")
    print(SEP)

    cases = [
        ("Oil",  m.ed_oil_bar,  0.20, 30),
        ("Oil",  m.ed_oil_bar,  0.20, 90),
        ("Oil",  m.ed_oil_bar,  0.50, 30),
        ("Oil",  m.ed_oil_bar,  0.50, 90),
        ("Coal", m.ed_coal_bar, 0.20, 30),
        ("Coal", m.ed_coal_bar, 0.20, 90),
        ("Coal", m.ed_coal_bar, 0.50, 30),
        ("Coal", m.ed_coal_bar, 0.50, 90),
    ]

    for comm, ed, shock, days in cases:
        r = m.compute_avoided_loss(ed, shock, days)
        print(
            f"  {comm:<12} {shock*100:>6.0f}%  {days:>8} d "
            f"  {r['loss_no_r']:>10.4f}%   {r['loss_with_r']:>12.4f}%  {r['avoided_loss']:>9.4f}%"
        )

    print(SEP)
    lin = m.gdp_loss_linear(0.20 * m.ed_oil_bar)
    exact = m.gdp_loss_pct(m.e_ss - 0.20 * m.ed_oil_bar)
    print(f"\nLinearised check:  s_E={m.s_E:.4f},  "
          f"20% oil shock ~= {lin:.4f}% GDP (linear)  vs  {exact:.4f}% (exact CES)")
