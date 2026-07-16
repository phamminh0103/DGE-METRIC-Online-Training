\
# Exercise — Sensitivity-Analysis Plan (Online Day 3 PM)

No live model re-run required for this exercise (a full calibration re-run takes longer than this block allows) — the deliverable is a documented **plan** a group could execute afterward, following the same rigor as this week's scenario/pathway metadata sheets. **New 2026-07-13**, replacing the wrap-up's synthesis/checklist blocks — see [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Task 1: Pick one structural parameter (group task, ~10 min of Block 5)

Choose one structural parameter from `docs/calibration.md`'s list: discount factor, depreciation, an elasticity of substitution, a tax rate, or an adjustment-cost parameter.

## Task 2: Draft your sensitivity-analysis plan (group task, ~20 min of Block 5)

Using [`sensitivity-plan-template.md`](sensitivity-plan-template.md), document:

1. Parameter chosen and its baseline value (cite `docs/calibration.md`, or mark `[SME REVIEW NEEDED]` if the baseline value isn't in the reviewed sources).
2. Perturbation: the specific alternative value or percentage change you'd test, and why that's a reasonable perturbation (not arbitrary).
3. Expected effect: which direction and which output indicators you expect to move, and why (mechanism, not just "it will change").
4. Accounting-coherence checks you'd re-run before trusting the perturbed result.
5. Any file location you're not certain of, marked `[SME REVIEW NEEDED]` rather than guessed.

## Reference facts

Structural parameters: discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs. Source: `../../../../../DGE-METRIC-VietNam/docs/calibration.md`. Do not invent specific baseline numeric values for these parameters if they are not in the reviewed sources — mark them `[SME REVIEW NEEDED]`.

## Deliverable

One completed sensitivity-analysis plan per group.

## Debrief prompt

If you actually ran this perturbation and the accounting-coherence checks failed, would that tell you something about the parameter, about the pipeline, or about your perturbation size — and how would you tell which?
