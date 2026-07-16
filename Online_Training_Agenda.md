# Online Training: Modifying the DGE-METRIC Model with VS Code and Agentic AI

## Training Overview

**Format**  
Live online, interactive, hands-on

**Recommended Duration**  
4 sessions of 2.5–3 hours each  
*(Usually better online than two full-day blocks)*

**Audience**  
Researchers, analysts, model developers, and technical policy teams working with DGE-METRIC, MATLAB, Dynare, VS Code, GitHub, Codex, Claude Code, and GitHub Copilot.

---

## Session 1: Online Setup And Codebase Orientation

### Objectives
- Confirm everyone can access the repo and tools.
- Understand the DGE-METRIC folder structure.
- Learn how to navigate the model in VS Code.

### Agenda

**Welcome & Setup (30 min)**
- Training goals and online collaboration norms
- Required tools and accounts:
  - VS Code
  - MATLAB
  - Dynare
  - Git / GitHub
  - Codex
  - Claude Code
  - GitHub Copilot

**Codebase Orientation (45 min)**
- Opening the DGE-METRIC repository
- Key files and folders:
  - `RunSimulations.m`
  - `DGE_Model.mod`
  - `DGE_CRED_Model.mod`
  - `ModFiles/`
  - `Functions/`
  - `ExcelFiles/`
- Source files vs generated Dynare files
- Live demo: trace how `RunSimulations.m` calls Dynare

**Hands-On Exercise (30 min)**
- Participants map one scenario execution path
- Breakout rooms for small navigation tasks
- Shared notes document for findings

### Online Interaction
- Screen sharing by instructor
- Participants follow along locally
- Breakout rooms for small debugging/navigation tasks
- Shared notes document for findings

---

## Session 2: Working With VS Code, Git, And AI Assistants

### Objectives
- Use VS Code efficiently for model development.
- Understand how to use Codex, Claude Code, and Copilot safely.
- Learn AI prompting patterns for code exploration.

### Agenda

**VS Code & Git Essentials (45 min)**
- VS Code workspace setup
- Searching across `.m` and `.mod` files
- Comparing files and reviewing diffs
- Git basics for safe model changes:
  - `branch`
  - `commit`
  - `diff`
  - `restore` (carefully)
- GitHub workflow overview

**AI Assistants Landscape (45 min)**
- AI assistants compared:
  - GitHub Copilot for inline help
  - Codex for repository-wide tasks
  - Claude Code for large-context reasoning
- Prompting examples:
  - "Find where this parameter is defined"
  - "Explain this execution path"
  - "Locate where this scenario changes the model"
  - "Suggest minimal diagnostics for this error"
- Live demo: use AI to locate an unintended console output

**Hands-On Exercise (30 min)**
- Participants ask an AI assistant to trace a selected variable or scenario through the model
- Verify the result manually in VS Code

---

## Session 3: Modifying Scenarios, Parameters, And `.mod` Files

### Objectives
- Make controlled changes to model scenarios and options.
- Understand Dynare macro syntax.
- Avoid common `.mod` editing mistakes.

### Agenda

**Model Modification Workflow (45 min)**
- Scenario configuration in `RunSimulations.m`
- How `change_mod_file.m` updates `DGE_Model.mod`
- Simulation horizon and scenario switches
- Parameter loading and calibration flow

**Dynare Macro Processor (30 min)**
- `@# define`
- `@# if`
- `@# include`
- Included model files in `ModFiles/`

**Common Issues & Best Practices (20 min)**
- Missing semicolons
- Accidental displayed values
- Editing generated files
- Mismatched macro conditions
- Live demo: make a small source-level model change
- Review the Git diff before running

**Hands-On Exercise (25 min)**
Participants make a small controlled change, such as:
- Add a scenario label
- Change a simulation horizon
- Modify a macro switch
- Add a diagnostic message

Then review the diff and explain the expected effect.

---

## Session 4: Debugging, Validation, And Team Workflow

### Objectives
- Diagnose common run failures.
- Use AI to support debugging without blindly trusting it.
- Establish a reproducible team workflow.

### Agenda

**Error Diagnosis & Troubleshooting (45 min)**
- Reading MATLAB and Dynare errors
- Understanding generated `driver.m` files
- Using `diagnostics_crash.m`
- Checking steady-state and residual issues
- Adding temporary diagnostics safely

**AI-Assisted Debugging Workflow (30 min)**
1. Capture the error
2. Ask AI to trace likely sources
3. Verify in source files
4. Make a minimal change
5. Review diff
6. Run validation
7. Document results

**Team Collaboration & Reproducibility (20 min)**
- Pull request checklist for model changes
- What to commit and what not to commit
- Reproducibility practices for online teams

**Final Q&A (15 min)**

**Hands-On Exercise (25 min)**
Participants debug or explain a prepared issue, for example:
- Unintended output in the console
- Missing file path
- Scenario not being picked up
- Failed parameter lookup
- Generated file edited by mistake

---

## Optional: Online Capstone Session

### Duration
2.5–3 hours

### Format
Guided workshop with breakout rooms

### Task
Each participant or group implements one small DGE-METRIC modification.

### Deliverables
- Git branch or patch
- Short change note
- Validation notes
- AI prompts used
- Risks or assumptions

### Example Capstone Topics
- Add a new policy scenario
- Add diagnostic output for failed runs
- Document the simulation pipeline
- Clean up accidental console output
- Compare two scenario configurations
- Refactor one helper function with tests or validation notes

---

## Recommended Online Structure

For best learning quality:

- **Spacing:** 4 sessions over 1–2 weeks
- **Duration:** 2.5–3 hours per session
- **Breaks:** 10-minute break halfway through each session
- **Collaboration:** Shared online notes, small-group breakout exercises
- **Support:** Instructor office hour after Session 4
- **Repositories:** Participants use their own copy or branch of the repository

---

## Pre-Training Checklist

Ensure all participants have:

- [ ] VS Code installed and updated
- [ ] MATLAB installed and licensed
- [ ] Dynare installed and configured
- [ ] Git installed and GitHub account set up
- [ ] Access to the DGE-METRIC repository
- [ ] Codex, Claude Code, or GitHub Copilot account set up
- [ ] Network bandwidth for screen sharing
- [ ] Audio/video equipment tested

