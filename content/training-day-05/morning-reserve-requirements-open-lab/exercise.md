\
# Exercise — Guided Open Lab: Reserve-Requirement Analysis (Online Day 3 AM)

No DGE-METRIC model run in this session — this uses the illustrative `Toy Model SOE MC` break-even table, not DGE-METRIC output. **Restructured 2026-07-13**: this exercise now covers only the hands-on lab (Parts A–C below); the break-even reading and carrier choice happened yesterday afternoon. See [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Part A: Confirm your carrier and recap the numbers (~15 min)

Using yesterday's implementation plan: confirm your chosen carrier/coverage row from `reserve_breakeven_table.md`, and recap the parameters — GDP (2024) USD 430,000m; crisis probability p = 0.04/yr; break-even divisor (1% GDP) = USD 172.0m.

## Part B: Work the MC = MB logic by hand, in full (~90 min)

1. Confirm: Break-even GDP loss % ≈ Annual cost ÷ 172.0 for your carrier.
2. Confirm the Step-2 "Avoided GDP% (20% shock)" and "(50% shock)" verdicts ("justified," "marginal," or "not justified") for your carrier.
3. If you completed a Day 2 AM efficiency-scenario comparison, use it here: would this scenario increase or decrease Vietnam's exposure to a supply disruption in your chosen carrier? Why?
4. List two DGE-METRIC outputs (once a DGE-METRIC reserve module exists) that would be needed to redo Steps 1–2 properly for your carrier, instead of relying on the toy model's CES stand-in.
5. Sensitivity: roughly how much larger would the crisis probability or shock size need to be for the verdict to flip toward "justified"? (Order-of-magnitude reasoning is fine.)

## Part C: Write up your reserve-requirement analysis note (~45 min)

Using [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md), combine:
- Yesterday's implementation plan (mechanism, DGE-METRIC outputs needed, codebase location).
- Today's completed MC = MB walkthrough (Part B).
- An explicit list of what is still `[SME REVIEW NEEDED]` before this could inform an actual decision.

## Deliverable

One reserve-requirement analysis note, covering Parts A–C, explicitly labeling all Step 1–3 numbers as illustrative toy-model proxy results.

## Debrief prompt

If the DGE-METRIC reserve module existed today, what is the first question you would ask it about your chosen carrier?
