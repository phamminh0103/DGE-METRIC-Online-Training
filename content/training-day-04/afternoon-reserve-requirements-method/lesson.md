\
# Training Day 4 (Online Day 2) — Afternoon: Reserve Requirements — Method and Implementation

**Date: Thursday 23 July 2026.** Status: **partially blocked, drafted as conceptual + illustrative-proxy content.** **Restructured 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). This session replaces the old "Energy Transition Pathways" session (DER and LNG-to-Hydrogen pathways are out of scope for this iteration; the pathway model-modification framing is repurposed here for reserve requirements). This is a design/prep session: no model run happens today — the illustrative calculation is worked by hand tomorrow morning's guided open lab. It does **not** resolve [`../../../qa/sme-questions.md`](../../../qa/sme-questions.md) item 2: no DGE-METRIC-specific reserve-requirement formula, target indicator, or optimality criterion currently exists in the reviewed sources, and `../../../CLAUDE.md` explicitly prohibits inventing one.

**How this module resolves that**: it teaches (a) the policy question and required inputs conceptually, (b) an existing, real methodology — the `Toy Model SOE MC` break-even and Monte-Carlo welfare framework — **explicitly and repeatedly labeled as an illustrative proxy on a separate stylized model, not a DGE-METRIC output**, and (c) how such an analysis would be implemented in the DGE-METRIC codebase once the formula is confirmed. Every number in Part 5.3 comes from the toy model, not from DGE-METRIC.

## 1. Session purpose

Teach participants how to frame the optimal-reserve-requirement question, what model outputs it needs as inputs, how the underlying MC = MB logic works using a fully worked illustrative example, and how such an analysis would be implemented in the codebase — while being explicit that the DGE-METRIC-specific version is not yet built.

## 2. Prerequisites from the previous on-site training

- Completed from Online Day 1–2: a validated finance-scenario comparison and energy-efficiency scenario comparison (Day 2 AM).
- No prior exposure to reserve-requirement analysis is assumed — this is new content, not a recap.

## 3. Learning objectives

By the end of this session, participants can:

1. State the reserve-requirement policy question in their own words: how much strategic reserve (of an energy carrier) is worth holding, given its cost and the crisis losses it avoids.
2. List which finance-scenario and efficiency-scenario outputs from Days 1–2 would need to feed into a reserve-adequacy analysis.
3. Explain the three-step MC = MB screening methodology using illustrative toy-model numbers.
4. Correctly distinguish which numbers in this session are illustrative-proxy results and which would need to come from DGE-METRIC before being used for an actual decision.
5. Explain the implementation pattern: which parts of a reserve-requirement analysis would be a post-processing script reading existing DGE-METRIC outputs, versus a structural addition to `ModFiles/`/`Functions/`.

## 4. Recap / bridge from the previous session

This morning's finance and efficiency scenarios each imply different exposure to supply disruption — e.g., a scenario with higher import dependence on a single fuel carrier has a different reserve-adequacy profile than one with more distributed, efficient domestic demand. Today connects "how financing and efficiency choices shape the energy system" (Days 1–2) to "how much buffer against disruption is worth holding" (today).

## 5. Conceptual explanation

### 5.1 The policy question

Definition: a strategic reserve requirement is a target level of stockpiled or standby capacity (crude oil, refined products, LNG, LPG, coal, or grid storage) held to buffer against a supply disruption. "Optimal" means the level at which the marginal cost of one more unit of coverage equals the marginal benefit (avoided crisis losses) — MC = MB.

### 5.2 Inputs needed from Days 1–2

- Energy-carrier demand and import dependence under the efficiency scenario vs. PDP8 baseline (Day 2 AM).
- GDP, investment, and fiscal paths under the finance scenarios (Days 1–2) — these determine how large a disruption's economic cost would be and how much fiscal space exists to hold reserves.

`[SME REVIEW NEEDED: confirm which specific DGE-METRIC output variables feed a production-network-based expected-GDP-loss-per-carrier calculation once the DGE-METRIC reserve module exists]`.

### 5.3 Illustrative proxy methodology: `Toy Model SOE MC`

**This is not DGE-METRIC.** Source: `Toy Model SOE MC/email_optimal_reserve_requirements.md` and `reserve_breakeven_table.md` (a separate stylized small-open-economy Monte Carlo model). The email is explicit: *"the full DGE-METRIC model is what will actually determine the expected GDP loss per energy carrier from a supply disruption... That run will only happen once the contract for the DGE-METRIC work has been finalised... treat [these] verdicts as illustrative/training-stage results, not the final word."*

The logic in one line: hold reserves up to the point where the marginal cost of one more day of coverage equals the marginal benefit (avoided crisis losses) — MC = MB. Three steps:

**Step 1 — Screen (break-even accounting).** For each carrier and coverage level, compute the annualized cost of holding the reserve (storage + capital recovery), then back out the minimum crisis GDP loss (%) that would make the reserve pay for itself. Baseline GDP (2024): USD 430,000m; crisis probability p: 0.04/yr; break-even divisor (1% GDP): USD 172.0m (= p × GDP/100). Illustrative ranking (lowest-to-highest break-even bar): refined-product tanks (8-day cover) and distributed BESS clear the lowest bar (≈0.16–0.18% of GDP); 90-day imported-coal cover and 6-MTA LNG need the largest crises (≈1.9–2.0% of GDP).

**Step 2 — Validate (endogenous CES shock test).** Feed a 20%-of-annual-supply and a 50% ("tail-event") disruption through the toy model's CES production function and read off the actual avoided GDP loss, compared against the Step-1 threshold. Illustrative current result: **every fuel carrier tested comes back "not justified" at both shock sizes** under the toy model's current calibration — the avoided GDP loss never reaches the break-even bar. Grid storage (PSHP/BESS) sits outside this test.

**Step 3 — Optimize (Monte-Carlo welfare maximization).** Search over a grid of coverage days for the level that maximizes Net Reserve Value, NRV(d) = insurance benefit(d) − storage cost(d) (a Monte-Carlo average over simulated crises). **Caveat carried over from the source**: the latest joint run hit the edge of the search grid (5-year cover) with a storage-cost figure that is clearly mis-scaled — treat as provisional pending a corrected re-run.

### 5.4 Reading the illustrative numbers responsibly

- These are **toy-model, illustrative-proxy numbers**, useful for teaching the MC = MB logic — not for citing as Vietnam's actual optimal reserve level.
- The "not justified" Step-2 verdicts depend entirely on the toy model's crisis-probability and shock-size assumptions, themselves flagged in the source as needing stakeholder discussion.
- Do not present any Step 1–3 number from this session as a DGE-METRIC output or as a policy recommendation.

### 5.5 [New 2026-07-13] Implementation: where this would live in DGE-METRIC

Reuses the structure-vs-calibration distinction previously taught for pathway model modification (now generalized, since DER/LNG-to-Hydrogen pathways themselves are out of scope this iteration):

- A reserve-requirement analysis most plausibly lives as a **post-processing script** reading existing DGE-METRIC scenario/pathway outputs (energy-carrier demand, import dependence, GDP/investment/fiscal paths) — analogous to how `HandsOn3_Group_Chart_and_Narrative.md`'s chart-building scripts read run outputs, rather than as a new structural equation block inside `ModFiles/`.
- If the formula turns out to require a genuinely new structural relationship (e.g., an endogenous crisis-cost channel inside the model itself, not just a post-processing calculation on its outputs), that piece would belong in `ModFiles/`, with its calibration/parameterization in `Functions/` or `ExcelFiles/` — the same pattern used throughout this course for any model modification.
- **This implementation pattern is itself provisional** until the DGE-METRIC-specific formula is confirmed — teach it as "how you would approach implementing this," not as a confirmed design.

## 6. Hands-on task (design/prep — no calculation run today)

See [`exercise.md`](exercise.md). In brief: read the illustrative break-even table; choose one carrier to work through in detail tomorrow morning's guided open lab; draft an implementation plan for that carrier documenting the mechanism, the DGE-METRIC outputs it would need, where the logic would live in the codebase, and what remains `[SME REVIEW NEEDED]`.

## 7. Expected output

One implementation plan per group (see [`expected-outputs.md`](expected-outputs.md)), stored in [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md), ready for tomorrow's hands-on lab to complete.

## 8. Debrief questions

- In your own words, what does MC = MB mean for a strategic reserve?
- Why does the source material insist on calling the Step 2 "not justified" results illustrative rather than final?
- For your chosen carrier's implementation plan, would this most likely be a post-processing script or a structural model change — and why?

## 9. Common errors and troubleshooting

- **Presenting toy-model numbers as DGE-METRIC results**: correct immediately — the two are explicitly different models with different scope.
- **Treating "not justified" as "no reserve is ever needed"**: the source flags this as dependent on unsettled crisis-probability/shock-size assumptions and explicitly excludes grid storage from the test.
- **Skipping the caveat on the Step 3 corner solution**: the 5-year/mis-scaled-cost result must be flagged as provisional, not reported as an optimum.
- **Presenting the implementation plan as a confirmed design**: it is a reasonable first approach, contingent on the formula itself being confirmed — mark it `[SME REVIEW NEEDED]` accordingly.

## 10. Documentation or reporting task

Each group records in [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md): the policy question framing, inputs needed from Days 1–2, the chosen carrier, and the implementation plan (mechanism, DGE-METRIC outputs needed, codebase location, open SME items).

## 11. Preparation for the next session

Online Day 3 morning is a guided open lab: participants finish the MC = MB walkthrough by hand for their chosen carrier and complete the full reserve-requirement analysis note, using today's implementation plan as the starting point.
