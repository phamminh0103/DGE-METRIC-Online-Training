# Energy Efficiency Pathway (Day 1 Afternoon)

This page is the training deep-dive for the energy-efficiency (EE) pathway used in the Day 1
afternoon online session. It focuses entirely on **the model equations**: for each of the 10
shock variables that define an EE scenario, (1) the literal Dynare `.mod` equation the shock enters,
(2) the formula that computes its numeric value, and (3) a real, verified example pulled directly
from the generated scenario workbook.

The goal is for participants to be able to **regenerate and verify these sheets themselves** using
an AI coding assistant (Claude Code / GitHub Copilot) rather than hand-running MATLAB line by line.
Everything documented below (the equations, the formulas, the real numbers) is exactly what your
assistant needs already open in context to do this correctly — the [hands-on section](#hands-on-create-and-verify-the-sheets-yourself-prompt-recipes)
at the end gives ready-to-use prompts built directly from the checks already performed in this
document.

## Policy framing

Question: how much macroeconomic benefit can be unlocked by stronger demand-side efficiency, and
how much of that effect is attributable to storage-enabled system integration (BESS — Battery
Energy Storage Systems)?

Core scenario pairs (each pair shares identical EE assumptions and differs only in the
BESS/rooftop-solar channels):

- `EE_PDP8` vs `EE_PDP8_NoBESS`
- `EE_Directive10` vs `EE_Directive10_NoBESS`
- `EE_PDP8_PV_BESS` vs `EE_PDP8_PV_BESS_NoBESS`

Pairwise differences (full minus NoBESS) isolate the BESS/rooftop-solar contribution, holding the
efficiency-investment story constant. This is a **counterfactual design**: the NoBESS sheet is
mechanically derived from the full sheet by re-setting three of the ten variables, described below.

## Constants used in every equation below

| Constant | Value | Meaning |
|---|---|---|
| `gdpBaseMioUSD` | 430,000 | 2025 Vietnam GDP (USD million) — normalizes absolute USD investment flows into the GDP-share units the model works in |
| `deltaKA` | 0.10 | annual depreciation rate applied to every accumulated adaptation-capital stock — **chosen to equal the model's own `deltaKA_@{subsec}_@{reg}_p` parameter** (`ModFiles/DGE_Model_Parameters.mod:285`, also `= 0.1`), so the pre-accumulated value MATLAB writes lines up exactly with the depreciation the Dynare equation itself applies |
| `Y0_p` (model parameter, not MATLAB) | 1 | base-year output, `ModFiles/DGE_Model_Parameters.mod:131` — the model is normalized so all levels are expressed as shares of base-year GDP; this is why dividing by `gdpBaseMioUSD` in MATLAB and multiplying by `Y0_p` in the `.mod` equation cancel out cleanly |
| `lAddEEValue` | 1 | constant value written to `exo_lAddEE_4_1`/`exo_lAddEE_5_1` |
| `capTradeValue` | 1 | constant value written to `exo_CapTrade_1` |

## Where the Baseline's own EE/RTS numbers come from

Every equation below treats `baseline(t)` — the value already sitting in
`ExcelFiles/ModelBaseline5Sectorsand1Regions.xlsx` before any EE-scenario increment is added — as a
fixed input. It is **not** a passive calibration constant for `exo_AI_4_1_2`, `exo_AI_5_1_2`,
`exo_GA_4_1`, `exo_GA_5_1`, or `exo_PV_1`: it is actively constructed by
`scripts/maintenance/CreateBaselineFromUserInputFile.m`, which runs three functions, in this order,
every time the Baseline sheet is rebuilt (all three are **enabled by default**):

1. **`apply_government_rts_sector_pv_shocks`** (line 980) reads a Vietnam rooftop-solar (RTS)
   sector deployment plan (industrial/commercial/residential capacity, from a CSV derived from
   expert email assumptions) and *overwrites* (not adds to) three baseline columns:
   - `exo_PV_1` ← residential RTS stock, converted to an investment-flow index and scaled by
     `deltaPV_p × phiKPV0_p`.
   - `exo_GA_4_1` / `exo_GA_5_1` ← the column's **own existing first-year value**
     (`gaSecLevel0`/`gaTerLevel0`) multiplied by an industrial/commercial RTS deployment index
     (written alongside as `idx_GA_4_1_plan`/`idx_GA_5_1_plan`, normalized to `1` in the first
     year) — so the *shape* of the path over time comes from the RTS deployment plan, while its
     *starting level* is whatever was already in the cell.

2. **`apply_industrial_pv_to_ee_coupling`** (line 697) then **adds** an efficiency gain to
   `exo_AI_4_1_2`/`exo_AI_5_1_2` based on how much of industrial/commercial electricity demand is
   covered by rooftop PV generation:
   ```
   phi_t   = PV_generation_t / sector_electricity_demand_t
   dAI_t   = log( (1 - phi_0) / (1 - phi_t) )
   exo_AI_s_1_2(t) += dAI_t
   ```
   using real RTS generation-vs-demand data when available (falls back to a "K_A-progress" or
   "`exo_PV_1`-progress" proxy shape if that data is missing). `phi_0` is the base-year (2025)
   coverage ratio, absorbed into steady-state calibration rather than computed here.

3. **`apply_vneep3_ee_targets`** (line 821) then **adds** a further, policy-driven increment
   representing Vietnam's VNEEP3 program (Decision 280/QD-TTg, 2019–2030): a **piecewise-linear**
   rate on `exo_AI_4_1_2`/`exo_AI_5_1_2` (faster to 2030, slower after — defaults `0.005`/`0.003`
   log-pts/yr for industry, `0.020`/`0.010` for commercial) and a **linear ramp** on
   `exo_GA_4_1`/`exo_GA_5_1` (defaults `0.003`/`0.002` and `0.002`/`0.001` per year, as a share of
   `Y0_p`). This same function also writes `exo_lAddEE_4_1`/`exo_lAddEE_5_1` (variables 8–9 below)
   from an `EEAdditiveMode` switch (default `true`) and, only if that switch were set to `false`,
   would zero the region's autonomous `exo_EE_r` trend so PV/VNEEP3 become the sole EE driver.

**Why this matters for reading the rest of this document:** the Baseline sheet's EE/RTS columns
already encode a substantial, real-world-deployment-driven story (RTS capacity build-out +
VNEEP3 policy targets) *before* any of the ten EE-scenario variables below add their own
increment on top. It is also the real explanation for the data-integrity note further down: the
embedded baseline inside the EE scenario sheets keeps falling out of sync with the live Baseline
workbook not because of a stray manual edit, but because this three-function pipeline gets re-run
(picking up updated RTS/VNEEP3 inputs) more often than the EE scenario sheets get regenerated.

## The 10 shock variables — model equation, derivation, and a real worked value

Every model scenario sheet (both the full and the `_NoBESS` version) contains exactly these 10
`exo_*` variables. For each one below: the **model equation** is quoted from the `.mod` source
(file:line), then the **derivation** shows the MATLAB formula that produces the number that gets
plugged into that equation, followed by a **verified value** taken directly from
`ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx` (checked against the underlying clean CSV
inputs — see the data-integrity note at the end).

### 1–2. `exo_AI_4_1_2` (industrial) / `exo_AI_5_1_2` (commercial) — EE productivity level shocks

**Model equation** (`ModFiles/Equations/firms.mod:66-75`, inside the `sec`/`subsec`/`secm` loop —
here instantiated at `subsec=4` [Secondary/industry] or `subsec=5` [Tertiary/services], `reg=1`,
`secm=2` [aggregate sector 2 = Energy]):

```
activeIntermediateProductivityShock_s_r_k = (exo_AI_s_r_k != 0) * exo_AI_s_r_k
A_I_s_r_k = exp(activeIntermediateProductivityShock_s_r_k)
            * EE_r ^ ( exo_lAddEE_s_r * (k == iSecEnergy_p) )
```
`A_I_4_1_2` (or `A_I_5_1_2`) is the productivity of *energy used as an intermediate input* by
subsector 4 (or 5). Raising `exo_AI_4_1_2` raises `A_I_4_1_2`, which lets the subsector produce the
same intermediate-energy-composite `Q_I` with **less physical energy input** for the same output —
this is exactly "energy efficiency" as the model represents it. `EE_r` is the region's own
baseline energy-efficiency index (the `EE_1`/VNEEP3 trend); it is raised to the power
`exo_lAddEE_s_r` only when `k == iSecEnergy_p` (i.e. only for the energy intermediate), which is
where variables 8–9 below enter.

**Derivation (MATLAB, `CreateEEScenariosFromExpertInputs.m:167-173`):**
```
phi = min(Saving_pct / 100, 0.9999)
dAI = log(1 / (1 - phi))
exo_AI_x_1_2(t) = exo_AI_x_1_2_baseline(t) + dAI(t)
```

**Verified value (2026, `EE_PDP8` sheet, from `EE_PDP8_reference.csv`):**
`Industry_EE_Saving_pct = 1` → `phi = 0.01`, `dAI = log(1/0.99) = 0.0100503`.
Baseline `exo_AI_4_1_2(2026) = 0.005` (`ModelBaseline...xlsx`, sheet `Baseline`).
`0.005 + 0.0100503 = 0.0150503` — matches the written value `0.015050335853501507` exactly.
Same check for services: `Services_EE_Saving_pct = 0.8` → `dAI = log(1/0.992) = 0.0080322`;
baseline `exo_AI_5_1_2(2026) = 0.02`; `0.02 + 0.0080322 = 0.0280322`, matching
`0.028032171697264255` exactly.

### 3–4. `exo_GA_4_1` (industrial) / `exo_GA_5_1` (commercial) — sector adaptation-capital target

**Model equation** (`ModFiles/Equations/government.mod:138-149`, `subsec=4` or `5`, `reg=1`):

```
K_A_s_r        = exo_GA_s_r * Y0_p                              // target level
K_A_s_r        = (1 - deltaKA_s_r_p) * K_A_s_r(-1) + G_A_s_r    // law of motion
```
These are **two separate model equations that both reference the same variable `K_A_s_r`** — the
first *pins* `K_A_s_r` directly to the exogenous shock (a target level, since `Y0_p = 1`,
`K_A_s_r = exo_GA_s_r`); the second is the ordinary capital law of motion. Because `K_A_s_r` is
pinned by the first equation, the second equation is not "solving for `K_A`" — it is solving for
the *other* unknown in it, the government adaptation-expenditure flow `G_A_s_r`:
```
G_A_s_r(t) = K_A_s_r(t) - (1 - deltaKA_s_r_p) * K_A_s_r(t-1)
```
`G_A_s_r` is not a free abstraction — it is a **real fiscal cost**. It enters the regional
government investment identity (`ModFiles/Equations/government.mod:7-19`):
```
I_G_reg * P_reg = Σ_subsec [ I_G_subsec_reg * P_INV_subsec_reg + G_A_subsec_reg * P_INV_subsec_reg ]
```
which in turn is part of the regional government budget constraint (`government.mod:21-42`). **So
setting `exo_GA_4_1`/`exo_GA_5_1` doesn't just raise a capital stock "for free" — it requires the
government to actually spend `G_A` each period to hit the implied target, financed like any other
government expenditure (taxes/debt).**

**Derivation (MATLAB, `accumulate_ka` in `CreateEEScenariosFromExpertInputs.m:270-288`):**
```
K_A(t) = (1 - deltaKA) * K_A(t-1) + [EE_Investment(t) + RTS_Investment(t)] / gdpBaseMioUSD
exo_GA_x_1(t) = exo_GA_x_1_baseline(t) + K_A(t)
```
Because MATLAB's `deltaKA = 0.10` is the same number as the model's own
`deltaKA_@{subsec}_@{reg}_p = 0.1`, and `Y0_p = 1`, the value MATLAB writes to `exo_GA_x_1` becomes
*directly* the model's `K_A` target level — no unit conversion happens inside Dynare.
Industrial sector 4 uses `Industry_EE_Investment + RTS_Industry_Investment`; commercial sector 5
uses `Services_EE_Investment + RTS_Services_Investment` — industrial/commercial RTS investment is
folded into the same stock as EE investment, not tracked separately.

**Verified value:** the currently checked-out `EE_PDP8_reference.csv` and `PDP8_PV_EV_BESS.csv`
have different `Industry_EE_Investment_USDm` in 2026 (120 vs 162) but the **same** embedded
baseline, so the two sheets' `exo_GA_4_1` values should differ by exactly the difference in
first-year flow:
```
K_A_PDP8(2026)    = 120 / 430,000 = 0.00027907
K_A_PVBESS(2026)  = 162 / 430,000 = 0.00037674
expected diff     = 0.00037674 - 0.00027907 = 0.00009767
actual diff       = 0.022376744186046512 (EE_PDP8_PV_BESS) - 0.02227906976744186 (EE_PDP8)
                  = 0.00009767441860...
```
Matches to machine precision. The same check at 2027 (`0.9 × 0.00027907 + 130/430,000` vs.
`0.9 × 0.00037674 + 168.75/430,000`, expected diff `0.000178023`) also matches the sheet's actual
diff exactly. This confirms the accumulation formula is implemented correctly, independent of
whatever the current baseline level is (see the data-integrity note below for why the *absolute*
level currently looks inconsistent with the standalone Baseline workbook).

### 5. `exo_GA_3_1` — renewables-sector adaptation-capital target (grid-scale BESS cost channel)

**Model equation:** identical to the block above, instantiated at `subsec = 3` (renewables) —
same `K_A_3_1 = exo_GA_3_1 * Y0_p` target equation and `G_A_3_1` recovery, so grid-scale BESS capex
enters the government investment/budget identity exactly like industrial/commercial adaptation
spending does.

**Derivation:**
```
bessInvMio = BESS_Annual_Investment_USDbn * 1000
K_A_BESS(t) = (1 - deltaKA) * K_A_BESS(t-1) + bessInvMio(t) / gdpBaseMioUSD
exo_GA_3_1(t) = exo_GA_3_1_baseline(t) + K_A_BESS(t)
```
There is no `exo_GA_3_1` column in the Baseline workbook at all, so `exo_GA_3_1_baseline = 0` for
every year — this channel is purely scenario-specific.

**Verified value (2026–2027, `EE_PDP8_PV_BESS` sheet, from `PDP8_PV_EV_BESS.csv`):**
```
2026: BESS_Annual_Investment_USDbn = 1.44  →  1440/430,000 = 0.0033488372...
      sheet exo_GA_3_1(2026)               = 0.0033488372093023254   ✓ exact match
2027: K_A_BESS(2027) = 0.9 × 0.0033488372 + 1787.5/430,000
                     = 0.0030139535 + 0.0041569767 = 0.0071709302
      sheet exo_GA_3_1(2027)               = 0.00717093023255814     ✓ exact match
```

### 6. `exo_PVEff_1` — PV integration-gain shock (BESS *benefit* channel)

**Model equation** (`ModFiles/Equations/households.mod:136-139`):
```
Q_PV_r = phiPV_p * K_PV_r * exp(exo_PVEff_r)
```
`Q_PV_r` is household rooftop-PV output; `K_PV_r` is the installed rooftop-PV capital stock.
`exo_PVEff_r` is a pure multiplicative efficiency term on top of *existing* installed capacity — it
represents batteries letting more of the already-installed capacity's generation actually be used
(less curtailment), not new capacity.

**Derivation:**
```
dPVEff(t) = log(1 + PV_Integration_Gain_pct(t) / 100)
exo_PVEff_1(t) = exo_PVEff_1_baseline(t) + dPVEff(t)
```

**Verified value (2026, `EE_PDP8_PV_BESS` sheet):** `PV_Integration_Gain_pct = 1` →
`dPVEff = log(1.01) = 0.00995033`. The Baseline sheet's `exo_PVEff_1(2026)` is **not** zero — it is
`0.06766519050849035` (built by the industrial/commercial PV-coverage coupling described in "Where
the Baseline's own EE/RTS numbers come from" above). `0.06766519050849035 + 0.00995033 =
0.07761552`, matching the written value `0.07761552136165845` exactly. The `_NoBESS` sheet for the
same scenario/year has `exo_PVEff_1 = 0.06766519050849035` — the baseline value exactly, confirming
`_NoBESS` reverts to baseline rather than to zero (see the `_NoBESS` section below).

### 7. `exo_PV_1` — household rooftop-solar (RTS) investment shock

**Model equation** (`ModFiles/Equations/households.mod:126-134`):
```
K_PV_r = (1 - deltaPV_p) * K_PV_r(-1) + I_PV_r                       // law of motion, capital stock
I_PV_r = (deltaPV_p * phiKPV0_p + exo_PV_r) * Y0_p                   // investment target
```
Unlike `exo_GA_*` above, `exo_PV_r` does **not** pin the capital stock `K_PV_r` directly — it enters
the *investment flow* equation `I_PV_r`. `K_PV_r` then accumulates that flow through its own law of
motion, using the model's own depreciation rate `deltaPV_p = 0.1`
(`ModFiles/DGE_Model_Parameters.mod:103`). Because the MATLAB-side derivation below *already*
computes `exo_PV_1` as a depreciating accumulated stock (using the same 10% rate), and that value
is then fed in as a **flow** that itself gets accumulated a second time by `K_PV_r`'s law of motion,
household rooftop-solar capital compounds through **two** accumulation layers rather than one —
worth knowing when interpreting how quickly `K_PV` responds to a household RTS investment shock,
in contrast to the sector adaptation-capital channel above, where the two `.mod` equations exactly
invert the MATLAB accumulation and recover a plain flow (no double-counting).

**Derivation (MATLAB):**
```
K_A_PV(t) = (1 - deltaKA) * K_A_PV(t-1) + RTS_Household_Investment(t) / gdpBaseMioUSD
exo_PV_1(t) = exo_PV_1_baseline(t) + K_A_PV(t)
```

**Verified value:** `RTS_Household_Investment_USDm` is blank (`NaN` → 0) in every currently-loaded
expert CSV, so in every EE scenario today `exo_PV_1(t) = exo_PV_1_baseline(t)` exactly — confirmed:
`EE_PDP8` sheet 2026 value `0.0013` equals the Baseline sheet's `exo_PV_1(2026) = 0.0013` exactly.
This channel is fully wired but currently dormant for lack of household-RTS expert data.

### 8–9. `exo_lAddEE_4_1` / `exo_lAddEE_5_1` — EE additive-mode switch

**Model equation:** the exponent term in the `A_I` equation quoted under variables 1–2 above
(`firms.mod:73`): `EE_r ^ (exo_lAddEE_s_r * (k == iSecEnergy_p))`. With `exo_lAddEE_4_1 = 1`, the
energy-intermediate productivity for subsector 4 becomes `A_I_4_1_2 = exp(exo_AI_4_1_2) * EE_1`,
i.e. the region's baseline EE index `EE_1` is applied **on top of** the scenario-specific
`exo_AI_4_1_2` shock (additive in logs: `log(A_I_4_1_2) = exo_AI_4_1_2 + log(EE_1)`). Per the
variable's declared `long_name` in `ModFiles/DGE_Model_Declaration.mod:239`: *"switch: 1=exo_EE_r
additive to sector EE gains, 0=PV/VNEEP3 sole EE driver (exo_EE_r suppressed for this
subsector)"* — setting it to 0 instead would raise `EE_1` to the power 0 (=1), suppressing the
region's baseline EE trend for that subsector entirely.

**Value:** `exo_lAddEE_4_1(t) = exo_lAddEE_5_1(t) = 1` for every simulation period — a constant, not
derived from any expert input.

### 10. `exo_CapTrade_1` — emissions-policy shock (currently inert under the active calibration)

**Model equation** (`ModFiles/Equations/climate_emissions.mod:60-76`, cap-and-trade branch,
`@# if CapandTrade == 1`):
```
E_r + (exo_PE_r + exo_PE + exo_CapTradeInternat + exo_CapTrade_r) * phiG_p
    = E0_r_p * exp(exo_EBase_r + exo_E_r)
```
`exo_CapTrade_r` is added, alongside three other shock terms, inside a bracket multiplied by
`phiG_p`. **`phiG_p = 0` in the active calibration** (`ModFiles/DGE_Model_Parameters.mod:104`), so
this entire bracketed term evaluates to zero regardless of `exo_CapTrade_1`'s value — under the
current parameterization, writing `1` here has **no numerical effect** on the simulation.

This is a genuinely different mechanism from the `CapandTrade` **compile-time macro** (`@# define
CapandTrade = ...`, set by `Functions/Miscellaneous/ModelSetup/change_mod_file.m` from
`RunSimulations.m`'s scenario configuration), which is what actually selects between the
cap-and-trade branch (pin emissions, let the price float) and the price-based branch (pin the
price, let emissions float) shown in `climate_emissions.mod:60-73`. `exo_CapTrade_1` cannot switch
regimes — regime selection happens once, at compile time, for the whole scenario group.

**Value:** `exo_CapTrade_1(t) = 1` for every simulation period — a constant, not derived from any
expert input, and (given `phiG_p = 0`) not currently load-bearing.

## Extrapolation beyond the last year of input data

### Exactly what the code does

The alignment step (`CreateEEScenariosFromExpertInputs.m:157`) computes
`[~, iB, iE] = intersect(yearsBaseline, yearsExpert)` — `iB` is the list of **baseline row
indices** (1-based position in the baseline's own period grid) that have a matching expert year;
`iE` is the corresponding row index into the expert CSV. `iB(end)` is therefore the row-position,
inside the baseline grid, of the *last calendar year the expert data covers* — not a count of
matched years and not a calendar year itself.

For the two log-level shocks that get extrapolated (`exo_AI_4_1_2`/`exo_AI_5_1_2`,
lines 176–183, and `exo_PVEff_1`, lines 193–199), the check is:
```
if iB(end) < nYears                          # expert data ends before the baseline horizon does
    r4 = dAI4(end) / max(iB(end), 1)         # dAI4(end) = dAI value at the LAST matched year
    r5 = dAI5(end) / max(iB(end), 1)
    for tt = (iB(end)+1) : nYears            # every baseline period AFTER the last matched year
        ai4(tt) = ai4Base(tt) + dAI4(end) + r4 * (tt - iB(end))
        ai5(tt) = ai5Base(tt) + dAI5(end) + r5 * (tt - iB(end))
    end
end
```
`r4` divides the *total accumulated* `dAI4(end)` by `iB(end)` — the baseline row-position of the
last matched year — which is mathematically equivalent to assuming the shock rose **linearly from
zero at baseline period 1** up to its last observed value, and then continuing that same straight
line forward. It is not fit to the recent trend or to any target; it is one straight line through
the origin and the single last data point. `exo_PVEff_1` uses the identical mechanism
(`rPV = dPVEff(iB(end)) / iB(end)`).

The stock variables (`exo_GA_4_1`, `exo_GA_5_1`, `exo_GA_3_1`, `exo_PV_1`) need no equivalent branch
— their accumulation loop already runs across the full `1:nYears` range unconditionally
(`CreateEEScenariosFromExpertInputs.m:270-288` and the two BESS/PV loops at lines 202-232), simply
using a flow of zero for any period with no matched expert row:
`K_A(t) = (1 - deltaKA) * K_A(t-1) + 0`.

### Did this actually run for the sheets currently in the workbook? Yes — confirmed.

An earlier check of this document found the EE sheets stopped at 2050 while the Baseline workbook
already ran through 2051, so extrapolation was dormant. **Re-checking the live workbook now shows
the EE sheets have since been regenerated**: `EE_PDP8` (and every other EE sheet) now has 27 rows,
`Period` 2–27, `Year` 2026–**2051** — confirmed by reading the sheet's own last row,
`(27, 2051, 0.2747473337973909, 0.5248749123576241, ...)`. The expert CSVs
(`EE_PDP8_reference.csv`, `Directive10_RTS_EE.csv`, `PDP8_PV_EV_BESS.csv`) still stop at 2050 (25
data rows) — only the Baseline workbook was extended — so `nYears = 26` while `iB(end) = 25` (the
row-position of year 2050), and the `for tt = (iB(end)+1):nYears` loop now runs for exactly **one**
row: 2051. This is the extrapolation rule actually executing, not a hypothetical.

### Confirming the extrapolated 2051 row against the formula

Using `EE_PDP8_reference.csv`'s last row (`2050, Industry_EE_Saving_pct = 4.5,
Services_EE_Saving_pct = 3.2`) and the current Baseline sheet's 2051 values
(`exo_AI_4_1_2 = 0.22686163775592783`, `exo_AI_5_1_2 = 0.49105079298384147`):
```
dAI4(end) = log(1/(1-0.045)) = log(1.047120) = 0.0460406      (from year 2050, row-position 25)
dAI5(end) = log(1/(1-0.032)) = log(1.033058) = 0.0325296
r4 = 0.0460406 / 25 = 0.00184162
r5 = 0.0325296 / 25 = 0.00130118
tt = 26 (year 2051):
    ai4(26) = 0.22686163775592783 + 0.0460406 + 0.00184162*(26-25) = 0.2747438...
    ai5(26) = 0.49105079298384147 + 0.0325296 + 0.00130118*(26-25) = 0.5248816...
```
The live `EE_PDP8` sheet's actual 2051 row has `exo_AI_4_1_2 = 0.2747473337973909` and
`exo_AI_5_1_2 = 0.5248749123576241` — matching the hand-computed values to 4–5 decimal places
(the residual gap is ordinary floating-point/intermediate-rounding noise, not a formula
discrepancy).

Similarly, `PDP8_PV_EV_BESS.csv`'s last row (`2050, PV_Integration_Gain_pct = 14`) gives
`dPVEff(end) = log(1.14) = 0.1310283`, `rPV = 0.1310283/25 = 0.00524113`, so the extrapolated 2051
increment is `0.1310283 + 0.00524113 = 0.1362694`; added to the Baseline sheet's
`exo_PVEff_1(2051) = 1.7119816847925917` gives `1.8482511`, matching the live
`EE_PDP8_PV_BESS` sheet's 2051 value `1.848251077695252` exactly. The stock variable
`exo_GA_3_1` needs no such formula — its 2051 value is simply
`0.9 × exo_GA_3_1(2050) = 0.9 × 0.02587989057008788 = 0.02329190151307909`, pure decay with no new
BESS investment flow beyond the last data year — and that is exactly what the live sheet has.

## The `_NoBESS` counterfactual — precisely what changes

`_NoBESS` does **not** zero the BESS variables — it re-sets them to whatever value the embedded
Baseline path has for that variable. That baseline value is **not always zero**: `exo_GA_3_1` has
no Baseline column at all (so it reverts to `0`), but `exo_PVEff_1` has a real, non-zero Baseline
path (`0.06766519050849035` at 2026 — see "Where the Baseline's own EE/RTS numbers come from"
above) — `_NoBESS` reverts to *that* value, not to zero.

```
Full sheet:    exo_AI_4_1_2, exo_AI_5_1_2, exo_GA_4_1, exo_GA_5_1, exo_GA_3_1,          exo_PVEff_1,          exo_PV_1
NoBESS sheet:  exo_AI_4_1_2, exo_AI_5_1_2, exo_GA_4_1, exo_GA_5_1, exo_GA_3_1_baseline, exo_PVEff_1_baseline, exo_PV_1_baseline
                └──────────────── identical in both ────────────────┘        └────────── reverted to baseline ──────────┘
```

Verified directly against the workbook: comparing `EE_PDP8_PV_BESS` to `EE_PDP8_PV_BESS_NoBESS`
row by row, `exo_AI_4_1_2`, `exo_AI_5_1_2`, `exo_GA_4_1`, `exo_GA_5_1`, `exo_lAddEE_4_1`,
`exo_lAddEE_5_1`, and `exo_CapTrade_1` are identical in every year 2026–2051; `exo_GA_3_1` is
non-zero in the full sheet and exactly `0` in the NoBESS sheet in every year (e.g. 2026:
`0.0033488372093023254` vs `0`); `exo_PVEff_1` is larger in the full sheet than in the NoBESS sheet
in every year, but the NoBESS value is the Baseline path, not zero (2026: `0.07761552136165845` vs
`0.06766519050849035`); `exo_PV_1` is identical in both (household RTS investment is 0 in the
current input data, so there is nothing to revert). So **exactly three of the ten variables**
distinguish a scenario from its NoBESS twin in the currently loaded data: `exo_GA_3_1`,
`exo_PVEff_1`, and (whenever household RTS data is eventually supplied) `exo_PV_1`.

## Summary table

| # | Variable | Model equation location | Functional form | Differs in `_NoBESS`? |
|---|---|---|---|---|
| 1 | `exo_AI_4_1_2` | `firms.mod:66-75` (`A_I_4_1_2`) | level: `log(1/(1-phi))` | No |
| 2 | `exo_AI_5_1_2` | `firms.mod:66-75` (`A_I_5_1_2`) | level: `log(1/(1-phi))` | No |
| 3 | `exo_GA_4_1` | `government.mod:138-149` (`K_A_4_1` target, `G_A_4_1` flow) | stock: `0.9·K_A(t-1) + flow/GDP` | No |
| 4 | `exo_GA_5_1` | `government.mod:138-149` (`K_A_5_1` target, `G_A_5_1` flow) | stock: `0.9·K_A(t-1) + flow/GDP` | No |
| 5 | `exo_GA_3_1` | `government.mod:138-149` (`K_A_3_1` target, `G_A_3_1` flow) | stock: `0.9·K_A(t-1) + flow/GDP` | **Yes** |
| 6 | `exo_PVEff_1` | `households.mod:136-139` (`Q_PV_1`) | level: `log(1+gain/100)` | **Yes** |
| 7 | `exo_PV_1` | `households.mod:126-134` (`I_PV_1`, `K_PV_1`) | stock (double-accumulated): `0.9·K_A(t-1) + flow/GDP` | **Yes** |
| 8 | `exo_lAddEE_4_1` | `firms.mod:73` (exponent on `EE_1`) | constant = 1 | No |
| 9 | `exo_lAddEE_5_1` | `firms.mod:73` (exponent on `EE_1`) | constant = 1 | No |
| 10 | `exo_CapTrade_1` | `climate_emissions.mod:60-76`, scaled by `phiG_p = 0` | constant = 1 (currently inert) | No |

## Data-integrity note (checked against the live workbook)

This section previously found the EE scenario sheets out of sync with the Baseline workbook —
`exo_GA_4_1`/`exo_GA_5_1`/`exo_PVEff_1` didn't match, and the sheets stopped a year short of the
Baseline's horizon. **The workbook has since been regenerated, and re-checking it now finds
everything in sync.** The before/after is worth walking through once, because it's the clearest
illustration in this whole document of why "regenerate before you trust absolute levels" (the
advice given throughout this doc) actually matters in practice.

**What was found before:** at 2026, the EE scenario sheets implied an embedded baseline of
`exo_GA_4_1 = 0.0220`, `exo_GA_5_1 = 0.0190`, `exo_PVEff_1 = 0` (backed out as scenario-value minus
the CSV-driven increment) — but the Baseline workbook on disk at the time had `0.0640`, `0.0470`,
and `0.0677` for those same three cells, and the EE sheets stopped at 2050 while the Baseline
workbook already ran to 2051. All three mismatches trace to the same root cause: the
baseline-construction pipeline described in "Where the Baseline's own EE/RTS numbers come from"
(`apply_government_rts_sector_pv_shocks`, `apply_industrial_pv_to_ee_coupling`,
`apply_vneep3_ee_targets`) had been re-run — rewriting `exo_GA_4_1`/`exo_GA_5_1`/`exo_PVEff_1` and
extending the horizon to 2051 — without the EE scenario sheets being regenerated to match.

**What is true now, re-verified directly against the live workbook:**

| Variable, 2026 | Baseline sheet | Backed out of `EE_PDP8`/`EE_PDP8_PV_BESS` (scenario − increment) | In sync? |
|---|---|---|---|
| `exo_AI_4_1_2` | `0.005` | `0.005` | Yes |
| `exo_AI_5_1_2` | `0.02` | `0.02` | Yes |
| `exo_GA_4_1` | `0.016` | `0.016` | **Yes — was 0.0220 vs 0.064** |
| `exo_GA_5_1` | `0.015` | `0.015` | **Yes — was 0.0190 vs 0.047** |
| `exo_GA_3_1` | `0` (no such column) | `0` | Yes |
| `exo_PVEff_1` | `0.06766519050849035` | `0.06766519050849035` | **Yes — was 0 vs 0.0677** |
| `exo_PV_1` | `0.0013` | `0.0013` | Yes |
| Horizon | 2026–2051 (27 rows) | 2026–2051 (27 rows) | **Yes — was 2026–2050 vs 2026–2051** |

Every one of the previously-flagged mismatches is now resolved because
`CreateEEScenariosFromExpertInputs.m` was re-run against the updated Baseline sheet — the
extrapolation section above shows the 2051 row this produced, computed from the formula and
confirmed against the live sheet. **The lesson, not just the specific numbers:** this pipeline
(`CreateBaselineFromUserInputFile.m` → `CreateEEScenariosFromExpertInputs.m`) is a two-step
dependency, and re-running only the first step silently stales the second. Whenever you're about to
rely on an EE scenario sheet's absolute (not differenced) levels, re-run both scripts in that order
first — don't assume last time's regeneration is still current.

## Hands-on: create and verify the sheets yourself (prompt recipes)

You do not need to be a MATLAB expert to do this — you need MATLAB installed and licensed
(the assistant runs the `.m` scripts for you via `run('scripts/maintenance/...')`, the repo's own
documented convention, from a MATLAB session or `matlab -batch`), and a coding assistant open in
the `DGE-METRIC` repo (not this training repo) with this page's content available for it to check
its own work against. Each recipe below is a prompt you can paste as-is; each is built from a check
already performed and verified earlier in this document, so you can tell immediately whether your
assistant's answer is right.

**Before you start:** confirm you're pointed at the main model repo (`DGE-METRIC`), not
`DGE-METRIC-Online-Training` — the scripts and workbooks referenced throughout this page
(`scripts/maintenance/CreateEEScenariosFromExpertInputs.m`,
`ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx`, etc.) live there.

### Recipe 1 — Regenerate all three EE scenario sheets from the expert workbook

```
Run scripts/maintenance/CreateEEScenariosFromExpertInputs.m from the DGE-METRIC repo root in
MATLAB (run('scripts/maintenance/CreateEEScenariosFromExpertInputs.m')). It will first
auto-regenerate the clean CSV inputs under ExcelFiles/Input/ExpertClean/, then write both a full
and a _NoBESS sheet into ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx for each of
EE_PDP8_reference, Directive10_RTS_EE, and PDP8_PV_EV_BESS. Show me:
1. the full console log for all three scenarios,
2. explicit confirmation that six sheets were written (three pairs),
3. any NoOverlap / NoUsableInput / SheetMissing warnings, and what they'd mean if they appeared.
```

### Recipe 2 — Recompute one variable by hand and check it against the sheet

```
Read ExcelFiles/Input/ExpertClean/EE_PDP8_reference.csv and
ExcelFiles/ModelBaseline5Sectorsand1Regions.xlsx (sheet Baseline) and
ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx (sheet EE_PDP8). For year 2035, recompute
exo_AI_4_1_2 by hand using: phi = min(Industry_EE_Saving_pct/100, 0.9999),
dAI = log(1/(1-phi)), exo_AI_4_1_2 = <Baseline sheet's exo_AI_4_1_2 for 2035> + dAI. Tell me
whether this matches what's actually written in the EE_PDP8 sheet for 2035, and if not, by how
much and your best explanation why (see docs/energy_efficiency_pathway.md in the training repo for
the reference formula and a worked 2026 example to check your own arithmetic against first).
```

### Recipe 3 — Change an expert assumption and regenerate

```
I want to raise Industry_EE_Saving_pct for EE_PDP8_reference by 2 percentage points in every year
from 2035 onward. Edit the source sheet EE_PDP8_reference in
"ExcelFiles/PDP8/Vietnam_EnergyExpert_ScenarioInputs - Adjust_2505.xlsx" (not the generated CSV —
that gets overwritten), then re-run CreateEEScenariosFromExpertInputs.m. Confirm the new
exo_AI_4_1_2 value for 2035 in the regenerated EE_PDP8 sheet equals the old value plus
log(1/(1-(old_saving_pct+2)/100)) - log(1/(1-old_saving_pct/100)) — i.e. the incremental dAI from
raising the saving percentage by exactly 2 points, holding the baseline term fixed.
```

### Recipe 4 — Verify the NoBESS counterfactual isolates the right variables

```
Compare EE_PDP8_PV_BESS and EE_PDP8_PV_BESS_NoBESS in
ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx column by column, for every year. Confirm
exo_AI_4_1_2, exo_AI_5_1_2, exo_GA_4_1, exo_GA_5_1, exo_lAddEE_4_1, exo_lAddEE_5_1, and
exo_CapTrade_1 are identical between the two sheets in every row, and that exo_GA_3_1 and
exo_PVEff_1 are non-zero in the full sheet and reverted to the Baseline sheet's value (not
necessarily zero) in the NoBESS sheet. Flag any row where this pattern doesn't hold — that would
mean the sheets are out of date or the writer script changed.
```

### Recipe 5 — Check the sheets are in sync with the current Baseline workbook before running anything

```
For EE_PDP8, EE_Directive10, and EE_PDP8_PV_BESS in
ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx: (a) compare each sheet's Year range against
ExcelFiles/ModelBaseline5Sectorsand1Regions.xlsx's Year range and flag any mismatch, and (b) for
exo_AI_4_1_2, exo_AI_5_1_2, exo_GA_4_1, exo_GA_5_1, exo_PV_1, and exo_PVEff_1, back out the implied
embedded baseline (scenario value minus the increment computed from the matching expert CSV row)
and compare it against the current Baseline sheet's actual value for that year. Report which
variables are in sync and which imply a stale baseline, so I know whether to regenerate before
running RunSimulations.m.
```

### Recipe 6 — Extend an EE scenario to cover a longer horizon (avoid triggering extrapolation)

```
The Baseline workbook now covers through 2051, but ExcelFiles/Input/ExpertClean/*.csv and the EE
scenario sheets only go through 2050. Add a 2051 row to EE_PDP8_reference, Directive10_RTS_EE, and
PDP8_PV_EV_BESS in the raw expert workbook (repeat or linearly extend each column's 2050 value —
your judgment call on which), regenerate the clean CSVs and scenario sheets, and confirm nYears now
matches iB(end) for all three scenarios (i.e. no extrapolated rows), per the extrapolation logic in
CreateEEScenariosFromExpertInputs.m lines 175-183 and 193-199.
```
