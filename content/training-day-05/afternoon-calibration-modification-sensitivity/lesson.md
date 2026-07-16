\
# Training Day 5 (Online Day 3) — Afternoon: Calibration Internals — Modification & Sensitivity Analysis, + Course Close

**Date: Friday 24 July 2026.** Status: approved for delivery. **Restructured 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). This folder was `afternoon-wrap-up`. Per the user's explicit decision, this session is now a full new technical module (calibration internals, modification, sensitivity analysis) ending in a 30-minute close, rather than the previous full wrap-up (synthesis, three checklists, group reflection, exit ticket, remaining questions, next steps). This is a deliberate, documented exception to `../../../CLAUDE.md`'s rule that the final afternoon must not be a new technical module — see the decision log entry for the full rationale.

## 1. Session purpose

Teach calibration internals in depth: the workbook structure, the IO calibration pipeline, how to modify a data input or a structural parameter, and how to run a one-at-a-time sensitivity analysis. Close the course with a short independent-use checklist and exit ticket.

## 2. Prerequisites from the previous on-site training

- Completed from Online Day 2 AM: a baseline calibration run and diagnostic note.
- Recap-level familiarity with the calibration workflow from Online Day 1 PM's brief pointer to `docs/calibration.md`.

## 3. Learning objectives

By the end of this session, participants can:

1. Explain the calibration workbook structure: data inputs vs. structural parameters.
2. Explain the IO calibration pipeline and its validation/audit checks.
3. Modify a calibration data input and a structural parameter, and state which files each requires touching.
4. Design and document a one-at-a-time sensitivity-analysis plan for one structural parameter.
5. Complete the course's independent-use checklist and exit ticket.

## 4. Recap / bridge from the previous session

Brief course-arc recap (5 minutes, folded into Block 1 — no separate synthesis block today):

| Day | Focus | What it produced |
|---|---|---|
| Day 1 PM | Finance & energy-efficiency scenario definition | Two completed scenario metadata sheets |
| Day 2 AM | Codebase nav, Git, calibration & scenario hands-on | Calibration diagnostic; finance + efficiency comparison charts |
| Day 2 PM | Reserve requirements — method & implementation | Implementation plan for a self-chosen carrier |
| Day 3 AM | Guided open lab | Completed reserve-requirement analysis note |

Today closes the loop back to calibration — the foundation everything else this week depended on — by going one level deeper: not just running it, but modifying it and testing how sensitive results are to its parameters.

## 5. Conceptual explanation

### 5.1 Calibration workbook structure

Source-grounded in [`docs/calibration.md`](../../../../../DGE-METRIC-VietNam/docs/calibration.md):

- **Data inputs** pinning down the steady state: sectoral employment, value-added, labour cost, export, import, and emission shares by sector (Primary, Fossil, Renewables, Secondary, Tertiary).
- **Structural parameters**: discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs.
- Calibration credibility rests on accounting coherence: sectoral value-added shares, intermediate-input shares, and import decomposition must sum consistently before the baseline is trusted for scenario comparison.

### 5.2 The IO calibration pipeline

Per [`../../../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`](../../../../Day%203/DGE_METRIC_Training_Day3_Session_Plan.md) Session 3: `Training/Day3_Calibration/IO_Calibration/run_pipeline.m` → `split_utilities_sector.m` → `aggregate_for_dge.m`, with validation (`IO_2019_5sec_for_DGE_validation.csv`) and audit (`IO_2019_5sec_for_DGE_audit.csv`) outputs. **Not verified present in this Dropbox copy** — `[SME REVIEW NEEDED: confirm live location of the IO_Calibration pipeline folder for this cohort — see qa/sme-questions.md item 3]`.

Quality checks the pipeline should enforce: output conservation, import conservation, value-added consistency, sectoral labor compensation plausibility, non-negativity of final matrices.

### 5.3 How to modify calibration

- **Changing a data input** (e.g. a sectoral employment or value-added share): edit the calibration workbook in `ExcelFiles/`, then re-run the pipeline and re-check the validation/audit outputs before trusting the result.
- **Changing a structural parameter** (e.g. an elasticity of substitution or the discount factor): typically set via a `Functions/` helper or a named range in the calibration workbook, depending on how this cohort's repository is configured — confirm the exact location before editing (`[SME REVIEW NEEDED: confirm structural-parameter file locations for this cohort's repository copy]`).
- Either change requires re-running the full calibration-to-baseline chain and re-validating accounting coherence — a parameter change is not "free" just because it's a single number.

### 5.4 [New 2026-07-13] Sensitivity analysis method

General good-practice methodology — **not itself a DGE-METRIC-specific procedure documented in the reviewed sources**, taught and flagged as such:

- **One-at-a-time (OAT) parameter perturbation**: pick one structural parameter, perturb it by a defined amount (e.g. ±10%, or a specific alternative value with its own justification), re-run the full calibration-to-baseline chain, and compare outputs against the unperturbed baseline.
- **Why isolate one parameter at a time**: if you perturb two parameters simultaneously, you cannot attribute the resulting output change to either one individually — the same discipline used throughout this course for scenario design ("do not modify unrelated baseline parameters to force a desired result," per `../../../CLAUDE.md` "Scenario design rules").
- **What to check**: the same accounting-coherence diagnostics used for any calibration run, plus the specific output indicators most likely to respond to your chosen parameter (e.g., an elasticity of substitution would plausibly move investment and sectoral output; the discount factor would plausibly move the savings/investment path).
- **Keeping a sensitivity log**: record the parameter, its baseline value, the perturbed value, the diagnostic result, and the output difference — the same metadata discipline used for scenario logs all week.

## 6. Hands-on task

See [`exercise.md`](exercise.md). In brief: in groups, pick one structural parameter, define a perturbation, state your expected effect and which output indicators you'd check, and draft a sensitivity-analysis plan using [`sensitivity-plan-template.md`](sensitivity-plan-template.md).

## 7. Expected output

See [`expected-outputs.md`](expected-outputs.md). One sensitivity-analysis plan per group; a completed independent-use checklist; a completed exit ticket.

## 8. Debrief questions

- Why would perturbing two structural parameters at once make your sensitivity result harder to interpret than perturbing one?
- Which of your course week's results (finance scenario, efficiency scenario, reserve-requirement carrier choice) would you now want to re-check against a calibration sensitivity test, and why?
- What's the single most useful thing you can now do independently that you couldn't do before this course?

## 9. Common errors and troubleshooting

- **Perturbing a data input and calling it a "sensitivity analysis"**: sensitivity analysis in this course refers specifically to structural-parameter perturbation, not re-calibrating to different source data (that's a calibration update, a different exercise).
- **Perturbing more than one parameter at once**: isolate one parameter per sensitivity run.
- **Skipping re-validation after a parameter change**: a perturbed run still needs the same accounting-coherence checks as any calibration run before its outputs are trusted.
- **Inventing a plausible-sounding parameter file location**: if you haven't verified where a structural parameter is actually set in this cohort's repository, mark it `[SME REVIEW NEEDED]` rather than guessing.

## 10. Documentation or reporting task

Each group records their sensitivity-analysis plan using [`sensitivity-plan-template.md`](sensitivity-plan-template.md): parameter, baseline value, perturbation, expected effect, output indicators to check, and any `[SME REVIEW NEEDED]` items.

## 11. Course close (30 min — replaces "preparation for the next session," as this is the final session)

See [`independent-use-checklist.md`](independent-use-checklist.md) and [`exit-ticket.md`](exit-ticket.md). Participants self-assess against a single combined independent-use checklist (folding in the reproducibility and policy-communication standards used all week, rather than three separate checklists), then submit an individual exit ticket. Open institutional/SME questions are not worked live in this session — they are tracked in [`../../../qa/sme-questions.md`](../../../qa/sme-questions.md) for asynchronous follow-up.
