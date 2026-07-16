\
# Facilitator Guide — Training Day 5 (Online Day 3) Afternoon — Friday 24 July 2026

Companion to [`lesson.md`](lesson.md), [`sensitivity-plan-template.md`](sensitivity-plan-template.md), [`independent-use-checklist.md`](independent-use-checklist.md), and [`exit-ticket.md`](exit-ticket.md).

`[SME REVIEW NEEDED: confirm start/end clock time and time zone for 24 July 2026 — see ../../../qa/sme-questions.md item 5]`. Durations below are relative minute blocks.

## Session length

180 minutes total.

**Restructured 2026-07-13**: this session was the full course wrap-up (synthesis, three checklists, group reflection, exit ticket, remaining questions, next steps). It is now calibration internals/modification/sensitivity analysis, ending in a 30-minute close. This is a deliberate, user-approved exception to `../../../CLAUDE.md`'s "final afternoon must not be a new technical module" rule — see [`../../../design/decision-log.md`](../../../design/decision-log.md). Resist the temptation to expand today's content further into re-teaching earlier sessions; the course-arc recap in Block 1 is brief by design.

## Trainer flow

| Block | Duration | Content | Source |
|---|---:|---|---|
| 1. Recap calibration workflow and why it matters | 10 min | Brief course-arc recap (table, `lesson.md` Part 4); why accounting coherence is the precondition for trusting any comparison | `lesson.md` Part 4 |
| 2. Calibration internals | 30 min | Data inputs vs. structural parameters; workbook structure; the IO calibration pipeline and its validation/audit outputs | `docs/calibration.md`; Day 3 plan Session 3 |
| 3. How to modify calibration | 25 min | Data-input change (`ExcelFiles/`) vs. structural-parameter change (`Functions/` helper); re-run and re-validate | `docs/calibration.md` |
| Break | 15 min | | |
| 4. Sensitivity analysis method | 30 min | One-at-a-time parameter perturbation; why isolating one parameter matters; sensitivity log | This lesson, Part 5.4 — general good practice, flagged as not DGE-METRIC-specific |
| 5. Draft sensitivity-analysis plan | 30 min | Groups pick one structural parameter and draft a plan using `sensitivity-plan-template.md` | |
| 6. Report-out | 10 min | Fast report-out across groups | |
| 7. Course close | 30 min | Independent-use checklist (single combined version); exit ticket | `independent-use-checklist.md`; `exit-ticket.md` |

## Facilitation quality gate

- Reject a sensitivity plan that perturbs more than one parameter at once, or that invents a parameter file location not verified in this cohort's repository — mark it `[SME REVIEW NEEDED]` instead.
- Block 7 is a self-assessment and a written submission, not a discussion — keep it moving; do not let it expand back into the old group-reflection format.

## Facilitation prompts

- "If your run's accounting-coherence check failed after a parameter perturbation, would you trust the resulting sensitivity result? Why or why not?"
- "Which of this week's results would most change if this parameter turned out to be wrong?"

## Risk checks

- If time runs short, protect Block 7 (course close) over Block 6 (report-out) — the exit ticket is the one output every participant must leave with, consistent with how the previous wrap-up structure protected its exit ticket.
- Open institutional/SME questions raised during the session are not worked live — direct them to [`../../../qa/sme-questions.md`](../../../qa/sme-questions.md) for asynchronous follow-up rather than spending Block 7 time on them.
