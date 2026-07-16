# DGE-METRIC Advanced Training - Track B: Model Calibration And Development

## 1. Track Purpose

This track is designed for participants who need to modify, calibrate, debug, and extend DGE-METRIC in a reproducible workflow. It uses policy scenarios as examples, but the main emphasis is on hands-on model development, VS Code, Git, MATLAB/Dynare troubleshooting, and practical AI-supported coding workflows.

Recommended use: select this track if survey responses show stronger demand for model calibration, code modification, debugging, AI-supported development, or team workflows.

## 2. Confirmed Planning Parameters

- Format: virtual-only.
- Timing: four afternoon sessions.
- Preferred week: July 20-24, 2026.
- Recommended core dates: Monday, July 20 to Thursday, July 23, 2026.
- Reserve date: Friday, July 24, 2026 for optional clinic, catch-up, or overflow.
- Suggested session time: 13:30-16:30 ICT / 08:30-11:30 CEST, with a short break.
- Context: ideally delivered before a possible NIEF consultation in the last week of July 2026, but primarily designed as technical capacity building.

## 3. Target Audience

- Model developers and technical analysts.
- Participants who will edit DGE-METRIC scenarios, calibration inputs, MATLAB scripts, Dynare files, or output routines.
- Participants expected to support other colleagues after the training.
- Participants comfortable with hands-on work in VS Code, MATLAB, Dynare, and possibly Git.

## 4. Learning Outcomes

By the end of Track B, participants should be able to:

1. Navigate the DGE-METRIC repository in VS Code and distinguish source files from generated files.
2. Trace how a model run moves from scripts and input files to Dynare execution and outputs.
3. Make controlled scenario, parameter, or code changes while preserving reproducibility.
4. Diagnose common MATLAB and Dynare errors using a structured debugging protocol.
5. Use Git or a lightweight diff-based workflow to review model changes.
6. Use AI assistants for code navigation, drafting, debugging, and documentation while validating all outputs manually.

## 5. Recommended Four-Session Schedule

| Session | Date | Main Focus | Group Output |
|---|---:|---|---|
| 1 | Monday, July 20, 2026 | VS Code setup, repository navigation, and execution path | Execution map |
| 2 | Tuesday, July 21, 2026 | Scenario and parameter changes | Controlled change note |
| 3 | Wednesday, July 22, 2026 | Calibration workflow, model edits, and diagnostics | Calibration or model-change note |
| 4 | Thursday, July 23, 2026 | Debugging, Git workflow, and guided technical lab | Debug note and validation evidence |

Detailed session folders:

- [Session 1: VS Code Setup And Execution Path](<Track B - Model Development/Session 1 - VS Code Setup And Execution Path/SESSION_PLAN.md>)
- [Session 2: Scenario And Parameter Changes](<Track B - Model Development/Session 2 - Scenario And Parameter Changes/SESSION_PLAN.md>)
- [Session 3: Calibration And Diagnostics](<Track B - Model Development/Session 3 - Calibration And Diagnostics/SESSION_PLAN.md>)
- [Session 4: Debugging And Technical Lab](<Track B - Model Development/Session 4 - Debugging And Technical Lab/SESSION_PLAN.md>)

## 6. Session Plan

### Session 1: VS Code Setup, Repository Navigation, And Execution Path

Purpose:

- Establish a shared technical workflow for online model development.
- Make VS Code the central working environment.
- Teach participants to find the right source files before changing anything.

Core blocks:

- Online setup check: MATLAB, Dynare, repository access, VS Code, terminal, paths.
- VS Code essentials: folder workspace, search, file symbols, integrated terminal, diff view.
- Repository orientation: scripts, model files, calibration inputs, scenario inputs, outputs, generated Dynare files.
- Run-path walkthrough: from main run script to model preprocessing, Dynare execution, and output files.
- AI-supported navigation: ask an AI assistant to trace a variable, parameter, or scenario switch, then verify the answer manually.

Hands-on exercise:

- Groups trace one execution path from a selected run command to output files.

Deliverable:

- Execution map identifying source files, generated files, inputs, and outputs.

### Session 2: Scenario And Parameter Changes

Purpose:

- Practice small, controlled changes that participants can understand, review, and validate.
- Build a habit of documenting assumptions before running the model.

Core blocks:

- Scenario configuration and naming conventions.
- Editing scenario assumptions and parameter inputs.
- Safe change workflow:
  - State expected effect.
  - Make the smallest meaningful edit.
  - Review the diff.
  - Run the model or a targeted check.
  - Compare outputs.
  - Document result and caveat.
- AI-supported drafting: generate candidate code or documentation, then manually inspect and simplify.
- Common mistakes: editing generated files, changing too many things at once, losing baseline comparability, undocumented assumptions.

Hands-on exercise:

- Each group makes one controlled scenario or parameter change in a training copy or prepared exercise file.

Deliverable:

- Controlled change note with assumption, edited file, expected effect, diff summary, and validation result.

### Session 3: Calibration Workflow, Model Edits, And Diagnostics

Purpose:

- Move from scenario-level changes to deeper model-development tasks.
- Clarify how calibration inputs, parameters, equations, and diagnostics connect.

Core blocks:

- Calibration workflow: data sources, input tables, parameters, targets, diagnostics.
- Locating where a parameter enters equations and outputs.
- Dynare file structure: declarations, model blocks, macro includes, steady state handling.
- Generating and adapting equations or code snippets with AI support.
- Diagnostics: residuals, steady-state issues, missing values, path and file problems.
- Documentation: recording what changed and why.

Hands-on exercise:

- Groups inspect or implement one calibration/model-development task, such as:
  - Locate and document one calibration parameter.
  - Change one parameter input and inspect downstream effects.
  - Add a small diagnostic output.
  - Trace one equation from source file to result.

Deliverable:

- Calibration or model-change note with file references, expected effect, and diagnostic check.

### Session 4: Debugging, Git Workflow, And Guided Technical Lab

Purpose:

- Practice a repeatable debugging method.
- Consolidate technical skills through guided participant use cases.

Core blocks:

- Debugging protocol:
  - Capture the exact error.
  - Identify whether it is MATLAB, Dynare, path, data, calibration, or logic related.
  - Trace the relevant source files.
  - Make a minimal fix.
  - Review the diff.
  - Re-run and validate.
  - Document the evidence.
- Git and collaboration basics: branch, diff, commit message, what to exclude from commits.
- AI-assisted debugging: asking targeted questions, rejecting overbroad fixes, verifying all changes.
- Guided open lab with typical technical use cases:
  - Fix a prepared run failure.
  - Diagnose a scenario not being picked up.
  - Identify an accidental generated-file edit.
  - Add a small output or chart hook.
  - Improve documentation for a model block.

Hands-on exercise:

- Groups debug one prepared issue or participant issue and validate the fix.

Deliverable:

- Debug note with issue, root cause, fix, diff summary, validation evidence, and remaining risk.

## 7. Materials To Prepare

- VS Code quick-start guide for DGE-METRIC.
- Repository map and source-vs-generated-files guide.
- AI-supported development prompt sheet.
- Responsible AI verification checklist.
- Git and diff mini-guide.
- Scenario-change template.
- Calibration and diagnostics checklist.
- Prepared failure cases for debugging.
- Shared notes document with one section per group.

## 8. Pre-Training Requirements

Participants should confirm before the first session:

- MATLAB works.
- Dynare is installed and visible from MATLAB.
- VS Code is installed.
- Repository access is available.
- Participants can open the repository folder in VS Code.
- Optional but recommended: Git installed and configured.
- Optional but useful: access to GitHub Copilot, Codex, Claude Code, or another AI coding assistant.

## 9. Role Of AI In This Track

AI assistants should be used mainly for:

- Repository navigation.
- Explaining unfamiliar MATLAB or Dynare code.
- Drafting small code or documentation changes.
- Suggesting likely causes of errors.
- Producing checklists for validation.
- Summarizing diffs and change notes.

Verification rule:

- AI output is never accepted directly. Participants must inspect source files, review diffs, run checks, and document validation evidence.

## 10. Completion Outputs

At the end of the track, each group should have:

- An execution map.
- A controlled scenario or parameter change note.
- A calibration or model-change note.
- A debug note with validation evidence.
- A lightweight workflow checklist for future model changes.

## 11. Open Decisions

- Which prepared technical exercises should be used after survey results are available?
- Should Friday, July 24, 2026 be reserved for installation catch-up or a technical clinic?
- Can a local or remote assistant support setup issues and breakout rooms?
- Which AI tools will participants actually have access to during the sessions?
- Should Git be required for all participants or treated as recommended background?
