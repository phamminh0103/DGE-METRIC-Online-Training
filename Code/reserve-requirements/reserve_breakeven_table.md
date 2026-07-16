## Break-Even Avoided GDP/Consumption Loss — Energy Reserve Optimality
### Vietnam | MC = MB condition:  Annual cost = p × Avoided GDP loss per crisis

**Key:**  *BE: GDP%* = minimum GDP loss (% of GDP) a crisis must cause for the reserve to be
cost-effective.  *MC/day* = annualised cost per additional day of coverage (USD m/yr).
For grid storage (PSHP, BESS) *MC* is the cost per dispatch event (USD m).

| Parameter | Value | Notes |
|---|---|---|
| GDP 2024 | USD 430,000m | IMF WEO 2024 |
| Crisis probability `p` | 0.04/yr | 1-in-25; IEA disruption database |
| C/Y ratio | 0.67 | World Bank Vietnam 2023 |
| CRF — oil/gas infrastructure | 0.0897 | 25-yr life, 7.5% SOE discount rate |
| CRF — PSHP | 0.0847 | 30-yr life, 7.5% |
| CRF — BESS | 0.1204 | 15-yr life, 8.5% |
| Break-even divisor (1% GDP) | USD 172.0m | `= p × GDP/100` |
| Break-even divisor (1% C)   | USD 115.2m | `= p × C/100` |

*Consumption flows (2030 basis):* crude oil 12 Mt/yr net imports;
petroleum products 20 Mt/yr total demand (density 0.85 t/m³);
LNG 10 Mt/yr (PDP8 target); LPG 2 Mt/yr imports;
coal 75 Mt/yr power-sector consumption.

---

### How to Determine the Optimal Reserve Requirement — Two-Step Method

**Step 1 — Screen (this document): break-even accounting.**
For each carrier and coverage level, compute the annualised cost of holding the
reserve (storage + capital recovery), then back out the minimum crisis GDP
loss (%) that reserve would have to prevent for `Annual cost = p × Avoided
GDP loss` to hold (MC = MB). This is a pure accounting exercise — it does not
say whether a crisis of that size is plausible, only what has to be true for
the reserve to pay for itself. *Script:* `compute_reserve_breakeven.py` (edit
Section 1 to update GDP, `p`, or discount rates).

**Step 2 — Validate: endogenous CES/DSGE welfare optimum.**
Feed a shock of a given size (20% / 50% of annual supply disrupted) into the
`ToyModelSOEMC` CES production function to get the *actual* avoided GDP loss
the reserve would deliver, and compare it to the Step-1 threshold. This is
the "Model Validation" table below — it tells you whether the break-even bar
is realistic given the model's calibrated shock distribution. *Script:*
`ces_gdp_loss.py`, or `toy_model_gdp_loss(M_, oo_)` in MATLAB for the fully
solved Dynare steady state.

**Step 3 — Optimise: Monte-Carlo welfare maximisation over the full policy space.** Rather than testing fixed coverage levels, run the Dynare model across a grid of coverage days — jointly with the drawdown rule and the capacity-investment rate — and pick the combination that maximises the **Net Reserve Value**:

> Net Reserve Value = Insurance benefit − Storage cost

The insurance benefit is the consumption-equivalent welfare gain from crisis protection (a Monte-Carlo average over simulated crises); the storage cost is the annualised storage and depreciation cost, as a share of consumption. The optimal coverage level is the one where marginal benefit equals marginal cost — the model's answer to "what is the optimal reserve requirement."

*Scripts:* `ToyModelSOEMC_optimal_stock.m` finds the optimal coverage for a single commodity; `ToyModelSOEMC_joint_optimal.m` finds the optimal coverage, drawdown rule, and capacity-investment rate jointly for oil and coal together. Both require `ToyModelSOEMC_run.m` to be run first, to set up the Dynare workspace.

**Reading the current results:** the Step-2 validation table below shows
every fuel carrier as **"not justified"** at both the 20% and 50% shock
levels — i.e. under the model's current calibration (`p = 0.04/yr`, energy
revenue share 4.1% of GDP), the endogenous GDP loss avoided never reaches
the break-even threshold, for any tested coverage. The latest Step-3 joint
run (`joint_optimal_results.txt`) returned a corner solution at the edge of
the search grid (`d* = 1825` days = 5 years) together with an implausible
storage-cost share (≈ −11,000% of consumption), which indicates a scaling
or sign error in that run rather than a genuine optimum — **treat those
numbers as provisional** pending a re-run with a corrected cost term and a
wider `d_grid`.

---

### Oil & Gas

| Carrier | Coverage | Volume | Annual cost (USD m/yr) | Cost % GDP | BE: GDP loss % | BE: C loss % | MC/day (USD m) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Crude oil — 1 MTA | 30 days | 1,000 KT | 30.4 | 0.0071% | **0.177%** | 0.264% | 1.000 |
| Crude oil — 2 MTA | 61 days | 2,000 KT | 60.8 | 0.0141% | **0.354%** | 0.528% | 1.000 |
| Crude oil — 3 MTA | 91 days | 3,000 KT | 91.2 | 0.0212% | **0.530%** | 0.792% | 1.000 |
| Ref. products — 500K m³ | 8 days | 500,000 m3 | 27.4 | 0.0064% | **0.159%** | 0.238% | 3.536 |
| Ref. products — 1,000K m³ | 16 days | 1,000,000 m3 | 54.9 | 0.0128% | **0.319%** | 0.476% | 3.536 |
| Ref. products — 1,500K m³ | 23 days | 1,500,000 m3 | 82.3 | 0.0191% | **0.478%** | 0.714% | 3.536 |
| LNG — 3 MTA | 110 days | 3,000 KT | 171.2 | 0.0398% | **0.995%** | 1.486% | 1.563 |
| LNG — 6 MTA | 219 days | 6,000 KT | 328.4 | 0.0764% | **1.909%** | 2.850% | 1.500 |
| LPG underground — 240 KT | 44 days | 240 KT | 50.9 | 0.0118% | **0.296%** | 0.442% | 1.162 |

### Coal

| Carrier | Coverage | Volume | Annual cost (USD m/yr) | Cost % GDP | BE: GDP loss % | BE: C loss % | MC/day (USD m) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Coal — Domestic | 30 days | 6.16 Mt | 60.4 | 0.0140% | **0.351%** | 0.524% | 2.012 |
| Coal — Imported | 30 days | 6.16 Mt | 113.1 | 0.0263% | **0.658%** | 0.982% | 3.771 |
| Coal — Domestic | 60 days | 12.33 Mt | 120.7 | 0.0281% | **0.702%** | 1.047% | 2.012 |
| Coal — Imported | 60 days | 12.33 Mt | 226.2 | 0.0526% | **1.315%** | 1.963% | 3.771 |
| Coal — Domestic | 90 days | 18.49 Mt | 181.1 | 0.0421% | **1.053%** | 1.571% | 2.012 |
| Coal — Imported | 90 days | 18.49 Mt | 339.4 | 0.0789% | **1.973%** | 2.945% | 3.771 |

### Grid Storage

| Carrier | Coverage | Volume | Annual cost (USD m/yr) | Cost % GDP | BE: GDP loss % | BE: C loss % | Cost/event (USD m) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| PSHP 1,200 MW / 8 h (Bac Ai Phase 1) | 1.92 TWh/yr  (250 cycles) | 1,200 MW | 189.6 | 0.0441% | **1.102%** | 1.645% | 0.758 |
| BESS 4 h, 1,000 MWh (distributed) | 0.29 TWh/yr  (365 cycles) | 1,000 MWh | 29.1 | 0.0068% | **0.169%** | 0.252% | 0.080 |

### Summary — All carriers ranked by break-even GDP loss %


| Carrier | Coverage | Volume | Annual cost (USD m/yr) | Cost % GDP | BE: GDP loss % | BE: C loss % | MC/day (USD m) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Ref. products — 500K m³ | 8 days | 500,000 m3 | 27.4 | 0.0064% | **0.159%** | 0.238% | 3.536 |
| BESS 4 h, 1,000 MWh (distributed) | 0.29 TWh/yr  (365 cycles) | 1,000 MWh | 29.1 | 0.0068% | **0.169%** | 0.252% | 0.080 |
| Crude oil — 1 MTA | 30 days | 1,000 KT | 30.4 | 0.0071% | **0.177%** | 0.264% | 1.000 |
| LPG underground — 240 KT | 44 days | 240 KT | 50.9 | 0.0118% | **0.296%** | 0.442% | 1.162 |
| Ref. products — 1,000K m³ | 16 days | 1,000,000 m3 | 54.9 | 0.0128% | **0.319%** | 0.476% | 3.536 |
| Coal — Domestic | 30 days | 6.16 Mt | 60.4 | 0.0140% | **0.351%** | 0.524% | 2.012 |
| Crude oil — 2 MTA | 61 days | 2,000 KT | 60.8 | 0.0141% | **0.354%** | 0.528% | 1.000 |
| Ref. products — 1,500K m³ | 23 days | 1,500,000 m3 | 82.3 | 0.0191% | **0.478%** | 0.714% | 3.536 |
| Crude oil — 3 MTA | 91 days | 3,000 KT | 91.2 | 0.0212% | **0.530%** | 0.792% | 1.000 |
| Coal — Imported | 30 days | 6.16 Mt | 113.1 | 0.0263% | **0.658%** | 0.982% | 3.771 |
| Coal — Domestic | 60 days | 12.33 Mt | 120.7 | 0.0281% | **0.702%** | 1.047% | 2.012 |
| LNG — 3 MTA | 110 days | 3,000 KT | 171.2 | 0.0398% | **0.995%** | 1.486% | 1.563 |
| Coal — Domestic | 90 days | 18.49 Mt | 181.1 | 0.0421% | **1.053%** | 1.571% | 2.012 |
| PSHP 1,200 MW / 8 h (Bac Ai Phase 1) | 1.92 TWh/yr  (250 cycles) | 1,200 MW | 189.6 | 0.0441% | **1.102%** | 1.645% | 0.758 |
| Coal — Imported | 60 days | 12.33 Mt | 226.2 | 0.0526% | **1.315%** | 1.963% | 3.771 |
| LNG — 6 MTA | 219 days | 6,000 KT | 328.4 | 0.0764% | **1.909%** | 2.850% | 1.500 |
| Coal — Imported | 90 days | 18.49 Mt | 339.4 | 0.0789% | **1.973%** | 2.945% | 3.771 |

---

### Model Validation — Endogenous GDP Loss vs Break-Even Threshold

**ToyModelSOEMC CES parameters (base case):**

- Energy share of output (α~E~): 15%
- Capital share of output (α~K~): 38%
- Labour share of output (α~L~): 47%
- CES substitution parameter (ρ): 0.333 — implied elasticity of substitution (η): 1.5
- Steady-state capital stock (K~ss~): 286.4 (normalised)
- Steady-state output (Y~ss~): 49.3 (normalised)
- Energy revenue share (s~E~): 4.1% of GDP

> **Reading the table:**  *Avoided GDP%* is how much GDP loss (% of GDP, in the crisis year) the reserve prevents, computed from the CES function with K and L fixed at steady-state values.  *BE: GDP%* is the minimum avoided loss needed for the reserve to break even under MC = MB.  **Justified** = avoided loss ≥ break-even.  **Marginal** = within 30% below break-even.  **Not justified** = avoided loss < 70% of break-even.  Shock scenarios: **20%** = 20% of annual commodity supply disrupted; **50%** = 50% disrupted (tail event).

| Carrier | Coverage | BE: GDP% | Avoided GDP% (20% shock) | Status (20%) | Avoided GDP% (50% shock) | Status (50%) | Note |
| --- | --- | ---: | ---: | :---: | ---: | :---: | --- |
| Crude oil — 1 MTA | 30 days | 0.177% | 0.105% | not justified | 0.112% | not justified |  |
| Crude oil — 2 MTA | 61 days | 0.354% | 0.126% | not justified | 0.223% | not justified |  |
| Crude oil — 3 MTA | 91 days | 0.530% | 0.126% | not justified | 0.331% | not justified |  |
| Ref. products — 500K m³ | 8 days | 0.159% | 0.027% | not justified | 0.029% | not justified |  |
| Ref. products — 1,000K m³ | 16 days | 0.319% | 0.054% | not justified | 0.058% | not justified |  |
| Ref. products — 1,500K m³ | 23 days | 0.478% | 0.081% | not justified | 0.086% | not justified |  |
| LNG — 3 MTA | 110 days | 0.995% | 0.025% | not justified | 0.062% | not justified | (LNG proxy: approx. as small coal-type, ED=0.06) |
| LNG — 6 MTA | 219 days | 1.909% | 0.025% | not justified | 0.062% | not justified | (LNG proxy: approx. as small coal-type, ED=0.06) |
| LPG underground — 240 KT | 44 days | 0.296% | 0.004% | not justified | 0.005% | not justified | (LPG proxy: refined-products fraction, ED=0.01) |
| Coal — Domestic | 30 days | 0.351% | 0.159% | not justified | 0.175% | not justified |  |
| Coal — Imported | 30 days | 0.658% | 0.159% | not justified | 0.175% | not justified |  |
| Coal — Domestic | 60 days | 0.702% | 0.192% | not justified | 0.346% | not justified |  |
| Coal — Imported | 60 days | 1.315% | 0.192% | not justified | 0.346% | not justified |  |
| Coal — Domestic | 90 days | 1.053% | 0.192% | not justified | 0.512% | not justified |  |
| Coal — Imported | 90 days | 1.973% | 0.192% | not justified | 0.512% | not justified |  |
| PSHP 1,200 MW / 8 h (Bac Ai Phase 1) | 1.92 TWh/yr  (250 cycles) | 1.102% | grid stability (sub-annual) |  | grid stability (sub-annual) |  | PSHP/BESS address frequency/inertia events; CES annual model does not apply |
| BESS 4 h, 1,000 MWh (distributed) | 0.29 TWh/yr  (365 cycles) | 0.169% | grid stability (sub-annual) |  | grid stability (sub-annual) |  | PSHP/BESS address frequency/inertia events; CES annual model does not apply |

**Interpretation notes:**  (1) The CES model treats the shock as an *annual* supply shortfall — a 20% shock means 20% of the commodity's yearly import never arrives. Real crises are shorter but more severe per day; the annual framing is conservative for short reserves (30 d).  (2) LNG/LPG estimates use proxy ED values (not separately calibrated in ToyModelSOEMC); treat them as order-of-magnitude.  (3) PSHP and BESS address grid inertia and frequency events (timescale: seconds to hours) — the annual CES model is not the relevant tool; their benefit is better measured by avoided blackout cost per MWh.  (4) To run with Dynare's solved K_ss, call `toy_model_gdp_loss(M_, oo_)` in MATLAB after `steady`, then re-run this Python script — it will read `toy_model_gdp_loss.csv` automatically.
