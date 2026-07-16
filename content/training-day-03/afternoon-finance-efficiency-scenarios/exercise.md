\
# Exercise — Finance & Energy-Efficiency Scenario Definition (Online Day 1 PM)

No model run in this session. Two scenario-definition tasks. **Restructured 2026-07-13**: codebase navigation and Git basics tasks moved to Online Day 2 AM's exercise (see [`../../../design/decision-log.md`](../../../design/decision-log.md)).

## Task 1: Finance-scenario metadata sheet (group task, ~45 min across Blocks 3–4)

Your group is assigned one row of the matrix below (facilitator assigns or group self-selects, avoiding duplicates where group count allows).

| Scenario ID | Emissions pathway | Public financing rate | Revenue recycling |
|---|---|---:|---|
| PDP8-Base | PDP8 | 8% | No |
| NZ-Base | Net Zero | 8% | No |
| PDP8-Concessional | PDP8 | 5% | No |
| NZ-Concessional | Net Zero | 5% | No |
| PDP8-Recycle | PDP8 | 8% | Yes |
| NZ-Recycle | Net Zero | 8% | Yes |

Using [`scenario-template.md`](scenario-template.md), document your assigned scenario's full metadata block: label, mechanism, exact file edits, exact variables changed, time path, start/end year, transition profile, expected effects, key output indicators, caveats, owner, date.

For the "expected effects" field specifically, also write:
1. Which base case it should be compared against (same emissions pathway, financing rate = 8%, no recycling).
2. The single variable that differs from that base case.

Record your answers in [`../../../scenarios/finance/scenario-log.md`](../../../scenarios/finance/scenario-log.md) before the session ends.

## Task 2: Energy-efficiency scenario metadata sheet (group task, ~30 min across Block 6)

Using [`efficiency-scenario-template.md`](efficiency-scenario-template.md), document the energy-efficiency & demand-side-management scenario's full metadata block, covering:

1. Mechanism (2–3 sentences): efficiency gains + DSM, and the channels they act through.
2. Sector-specific assumptions and required inputs, with source citation for every numeric value — write `[SME REVIEW NEEDED: ...]` for anything not in `energy_efficiency_pathway.md`.
3. Affected sectors: manufacturing, services/commercial, households.
4. Time path: when savings ramp in, through 2030.
5. Expected mechanisms and effects, **including the documented rebound effect**.
6. Key output indicators: energy intensity, final energy demand, GDP, investment, energy prices/expenditure.
7. Caveats and data limitations.

Record your answers in [`../../../scenarios/energy-efficiency/efficiency-scenario-log.md`](../../../scenarios/energy-efficiency/efficiency-scenario-log.md) before the session ends.

## Reference facts (energy-efficiency scenario)

2030 savings potential ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households; quantified investment need ≈USD 361 million/year (≈0.076% of 2024 GDP, USD 476.3 bn). Source: `../../../../../DGE-METRIC-VietNam/docs/energy_efficiency_pathway.md`.

## Deliverable

- One completed finance-scenario metadata sheet per group (Task 1).
- One completed energy-efficiency scenario metadata sheet per group (Task 2).
