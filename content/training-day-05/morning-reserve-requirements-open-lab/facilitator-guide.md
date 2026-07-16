\
# Facilitator Guide — Training Day 5 (Online Day 3) Morning — Friday 24 July 2026

Companion to [`lesson.md`](lesson.md).

`[SME REVIEW NEEDED: confirm start/end clock time and time zone for 24 July 2026 — see ../../../qa/sme-questions.md item 5]`. Durations below are relative minute blocks.

## Session length

180 minutes total.

**Restructured 2026-07-13**: this session was "Optimal Reserve Requirements" and carried both the core method (blocks 1–4 of the old trainer flow) and the guided open lab (block 5) in one 180-minute session. The core method moved to yesterday afternoon; this entire session is now the open lab. See [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Before this session runs

Restate, verbally and on the first slide: *"Today's numbers come from a separate illustrative toy model, not from DGE-METRIC. DGE-METRIC's own reserve-requirement analysis has not yet been built."* Do not soften or drop this framing.

## Trainer flow

| Block | Duration | Content | Source |
|---|---:|---|---|
| 1. Recap method and implementation plan | 15 min | Recap yesterday's MC = MB logic and each group's implementation plan; confirm chosen carrier | Yesterday's `lesson.md` |
| 2. Guided open lab, part 1 | 90 min | Work the break-even and validation logic by hand for the chosen carrier; facilitator circulates rather than presenting one worked example for the whole room | `exercise.md`; `reserve_breakeven_table.md` |
| Break | 15 min | | |
| 3. Guided open lab, part 2 — write it up | 45 min | Finish the reserve-requirement analysis note: inputs, walkthrough, sensitivity notes, remaining SME items | `reserve-analysis-template.md` |
| 4. Report-out and debrief | 15 min | Fast report-out across groups; debrief questions from `lesson.md` Part 8 | |

## Facilitation quality gate

- Reject any framing that presents a Step 1–3 number as a DGE-METRIC output, a Vietnam policy recommendation, or a settled fact — the "illustrative toy-model proxy" qualifier still applies no matter which carrier a group picked.

## Facilitation prompts

- "What would have to be true about crisis probability or shock size for a 'not justified' verdict to flip to 'justified'?"
- "Which DGE-METRIC output — once it exists — would replace the toy model's CES GDP-loss calculation in Step 2?"

## Risk checks

- If a participant (or stakeholder observer) asks for "the" optimal reserve number for Vietnam, restate the caveat rather than answering with a toy-model figure as if it were final.
- Since groups self-select a carrier, circulate actively — with multiple different carriers in play at once, no single worked example on screen will fit every group; be ready to answer break-even-calculation questions for any of the carriers in `reserve_breakeven_table.md`.
- If a group did not complete yesterday's implementation plan, have them draft a minimal version (carrier, mechanism, one input needed) in the first 10 minutes of block 1 rather than skipping it.
