"""
gdp_energy_growth_analysis.py
───────────────────────────────────────────────────────────────────────────────
Scatterplot + regression analysis: GDP growth vs. primary energy consumption
growth, panel of countries, 1965-2023.

DATA SOURCES
  Energy   Energy Institute Statistical Review of World Energy
           "Primary energy cons - EJ" sheet of EI-Stats-Review-All-Data.xlsx
           (annual primary energy consumption, exajoules, by country), plus
           the six per-carrier sheets in CARRIER_SHEETS (oil, gas, coal,
           nuclear, hydro, renewables) for the carrier-level regressions.
  GDP      World Bank API, indicator NY.GDP.MKTP.KD
           (GDP, constant 2015 US$ -- real GDP, so growth is real GDP growth)
           Fetched live from https://api.worldbank.org

METHOD
  1. Parse the EI sheet into a long (country, year, energy_ej) panel, dropping
     regional aggregate rows ("Total ...", "Other ..."), the World/OECD
     summary rows, and footnotes. Leading/embedded 0.0 values are treated as
     "no data" (EI uses 0 before a country's data series begins, e.g. Croatia
     pre-1991) rather than literal zero consumption.
  2. Map EI country labels to ISO3 codes (hardcoded dict below -- the EI sheet
     uses a mix of short names, historical blocs, and non-WB entities that
     don't resolve automatically) and fetch matching World Bank GDP levels.
  3. Compute year-over-year growth rates (%) within each country for both
     series, merge on (iso3, year).
  4. Winsorize both growth series at the WINSOR_PCT / (100-WINSOR_PCT)
     percentiles (cap, don't drop). A handful of country-years -- mostly
     tiny-base oil-state takeoffs (Oman/UAE/Qatar 1967-80) and war episodes
     (Iraq/Kuwait 1990-92) -- post four-digit percentage swings off a
     near-zero starting level; left uncapped they single-handedly set the OLS
     slope and the plot's axis scale.
  5. Regress GDP growth on energy consumption growth (dependent: GDP growth;
     independent: energy growth) on the winsorized sample:
       (a) pooled OLS,                                gdp_g = a + b * energy_g
       (b) OLS with country and year fixed effects,    clustered SE by country
       (c) conditional (asymmetric) regression that lets both the intercept
           and the slope differ when energy consumption growth is negative,
           via an interaction with 1{energy_g < 0}:
             gdp_g = a + b*energy_g + c*neg_energy + d*energy_g*neg_energy
           so the energy-growth slope is b when energy growth is positive and
           (b + d) when it is negative,
       (d) the same conditional/asymmetric specification with country and
           year fixed effects added, clustered SE by country.
     (b) and (d) net out country-specific trends and global shocks (e.g.
     2009, 2020) that would otherwise show up as spurious correlation in the
     pooled fits.
  6. Two scatterplots: the pooled relationship (energy growth on the x-axis,
     GDP growth on the y-axis) with the pooled regression line, and a second
     one split into the two regimes (energy growth >= 0 / < 0) with their
     separate fitted lines from the conditional regression.
  7. For each carrier (oil, gas, coal, nuclear, hydro, renewables): build its
     own growth panel from the matching EI sheet, compute that carrier's
     share of TOTAL primary energy consumption in the PREVIOUS year
     (share_lag -- predetermined, so it isn't mechanically part of the same
     year's growth rate), winsorize the carrier's growth series the same way,
     and regress
       gdp_g = a + b*carrier_g + c*share_lag + d*carrier_g*share_lag
     The interaction (d) tests whether a carrier's growth rate matters more
     for GDP growth the larger that carrier's predetermined weight in the
     energy mix already was -- e.g. an oil-growth shock should matter more in
     an oil-heavy economy than the same growth rate would in a renewables-
     heavy one.

OUTPUT (written next to this script)
  gdp_energy_panel.csv                       merged long panel (iso3, country,
                                              year, energy_ej, gdp_growth_pct,
                                              energy_growth_pct, plus winsorized
                                              _w columns used for the fits)
  gdp_carrier_panel.csv                      stacked long panel across all six
                                              carriers (carrier, iso3, country,
                                              year, carrier_ej, carrier_growth_pct(_w),
                                              share_lag, gdp_growth_pct_w)
  gdp_energy_growth_scatter.png              pooled scatterplot
  gdp_energy_growth_conditional_scatter.png  scatterplot split by energy-growth sign
  gdp_energy_growth_regression.txt           regression summary (specs 1-4)
  gdp_carrier_growth_regression.txt          per-carrier regression summary

USAGE
  python gdp_energy_growth_analysis.py
───────────────────────────────────────────────────────────────────────────────
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import statsmodels.formula.api as smf

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
EI_PATH = Path(
    r"C:\Users\schul\Dropbox\2025_GIZ_Vietnam\Data\EnergyInstitute\EI-Stats-Review-All-Data.xlsx"
)
EI_SHEET = "Primary energy cons - EJ"

# Per-carrier consumption sheets -- same layout as EI_SHEET (see load_energy_panel)
CARRIER_SHEETS: dict[str, str] = {
    "oil": "Oil Consumption - EJ",
    "gas": "Gas Consumption - EJ",
    "coal": "Coal Consumption - EJ",
    "nuclear": "Nuclear Consumption - EJ",
    "hydro": "Hydro Consumption - EJ",
    "renewables": "Renewables Consumption -EJ",
}

OUT_PANEL_CSV = SCRIPT_DIR / "gdp_energy_panel.csv"
OUT_CARRIER_PANEL_CSV = SCRIPT_DIR / "gdp_carrier_panel.csv"
OUT_SCATTER_PNG = SCRIPT_DIR / "gdp_energy_growth_scatter.png"
OUT_COND_SCATTER_PNG = SCRIPT_DIR / "gdp_energy_growth_conditional_scatter.png"
OUT_REGRESSION_TXT = SCRIPT_DIR / "gdp_energy_growth_regression.txt"
OUT_CARRIER_REGRESSION_TXT = SCRIPT_DIR / "gdp_carrier_growth_regression.txt"

WB_INDICATOR = "NY.GDP.MKTP.KD"  # GDP, constant 2015 US$
WB_DATE_RANGE = "1960:2023"

WINSOR_PCT = 1.0  # cap each growth series at the [p, 100-p] percentiles

# ── EI country label -> ISO3 code ────────────────────────────────────────────
# None = regional aggregate or entity with no matching World Bank GDP series
# (Taiwan is not a World Bank member and has no NY.GDP.MKTP.KD series).
EI_TO_ISO3: dict[str, str | None] = {
    "Canada": "CAN", "Mexico": "MEX", "US": "USA",
    "Argentina": "ARG", "Brazil": "BRA", "Chile": "CHL", "Colombia": "COL",
    "Ecuador": "ECU", "Peru": "PER", "Trinidad & Tobago": "TTO",
    "Venezuela": "VEN", "Central America": None,
    "Austria": "AUT", "Belgium": "BEL", "Bulgaria": "BGR", "Croatia": "HRV",
    "Cyprus": "CYP", "Czech Republic": "CZE", "Denmark": "DNK",
    "Estonia": "EST", "Finland": "FIN", "France": "FRA", "Germany": "DEU",
    "Greece": "GRC", "Hungary": "HUN", "Iceland": "ISL", "Ireland": "IRL",
    "Italy": "ITA", "Latvia": "LVA", "Lithuania": "LTU", "Luxembourg": "LUX",
    "Netherlands": "NLD", "North Macedonia": "MKD", "Norway": "NOR",
    "Poland": "POL", "Portugal": "PRT", "Romania": "ROU", "Slovakia": "SVK",
    "Slovenia": "SVN", "Spain": "ESP", "Sweden": "SWE", "Switzerland": "CHE",
    "Turkey": "TUR", "Ukraine": "UKR", "United Kingdom": "GBR",
    "Azerbaijan": "AZE", "Belarus": "BLR", "Kazakhstan": "KAZ",
    "Russian Federation": "RUS", "Turkmenistan": "TKM", "Uzbekistan": "UZB",
    "Iran": "IRN", "Iraq": "IRQ", "Israel": "ISR", "Kuwait": "KWT",
    "Oman": "OMN", "Qatar": "QAT", "Saudi Arabia": "SAU",
    "United Arab Emirates": "ARE",
    "Algeria": "DZA", "Egypt": "EGY", "Morocco": "MAR", "South Africa": "ZAF",
    "Eastern Africa": None, "Middle Africa": None, "Western Africa": None,
    "Australia": "AUS", "Bangladesh": "BGD", "China": "CHN",
    "China Hong Kong SAR": "HKG", "India": "IND", "Indonesia": "IDN",
    "Japan": "JPN", "Malaysia": "MYS", "New Zealand": "NZL",
    "Pakistan": "PAK", "Philippines": "PHL", "Singapore": "SGP",
    "South Korea": "KOR", "Sri Lanka": "LKA", "Taiwan": None,
    "Thailand": "THA", "Vietnam": "VNM",
}

# Row labels that mark aggregate/summary rows to exclude even if not in the
# dict above (belt-and-braces against sheet edits).
_EXCLUDE_KEYWORDS = ("Total", "Other", "of which")


# ── Step 1: load Energy Institute panel ──────────────────────────────────────
def load_energy_panel(path: Path, sheet: str, value_col: str = "energy_ej") -> pd.DataFrame:
    """Load one EI Statistical Review consumption sheet into a long panel.

    Every "<carrier> Consumption - EJ" sheet shares the layout of the
    "Primary energy cons - EJ" sheet (country label in col 0, year header in
    row 2, same aggregate-row keywords), so this loader is reused for the
    per-carrier sheets with a different `value_col` name.
    """
    raw = pd.read_excel(path, sheet_name=sheet, header=None)

    # The sheet appends trailing summary columns after the annual series
    # (a repeated latest-year column, a "2013-23" CAGR column, ...). Years run
    # strictly increasing 1965, 1966, ... -- stop at the first column that
    # breaks that sequence rather than trusting "looks like a year" alone.
    year_row = raw.iloc[2]
    year_cols: list = []
    years: list[int] = []
    prev_year = -1
    for c in raw.columns[1:]:
        v = year_row[c]
        if not (isinstance(v, (int, float)) and not pd.isna(v) and 1900 < v < 2100):
            break
        if int(v) <= prev_year:
            break
        year_cols.append(c)
        years.append(int(v))
        prev_year = int(v)

    records = []
    for _, row in raw.iterrows():
        label = row[0]
        if not isinstance(label, str):
            continue
        label = label.strip()
        if label not in EI_TO_ISO3 or any(k in label for k in _EXCLUDE_KEYWORDS):
            continue
        iso3 = EI_TO_ISO3[label]
        if iso3 is None:
            continue
        for c, yr in zip(year_cols, years):
            val = row[c]
            if isinstance(val, (int, float)) and val > 0:  # 0.0 = no data in EI sheet
                records.append((iso3, label, yr, float(val)))

    panel = pd.DataFrame(records, columns=["iso3", "country", "year", value_col])
    panel = panel.sort_values(["iso3", "year"]).reset_index(drop=True)
    return panel


# ── Step 2: fetch World Bank GDP levels ──────────────────────────────────────
def fetch_wb_gdp(iso3_codes: list[str], indicator: str, date_range: str) -> pd.DataFrame:
    codes = ";".join(sorted(set(iso3_codes)))
    url = f"https://api.worldbank.org/v2/country/{codes}/indicator/{indicator}"
    params = {"date": date_range, "format": "json", "per_page": 20000}

    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    payload = resp.json()

    if not isinstance(payload, list) or len(payload) < 2 or payload[1] is None:
        raise RuntimeError(f"Unexpected World Bank API response: {payload}")

    meta, rows = payload[0], payload[1]
    if meta.get("pages", 1) > 1:
        raise RuntimeError(
            f"World Bank response paginated ({meta['pages']} pages) -- "
            "increase per_page or add pagination."
        )

    records = [
        (r["countryiso3code"], int(r["date"]), float(r["value"]))
        for r in rows
        if r["value"] is not None
    ]
    gdp = pd.DataFrame(records, columns=["iso3", "year", "gdp_constant_usd"])
    return gdp.sort_values(["iso3", "year"]).reset_index(drop=True)


# ── Step 3: growth rates + merge ─────────────────────────────────────────────
def build_growth_panel(energy: pd.DataFrame, gdp: pd.DataFrame) -> pd.DataFrame:
    energy = energy.copy()
    energy["energy_growth_pct"] = (
        energy.groupby("iso3")["energy_ej"].pct_change() * 100
    )

    gdp = gdp.copy()
    gdp["gdp_growth_pct"] = gdp.groupby("iso3")["gdp_constant_usd"].pct_change() * 100

    merged = energy.merge(
        gdp[["iso3", "year", "gdp_growth_pct"]], on=["iso3", "year"], how="inner"
    )
    merged = merged.dropna(subset=["energy_growth_pct", "gdp_growth_pct"])
    merged = merged[np.isfinite(merged["energy_growth_pct"]) & np.isfinite(merged["gdp_growth_pct"])]
    return merged.reset_index(drop=True)


def winsorize_panel(df: pd.DataFrame, pct: float) -> pd.DataFrame:
    """Cap (not drop) each growth series at its [pct, 100-pct] percentiles."""
    df = df.copy()
    for col in ("gdp_growth_pct", "energy_growth_pct"):
        lower, upper = df[col].quantile([pct / 100, 1 - pct / 100])
        df[f"{col}_w"] = df[col].clip(lower, upper)
    return df


# ── Step 4: regressions ───────────────────────────────────────────────────────
def run_regressions(df: pd.DataFrame):
    """Pooled OLS and country+year FE OLS of GDP growth on energy growth."""
    pooled = smf.ols("gdp_growth_pct_w ~ energy_growth_pct_w", data=df).fit(
        cov_type="cluster", cov_kwds={"groups": df["iso3"]}
    )
    fe = smf.ols(
        "gdp_growth_pct_w ~ energy_growth_pct_w + C(iso3) + C(year)", data=df
    ).fit(cov_type="cluster", cov_kwds={"groups": df["iso3"]})
    return pooled, fe


def run_conditional_regression(df: pd.DataFrame):
    """
    Asymmetric regression: allows GDP growth's response to energy growth to
    differ when energy consumption growth is negative (energy_g < 0), via an
    interaction with the dummy neg_energy = 1{energy_growth_pct_w < 0}.
    Returns (pooled, fe) -- the pooled fit and its country+year FE counterpart.
    """
    df = df.copy()
    df["neg_energy"] = (df["energy_growth_pct_w"] < 0).astype(int)
    cond = smf.ols(
        "gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy", data=df
    ).fit(cov_type="cluster", cov_kwds={"groups": df["iso3"]})
    cond_fe = smf.ols(
        "gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy + C(iso3) + C(year)", data=df
    ).fit(cov_type="cluster", cov_kwds={"groups": df["iso3"]})
    return cond, cond_fe


# ── Step 4b: per-carrier growth panels + regressions ─────────────────────────
def build_carrier_panel(
    carrier: str, sheet: str, total_energy: pd.DataFrame, gdp_growth: pd.DataFrame, pct: float
) -> pd.DataFrame:
    """
    Build the regression panel for one energy carrier (oil, gas, coal, ...):
      carrier_growth_pct_w  winsorized y/y growth of that carrier's consumption
      share_lag             the carrier's share of *total* primary energy
                             consumption in the PREVIOUS year (t-1), so it is
                             predetermined relative to the current growth rate
      gdp_growth_pct_w      the same winsorized GDP growth used throughout
    """
    carrier_ej = load_energy_panel(EI_PATH, sheet, value_col="carrier_ej")

    combined = carrier_ej.merge(
        total_energy[["iso3", "year", "energy_ej"]], on=["iso3", "year"], how="inner"
    ).sort_values(["iso3", "year"])

    combined["carrier_growth_pct"] = combined.groupby("iso3")["carrier_ej"].pct_change() * 100
    combined["share"] = combined["carrier_ej"] / combined["energy_ej"]
    combined["share_lag"] = combined.groupby("iso3")["share"].shift(1)

    combined = combined.dropna(subset=["carrier_growth_pct", "share_lag"])
    combined = combined[np.isfinite(combined["carrier_growth_pct"]) & np.isfinite(combined["share_lag"])]

    lower, upper = combined["carrier_growth_pct"].quantile([pct / 100, 1 - pct / 100])
    combined["carrier_growth_pct_w"] = combined["carrier_growth_pct"].clip(lower, upper)

    panel = combined.merge(
        gdp_growth[["iso3", "year", "gdp_growth_pct_w"]], on=["iso3", "year"], how="inner"
    )
    panel.insert(0, "carrier", carrier)
    return panel[[
        "carrier", "iso3", "country", "year", "carrier_ej", "carrier_growth_pct",
        "carrier_growth_pct_w", "share_lag", "gdp_growth_pct_w",
    ]].reset_index(drop=True)


def run_carrier_regression(df: pd.DataFrame):
    """
    gdp_growth_w ~ carrier_growth_w * share_lag  --  the interaction tests
    whether a given carrier's growth rate matters more for GDP growth the
    larger that carrier's (predetermined) share of the energy mix was.
    """
    return smf.ols(
        "gdp_growth_pct_w ~ carrier_growth_pct_w * share_lag", data=df
    ).fit(cov_type="cluster", cov_kwds={"groups": df["iso3"]})


# ── Step 5: scatterplot ───────────────────────────────────────────────────────
# Palette per the dataviz skill's validated default (references/palette.md)
COLOR_POINTS = "#2a78d6"   # categorical slot 1 (blue) -- single series
COLOR_LINE = "#e34948"     # diverging pole (red) -- reads as a distinct overlay
COLOR_SURFACE = "#fcfcfb"
COLOR_INK_PRIMARY = "#0b0b0b"
COLOR_INK_SECONDARY = "#52514e"
COLOR_INK_MUTED = "#898781"
COLOR_GRID = "#e1e0d9"
COLOR_AXIS = "#c3c2b7"

# Two-group categorical split (energy growth >= 0 vs. < 0) -- fixed slot order
COLOR_POS = "#2a78d6"   # categorical slot 1 (blue) -- energy growth >= 0
COLOR_NEG = "#008300"   # categorical slot 2 (green) -- energy growth < 0


def make_scatter(df: pd.DataFrame, pooled_fit, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 6.5), dpi=150)
    fig.patch.set_facecolor(COLOR_SURFACE)
    ax.set_facecolor(COLOR_SURFACE)

    ax.scatter(
        df["energy_growth_pct_w"], df["gdp_growth_pct_w"],
        s=16, color=COLOR_POINTS, alpha=0.35, linewidths=0,
        label="Country-year observations",
    )

    x_line = np.linspace(df["energy_growth_pct_w"].min(), df["energy_growth_pct_w"].max(), 100)
    b0, b1 = pooled_fit.params["Intercept"], pooled_fit.params["energy_growth_pct_w"]
    ax.plot(x_line, b0 + b1 * x_line, color=COLOR_LINE, linewidth=2, zorder=5,
             label="Pooled OLS fit")

    r2 = pooled_fit.rsquared
    n = int(pooled_fit.nobs)
    se = pooled_fit.bse["energy_growth_pct_w"]
    ax.text(
        0.02, 0.97,
        f"GDP growth = {b0:.2f} + {b1:.3f} × energy growth\n"
        f"(clustered s.e. = {se:.3f})   R² = {r2:.3f}   N = {n:,}",
        transform=ax.transAxes, ha="left", va="top", fontsize=10,
        color=COLOR_INK_SECONDARY,
    )

    ax.axhline(0, color=COLOR_AXIS, linewidth=0.8, zorder=1)
    ax.axvline(0, color=COLOR_AXIS, linewidth=0.8, zorder=1)
    ax.set_xlabel("Primary energy consumption growth (%, y/y)", color=COLOR_INK_PRIMARY, fontsize=11)
    ax.set_ylabel("Real GDP growth (%, y/y)", color=COLOR_INK_PRIMARY, fontsize=11)
    ax.set_title(
        "Energy consumption growth vs. GDP growth\n"
        "Country panel, 1965–2023 — Energy Institute Statistical Review × World Bank",
        color=COLOR_INK_PRIMARY, fontsize=12, pad=14,
    )
    ax.text(
        0.5, -0.14,
        f"Both series winsorized at the {WINSOR_PCT:.0f}% / {100-WINSOR_PCT:.0f}% percentiles "
        "(caps tiny-base oil-state takeoffs and war-episode outliers, doesn't drop them)",
        transform=ax.transAxes, ha="center", va="top", fontsize=8, color=COLOR_INK_MUTED,
    )

    ax.grid(True, color=COLOR_GRID, linewidth=0.8, zorder=0)
    for spine in ax.spines.values():
        spine.set_color(COLOR_AXIS)
    ax.tick_params(colors=COLOR_INK_MUTED, labelsize=9)

    legend = ax.legend(loc="lower right", frameon=False, fontsize=9)
    for text in legend.get_texts():
        text.set_color(COLOR_INK_SECONDARY)

    fig.tight_layout()
    fig.savefig(out_path, facecolor=COLOR_SURFACE)
    plt.close(fig)


def make_conditional_scatter(df: pd.DataFrame, cond_fit, out_path: Path) -> None:
    """
    Same GDP-growth-on-energy-growth scatter, split into two regimes --
    energy growth >= 0 vs. < 0 -- each with its own fitted line, reading off
    the conditional (asymmetric) regression's coefficients directly.
    """
    fig, ax = plt.subplots(figsize=(9, 6.5), dpi=150)
    fig.patch.set_facecolor(COLOR_SURFACE)
    ax.set_facecolor(COLOR_SURFACE)

    pos = df[df["energy_growth_pct_w"] >= 0]
    neg = df[df["energy_growth_pct_w"] < 0]

    ax.scatter(pos["energy_growth_pct_w"], pos["gdp_growth_pct_w"],
               s=16, color=COLOR_POS, alpha=0.35, linewidths=0,
               label="Energy growth ≥ 0")
    ax.scatter(neg["energy_growth_pct_w"], neg["gdp_growth_pct_w"],
               s=16, color=COLOR_NEG, alpha=0.35, linewidths=0,
               label="Energy growth < 0")

    b0 = cond_fit.params["Intercept"]
    b1 = cond_fit.params["energy_growth_pct_w"]
    d0 = cond_fit.params["neg_energy"]
    d1 = cond_fit.params["energy_growth_pct_w:neg_energy"]
    p_d1 = cond_fit.pvalues["energy_growth_pct_w:neg_energy"]

    x_pos = np.linspace(0, pos["energy_growth_pct_w"].max(), 50)
    ax.plot(x_pos, b0 + b1 * x_pos, color=COLOR_POS, linewidth=2.5, zorder=5,
            label=f"Fit, energy growth ≥ 0 (slope {b1:.3f})")

    x_neg = np.linspace(neg["energy_growth_pct_w"].min(), 0, 50)
    ax.plot(x_neg, (b0 + d0) + (b1 + d1) * x_neg, color=COLOR_NEG, linewidth=2.5,
            zorder=5, label=f"Fit, energy growth < 0 (slope {b1 + d1:.3f})")

    n_pos, n_neg = len(pos), len(neg)
    ax.text(
        0.02, 0.97,
        f"Slope, energy growth ≥ 0:  {b1:.3f}  (N = {n_pos:,})\n"
        f"Slope, energy growth < 0:  {b1 + d1:.3f}  (N = {n_neg:,})\n"
        f"Difference in slopes: {d1:+.3f}  (p = {p_d1:.3f})   R² = {cond_fit.rsquared:.3f}",
        transform=ax.transAxes, ha="left", va="top", fontsize=10,
        color=COLOR_INK_SECONDARY,
    )

    ax.axhline(0, color=COLOR_AXIS, linewidth=0.8, zorder=1)
    ax.axvline(0, color=COLOR_AXIS, linewidth=0.8, zorder=1)
    ax.set_xlabel("Primary energy consumption growth (%, y/y)", color=COLOR_INK_PRIMARY, fontsize=11)
    ax.set_ylabel("Real GDP growth (%, y/y)", color=COLOR_INK_PRIMARY, fontsize=11)
    ax.set_title(
        "GDP growth conditional on the sign of energy consumption growth\n"
        "Country panel, 1965–2023 — Energy Institute Statistical Review × World Bank",
        color=COLOR_INK_PRIMARY, fontsize=12, pad=14,
    )
    ax.text(
        0.5, -0.14,
        f"Both series winsorized at the {WINSOR_PCT:.0f}% / {100-WINSOR_PCT:.0f}% percentiles; "
        "lines from gdp_growth_pct_w ~ energy_growth_pct_w * 1{energy_growth < 0}",
        transform=ax.transAxes, ha="center", va="top", fontsize=8, color=COLOR_INK_MUTED,
    )

    ax.grid(True, color=COLOR_GRID, linewidth=0.8, zorder=0)
    for spine in ax.spines.values():
        spine.set_color(COLOR_AXIS)
    ax.tick_params(colors=COLOR_INK_MUTED, labelsize=9)

    legend = ax.legend(loc="lower right", frameon=False, fontsize=9)
    for text in legend.get_texts():
        text.set_color(COLOR_INK_SECONDARY)

    fig.tight_layout()
    fig.savefig(out_path, facecolor=COLOR_SURFACE)
    plt.close(fig)


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    print(f"Loading energy panel from {EI_PATH.name} ...")
    energy = load_energy_panel(EI_PATH, EI_SHEET)
    n_countries = energy["iso3"].nunique()
    print(f"  {len(energy):,} country-year observations, {n_countries} countries, "
          f"{energy['year'].min()}-{energy['year'].max()}")

    print("Fetching World Bank GDP data (NY.GDP.MKTP.KD) ...")
    gdp = fetch_wb_gdp(list(energy["iso3"].unique()), WB_INDICATOR, WB_DATE_RANGE)
    print(f"  {len(gdp):,} country-year GDP observations")

    print("Computing growth rates and merging ...")
    panel = build_growth_panel(energy, gdp)
    print(f"  {len(panel):,} country-year observations with both growth rates, "
          f"{panel['iso3'].nunique()} countries, {panel['year'].min()}-{panel['year'].max()}")

    panel = winsorize_panel(panel, WINSOR_PCT)
    panel.to_csv(OUT_PANEL_CSV, index=False)
    print(f"  panel written to {OUT_PANEL_CSV.name}")
    n_capped_gdp = int((panel["gdp_growth_pct"] != panel["gdp_growth_pct_w"]).sum())
    n_capped_energy = int((panel["energy_growth_pct"] != panel["energy_growth_pct_w"]).sum())
    print(f"Winsorizing at {WINSOR_PCT:.0f}%/{100-WINSOR_PCT:.0f}%: capped "
          f"{n_capped_gdp} GDP growth and {n_capped_energy} energy growth observations")

    print("Running regressions ...")
    pooled, fe = run_regressions(panel)
    cond, cond_fe = run_conditional_regression(panel)

    n_neg = int((panel["energy_growth_pct_w"] < 0).sum())

    with OUT_REGRESSION_TXT.open("w", encoding="utf-8") as f:
        f.write("Energy consumption growth vs. GDP growth -- regression analysis\n")
        f.write(f"Dependent variable: GDP growth (%, y/y)   "
                f"Independent variable: energy consumption growth (%, y/y)\n")
        f.write(f"Panel: {panel['iso3'].nunique()} countries, "
                f"{panel['year'].min()}-{panel['year'].max()}, N = {len(panel)}   "
                f"(winsorized at {WINSOR_PCT:.0f}%/{100-WINSOR_PCT:.0f}%; "
                f"{n_neg} obs with negative energy growth)\n")
        f.write("=" * 78 + "\n\n")
        f.write("(1) Pooled OLS -- gdp_growth_pct_w ~ energy_growth_pct_w\n")
        f.write("    Standard errors clustered by country\n")
        f.write("-" * 78 + "\n")
        f.write(pooled.summary().as_text())
        f.write("\n\n")
        f.write("(2) OLS with country and year fixed effects\n")
        f.write("    gdp_growth_pct_w ~ energy_growth_pct_w + C(iso3) + C(year)\n")
        f.write("    Standard errors clustered by country (fixed-effect dummies omitted below)\n")
        f.write("-" * 78 + "\n")
        coef_table = fe.summary2().tables[1]
        keep = [i for i in coef_table.index if not i.startswith("C(")]
        f.write(coef_table.loc[keep].to_string())
        f.write(f"\n\nR-squared: {fe.rsquared:.4f}   N: {int(fe.nobs)}\n\n")
        f.write("(3) Conditional (asymmetric) regression\n")
        f.write("    gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy\n")
        f.write("    neg_energy = 1{energy_growth_pct_w < 0}   Standard errors clustered by country\n")
        f.write("    energy-growth slope is b[energy_growth_pct_w] when energy growth >= 0,\n")
        f.write("    and b[energy_growth_pct_w] + b[energy_growth_pct_w:neg_energy] when energy growth < 0\n")
        f.write("-" * 78 + "\n")
        f.write(cond.summary().as_text())
        f.write("\n\n")
        f.write("(4) Conditional (asymmetric) regression with country and year fixed effects\n")
        f.write("    gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy + C(iso3) + C(year)\n")
        f.write("    Standard errors clustered by country (fixed-effect dummies omitted below)\n")
        f.write("-" * 78 + "\n")
        coef_table = cond_fe.summary2().tables[1]
        keep = [i for i in coef_table.index if not i.startswith("C(")]
        f.write(coef_table.loc[keep].to_string())
        f.write(f"\n\nR-squared: {cond_fe.rsquared:.4f}   N: {int(cond_fe.nobs)}\n")
    print(f"  regression summary written to {OUT_REGRESSION_TXT.name}")

    print("Drawing scatterplots ...")
    make_scatter(panel, pooled, OUT_SCATTER_PNG)
    print(f"  scatterplot written to {OUT_SCATTER_PNG.name}")
    make_conditional_scatter(panel, cond, OUT_COND_SCATTER_PNG)
    print(f"  conditional scatterplot written to {OUT_COND_SCATTER_PNG.name}")

    b1 = pooled.params["energy_growth_pct_w"]
    b1_neg_delta = cond.params["energy_growth_pct_w:neg_energy"]
    print(f"\nPooled OLS: a 1pp increase in energy consumption growth is associated "
          f"with a {b1:.3f}pp change in GDP growth")
    print(f"Conditional on negative energy growth, that slope shifts by "
          f"{b1_neg_delta:+.3f}pp (to {b1 + b1_neg_delta:.3f}pp), "
          f"p={cond.pvalues['energy_growth_pct_w:neg_energy']:.3f}")

    # ── Per-carrier growth regressions ───────────────────────────────────────
    print("\nBuilding per-carrier growth panels ...")
    carrier_panels = []
    carrier_fits = {}
    for carrier, sheet in CARRIER_SHEETS.items():
        cp = build_carrier_panel(carrier, sheet, energy, panel, WINSOR_PCT)
        carrier_panels.append(cp)
        carrier_fits[carrier] = run_carrier_regression(cp)
        print(f"  {carrier:<10} {len(cp):,} obs, {cp['iso3'].nunique()} countries")

    carrier_panel_all = pd.concat(carrier_panels, ignore_index=True)
    carrier_panel_all.to_csv(OUT_CARRIER_PANEL_CSV, index=False)
    print(f"  carrier panel written to {OUT_CARRIER_PANEL_CSV.name}")

    with OUT_CARRIER_REGRESSION_TXT.open("w", encoding="utf-8") as f:
        f.write("GDP growth vs. per-carrier energy consumption growth -- regression analysis\n")
        f.write("Dependent variable: GDP growth (%, y/y, winsorized -- gdp_growth_pct_w)\n")
        f.write("Independent variable: carrier's own consumption growth (%, y/y, winsorized\n")
        f.write("per carrier -- carrier_growth_pct_w), interacted with share_lag = that\n")
        f.write("carrier's share of TOTAL primary energy consumption in the PREVIOUS year.\n")
        f.write("The interaction tests whether a carrier's growth matters more for GDP\n")
        f.write("growth the larger its predetermined weight in the energy mix.\n")
        f.write("=" * 88 + "\n\n")

        f.write("Summary across carriers\n")
        f.write("-" * 88 + "\n")
        header = f"{'Carrier':<12}{'N':>7}{'b(growth)':>12}{'b(share_lag)':>14}{'b(interaction)':>16}{'p(interact)':>13}{'R2':>8}\n"
        f.write(header)
        for carrier, fit in carrier_fits.items():
            b_g = fit.params["carrier_growth_pct_w"]
            b_s = fit.params["share_lag"]
            b_i = fit.params["carrier_growth_pct_w:share_lag"]
            p_i = fit.pvalues["carrier_growth_pct_w:share_lag"]
            f.write(
                f"{carrier:<12}{int(fit.nobs):>7}{b_g:>12.3f}{b_s:>14.3f}"
                f"{b_i:>16.3f}{p_i:>13.3f}{fit.rsquared:>8.3f}\n"
            )
        f.write("\n" + "=" * 88 + "\n\n")

        for i, (carrier, fit) in enumerate(carrier_fits.items(), start=1):
            cp = carrier_panels[i - 1]
            f.write(f"({i}) {carrier} -- gdp_growth_pct_w ~ carrier_growth_pct_w * share_lag\n")
            f.write(f"    N = {len(cp)}, {cp['iso3'].nunique()} countries, "
                    f"{cp['year'].min()}-{cp['year'].max()}\n")
            f.write("    Standard errors clustered by country\n")
            f.write("-" * 88 + "\n")
            f.write(fit.summary().as_text())
            f.write("\n\n")
    print(f"  carrier regression summary written to {OUT_CARRIER_REGRESSION_TXT.name}")


if __name__ == "__main__":
    sys.exit(main())
