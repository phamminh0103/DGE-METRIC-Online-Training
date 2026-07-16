\
# Sensitivity-Analysis Plan Template

**New 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). One-at-a-time parameter perturbation is general good-practice methodology, not a DGE-METRIC-specific procedure documented in the reviewed sources — mark any DGE-METRIC-specific detail (exact file location, exact baseline value) `[SME REVIEW NEEDED]` unless it is confirmed in `docs/calibration.md` or the live repository.

```text
Parameter: <e.g. elasticity of substitution between fossil and renewable energy>
Baseline value: <value and source, or [SME REVIEW NEEDED]>
Perturbation tested: <e.g. +10%, -10%, or a specific alternative value>
Reasoning for this perturbation size: <one sentence — why this is a reasonable test, not arbitrary>

Expected effect:
- Direction: <which way key indicators should move>
- Mechanism: <why — one paragraph>
- Output indicators to check: <e.g. GDP, investment, sectoral output, renewable capital>

Re-validation checklist before trusting the result:
- [ ] Output conservation
- [ ] Import conservation
- [ ] Value-added consistency
- [ ] Non-negativity of final matrices
- [ ] Steady-state / transition convergence

File(s) this perturbation would touch: <ExcelFiles/ workbook+cell, or Functions/ helper — or [SME REVIEW NEEDED] if not verified>

Remaining SME review items:
- <any parameter baseline value, file location, or reasonable-range assumption not confirmed in docs/calibration.md>
```

## Worked example

```text
Parameter: Discount factor
Baseline value: [SME REVIEW NEEDED: confirm this cohort's calibrated discount factor value — not stated in the reviewed sources]
Perturbation tested: -1 percentage point (annualized), representing a more impatient household/planner
Reasoning for this perturbation size: a 1pp change is large enough to plausibly move investment timing but small enough to stay within a range typically considered for this class of parameter

Expected effect:
- Direction: lower discount factor (more impatience) should reduce near-term investment and renewable capital accumulation relative to baseline
- Mechanism: a more impatient household/planner discounts future consumption/returns more heavily, reducing the incentive to save and invest today for future payoffs
- Output indicators to check: investment, renewable capital stock, GDP path, savings rate

Re-validation checklist before trusting the result:
- [ ] Output conservation
- [ ] Import conservation
- [ ] Value-added consistency
- [ ] Non-negativity of final matrices
- [ ] Steady-state / transition convergence

File(s) this perturbation would touch: [SME REVIEW NEEDED: confirm whether the discount factor is set in a Functions/ helper or a named range in the calibration workbook for this cohort's repository copy]

Remaining SME review items:
- [SME REVIEW NEEDED: confirm baseline discount factor value]
- [SME REVIEW NEEDED: confirm file location for editing this parameter]
```

Do not remove or leave blank any field. If a value is not known or not in the source documents, write `[SME REVIEW NEEDED: ...]` rather than inventing it.
