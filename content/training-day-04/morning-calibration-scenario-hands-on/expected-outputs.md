\
# Expected Outputs — Online Day 2 AM

## Codebase navigation & version control

- [ ] Names a specific equation location in `ModFiles/`, not just "the model file" generically, and correctly identifies whether its referenced value comes from a `Functions/` helper or directly from `ExcelFiles/`.
- [ ] `git log` (visible via GitHub Desktop or VS Code's Source Control panel) shows at least one commit.

## Calibration diagnostic note

- [ ] Names the specific diagnostic checked (residuals, convergence, accounting identity, or output-file check).
- [ ] States Pass or Needs attention for each of the five minimum quality checks in `exercise.md` Part C.
- [ ] Includes a one-sentence interpretation of what the diagnostic implies for using this baseline in scenario comparison.
- [ ] If a failure occurred, names the correct category (path / missing-or-locked input / non-convergence / syntax) and the fix applied.

## Finance-scenario comparison table

- [ ] Base case and scenario share the same emissions pathway (PDP8 or NZ) and identical run settings.
- [ ] Exactly one input differs (financing rate or recycling flag).
- [ ] Table includes at minimum: GDP, investment, and one finance-specific indicator.
- [ ] Every row has an interpretation, not just a number.

## Energy-efficiency comparison table

- [ ] Compares against the PDP8 baseline (not a finance scenario).
- [ ] Table includes at minimum: energy intensity or final energy demand, GDP, and investment.
- [ ] The interpretation accounts for the rebound effect — net GDP/energy effects are smaller than the gross efficiency gain, not equal to it.

## Chart and narrative

- [ ] Chart title states base case vs. scenario clearly, with units and time period.
- [ ] Narrative follows the 4-sentence template (result, mechanism, policy implication, caveat).
- [ ] Caveat is explicit and specific (not a generic "results may vary").

## Self-check question

Could a participant from a different group read your comparison tables and narrative and correctly state which single variable you changed in each scenario? If not, tighten the scenario-log entry before moving on.
