\
# Exercise — Codebase Navigation, Git/GitHub Desktop, Calibration & Scenario Hands-On (Online Day 2 AM)

Adapted from [`06_HandsOn_Materials/Day3/HandsOn1_Baseline_Calibration.md`](../../../../../06_HandsOn_Materials/Day3/HandsOn1_Baseline_Calibration.md) and [`HandsOn2_Baseline_vs_Alternative.md`](../../../../../06_HandsOn_Materials/Day3/HandsOn2_Baseline_vs_Alternative.md). **Restructured 2026-07-13**: Parts A and B (codebase navigation, Git/GitHub Desktop) moved here from the old Day 1 PM exercise; Part E (efficiency-scenario run) is new — see [`../../../design/decision-log.md`](../../../design/decision-log.md).

## Part A: Equation → helper-function trace (pair task, ~15 min)

1. Open `ModFiles/` and pick one equation your pair can both read (ask the facilitator for a suggested starting equation if the file is large).
2. Identify one parameter or variable that equation references but does not itself compute.
3. Search `Functions/` for the helper that computes or supplies that value. If it isn't in `Functions/`, check whether it's a direct calibration input from `ExcelFiles/` instead.
4. Write down: equation name/location → referenced parameter → where it's actually set (function name, or "direct calibration input").

## Part B: Version control with GitHub Desktop + VS Code (individual task, ~15 min)

1. Clone the repository using GitHub Desktop's visual interface (no command line).
2. Make one commit: create or edit a short scratch file, stage it, and commit with a one-line message.
3. Open the same repository folder in VS Code; find the Source Control panel and confirm it shows the same commit history as GitHub Desktop.
4. Note one thing you'd use GitHub Desktop for and one thing you'd use VS Code's Source Control panel for.

## Part C: Baseline calibration run (~25 min)

1. Start from a clean MATLAB session for your group; set the working directory to the model root.
2. Run the baseline calibration script (`[SME REVIEW NEEDED: confirm the exact script name/entry point for this repository copy]`).
3. Confirm the run completed without solver failure.
4. Check core diagnostics — mark each Pass or Needs attention: run completed without fatal errors; residuals within acceptable tolerance; steady-state or transition solver convergence achieved; key accounting identities hold; output files generated in expected location.
5. Record one diagnostic result and its one-sentence interpretation. If the run failed, categorize the failure (path / missing-or-locked input / non-convergence / syntax — see `lesson.md` Part 5.4) and apply the matching fix before continuing.

## Part D: Finance-scenario run (~20 min of Block 5's 35)

Scenario design rule: change only scenario-relevant assumptions. Do not change unrelated baseline parameters.

1. Duplicate/copy your baseline run configuration; rename it using yesterday's scenario ID (e.g. `PDP8-Concessional`).
2. Edit only your assigned scenario's input (financing rate to 5%, or recycling flag to on). Try asking an AI coding assistant in VS Code to help you locate exactly which line/cell controls this setting before editing it by hand.
3. Run your scenario and its matching base case with the same solver options and horizon; export both to a comparable format.

## Part E: [Added] Energy-efficiency scenario run (~15 min of Block 5's 35)

1. Duplicate/copy the PDP8 baseline run configuration; rename it `efficiency-dsm-baseline`.
2. Apply the sector-specific efficiency coefficients from yesterday's metadata sheet.
3. Run the efficiency scenario and the PDP8 baseline with the same solver options and horizon; export both to a comparable format.

## Part F: Comparison tables (~20 min of Block 6's 35)

**Finance scenario:**

| Indicator | Base case | Your scenario | Difference | Interpretation |
|---|---:|---:|---:|---|
| Public financing rate | | | | |
| Renewable capital stock | | | | |
| GDP | | | | |
| Investment | | | | |
| Emission-tax revenue | | | | |
| Renewable generation | | | | |

**Energy-efficiency scenario:**

| Indicator | PDP8 baseline | Efficiency scenario | Difference | Interpretation |
|---|---:|---:|---:|---|
| Energy intensity | | | | |
| Final energy demand | | | | |
| GDP | | | | |
| Investment | | | | |
| Energy prices/expenditure | | | | |

Quality checks: base case and scenario use identical run settings; finance base case uses the **same emissions pathway** as the scenario; every difference is interpreted, not only reported; the efficiency scenario's GDP effect accounts for the rebound effect (net, not gross, savings).

## Part G: Chart and narrative (~15 min of Block 6's 35)

Choose one indicator with clear policy relevance from either comparison table. Build one chart and write the 4-sentence narrative: result, mechanism, policy implication, caveat.

## Common issues and quick fixes

- Path error: re-run `setup_paths.m`/`addpath` and confirm current folder.
- No difference between scenario and base case: verify the scenario input was actually changed.
- Cross-pathway mismatch: check emissions-pathway labels match before comparing (finance scenario only — the efficiency scenario always compares against PDP8).

## Deliverable

Codebase-navigation trace; a local repository with at least one GitHub Desktop commit; one calibration diagnostic note; two comparison tables (finance, efficiency); one chart plus 4-sentence narrative — recorded in the finance and energy-efficiency scenario logs.
