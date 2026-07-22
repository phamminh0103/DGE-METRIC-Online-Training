# Financing Pathway (Day 1 Afternoon)

This page is the training deep-dive for the green-finance pathway used in the Day 1 afternoon
online session. Like `docs/energy_efficiency_pathway.md`, it focuses on **the model equations**:
for each shock variable that defines a green-finance (GF) scenario, (1) the literal Dynare `.mod`
equation it enters, (2) the formula that computes its value from the finance-assumptions workbook,
and (3) a real, verified example pulled directly from the generated scenario workbook.

## Your worksheet — the target, blank

This is what you're ultimately filling in: six scenario sheets
(`PDP8_GF_A/B/C`, `NZ_GF_A/B/C`), each with the same 8 columns. Unlike the EE pathway, there is no
25-row time series to fill in here — every value below (other than the two switch columns'
last-year exception) is a **single constant applied to all 25 years**, so the worksheet only needs
one row per financing scenario, not one row per year.

### The 4 values that differ by scenario (A vs B vs C) — identical for the PDP8 and NZ parent

| Scenario | `exo_r_G_3_1` | `exo_r_FDI_3_1` | `exo_sIGShare_3_1` | `exo_sFDIShare_3_1` |
|---|---|---|---|---|
| A — Balanced | | | | |
| B — Market-led | | | | |
| C — Public-led | | | | |

Each row above gets copied into **two** sheets: e.g. row A's four values go into both
`PDP8_GF_A` and `NZ_GF_A`, unchanged — that's the whole reason 3 rows of arithmetic produce 6
scenario sheets.

### The 2 values that are the same in every scenario and every sheet — fill in now, no calculation needed

| | Every year except the last | The last simulated year only |
|---|---|---|
| `exo_lIGShare_3_1` | | |
| `exo_lFDIShare_3_1` | | |
| `exo_CapTrade_1` | | *(same value both columns)* |

Work through the sections below, then come back and fill in every blank cell above.

## Policy framing

Question: how much macroeconomic difference comes from *how* the transition is financed
(public-led vs market-led vs concessional-heavy), holding the physical transition task (capacity
build-out, emissions path) constant?

Scenario family — three financing mixes, applied only to the **renewables subsector** (subsector 3,
region 1):

- `GF_A` — balanced finance
- `GF_B` — market-led finance
- `GF_C` — public-led (concessional-heavy) finance

Each is run on two parent paths, giving 6 scenario sheets total:

- PDP8 baseline parent: `PDP8_GF_A`, `PDP8_GF_B`, `PDP8_GF_C`
- Net-zero parent: `NZ_GF_A`, `NZ_GF_B`, `NZ_GF_C`

**Unlike the EE pathway, there is no "stripped-down" counterfactual sheet here.** The EE pathway's
`_NoBESS` twin isolates one channel by reverting 3 of 10 columns to baseline; the financing pathway
instead compares three *complete* alternatives (A vs B vs C) against each other directly — each
represents a different, internally-consistent financing mix, not a full scenario with one piece
removed. The PDP8-vs-NZ split additionally shows whether the financing effect is bigger or smaller
depending on how ambitious the underlying physical transition is.

## Source data

Primary source workbook: `ExcelFiles/PDP8/Vietnam_Green_Finance_Scenarios_April2026.xlsx`, sheet
`Assumptions`. Rows 7–13 hold, per financing instrument, an **allocation share** (% of the total
PDP8 investment need routed through that instrument) and an **interest rate** (% p.a.), each given
separately for scenarios A/B/C:

| Instrument | Routed to | A share | B share | C share | A rate | B rate | C rate |
|---|---|---|---|---|---|---|---|
| ODA / bilateral concessional | public (`K_G`) | 4% | 2% | 8% | 1.5% | 1.5% | 1.0% |
| MDB concessional | public (`K_G`) | 4% | 2% | 8% | 1.0% | 1.0% | 0.9% |
| Blended finance — public sub-tranche | public (`K_G`) | 1% | 0.6% | 3% | 1.0% | 1.0% | 1.0% |
| Blended finance — private sub-tranche | FDI (`K_FDI`) | 4% | 2.4% | 12% | 6.0% | 6.5% | 6.0% |
| Green bonds — sovereign/quasi | public (`K_G`) | 10% | 5% | 17.5% | 4.0% | 4.3% | 3.6% |
| Green bonds — corporate | FDI (`K_FDI`) | 10% | 10% | 7% | 6.5% | 7.0% | 6.0% |
| Green credit — commercial banks | *residual* (`K_H`) | 67% | 78% | 44.5% | 7.5% | 8.0% | 7.0% |

Each column of shares sums to 100%. **Only 6 of the 7 instruments feed an `exo_*` shock at all** —
green credit from commercial banks is treated as ordinary domestic private capital (`K_H`) and gets
no special treatment; it is what's left over once the public and FDI buckets are pulled out. This
is a structural modeling choice, not a data gap: the model only needs to represent financing
*channels that behave differently* from ordinary domestic capital (government-backed and
foreign-owned), so bank credit — priced and behaved like any other domestic loan — doesn't need its
own variable.

## Constants used in every equation below

| Constant | Value | Meaning |
|---|---|---|
| `rf0_p` | `1/beta_p − 1 + deltaB_p = 1/0.95 − 1 + 0.05 = 0.10263` (≈10.26%) | the model's benchmark required return — every financing rate below is expressed as a **wedge relative to this**, not as a rate in isolation |
| `iSubsecRen`, `iReg` | `3`, `1` | all financing shocks in this pathway apply only to the renewables subsector, region 1 — hence every variable name ends in `_3_1` |

Because every real financing rate in the Assumptions sheet (1–8% p.a.) is well below `rf0_p`
(10.26%), every rate-wedge shock computed below comes out **negative** — concessional/public/FDI
financing is being modeled as cheaper than the model's default cost of capital, which is exactly the
mechanism a "green finance" scenario is meant to represent.

## The 7 shock variables — model equation, derivation, and a real worked value

Every GF scenario sheet has 8 columns: `Time`, the 6 variables below computed by
`scripts/maintenance/CreateGreenFinanceScenarios.m`, plus `exo_CapTrade_1` (see the note on this
one at the end — it is present in the live workbook but **not** written by the script as it exists
today).

### 1. `exo_r_G_3_1` — public-capital rental-rate wedge

**Model equation** (`ModFiles/Equations/government.mod:182-188`):
```
r_G_3_1 * P_K_3_1 / P_INV_3_1(-1) = rf0_p + exo_r_G_3_1
```
`r_G_3_1` is the rental rate the model pays on government-backed capital (`K_G`) in the renewables
sector. Setting `exo_r_G_3_1` to a negative number lowers this required return below the model's
benchmark `rf0_p` — representing concessional/public financing being cheaper than ordinary capital.

**Derivation (MATLAB):**
```
WACF = Σ_instrument (share_instrument × rate_instrument)      # weighted-average cost of finance
exo_r_G_3_1 = WACF − rf0_p
```
using every instrument's share and rate (all 7 rows, not just the public ones — WACF is a
blended cost across the *whole* $136bn financing need, then applied as the public-capital rate).

**Verified value:** using the table above for scenario A: `WACF_A = 0.04×0.015 + 0.04×0.01 +
0.01×0.01 + 0.04×0.06 + 0.10×0.04 + 0.10×0.065 + 0.67×0.075 = 0.06425` (6.425%, matching the
Assumptions sheet's own "Weighted Avg Cost of Finance" cell exactly). `exo_r_G_3_1 = 0.06425 −
0.10263 = −0.03838`. **The live `PDP8_GF_A` sheet currently has `exo_r_G_3_1 = −0.016`, not
−0.03838 — see the data-integrity note below.**

### 2. `exo_r_FDI_3_1` — FDI-capital rental-rate wedge

**Model equation** (`ModFiles/Equations/government.mod:206-213`):
```
r_FDI_3_1 * (P_K_3_1 / P_INV_3_1(-1)) ^ exo_lIGShare_3_1 = exo_r_FDI_3_1 + rf0_p
```
Same idea as `exo_r_G_3_1`, but for foreign-owned capital (`K_FDI`) — the rate of return that flows
back abroad to foreign investors via the net-foreign-asset law of motion in `households.mod`. (The
`^ exo_lIGShare_3_1` exponent is a unit-normalization detail tied to whether public capital is in
share mode or level mode that period — it does not change which instruments feed this variable.)

**Derivation:**
```
fdi_rate = Σ_(FDI instruments) (share × rate) / Σ_(FDI instruments) share     # share-weighted average, FDI instruments only
exo_r_FDI_3_1 = fdi_rate − rf0_p
```
Only the two instruments routed to FDI (blended-finance private sub-tranche, corporate green
bonds) enter this average — not the full 7-instrument mix used for `exo_r_G_3_1`.

**Verified value (scenario A):** `fdi_rate_A = (0.04×0.06 + 0.10×0.065) / (0.04+0.10) = 0.0089 /
0.14 = 0.063571` (6.357%). `exo_r_FDI_3_1 = 0.063571 − 0.10263 = −0.03906`. **The live sheet has
`exo_r_FDI_3_1 = −0.0173`, not −0.03906 — same data-integrity caveat as above.**

### 3–4. `exo_lIGShare_3_1` / `exo_sIGShare_3_1` — public-capital share target

**Model equation** (`ModFiles/Equations/government.mod:190-204`):
```
I_G_3_1 = (1 − exo_lIGShare_3_1) × [ phiG_3_1_p × delta_3_1_p × K0_3_1_p × exp(exo_K_G_3_1) ]
        +      exo_lIGShare_3_1  × [ exo_sIGShare_3_1 × I_3_1 ]
```
When `exo_lIGShare_3_1 = 0` (the model's ordinary default), government investment `I_G` in
renewables just replaces depreciated public capital along an exogenous path. When
`exo_lIGShare_3_1 = 1` (what every GF scenario sets, in every year but the last), the equation
switches branches entirely: `I_G` is instead forced to equal `exo_sIGShare_3_1` **times total
sector investment** `I_3_1` — i.e. public financing is pinned to always fund exactly that fraction
of whatever renewables investment happens to be that period, growing or shrinking automatically
with the sector.

**Derivation:**
```
exo_lIGShare_3_1(t) = 1  for every year except the last simulated year, where it is 0
exo_sIGShare_3_1(t) = Σ_(public instruments) share       (ODA + MDB + blended-public + sovereign bonds)
                       — constant across every year
```

**Verified value:** scenario A public share = `0.04+0.04+0.01+0.10 = 0.19`. The live `PDP8_GF_A`
sheet has `exo_sIGShare_3_1 = 0.19` in every row — **this one matches exactly**, unlike the rate
variables above (see data-integrity note). `exo_lIGShare_3_1` is `1` for rows (Time) 2–25 and `0` on
the final row (Time 26) in every GF sheet — confirmed directly.

**Why does the switch flip to 0 only in the last period?** Share mode (`=1`) makes `I_G` depend on
the *current-period* value of total investment `I_3_1`. In the very last period of a
perfect-foresight simulation there is no future to pin down a terminal condition the normal way, so
the scenario writer reverts to the ordinary exogenous-replacement branch for that one period only,
avoiding a simultaneity issue at the terminal date. This is a numerical housekeeping detail, not a
policy statement about the last year.

### 5–6. `exo_lFDIShare_3_1` / `exo_sFDIShare_3_1` — FDI-capital share target

**Model equation** (`ModFiles/Equations/investment_wedge.mod:56-61`):
```
sFDI_eff_3_1 = exo_sFDIShare_3_1
(1 − exo_lFDIShare_3_1) × I_FDI_3_1 × P_INV_3_1  +  exo_lFDIShare_3_1 × I_FDI_3_1
    = (1 − exo_lFDIShare_3_1) × phiFDI0_3_1_p × (1 − exo_I_FDI_3_1) × Y0_p
    +      exo_lFDIShare_3_1  × sFDI_eff_3_1 / (1 − phiG_3_1_p) × I_3_1
```
Exactly the same mechanic as `exo_lIGShare_3_1`/`exo_sIGShare_3_1` above, but for foreign-owned
capital: when `exo_lFDIShare_3_1 = 1`, `K_FDI` is targeted as a share of total sector capital, and
the implied FDI investment flow `I_FDI` is backed out from `K_FDI`'s own law of motion
(`investment_wedge.mod:47-52`, `K_FDI/PoP = (1−delta)×K_FDI(-1)/PoP(-1) + I_FDI/PoP`).

**Derivation:**
```
exo_lFDIShare_3_1(t) = 1  for every year except the last (same terminal-period rule as above)
exo_sFDIShare_3_1(t) = Σ_(FDI instruments) share       (blended-private + corporate green bonds)
                        — constant across every year
```

**Verified value:** scenario A FDI share = `0.04+0.10 = 0.14`. The live sheet has
`exo_sFDIShare_3_1 = 0.14` in every row — matches exactly.

### 7. `exo_CapTrade_1` — present in the live sheet, not written by the current script

The live `PDP8_GF_A`/`PDP8_GF_B`/`PDP8_GF_C`/`NZ_GF_*` sheets each have an 8th column,
`exo_CapTrade_1`, set to `1` in every row. **`CreateGreenFinanceScenarios.m` as it exists today does
not write this column at all** — its header list (`hdrs` in the script) has only 7 entries (`Time`
plus the 6 financing variables above). This means the 6 GF sheets currently in the workbook were
generated by an earlier version of the script (or written/edited by some other means) and are
already out of sync with what re-running the current script would produce — regenerating today
would **drop this column entirely**, in addition to changing the rate values (below). See the
energy-efficiency pathway doc for what `exo_CapTrade_1` does when it is present
(`ModFiles/Equations/climate_emissions.mod:60-76`, scaled by `phiG_p = 0` in the active
calibration — currently inert either way).

## Summary table

| # | Variable | Model equation location | Fed by (Assumptions workbook) | Time-varying? |
|---|---|---|---|---|
| 1 | `exo_r_G_3_1` | `government.mod:182-188` | WACF across all 7 instruments, minus `rf0_p` | No — constant every year |
| 2 | `exo_r_FDI_3_1` | `government.mod:206-213` | share-weighted rate of the 2 FDI instruments, minus `rf0_p` | No — constant every year |
| 3 | `exo_lIGShare_3_1` | `government.mod:190-204` | always 1, except last year (0) | Only at the terminal period |
| 4 | `exo_sIGShare_3_1` | `government.mod:190-204` | sum of the 4 public-instrument shares | No — constant every year |
| 5 | `exo_lFDIShare_3_1` | `investment_wedge.mod:56-61` | always 1, except last year (0) | Only at the terminal period |
| 6 | `exo_sFDIShare_3_1` | `investment_wedge.mod:56-61` | sum of the 2 FDI-instrument shares | No — constant every year |
| 7 | `exo_CapTrade_1` | `climate_emissions.mod:60-76`, scaled by `phiG_p = 0` | constant `1`, not written by the current script | No — and currently inert |

## Why there is no extrapolation section here

The EE pathway needs an extrapolation rule because expert data is given year-by-year and can run
out before the simulation horizon ends. The financing pathway has the opposite structure: every
variable except the two share-mode switches is a **single number derived once** from the
Assumptions workbook and then held constant for the entire 25-year horizon — there is no year-by-
year data to run out of, so there is nothing to extrapolate. The only place time enters at all is
the one-period terminal-year override on `exo_lIGShare_3_1`/`exo_lFDIShare_3_1` described above,
which is a fixed rule (last period only), not a trend continuation.

## Data-integrity note (checked against the live workbook)

Comparing the values actually written into `PDP8_GF_A`/`PDP8_GF_B`/`PDP8_GF_C` against the current
`Vietnam_Green_Finance_Scenarios_April2026.xlsx`:

- **Shares are in sync.** `exo_sIGShare_3_1` and `exo_sFDIShare_3_1` for all three scenarios match
  the current Assumptions sheet's allocation shares exactly (A: 0.19/0.14, B: 0.096/0.124,
  C: 0.365/0.19).
- **Rates are not in sync.** Recomputing `exo_r_G_3_1`/`exo_r_FDI_3_1` from the current
  Assumptions sheet's interest-rate column gives −0.03838/−0.03906 (A), but the live sheet has
  −0.016/−0.0173. Backing out the implied WACF from the live sheet
  (`exo_r_G_3_1 + rf0_p`) gives ≈8.66% for scenario A, versus the Assumptions sheet's current
  6.425% — the **interest-rate assumptions have been revised since these sheets were last
  generated**, while the **allocation-share assumptions have not**.
- **A whole column has been added or dropped.** `exo_CapTrade_1` exists in the live sheets but is
  absent from the current script's output columns (see variable 7 above).

Regenerate the GF scenario sheets with `run('scripts/maintenance/CreateGreenFinanceScenarios.m')`
before using them for any run whose conclusions depend on the specific financing-rate wedge, not
just the relative ordering of A vs B vs C (which is unaffected — C is public-led/cheapest in both
the live sheet and a fresh recompute, in both cases).

## Day 1 afternoon workflow

1. Confirm scenario assumptions and WACF mapping in the finance source workbook.
2. Check that translated shock paths are present in the model scenarios workbook — and, given the
   data-integrity note above, whether they need regenerating first.
3. Verify the intended run set in `RunSimulations.m` (or `DGE_SCENARIO_GROUPS`).
4. Run scenarios.
5. Review comparative outputs with a focus on renewable WACC and GDP-growth deviations.

## Related references

- `docs/scenarios_overview.md`
- `docs/use_cases_finance.md`
- `docs/running.md`
- `docs/energy_efficiency_pathway.md` — the companion EE pathway doc, same equation-first structure
