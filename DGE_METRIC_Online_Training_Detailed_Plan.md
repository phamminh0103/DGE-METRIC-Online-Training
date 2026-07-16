# DGE-METRIC Online Training Detailed Plan

## 1) Training Purpose

Build practical capacity to run, modify, validate, and communicate DGE-METRIC scenarios for policy analysis in a reproducible workflow.

## 2) Target Audience

- Government analysts and technical staff
- Research teams and model developers
- Policy advisors using macro-energy scenario evidence

## 3) Delivery Format

- Live online, instructor-led, interactive sessions
- Recommended: 5 sessions, 2.5 to 3 hours each
- Alternative compact format: 4 sessions with optional capstone office hour

## 4) Learning Outcomes

By the end of the program, participants can:

1. Navigate the DGE-METRIC repository and identify source vs generated files.
2. Run baseline calibration and scenario simulations in a reproducible way.
3. Implement controlled scenario and parameter changes safely.
4. Diagnose common MATLAB and Dynare failures using structured debugging.
5. Compare baseline vs policy scenarios and communicate policy trade-offs clearly.
6. Use AI coding assistants responsibly for code navigation, drafting, and troubleshooting.

## 5) Prerequisites

- Working MATLAB installation
- Working Dynare installation (recommended 6.x or newer used by your team)
- VS Code and Git installed
- Access to DGE-METRIC repository
- Basic familiarity with macro modeling concepts

## 6) Pre-Training Setup Checklist

- [ ] Repository access confirmed
- [ ] MATLAB, Dynare, and VS Code tested with a dry run
- [ ] Git identity configured
- [ ] Shared collaboration channel created (chat + notes)
- [ ] Sample scenario files distributed
- [ ] Participants assigned to small groups (3-4 people)
- [ ] Troubleshooting guide prepared

## 7) Session Plan (Recommended 5 Sessions)

## Session 1: Setup and Model Orientation (2.5-3h)

### Objectives

- Confirm technical setup for all participants
- Understand codebase structure and workflow entry points
- Trace one full baseline run path

### Agenda

- 00:00-00:20 Welcome, goals, online norms
- 00:20-00:50 Tool and environment check
- 00:50-01:30 Repository orientation and key files
- 01:30-01:40 Break
- 01:40-02:20 Execution-path walkthrough (from run script to outputs)
- 02:20-02:50 Group exercise: map one scenario pipeline
- 02:50-03:00 Debrief and takeaways

### Hands-on task

- Each group documents one run path from script to output folder.

### Deliverable

- One-page execution map per group.

---

## Session 2: Advanced Scenario Design (2.5-3h)

### Objectives

- Design robust baseline vs policy alternatives
- Edit scenario assumptions while preserving comparability
- Use consistent naming and metadata

### Agenda

- 00:00-00:25 Recap and design principles
- 00:25-01:10 Scenario inputs and configuration files
- 01:10-01:35 Common pitfalls in scenario setup
- 01:35-01:45 Break
- 01:45-02:30 Hands-on: create one custom scenario
- 02:30-03:00 Group check and peer review

### Hands-on task

- Implement one scenario variant and document expected channels.

### Deliverable

- Scenario sheet with assumptions, channels, and expected outcomes.

---

## Session 3: Model Extensions and Sensitivity Analysis (2.5-3h)

### Objectives

- Understand where and how to extend model structure
- Run sensitivity tests and interpret robustness
- Automate repeated runs where feasible

### Agenda

- 00:00-00:30 Extension points in model and scripts
- 00:30-01:10 Parameter sweeps and uncertainty framing
- 01:10-01:30 Batch runs and output collection
- 01:30-01:40 Break
- 01:40-02:30 Hands-on: mini sensitivity lab
- 02:30-03:00 Interpretation clinic

### Hands-on task

- Vary one key parameter and compare results across at least three values.

### Deliverable

- Sensitivity table with one interpretation paragraph.

---

## Session 4: Output Analysis and Policy Communication (2.5-3h)

### Objectives

- Build clear baseline vs alternative comparisons
- Create policy-ready charts and narratives
- Communicate caveats without weakening insight

### Agenda

- 00:00-00:30 Indicator selection and comparison logic
- 00:30-01:10 Visualization standards for policy slides
- 01:10-01:30 Narrative framework: result, mechanism, implication, caveat
- 01:30-01:40 Break
- 01:40-02:30 Hands-on: chart + 4-sentence narrative
- 02:30-03:00 Group presentations and feedback

### Hands-on task

- Produce one chart comparing baseline vs one policy scenario.

### Deliverable

- One chart and a short policy narrative.

---

## Session 5: Open Lab, Debugging, and Team Workflow (2.5-3h)

### Objectives

- Resolve participant-specific blockers
- Practice a reliable debugging workflow
- Standardize team reproducibility and review practices

### Agenda

- 00:00-00:30 Structured debugging workflow
- 00:30-01:10 AI-assisted debugging with verification steps
- 01:10-01:30 Git workflow for safe collaboration
- 01:30-01:40 Break
- 01:40-02:40 Open lab by group use case
- 02:40-03:00 Wrap-up, feedback, next-step commitments

### Hands-on task

- Diagnose one prepared failure case or participant case.

### Deliverable

- Debug note: issue, root cause, fix, and validation evidence.

## 8) Responsible AI Use Protocol

Use AI assistants to accelerate work, not replace validation.

1. Ask for code navigation, explanation, or draft changes.
2. Verify every suggested change in source files.
3. Review diffs before execution.
4. Run model checks after each meaningful change.
5. Record prompts used for transparency and reproducibility.

## 9) Evaluation and Completion Criteria

Participants successfully complete the training when they:

- Run one baseline and one alternative scenario end-to-end.
- Submit one scenario design sheet.
- Submit one comparison chart with narrative.
- Submit one debugging note with validation evidence.
- Explain one key trade-off in policy terms.

## 10) Recommended Artifacts per Group

- Execution map (Session 1)
- Scenario sheet (Session 2)
- Sensitivity table (Session 3)
- Chart + narrative (Session 4)
- Debug note (Session 5)

## 11) Facilitation and Logistics Notes

- Keep breakout groups stable across sessions.
- Use one shared notes document with fixed sections per session.
- Reserve 10 minutes each session for troubleshooting queue.
- Track unresolved issues in a visible backlog.
- Offer one optional post-training office hour.

## 12) Optional Compact 4-Session Variant

If schedule is constrained:

- Session A: Setup + orientation
- Session B: Scenario design + run
- Session C: Sensitivity + debugging
- Session D: Analysis + presentations

Then add a 90-minute optional capstone clinic.

## 13) Next-Step Recommendations

After training, teams should:

1. Define a standard scenario template for internal use.
2. Maintain a shared diagnostics checklist for all runs.
3. Establish a lightweight change-review workflow using Git.
4. Build a small library of policy-ready chart templates.
