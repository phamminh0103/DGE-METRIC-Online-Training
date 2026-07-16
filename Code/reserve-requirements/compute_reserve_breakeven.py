"""
compute_reserve_breakeven.py
────────────────────────────────────────────────────────────────────────────────
Reads raw cost data from 'Data for DCE-METRIC.xlsx' and computes the
break-even avoided GDP / consumption loss for each energy reserve option
under the simple MC = MB optimality condition:

    Annual storage cost  =  p_crisis  ×  Avoided GDP loss (per crisis event)

    Break-even avoided GDP% = Annual cost / (p_crisis × GDP)

GDP loss from a supply disruption is a MODEL OUTPUT — it emerges from the
CES production chain in DGE-METRIC when augmented energy supply Q_2_aug_r
falls below firm demand. The break-even threshold computed here is what that
model output must exceed for the reserve to pass the cost-benefit test.

Outputs
───────
  reserve_breakeven_table.md    Formatted markdown table (same folder)
  reserve_breakeven_table.csv   Machine-readable CSV (same folder)
  Console summary table

Requirements
────────────
  Python ≥ 3.8
  openpyxl  (pip install openpyxl)   — for Excel reading
  tabulate  (pip install tabulate)   — for console table formatting

If openpyxl is not available the script falls back to the hardcoded data
arrays in Section 2, which are the verified values from the Excel file.

Usage
─────
  python compute_reserve_breakeven.py

To change the GDP figure or crisis probability, edit Section 1 only.
────────────────────────────────────────────────────────────────────────────────
"""

from __future__ import annotations
import math
import sys
from pathlib import Path

# ── Optional imports ─────────────────────────────────────────────────────────
try:
    import openpyxl
    _HAS_OPENPYXL = True
except ImportError:
    _HAS_OPENPYXL = False
    print("[WARN] openpyxl not found — using hardcoded data. Install with: pip install openpyxl")

try:
    from tabulate import tabulate
    _HAS_TABULATE = True
except ImportError:
    _HAS_TABULATE = False

try:
    import ces_gdp_loss as _ces
    _HAS_CES_MODEL = True
except ImportError:
    _HAS_CES_MODEL = False
    print("[INFO] ces_gdp_loss.py not found — model GDP loss columns will be skipped.")

# ── File paths ────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
EXCEL_FILE = SCRIPT_DIR / "Data for DCE-METRIC.xlsx"
OUT_MD     = SCRIPT_DIR / "reserve_breakeven_table.md"
OUT_CSV    = SCRIPT_DIR / "reserve_breakeven_table.csv"


# ══════════════════════════════════════════════════════════════════════════════
# 1.  MACRO PARAMETERS  ← edit here to update the whole table
# ══════════════════════════════════════════════════════════════════════════════

GDP_USD_M  = 430_000   # Vietnam nominal GDP 2024 (USD million) — IMF WEO 2024
P_CRISIS   = 0.04      # Annual probability of a major supply disruption (1-in-25)
                       # Source: IEA supply disruption database; ToyModelSOEMC calibration
C_Y_RATIO  = 0.67      # Private consumption / GDP — World Bank Vietnam 2023

# Annuity / Capital Recovery Factor:  CRF = r(1+r)^n / ((1+r)^n − 1)
def crf(r: float, n: int) -> float:
    return r * (1 + r)**n / ((1 + r)**n - 1)

CRF_OIL_GAS = crf(0.075, 25)   # oil/gas/LNG infrastructure: 25-yr life, 7.5% SOE rate
CRF_PSHP    = crf(0.075, 30)   # PSHP: 30-yr (from sheet)
CRF_BESS    = crf(0.085, 15)   # BESS: 15-yr, 8.5% private preferential (from sheet)

# ── Consumption flow denominators (KT/day) ────────────────────────────────────
# Used to convert stored volume → days of import coverage.
# All based on 2030 projections (PDP8 / IEA) — the planning horizon for new reserves.
DAILY_FLOW = {
    "crude_oil":  12_000 / 365,   # net crude + product imports 12 Mt/yr
    "ref_prods":  20_000 / 365,   # total refined product demand 20 Mt/yr
    "lng":        10_000 / 365,   # LNG imports under PDP8 2030 target ~10 Mt/yr
    "lpg":         2_000 / 365,   # LPG imports 2 Mt/yr
    "coal":       75_000 / 365,   # coal power-sector use 75 Mt/yr
}

# ── Break-even denominators ──────────────────────────────────────────────────
# 1% of GDP (or consumption C) expressed in USD million
DENOM_GDP = P_CRISIS * GDP_USD_M / 100          # USD m per 1% GDP
DENOM_C   = P_CRISIS * GDP_USD_M * C_Y_RATIO / 100


# ══════════════════════════════════════════════════════════════════════════════
# 2.  SOURCE DATA  (hardcoded from Excel; overridden by Excel read in Section 3)
# ══════════════════════════════════════════════════════════════════════════════
#
# Oil & Gas sheet columns: Label | Capacity | Unit | CAPEX (USD m) | OPEX (USD m/yr)
# Annual cost computed as: CAPEX × CRF_OIL_GAS + OPEX
#
# Coal sheet: annual total cost (storage + maintenance + financing/carry) read directly.
# PSHP/BESS: parameters read from the techno-economic table in the sheet.

OIL_GAS_DATA: list[tuple] = [
    # (label,                         capex_usdm, opex_usdm_yr, volume, unit)
    ("Crude oil — 1 MTA",               300,   3.5,    1_000,     "KT"),
    ("Crude oil — 2 MTA",               600,   7.0,    2_000,     "KT"),
    ("Crude oil — 3 MTA",               900,  10.5,    3_000,     "KT"),
    ("Ref. products — 500K m³",         250,   5.0,  500_000,     "m3"),
    ("Ref. products — 1,000K m³",       500,  10.0, 1_000_000,    "m3"),
    ("Ref. products — 1,500K m³",       750,  15.0, 1_500_000,    "m3"),
    ("LNG — 3 MTA",                   1_050,  77.0,    3_000,     "KT"),
    ("LNG — 6 MTA",                   2_100, 140.0,    6_000,     "KT"),
    ("LPG underground — 240 KT",        400,  15.0,      240,     "KT"),
]

# (days_coverage, source_type, ann_total_cost_usdm, useful_elec_twh)
# Annual cost from sheet includes storage & maintenance + financing/carry.
COAL_DATA: list[tuple] = [
    (30, "Domestic",  60.4, 15.0),
    (30, "Imported", 113.1, 16.3),
    (60, "Domestic", 120.7, 30.0),
    (60, "Imported", 226.2, 32.7),
    (90, "Domestic", 181.1, 45.0),
    (90, "Imported", 339.4, 49.0),
]

# Coal volume (Mt) per coverage level — from sheet column "Volume (Mt)"
COAL_VOLUME_MT = {30: 6.16, 60: 12.33, 90: 18.49}

PSHP_DATA = {
    "label":          "PSHP 1,200 MW / 8 h (Bac Ai Phase 1)",
    "capex_plant":     1_800,    # USD m
    "capex_conn":        120,    # USD m grid connection
    "opex_pct":         0.015,   # 1.5% of plant CAPEX per year
    "crf":           CRF_PSHP,
    "capacity_mw":   1_200,
    "discharge_h":        8,
    "rte":             0.80,
    "cycles_yr":        250,
    "twh_yr":           1.92,    # net energy delivered per year (after RTE)
}

BESS_DATA = {
    "label":          "BESS 4 h, 1,000 MWh (distributed)",
    "capex":             200,    # USD m
    "opex_pct":         0.025,   # 2.5% of CAPEX per year
    "crf":           CRF_BESS,
    "capacity_mwh":  1_000,
    "rte":             0.88,
    "dod":             0.90,
    "cycles_yr":        365,
    "twh_yr":           0.29,    # net energy delivered per year
}


# ══════════════════════════════════════════════════════════════════════════════
# 3.  EXCEL READER  (optional — overrides hardcoded data where readable)
# ══════════════════════════════════════════════════════════════════════════════

def _cell_float(ws, row: int, col: int):
    """Return cell value as float, or None if not numeric."""
    v = ws.cell(row=row, column=col).value
    return float(v) if isinstance(v, (int, float)) else None


def load_from_excel() -> dict:
    """
    Attempt to read Oil & Gas and Coal data from the Excel file.
    Returns dict with keys 'oil_gas', 'coal', 'pshp', 'bess' where
    each is either the Excel-sourced data or the hardcoded fallback.
    """
    oil_gas = list(OIL_GAS_DATA)   # start from hardcoded
    coal    = list(COAL_DATA)
    pshp    = dict(PSHP_DATA)
    bess    = dict(BESS_DATA)

    if not (_HAS_OPENPYXL and EXCEL_FILE.exists()):
        print(f"[INFO] Excel file not found or openpyxl unavailable — using hardcoded data.")
        return {"oil_gas": oil_gas, "coal": coal, "pshp": pshp, "bess": bess}

    try:
        wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)

        # ── Oil & Gas sheet (header row 2; data rows 3–11) ────────────────────
        ws_og = wb["Oil & Gas"]
        # Column layout: A=label, B=capacity/volume, C=unit, D=CAPEX, E=OPEX
        og_labels = [row[0] for row in OIL_GAS_DATA]
        og_xl = []
        for row_i, lbl in zip(range(3, 12), og_labels):
            vol   = _cell_float(ws_og, row_i, 2)
            capex = _cell_float(ws_og, row_i, 4)
            opex  = _cell_float(ws_og, row_i, 5)
            unit  = OIL_GAS_DATA[row_i - 3][4]   # keep original unit label
            if vol and capex and opex:
                og_xl.append((lbl, capex, opex, vol, unit))
        if len(og_xl) == 9:
            oil_gas = og_xl
            print("[INFO] Oil & Gas data loaded from Excel.")
        else:
            print(f"[WARN] Oil & Gas: read {len(og_xl)}/9 rows — using hardcoded fallback.")

        # ── Coal sheet (header row 10; data rows 11–16) ───────────────────────
        ws_c = wb["Inputs_Coal-BESS-PHS"]
        # Column layout: A=coverage, B=commodity, C=volume, D=storage, E=financing, F=TOTAL, G=thermal, H=useful_elec
        coal_meta = [(11, 30, "Domestic"), (12, 30, "Imported"),
                     (13, 60, "Domestic"), (14, 60, "Imported"),
                     (15, 90, "Domestic"), (16, 90, "Imported")]
        coal_xl = []
        for row_i, days, typ in coal_meta:
            ann = _cell_float(ws_c, row_i, 6)   # col F = TOTAL cost/yr
            twh = _cell_float(ws_c, row_i, 8)   # col H = useful electricity
            if ann and twh:
                coal_xl.append((days, typ, ann, twh))
        if len(coal_xl) == 6:
            coal = coal_xl
            print("[INFO] Coal data loaded from Excel.")
        else:
            print(f"[WARN] Coal: read {len(coal_xl)}/6 rows — using hardcoded fallback.")

        # ── PSHP row 31, BESS row 32 ──────────────────────────────────────────
        # Column layout: B=technology, C=capacity, D=unit, E=CAPEX, F=ann_cost, G=TWh, H=conn_capex
        for row_i, target, name in [(31, pshp, "PSHP"), (32, bess, "BESS")]:
            capex_xl = _cell_float(ws_c, row_i, 5)
            twh_xl   = _cell_float(ws_c, row_i, 7)
            conn_xl  = _cell_float(ws_c, row_i, 8)
            if capex_xl:
                if name == "PSHP":
                    target["capex_plant"] = capex_xl
                    if conn_xl:
                        target["capex_conn"] = conn_xl
                else:
                    target["capex"] = capex_xl
                if twh_xl:
                    target["twh_yr"] = twh_xl
                print(f"[INFO] {name} data loaded from Excel.")

        wb.close()
    except Exception as exc:
        print(f"[WARN] Excel read failed ({exc}) — using hardcoded data.")

    return {"oil_gas": oil_gas, "coal": coal, "pshp": pshp, "bess": bess}


# ══════════════════════════════════════════════════════════════════════════════
# 4.  COMPUTATION
# ══════════════════════════════════════════════════════════════════════════════

# Explicit carrier → flow key mapping (avoids volume-range ambiguity)
_CARRIER_FLOW = {
    "Crude oil":     "crude_oil",
    "Ref. products": "ref_prods",
    "LNG":           "lng",
    "LPG":           "lpg",
}

DENSITY_LIQUID = 0.85   # t/m³ average density for petroleum products


def _ann_cost_oil_gas(capex: float, opex: float) -> float:
    """Annualised infrastructure cost using CRF_OIL_GAS."""
    return capex * CRF_OIL_GAS + opex


def _days(volume: float, unit: str, flow_key: str) -> float:
    """Convert stored volume to days of import coverage."""
    kt = volume * DENSITY_LIQUID / 1_000 if unit == "m3" else volume
    return kt / DAILY_FLOW[flow_key]


def _breakeven(ann_cost: float) -> tuple[float, float]:
    """Return (break-even GDP %, break-even C %) conditional on crisis occurring."""
    return ann_cost / DENOM_GDP, ann_cost / DENOM_C


def build_rows(data: dict) -> list[dict]:
    rows: list[dict] = []

    # ── Oil & Gas ──────────────────────────────────────────────────────────────
    for label, capex, opex, volume, unit in data["oil_gas"]:
        carrier_key = next((k for k in _CARRIER_FLOW if label.startswith(k)), None)
        if carrier_key is None:
            continue
        flow_key = _CARRIER_FLOW[carrier_key]
        ac   = _ann_cost_oil_gas(capex, opex)
        days = _days(volume, unit, flow_key)
        be_g, be_c = _breakeven(ac)
        rows.append({
            "section":   "Oil & Gas",
            "carrier":   label,
            "coverage":  days,
            "cov_label": f"{days:.0f} days",
            "volume":    f"{volume:,.0f} {unit}",
            "ann_cost":  ac,
            "pct_gdp":   ac / GDP_USD_M * 100,
            "be_gdp":    be_g,
            "be_c":      be_c,
            "mc_day":    ac / days,       # USD m per additional day of coverage
            "twh_yr":    None,
        })

    # ── Coal ───────────────────────────────────────────────────────────────────
    for days, src_type, ac, twh in data["coal"]:
        vol_mt = COAL_VOLUME_MT[days]
        be_g, be_c = _breakeven(ac)
        rows.append({
            "section":   "Coal",
            "carrier":   f"Coal — {src_type}",
            "coverage":  days,
            "cov_label": f"{days} days",
            "volume":    f"{vol_mt:.2f} Mt",
            "ann_cost":  ac,
            "pct_gdp":   ac / GDP_USD_M * 100,
            "be_gdp":    be_g,
            "be_c":      be_c,
            "mc_day":    ac / days,
            "twh_yr":    twh,
        })

    # ── PSHP ──────────────────────────────────────────────────────────────────
    p = data["pshp"]
    plant_ann = p["capex_plant"] * p["crf"] + p["capex_plant"] * p["opex_pct"]
    conn_ann  = p["capex_conn"]  * p["crf"]
    total_ann = plant_ann + conn_ann
    gwh_event = p["capacity_mw"] * p["discharge_h"] * p["rte"] / 1_000   # GWh net
    cost_per_event = total_ann / p["cycles_yr"]
    cost_per_mwh   = cost_per_event * 1e6 / (gwh_event * 1_000)          # USD / MWh
    be_g, be_c = _breakeven(total_ann)
    rows.append({
        "section":   "Grid Storage",
        "carrier":   p["label"],
        "coverage":  p["twh_yr"],
        "cov_label": f"{p['twh_yr']:.2f} TWh/yr  ({p['cycles_yr']} cycles)",
        "volume":    f"{p['capacity_mw']:,} MW",
        "ann_cost":  total_ann,
        "pct_gdp":   total_ann / GDP_USD_M * 100,
        "be_gdp":    be_g,
        "be_c":      be_c,
        "mc_day":    cost_per_event,          # USD m per dispatch event
        "twh_yr":    p["twh_yr"],
        "cost_per_mwh": cost_per_mwh,
        "gwh_event": gwh_event,
    })

    # ── BESS ──────────────────────────────────────────────────────────────────
    b = data["bess"]
    b_ann = b["capex"] * b["crf"] + b["capex"] * b["opex_pct"]
    gwh_event_b    = b["capacity_mwh"] * b["dod"] * b["rte"] / 1_000
    cost_per_evt_b = b_ann / b["cycles_yr"]
    cost_per_mwh_b = cost_per_evt_b * 1e6 / (gwh_event_b * 1_000)       # USD / MWh
    be_g, be_c = _breakeven(b_ann)
    rows.append({
        "section":   "Grid Storage",
        "carrier":   b["label"],
        "coverage":  b["twh_yr"],
        "cov_label": f"{b['twh_yr']:.2f} TWh/yr  ({b['cycles_yr']} cycles)",
        "volume":    f"{b['capacity_mwh']:,} MWh",
        "ann_cost":  b_ann,
        "pct_gdp":   b_ann / GDP_USD_M * 100,
        "be_gdp":    be_g,
        "be_c":      be_c,
        "mc_day":    cost_per_evt_b,
        "twh_yr":    b["twh_yr"],
        "cost_per_mwh": cost_per_mwh_b,
        "gwh_event": gwh_event_b,
    })

    return rows


# ══════════════════════════════════════════════════════════════════════════════
# 5.  OUTPUT FORMATTERS
# ══════════════════════════════════════════════════════════════════════════════

_PARAM_BLOCK = f"""\
## Break-Even Avoided GDP/Consumption Loss — Energy Reserve Optimality
### Vietnam | MC = MB condition:  Annual cost = p × Avoided GDP loss per crisis

**Key:**  *BE: GDP%* = minimum GDP loss (% of GDP) a crisis must cause for the reserve to be
cost-effective.  *MC/day* = annualised cost per additional day of coverage (USD m/yr).
For grid storage (PSHP, BESS) *MC* is the cost per dispatch event (USD m).

| Parameter | Value | Notes |
|---|---|---|
| GDP 2024 | USD {GDP_USD_M:,.0f}m | IMF WEO 2024 |
| Crisis probability `p` | {P_CRISIS:.2f}/yr | 1-in-25; IEA disruption database |
| C/Y ratio | {C_Y_RATIO:.2f} | World Bank Vietnam 2023 |
| CRF — oil/gas infrastructure | {CRF_OIL_GAS:.4f} | 25-yr life, 7.5% SOE discount rate |
| CRF — PSHP | {CRF_PSHP:.4f} | 30-yr life, 7.5% |
| CRF — BESS | {CRF_BESS:.4f} | 15-yr life, 8.5% |
| Break-even divisor (1% GDP) | USD {DENOM_GDP:.1f}m | `= p × GDP/100` |
| Break-even divisor (1% C)   | USD {DENOM_C:.1f}m | `= p × C/100` |

*Consumption flows (2030 basis):* crude oil 12 Mt/yr net imports;
petroleum products 20 Mt/yr total demand (density 0.85 t/m³);
LNG 10 Mt/yr (PDP8 target); LPG 2 Mt/yr imports;
coal 75 Mt/yr power-sector consumption.

"""

_COL_HEADERS = [
    "Carrier", "Coverage", "Volume",
    "Ann. cost\n(USD m/yr)", "Cost\n% GDP",
    "BE: GDP\nloss %", "BE: C\nloss %",
    "MC / day\n(USD m)",
]


def _section_md(section_name: str, rows: list[dict]) -> str:
    mc_col = "MC/day (USD m)" if section_name != "Grid Storage" else "Cost/event (USD m)"
    header = (
        f"| Carrier | Coverage | Volume | Ann. cost (USD m/yr) | Cost % GDP "
        f"| BE: GDP loss % | BE: C loss % | {mc_col} |"
    )
    sep = "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |"
    body_lines = []
    for r in rows:
        body_lines.append(
            f"| {r['carrier']} | {r['cov_label']} | {r['volume']} "
            f"| {r['ann_cost']:.1f} | {r['pct_gdp']:.4f}% "
            f"| **{r['be_gdp']:.3f}%** | {r['be_c']:.3f}% "
            f"| {r['mc_day']:.3f} |"
        )
    return "\n".join([f"### {section_name}", "", header, sep] + body_lines + [""])


def to_markdown(rows: list[dict]) -> str:
    sections: dict[str, list] = {}
    for r in rows:
        sections.setdefault(r["section"], []).append(r)
    parts = [_PARAM_BLOCK]
    for sec, sec_rows in sections.items():
        parts.append(_section_md(sec, sec_rows))
    # Summary
    parts.append("### Summary — All carriers ranked by break-even GDP loss %\n")
    sorted_rows = sorted(rows, key=lambda r: r["be_gdp"])
    parts.append(_section_md("", sorted_rows).replace("### \n", ""))
    # CES model validation (requires ces_gdp_loss.py)
    if _HAS_CES_MODEL:
        parts.append(_ces.model_section_md(rows))
    return "\n".join(parts)


def to_csv(rows: list[dict]) -> str:
    ces_header, ces_vals = ("", [""] * len(rows))
    if _HAS_CES_MODEL:
        ces_header, ces_vals = _ces.model_csv_columns(rows)
        ces_header = "," + ces_header

    header = (
        "Section,Carrier,Coverage_days_or_TWh,Volume,"
        "AnnCost_USDm,Cost_pct_GDP,"
        "BE_GDP_pct,BE_C_pct,"
        f"MC_per_day_USDm,TWh_yr{ces_header}\n"
    )
    lines = [header]
    for r, cv in zip(rows, ces_vals):
        twh = f"{r['twh_yr']:.3f}" if r.get("twh_yr") is not None else ""
        ces_suffix = f",{cv}" if cv else ""
        lines.append(
            f"{r['section']},\"{r['carrier']}\",{r['coverage']:.1f},"
            f"\"{r['volume']}\","
            f"{r['ann_cost']:.2f},{r['pct_gdp']:.6f},"
            f"{r['be_gdp']:.4f},{r['be_c']:.4f},"
            f"{r['mc_day']:.4f},{twh}{ces_suffix}\n"
        )
    return "".join(lines)


def print_console(rows: list[dict]) -> None:
    width = 100
    print("\n" + "=" * width)
    print(f"  BREAK-EVEN AVOIDED GDP LOSS   |  p = {P_CRISIS}  |  GDP = USD {GDP_USD_M:,}m  |  C/Y = {C_Y_RATIO}")
    print("  (minimum GDP% loss a crisis must cause for the reserve to be cost-effective)")
    print("=" * width)
    if _HAS_TABULATE:
        table_data = [
            [r["carrier"], r["cov_label"], r["ann_cost"], r["pct_gdp"],
             r["be_gdp"], r["be_c"], r["mc_day"]]
            for r in rows
        ]
        print(tabulate(
            table_data,
            headers=["Carrier", "Coverage", "Ann.cost\n(USDm)", "Cost\n%GDP",
                     "BE: GDP%", "BE: C%", "MC/day\n(USDm)"],
            floatfmt=(".0f", ".0f", ".1f", ".4f", ".3f", ".3f", ".3f"),
            tablefmt="simple",
        ))
    else:
        hdr = f"  {'Carrier':<44} {'Coverage':<22} {'Ann cost':>10}  {'BE GDP%':>8}  {'BE C%':>8}  {'MC/day':>8}"
        print(hdr)
        print("-" * width)
        for r in rows:
            print(
                f"  {r['carrier']:<44} {r['cov_label']:<22} "
                f"{r['ann_cost']:>9.1f}m  {r['be_gdp']:>7.3f}%  "
                f"{r['be_c']:>7.3f}%  {r['mc_day']:>7.3f}m"
            )
    print("=" * width)
    # Grid storage addendum
    for r in rows:
        if r["section"] == "Grid Storage":
            mwh  = r.get("gwh_event", 0) * 1_000
            cmwh = r.get("cost_per_mwh", r["mc_day"] * 1e6 / max(mwh, 1))
            print(
                f"  {r['carrier'][:55]:<56}  "
                f"USD {r['mc_day']*1e3:.0f}k/event  |  USD {cmwh:.1f}/MWh dispatched"
            )
    print()


# ══════════════════════════════════════════════════════════════════════════════
# 6.  MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    # Verify CRF formulas
    print(f"CRF — oil/gas: {CRF_OIL_GAS:.4f} | PSHP: {CRF_PSHP:.4f} | BESS: {CRF_BESS:.4f}")
    print(f"Break-even divisors — GDP: {DENOM_GDP:.1f} USD m/1%  |  C: {DENOM_C:.1f} USD m/1%")

    # Load data
    data = load_from_excel()

    # Compute
    rows = build_rows(data)

    # Augment with CES model GDP loss columns
    if _HAS_CES_MODEL:
        _ces.add_model_columns(rows, script_dir=SCRIPT_DIR)

    # Console output
    print_console(rows)

    # Markdown
    md_text = to_markdown(rows)
    OUT_MD.write_text(md_text, encoding="utf-8")
    print(f"[OK] Markdown written -> {OUT_MD}")

    # CSV
    csv_text = to_csv(rows)
    OUT_CSV.write_text(csv_text, encoding="utf-8")
    print(f"[OK] CSV written      -> {OUT_CSV}")


if __name__ == "__main__":
    main()
