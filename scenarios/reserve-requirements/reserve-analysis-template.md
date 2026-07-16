\
# Reserve-Requirement Analysis Note Template

Every entry must clearly separate **conceptual/DGE-METRIC-relevant content** from **illustrative `Toy Model SOE MC` proxy numbers**. Do not blend the two without labeling. **Restructured 2026-07-13** (see [`../../design/decision-log.md`](../../design/decision-log.md)): the "Implementation approach" section is started Online Day 2 PM; the rest is completed Online Day 3 AM.

```text
Group: <name>
Carrier / coverage chosen: <e.g. Crude oil - 1 MTA, 30 days>

Policy question (in your own words): <one sentence, MC = MB framing>

Inputs needed from Days 1-2 (conceptual, DGE-METRIC-relevant):
- <finance-scenario output — name the specific indicator>
- <energy-efficiency scenario output — name the specific indicator>

Illustrative proxy walkthrough (Toy Model SOE MC — NOT DGE-METRIC):
- Annual cost (USD m/yr): <value from reserve_breakeven_table.md>
- Break-even GDP loss %: <value, and confirm ~ Annual cost / 172.0>
- Avoided GDP% at 20% shock / verdict: <value / justified-marginal-not justified>
- Avoided GDP% at 50% shock / verdict: <value / justified-marginal-not justified>

Implementation approach [drafted Day 2 PM, per implementation-plan-template.md]:
- Most plausible location: <post-processing script reading DGE-METRIC outputs, OR structural addition to ModFiles/ + calibration in Functions/ExcelFiles/, OR both>
- Reasoning: <one sentence>

Link to energy-efficiency scenario (Day 1 PM / Day 2 AM):
- Effect on this carrier's exposure: <increases/decreases, and why>

Sensitivity notes:
- <what would change the verdict — e.g. crisis probability p, shock size>

Caveats:
- All Step 1-3 numbers above are illustrative Toy Model SOE MC proxy results, not DGE-METRIC output.
- <any other carrier-specific caveat from reserve_breakeven_table.md, e.g. grid storage sub-annual scope note>

Remaining SME review items:
- [SME REVIEW NEEDED: confirm the DGE-METRIC reserve-requirement formula, target indicator, and optimality criterion]
- <any additional carrier-specific gap>
```

## Worked example (illustrative only)

```text
Group: Example group
Carrier / coverage assigned: Crude oil - 1 MTA, 30 days

Policy question: How much crude oil reserve is worth holding, given its annual storage/capital-recovery cost versus the GDP loss it would avoid in a supply disruption?

Inputs needed from Days 1-2 (conceptual, DGE-METRIC-relevant):
- GDP and investment paths under baseline vs. finance scenarios (Day 1 PM / Day 2 AM)
- Import dependence and final energy demand under the energy-efficiency scenario vs. PDP8 baseline (Day 2 AM)

Illustrative proxy walkthrough (Toy Model SOE MC - NOT DGE-METRIC):
- Annual cost (USD m/yr): 30.4
- Break-even GDP loss %: 0.177% (≈ 30.4 / 172.0)
- Avoided GDP% at 20% shock / verdict: 0.105% / not justified
- Avoided GDP% at 50% shock / verdict: 0.112% / not justified

Implementation approach [drafted Day 2 PM]:
- Most plausible location: post-processing script reading DGE-METRIC outputs
- Reasoning: the break-even and validation steps are arithmetic on top of run outputs, not a new structural relationship the model needs to solve internally

Link to energy-efficiency scenario (Day 1 PM / Day 2 AM):
- Effect on this carrier's exposure: a stronger efficiency scenario would lower final energy demand and plausibly reduce near-term reliance on imported crude/products — but the efficiency scenario's rebound effect means this reduction is smaller than the gross savings figure would suggest

Sensitivity notes:
- A higher crisis probability p or larger assumed shock size would raise the avoided-GDP% figures and could flip "not justified" toward "marginal" or "justified"

Caveats:
- All numbers above are illustrative Toy Model SOE MC proxy results, not DGE-METRIC output
- The toy model's CES shock is framed as an annual supply shortfall, which is conservative for short (30-day) reserves relative to real crises (shorter, more severe per day)

Remaining SME review items:
- [SME REVIEW NEEDED: confirm the DGE-METRIC reserve-requirement formula, target indicator, and optimality criterion]
- [SME REVIEW NEEDED: confirm crisis-probability and shock-size assumptions for Vietnam with EVN/PVN/GSO, per email_optimal_reserve_requirements.md Next Steps item 2]
```
