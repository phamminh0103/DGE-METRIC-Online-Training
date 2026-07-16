\
# Facilitator Guide — Training Day 4 (Online Day 2) Morning — Thursday 23 July 2026

Companion to [`lesson.md`](lesson.md).

`[SME REVIEW NEEDED: confirm start/end clock time and time zone for 23 July 2026 — see ../../../qa/sme-questions.md item 5]`. Durations below are relative minute blocks.

## Session length

180 minutes total.

**Restructured 2026-07-13**: codebase navigation and Git/GitHub Desktop content moved here from the old Day 1 PM session (Block 2 below); this session's finance-scenario run now runs alongside the energy-efficiency scenario (Block 5), not just the finance matrix alone. See [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Trainer flow

| Block | Duration | Content | Source |
|---|---:|---|---|
| 1. Objective and setup check | 10 min | Restate expected outputs; confirm MATLAB/Dynare/paths working for every group | Day 3 plan Session 4 |
| 2. Codebase navigation & version control | 30 min | Locate one equation in `ModFiles/`, trace it to `Functions/`; clone + first commit in GitHub Desktop; open in VS Code, use Source Control panel | `docs/index.md`; general Git/GitHub Desktop practice |
| 3. Baseline calibration run | 25 min | Guided execution; diagnostic interpretation (one finding per group) | HandsOn1_Baseline_Calibration.md |
| 4. Debugging common MATLAB/Dynare errors | 20 min | Categorize a failure (path, missing/locked input, non-convergence, syntax) before trying a fix; work through one deliberately-broken example together | `docs/running.md`; existing troubleshooting checklists in HandsOn1/HandsOn2 |
| Break | 15 min | Verify every group has a valid baseline run before continuing | |
| 5. Finance + efficiency scenario run, AI-assisted VS Code demo | 35 min | Each group runs its assigned finance scenario + matching base case, and the efficiency scenario vs. PDP8 baseline, under identical settings; live demo of an AI coding assistant in VS Code locating/explaining the script being edited | HandsOn2_Baseline_vs_Alternative.md; `financing_pathway.md`; `energy_efficiency_pathway.md` |
| 6. Comparison table, chart & narrative | 35 min | Build comparison tables for both scenario families; one chart + 4-sentence narrative per group | HandsOn2/HandsOn3 templates |
| 7. Report-out and debrief | 10 min | Fast report-out; debrief questions from `lesson.md` Part 8 | |

## Pre-session technical checklist

- Confirm required Excel workbooks exist and are not locked.
- Confirm at least one baseline, one finance-scenario, and the efficiency-scenario output can each be produced end-to-end before the session (dry run).
- Pre-create the group → scenario assignment list from yesterday's worksheet to avoid restart delay.
- Confirm GitHub Desktop is installed or installable for every group (see `outreach/detailed-agenda.md` "Before you join").

## Facilitation quality gate

- Reject a group's comparison table if it compares across emissions pathways (e.g. `PDP8-Concessional` vs. `NZ-Base`) — redirect to the correct same-pathway base case.
- The debugging block (4) teaches a categorization method, not an exhaustive bug list — don't let it sprawl into open-ended Q&A on every participant's individual error; park those for the break or a follow-up slot.
- The AI-assistant demo (block 5) is a workflow demonstration, not a claim about DGE-METRIC specifics.
- Block 2's Git teaching is scoped to individual, local version control — do not expand into team branching/merge workflow discussion.

## Risk checks

- If a group's run fails to converge, use it as a live example for block 4 if timing allows; otherwise assign a buddy group and park detailed debugging for a follow-up slot.
- If repository access differs from what was assumed in `exercise.md` (see open item 3), substitute the instructor-provided equivalent script/workbook path and note the substitution in the group's diagnostic note.
- If a participant's environment cannot run the AI assistant (no license/access), demonstrate on the facilitator's screen only.
- Running both scenario families in one 35-minute block is tight — if a group is behind, prioritize finishing the finance scenario (their own assignment) over the efficiency scenario (shared across all groups), and catch up on the efficiency comparison during block 6.
