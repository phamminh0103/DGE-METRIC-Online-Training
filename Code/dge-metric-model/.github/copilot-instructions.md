# Copilot Instructions

Use `AGENTS.md` as the canonical repository-wide rule set.
Use `CLAUDE.md` for repository-specific operational detail.

## Must-follow

- Do not hand-edit generated Dynare outputs (`+DGE_Model/`, `DGE_Model/`, `*_dynamic.m`, `*_static.m`, `*_set_auxiliary_variables.m`).
- Keep source edits in hand-maintained files (`DGE_Model.mod`, `ModFiles/`, `Functions/`, `scripts/`, `docs/`, input workbooks under `ExcelFiles/`).
- Keep implementation plan documents in `docs/implementation_plans/`.
- Update documentation links when moving files.
- For a Baseline-only endogenous target (variable floats to hit a target in Baseline, ordinary exogenous elsewhere — e.g. `EE_reg`/`Q_fossil`, `tauCEndo`/`G_reg`): reuse an existing Baseline-correlated compile-time indicator (e.g. `lEndogenousY_p`) rather than a new parameter; branch with a runtime multiplier in one equation, not `@#if`/`@#else`; free the variable only inside the hybrid steady-state solver (`lCalibration_p == 2`); transfer the Baseline path to other scenarios via `apply_baseline_shock_structure`. See `CLAUDE.md`'s "Standard workflow: Baseline-only endogenous targets" section.

If these instructions conflict with `AGENTS.md`, follow `AGENTS.md`.
