\
# Training Day 5 (Online Day 3) — Morning: Guided Open Lab — Applying the Reserve-Requirement Method

**Date: Friday 24 July 2026.** Status: **partially blocked, drafted as conceptual + illustrative-proxy content** (same status as yesterday's method session). **Restructured 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). This session previously carried both the reserve-requirement core method (break-even table, Steps 1–3) and the guided open lab in one 180-minute session. The core method moved to yesterday afternoon ([`../../training-day-04/afternoon-reserve-requirements-method/`](../../training-day-04/afternoon-reserve-requirements-method/)); this entire session is now the hands-on lab.

## 1. Session purpose

Hands-on application of yesterday afternoon's MC = MB method to each group's self-chosen energy carrier, finishing the reserve-requirement analysis note. No new conceptual content is introduced today — this is guided practice.

## 2. Prerequisites from the previous on-site training

- Completed from yesterday afternoon (Online Day 2 PM): the implementation plan for your chosen carrier, in [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md).
- The scope note stated yesterday still applies: today's numbers come from a separate illustrative toy model, not DGE-METRIC.

## 3. Learning objectives

By the end of this session, participants can:

1. Apply the MC = MB break-even and validation logic by hand to their chosen carrier.
2. Correctly distinguish illustrative-proxy numbers from anything that would need to be a DGE-METRIC output.
3. Produce a complete reserve-requirement analysis note: inputs, walkthrough, sensitivity notes, caveats.

## 4. Recap / bridge from the previous session

Yesterday afternoon: the policy question, the three-step MC = MB methodology (screen → validate → optimize) using the illustrative `Toy Model SOE MC` numbers, and each group's implementation plan for a self-chosen carrier. Today applies that method to finish the analysis.

## 5. Conceptual explanation

No new conceptual content. Recap only, from yesterday afternoon ([`../../training-day-04/afternoon-reserve-requirements-method/lesson.md`](../../training-day-04/afternoon-reserve-requirements-method/lesson.md) Part 5):

- MC = MB logic; the three-step methodology; baseline GDP (2024) USD 430,000m, crisis probability p = 0.04/yr, break-even divisor USD 172.0m.
- **Restate before starting hands-on work**: *"Today's numbers come from a separate illustrative toy model, not from DGE-METRIC. DGE-METRIC's own reserve-requirement analysis has not yet been built."*

## 6. Hands-on task

See [`exercise.md`](exercise.md). In brief: work the break-even and validation logic by hand for your chosen carrier; identify which carrier(s) clear the lowest break-even bar and explain why in plain language; finish writing your reserve-requirement analysis note, including sensitivity notes and an explicit list of what remains `[SME REVIEW NEEDED]`.

## 7. Expected output

One completed reserve-requirement analysis note per group (see [`expected-outputs.md`](expected-outputs.md)), built around the group's own chosen carrier, documenting inputs, the illustrative-proxy walkthrough, sensitivity considerations, and caveats — explicitly distinguishing conceptual/proxy content from anything DGE-METRIC-specific.

## 8. Debrief questions

- In your own words, what does MC = MB mean for a strategic reserve, using the carrier you chose as an example?
- Why does the source material insist on calling the Step 2 "not justified" results illustrative rather than final?
- Roughly how much larger would the crisis probability or shock size need to be for your carrier's verdict to flip toward "justified"?

## 9. Common errors and troubleshooting

- **Presenting toy-model numbers as DGE-METRIC results**: correct immediately.
- **Treating "not justified" as "no reserve is ever needed"**: dependent on unsettled crisis-probability/shock-size assumptions; grid storage is explicitly excluded from this test.
- **Skipping the caveat on the Step 3 corner solution**: the 5-year/mis-scaled-cost result must be flagged as provisional.
- **Leaving the analysis note's implementation section unfinished**: yesterday's implementation plan is the starting point — carry it forward, don't restart it.

## 10. Documentation or reporting task

Each group completes [`../../../scenarios/reserve-requirements/reserve-analysis-template.md`](../../../scenarios/reserve-requirements/reserve-analysis-template.md): the policy question framing, inputs needed from Days 1–2, the illustrative-proxy walkthrough for their chosen carrier, sensitivity notes, the implementation plan from yesterday, and an explicit list of what is still `[SME REVIEW NEEDED]`.

## 11. Preparation for the next session

This afternoon shifts topic entirely, to calibration internals, modification, and sensitivity analysis — there is no dependency on this session's specific carrier choice.
