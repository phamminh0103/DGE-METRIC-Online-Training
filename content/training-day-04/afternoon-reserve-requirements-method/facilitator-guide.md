\
# Facilitator Guide — Training Day 4 (Online Day 2) Afternoon — Thursday 23 July 2026

Companion to [`lesson.md`](lesson.md).

`[SME REVIEW NEEDED: confirm start/end clock time and time zone for 23 July 2026 — see ../../../qa/sme-questions.md item 5]`. Durations below are relative minute blocks.

## Session length

180 minutes total.

**Restructured 2026-07-13**: this session was "Energy Transition Pathways" (DER, Efficiency/DSM, LNG-to-Hydrogen). It is now "Reserve Requirements — Method and Implementation" — the core-method content previously taught in the old Day 3 AM session (blocks 1–4 below) moved here, and a new implementation block (5) repurposes the old pathway model-modification framing. See [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Before this session runs

State to participants, verbally and on the first slide: *"Today's numbers come from a separate illustrative toy model, not from DGE-METRIC. DGE-METRIC's own reserve-requirement analysis has not yet been built."* Do not soften or drop this framing — it is a `../../../CLAUDE.md` requirement (see "Optimal reserve requirement rules").

## Trainer flow

| Block | Duration | Content | Source |
|---|---:|---|---|
| 1. Frame the question and the caveat | 15 min | State the policy question; state the DGE-METRIC/toy-model distinction up front | `Toy Model SOE MC/email_optimal_reserve_requirements.md` |
| 2. Inputs from Days 1–2 | 15 min | Map which finance-scenario and efficiency-scenario outputs feed a reserve-adequacy analysis | This lesson, Part 5.2 |
| 3. Walk through Step 1 (break-even) | 25 min | Present the break-even table; explain the MC = MB accounting logic | `reserve_breakeven_table.md` |
| 4. Walk through Steps 2–3 (validate, optimize) | 25 min | Present the "not justified" verdicts and the Step-3 caveat; discuss why these are illustrative | Same source |
| Break | 15 min | | |
| 5. [New] Implementation: where this would live in DGE-METRIC | 35 min | Structure-vs-calibration pattern (post-processing script vs. `ModFiles/`/`Functions/`), applied to reserve requirements | This lesson, Part 5.5 |
| 6. Draft implementation plan | 35 min | Groups choose a carrier and draft an implementation plan | `exercise.md` |
| 7. Wrap and preview | 15 min | Confirm implementation plan recorded; preview tomorrow's guided open lab | |

## Facilitation quality gate

- Reject any framing, written or verbal, that presents a Step 1–3 number as a DGE-METRIC output, a Vietnam policy recommendation, or a settled fact. Every mention of a specific number must carry the "illustrative toy-model proxy" qualifier the first time it is used in each block.
- Block 5's implementation framing is a reasonable first approach, not a confirmed design — do not let groups present their implementation plan as settled.

## Facilitation prompts

- "What would have to be true about crisis probability or shock size for a 'not justified' verdict to flip to 'justified'?"
- "Why does the source material treat the Step-3 corner solution as a bug, not a result?"
- "For your chosen carrier, would implementing this analysis mean writing a new post-processing script, or touching the model's structural equations — and how do you know?"

## Risk checks

- If a participant (or stakeholder observer) asks for "the" optimal reserve number for Vietnam, restate the caveat rather than answering with a toy-model figure as if it were final.
- If a group's carrier choice has thin source support (e.g. LNG or coal specifics), let them proceed with the break-even table's numbers but flag any narrative claim beyond the table as `[SME REVIEW NEEDED]`.
