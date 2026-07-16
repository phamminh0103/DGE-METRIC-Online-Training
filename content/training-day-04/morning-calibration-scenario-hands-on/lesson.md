\
# Training Day 4 (Online Day 2) — Morning: Calibration & Scenario Hands-On — Codebase Navigation, Git/GitHub Desktop, Debugging, AI-Assisted VS Code

**Date: Thursday 23 July 2026.** Status: approved for delivery. **Restructured 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). Codebase navigation and Git/GitHub Desktop content moved here from the old Day 1 PM session; this session now also runs the energy-efficiency scenario alongside the finance matrix (previously the efficiency scenario was only designed, not run, in the old Day 2 PM pathway session).

## 1. Session purpose

Build codebase-navigation and version-control fluency, run the baseline calibration, read its diagnostics, then run and interpret both the six-scenario finance matrix and the energy-efficiency scenario prepared yesterday afternoon. Produce one calibration diagnostic note and one comparison chart with a policy narrative covering both scenario families.

## 2. Prerequisites from the previous on-site training

- MATLAB and Dynare installed and working; repository paths loaded (`setup_paths.m`).
- Baseline input files present in the standard project structure.
- Completed from yesterday (Online Day 1 PM): finance-scenario metadata sheet and energy-efficiency scenario metadata sheet, in [`../../../scenarios/finance/scenario-log.md`](../../../scenarios/finance/scenario-log.md) and [`../../../scenarios/energy-efficiency/efficiency-scenario-log.md`](../../../scenarios/energy-efficiency/efficiency-scenario-log.md).

`[SME REVIEW NEEDED: confirm where online participants access the live model repository (calibration workbooks, .mod/.m files) for this hands-on session — see ../../../qa/sme-questions.md item 3]`.

## 3. Learning objectives

By the end of this session, participants can:

1. Locate a specific equation in `ModFiles/` and trace it to the MATLAB helper in `Functions/` that computes its inputs.
2. Clone a repository and commit via GitHub Desktop's visual interface; use VS Code's Source Control panel alongside it.
3. Execute a baseline calibration run and read its core diagnostics.
4. Categorize a MATLAB/Dynare failure (path, missing/locked input, non-convergence, or syntax) before attempting a fix.
5. Run their assigned finance scenario against the correct base case, and the energy-efficiency scenario against the PDP8 baseline, under identical settings.
6. Use an AI coding assistant in VS Code to help locate or explain a script's logic.
7. Interpret GDP, investment, fiscal, emissions, and efficiency-specific effects across both scenario families.

## 4. Recap / bridge from the previous session

From yesterday afternoon: the six-scenario finance matrix (`PDP8-Base`, `NZ-Base`, `PDP8-Concessional`, `NZ-Concessional`, `PDP8-Recycle`, `NZ-Recycle`) with each group's scenario assignment and expected mechanism, and the energy-efficiency scenario's full metadata sheet. Confirm every group still has both before starting.

## 5. Conceptual explanation

### 5.1 Codebase navigation: from equation to helper function

Per [`docs/index.md`](../../../../../DGE-METRIC-VietNam/docs/index.md):

- `ModFiles/` holds the Dynare model blocks and equations. Each equation typically references parameters and variables that are computed or set elsewhere in the repository, not hard-coded in the `.mod` file itself.
- `Functions/` holds MATLAB helpers: steady-state computation, aggregation/input–output blocks, plotting and diagnostics. A parameter or initial value referenced in a `ModFiles/` equation is frequently populated by a corresponding function in `Functions/`, or read from `ExcelFiles/` via an Excel-helper function.
- **The navigation skill**: given an equation, identify (a) which parameters/variables it references, (b) whether each is set directly in the calibration workbook (`ExcelFiles/`) or computed by a function in `Functions/`, and (c) which function that is.

### 5.2 Version control with GitHub Desktop and VS Code

- **Why it matters here**: the course requires documenting every scenario with a metadata block and storing it in a shared, reviewable log. Version control turns "a file with a history of manual edits" into "a file with a reviewable, revertible history."
- **Today's workflow — no command line required**: clone the repository and make your first commit using GitHub Desktop's visual interface; open the same repository in VS Code — the two tools share one Git history; use VS Code's Source Control panel to review and stage changes alongside GitHub Desktop.
- **Scope for today**: individual, local version control of a participant's own scenario files — not team branching/merging workflows.

### 5.3 What "baseline calibration" means here

Per [`docs/calibration.md`](../../../../../DGE-METRIC-VietNam/docs/calibration.md), the baseline calibration solves the model's steady state from the Excel-derived data inputs and structural parameters. A calibration run is only usable for scenario comparison once its diagnostics pass.

### 5.4 Debugging as a categorization skill

1. **Path error** — the run can't find a file it needs. Check the current folder and whether `setup_paths.m`/`addpath` ran.
2. **Missing or locked input** — a required workbook or file isn't where the run expects it, or is open/locked elsewhere.
3. **Non-convergence** — the run executes but the solver doesn't reach a steady state or transition path. Check initial values and baseline assumptions before touching solver tolerances.
4. **Syntax/structural error** — a `.mod` file or script has a structural problem. Usually caught by Dynare's own error message pointing at a line/block.

### 5.5 What "comparable" means for both scenario families

Baseline and alternative must be run with identical solver options and horizon, changing only the scenario-relevant assumption:

- `PDP8-Concessional` vs. `PDP8-Base` (financing rate only differs); `NZ-Concessional` vs. `NZ-Base`; `PDP8-Recycle` vs. `PDP8-Base`; `NZ-Recycle` vs. `NZ-Base`.
- Energy-efficiency scenario vs. **PDP8 baseline** (efficiency coefficients differ; emissions pathway held at PDP8).

### 5.6 Indicators to read

Finance: public financing rate, renewable capital stock, GDP, investment, emission-tax revenue, recycled renewable investment (recycling scenarios only), emissions, renewable generation. Efficiency: energy intensity, final energy demand, GDP, investment, energy prices/expenditure — remembering the rebound effect means net GDP/energy effects are smaller than the gross efficiency gain.

### 5.7 AI-assisted development in VS Code

An AI coding assistant inside VS Code can help **locate** a function or variable across a large codebase, **explain** what an unfamiliar block of MATLAB or Dynare code does in plain language, and **draft** a small, well-scoped edit for review. **Always review AI-suggested edits against the source-grounding rules in `../../../CLAUDE.md`** before applying them to a model file.

## 6. Hands-on task

See [`exercise.md`](exercise.md) for full steps. In brief:

1. Codebase navigation: locate one equation in `ModFiles/` and trace it to its `Functions/` helper.
2. Version control: clone the repository, commit via GitHub Desktop, open in VS Code.
3. Run the baseline calibration; check diagnostics. If it fails, categorize the failure before fixing it.
4. Run your group's assigned finance scenario and its matching base case; run the energy-efficiency scenario against PDP8 baseline. Try using an AI coding assistant to help locate the setting you need to change.
5. Build a comparison table and produce one chart with a 4-sentence policy narrative.

## 7. Expected output

See [`expected-outputs.md`](expected-outputs.md). One calibration diagnostic note (including a failure category if you hit one); one comparison chart and 4-sentence narrative covering both the finance scenario and the efficiency scenario; a local repository committed to via GitHub Desktop.

## 8. Debrief questions

- What does your calibration diagnostic tell you about baseline reliability for scenario comparison?
- If you hit an error, which of the four categories was it, and how did knowing the category change where you looked for the fix?
- Did the AI assistant's suggestion need correcting before you trusted it? What did you check before applying it?
- Which transmission channel best explains the difference between your finance scenario and its base case? Between the efficiency scenario and PDP8 baseline?
- Does the direction and rough magnitude of your results match the expected mechanisms you wrote down yesterday? If not, what might explain the gap?

## 9. Common errors and troubleshooting

- **Tracing the wrong direction**: look for what an equation consumes (inputs), not what it produces.
- **Path error**: re-run `addpath`/`setup_paths.m` and confirm the current folder is the repository root.
- **Missing or locked input**: verify the baseline workbook and model file locations, and that no one else has the workbook open.
- **Non-convergence**: re-check initial values and baseline assumptions rather than changing solver tolerances first.
- **Syntax/structural error**: read the Dynare error message for the specific line/block it flags.
- **No difference between scenario and base case**: verify the scenario input was actually changed — a common cause is re-running the base-case configuration by mistake.
- **Cross-pathway comparison by mistake**: check the emissions-pathway label matches between your finance scenario and its base case.
- **Trusting an AI-suggested edit without checking it**: always confirm the assistant's suggestion matches the actual variable/units before applying it.
- **Committing before staging**: check what's staged in GitHub Desktop before you commit.

## 10. Documentation or reporting task

Each group records, appended to the relevant log:

- Codebase-navigation trace and Git commit confirmation.
- Diagnostic checked, result observed, interpretation (calibration), and failure category if applicable — in [`../../../scenarios/finance/scenario-log.md`](../../../scenarios/finance/scenario-log.md).
- Comparison table and 4-sentence narrative for the finance scenario — in the finance scenario log.
- Comparison table and 4-sentence narrative for the efficiency scenario — in [`../../../scenarios/energy-efficiency/efficiency-scenario-log.md`](../../../scenarios/energy-efficiency/efficiency-scenario-log.md).

## 11. Preparation for the next session

This afternoon (Online Day 2 PM) shifts to reserve requirements — the method and how it would be implemented in the DGE-METRIC codebase, using the same structure-vs-calibration distinction you just practiced in Part 5.1. Bring your calibration diagnostic note as evidence the baseline is usable.
