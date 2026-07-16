\
# Reserve-Requirement Implementation Plan Template

**New 2026-07-13**, replacing `pathway-template.md` (DER and LNG-to-Hydrogen pathways are out of scope for this iteration — see [`../../../design/decision-log.md`](../../../design/decision-log.md)). Covers the "method and implementation" framing for reserve requirements; the illustrative MC = MB walkthrough itself is completed tomorrow morning ([`../../training-day-05/morning-reserve-requirements-open-lab/`](../../training-day-05/morning-reserve-requirements-open-lab/)) using [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md).

```text
Carrier / coverage chosen: <e.g. Crude oil - 1 MTA, 30 days>
Policy question (in your own words): <one sentence, MC = MB framing, specific to this carrier>

Inputs needed from Days 1-2 (conceptual, DGE-METRIC-relevant):
- <finance-scenario output — name the specific indicator>
- <energy-efficiency scenario output — name the specific indicator>

Illustrative proxy numbers (Toy Model SOE MC — NOT DGE-METRIC):
- Annual cost (USD m/yr): <value from reserve_breakeven_table.md>
- Break-even GDP loss %: <value, confirm ~ Annual cost / 172.0>
- Step-2 verdict at 20% / 50% shock: <justified / marginal / not justified>

Implementation approach:
- Most plausible location: <post-processing script reading DGE-METRIC outputs, OR structural addition to ModFiles/ + calibration in Functions/ExcelFiles/, OR both>
- Reasoning: <one sentence — why this classification>
- DGE-METRIC output variables this would read (once available): <list>

Remaining SME review items:
- [SME REVIEW NEEDED: confirm the DGE-METRIC reserve-requirement formula, target indicator, and optimality criterion]
- <any additional carrier-specific or implementation-specific gap>
```

## Worked example

```text
Carrier / coverage chosen: Crude oil - 1 MTA, 30 days
Policy question: How much crude oil reserve is worth holding, given its annual storage/capital-recovery cost versus the GDP loss it would avoid in a supply disruption?

Inputs needed from Days 1-2 (conceptual, DGE-METRIC-relevant):
- GDP and investment paths under the finance scenarios (Day 1 PM / Day 2 AM)
- Import dependence and final energy demand under the efficiency scenario vs. PDP8 baseline (Day 2 AM)

Illustrative proxy numbers (Toy Model SOE MC - NOT DGE-METRIC):
- Annual cost (USD m/yr): 30.4
- Break-even GDP loss %: 0.177% (≈ 30.4 / 172.0)
- Step-2 verdict at 20% / 50% shock: not justified / not justified

Implementation approach:
- Most plausible location: post-processing script reading DGE-METRIC outputs — this is an accounting/comparison calculation over existing model outputs (energy-carrier demand, GDP, investment), not a new structural relationship the model needs to solve internally
- Reasoning: the break-even and validation steps are arithmetic on top of run outputs, analogous to the chart-and-narrative scripts already used for scenario comparison; only if a genuinely endogenous crisis-cost channel were added to the model itself would this touch ModFiles/
- DGE-METRIC output variables this would read (once available): GDP path, investment path, energy-carrier import volumes, sectoral output under disruption-affected sectors

Remaining SME review items:
- [SME REVIEW NEEDED: confirm the DGE-METRIC reserve-requirement formula, target indicator, and optimality criterion]
- [SME REVIEW NEEDED: confirm crisis-probability and shock-size assumptions for Vietnam with EVN/PVN/GSO, per email_optimal_reserve_requirements.md Next Steps item 2]
```

Do not remove or leave blank any field. If a value is not known or not in the source documents, write `[SME REVIEW NEEDED: ...]` rather than inventing it.
