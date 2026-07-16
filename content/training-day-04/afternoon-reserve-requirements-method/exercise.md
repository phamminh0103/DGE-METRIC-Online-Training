\
# Exercise — Reserve-Requirement Method & Implementation Plan (Online Day 2 PM)

No model run in this session — this uses the illustrative `Toy Model SOE MC` break-even table, not DGE-METRIC output. **New 2026-07-13**, replacing the old pathway-design exercise (see [`../../../design/decision-log.md`](../../../design/decision-log.md)).

## Part A: Read the break-even ranking and choose your carrier (~15 min, within Block 3)

From the summary ranking in `reserve_breakeven_table.md` (lowest to highest break-even bar): refined-product tanks (8-day cover, 0.159% BE GDP loss), distributed BESS (0.169%), 1-MTA crude oil (0.177%) ... up to 90-day imported coal (1.973%) and 6-MTA LNG (1.909%).

1. Which carrier/coverage combination clears the lowest break-even bar, and in plain language, why does that make it "cheap insurance" relative to the others?
2. **Choose one carrier/coverage row for your own group to work through in detail tomorrow morning's guided open lab.**

## Part B: Work the MC = MB logic by hand for your chosen carrier (~15 min, within Block 4)

Using: GDP (2024) USD 430,000m; crisis probability p = 0.04/yr; break-even divisor (1% GDP) = USD 172.0m (= p × GDP/100).

1. Look up your chosen carrier's annual cost (USD m/yr) from the table.
2. Confirm: Break-even GDP loss % ≈ Annual cost ÷ 172.0.
3. Look up the Step-2 "Avoided GDP% (20% shock)" and "(50% shock)" for your carrier. Is the verdict "justified," "marginal," or "not justified"?

## Part C: Draft your implementation plan (group task, ~35 min, Block 6)

Using [`implementation-plan-template.md`](implementation-plan-template.md), document for your chosen carrier:

1. Mechanism (one sentence, MC = MB framing, specific to your carrier).
2. Which finance-scenario and efficiency-scenario outputs from Days 1–2 this analysis would need (be specific — name the indicator, not just "GDP").
3. Where the logic would most plausibly live in the codebase: a post-processing script reading existing DGE-METRIC outputs, or a structural addition to `ModFiles/`/`Functions/` — and why, following the pattern in `lesson.md` Part 5.5.
4. What remains `[SME REVIEW NEEDED]` before this could run against real DGE-METRIC output.

## Deliverable

One completed implementation plan per group, recorded in [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md), ready to complete tomorrow morning.

## Debrief prompt

If the DGE-METRIC reserve module existed today, what is the first question you would ask it about your chosen carrier?
