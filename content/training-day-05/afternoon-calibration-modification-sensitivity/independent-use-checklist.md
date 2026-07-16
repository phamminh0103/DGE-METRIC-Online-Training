\
# Course Close — Independent-Use Checklist

Companion to [`lesson.md`](lesson.md) Part 11. **Restructured 2026-07-13**: previously three separate checklists (independent-use, reproducibility, policy-communication) across a dedicated wrap-up session; now one combined checklist in a 30-minute close — see [`../../../design/decision-log.md`](../../../design/decision-log.md). Participants self-assess against each item; facilitator collects a show-of-hands or written self-rating.

## Can you, without instructor support:

**Calibration and codebase**
- [ ] Locate the role of each major repository folder (`docs/`, `ExcelFiles/`, `Functions/`, `ModFiles/`, `scripts/`, `Training/`)?
- [ ] Trace an equation in `ModFiles/` to the `Functions/` helper that feeds it, and categorize a MATLAB/Dynare failure before attempting a fix?
- [ ] Run a baseline calibration and read its core diagnostics (residuals, convergence, accounting identities)?
- [ ] Explain the difference between modifying a calibration data input and modifying a structural parameter, and which files each touches?
- [ ] Design a one-at-a-time sensitivity-analysis plan for a structural parameter?

**Scenario design**
- [ ] Set up a finance scenario that changes exactly one assumption relative to its correct base case?
- [ ] Draft a source-grounded energy-efficiency scenario, marking any unsourced assumption `[SME REVIEW NEEDED]` rather than inventing it?
- [ ] Produce one chart and a 4-sentence policy narrative (result, mechanism, implication, caveat) from a scenario comparison, with any illustrative-proxy or toy-model result clearly labeled as such?

**Reserve requirements**
- [ ] Explain the MC = MB logic behind a reserve-requirement question, and state clearly when a number is illustrative-proxy versus DGE-METRIC-specific?
- [ ] Sketch where a reserve-requirement analysis would live in the codebase (post-processing script vs. structural model change)?

**Reproducibility**
- [ ] Every scenario/pathway you worked on this week has a completed metadata block, stored in the shared logs (`../../scenarios/`), not only in personal notes?
- [ ] Your scenario logs are under version control via GitHub Desktop, giving you a reviewable, revertible history?
- [ ] File edits and diagnostic checks are documented well enough that another analyst could reproduce your run from your notes alone?

## Self-check question

Which item above are you least confident in — and is that a "practice more on your own" gap, or a "flag to the course owner" gap?
