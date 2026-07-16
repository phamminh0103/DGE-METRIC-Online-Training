# DGE-METRIC Advanced Training Plan - July 2026

## 1. Planning Status

This plan incorporates the latest organizing discussion from June 30, 2026.

- Survey launch: July 1, 2026.
- Delivery format: virtual-only, not hybrid.
- Preferred delivery window: week of July 20, 2026, before a potential NIEF consultation in the last week of July.
- Session structure: four afternoon sessions.
- Final dates and topic depth: to be confirmed after survey responses.

## 2. Working Assumptions

- The training is designed for participants who already attended the introductory DGE-METRIC/Dynare training or have comparable prior exposure.
- The sessions are live, interactive, and hands-on.
- "Afternoon sessions" are understood as Vietnam afternoon sessions, for example 13:30-16:30 ICT / 08:30-11:30 CEST, including a short break.
- The week of July 20-24, 2026 is preferred. A compact Monday-Thursday sequence is recommended, with Friday kept as a buffer, catch-up slot, or optional clinic.
- The week of July 27-31, 2026 remains a fallback only if survey responses make the preferred week impractical; it may conflict with or follow the possible NIEF consultation.

## 3. Recommended Dates

Recommended core schedule:

| Session | Date | Format | Focus |
|---|---:|---|---|
| 1 | Monday, July 20, 2026 | Virtual afternoon | Setup, VS Code, model navigation, AI-supported workflow |
| 2 | Tuesday, July 21, 2026 | Virtual afternoon | Scenario design and application of results |
| 3 | Wednesday, July 22, 2026 | Virtual afternoon | Calibration, model modification, and debugging |
| 4 | Thursday, July 23, 2026 | Virtual afternoon | Guided open lab, team workflow, and policy-use case consolidation |

Optional reserve:

- Friday, July 24, 2026: setup catch-up, additional open clinic, or overflow if one of the core dates is not feasible.

## 4. Training Objective

The advanced training should help participants move from using DGE-METRIC outputs to modifying, validating, and communicating their own DGE-METRIC applications in a reproducible workflow.

The central design principle is to make AI-supported model development practical rather than abstract. AI tools should be used for code navigation, drafting model or scenario changes, debugging, documentation, and repetitive workflow support, while participants learn to verify every AI suggestion through source inspection, model runs, and result checks.

## 5. Topic Emphasis

The survey should determine how deeply the training emphasizes each of the following two tracks.

### Track A: Content And Policy Applications

- Scenario design for Vietnamese energy transition questions.
- Application and interpretation of results.
- Communicating GDP, investment, emissions, energy prices, financing, and distributional trade-offs.
- Preparing model evidence for consultations, including potential NIEF discussions.

### Track B: Model Calibration And Development

- Hands-on model modification.
- Calibration workflow and data updates.
- Debugging MATLAB/Dynare issues.
- Extending scenarios, equations, parameters, and outputs.
- Working efficiently with VS Code, Git, and AI assistants.

Recommended default: use Track B as the technical spine of the course, while using Track A examples as the applied use cases. This keeps the course practical and aligns with the proposed AI-supported model development focus without losing the policy relevance requested by GIZ colleagues.

The content examples should be treated as provisional options rather than fixed commitments, since they were proposed during the current planning discussion and not derived directly from the previous post-training survey. The new survey should therefore be used to decide whether to keep, revise, or reprioritize them.

Two track-specific plans are available as standalone options:

- [Track A: Content And Policy Applications](DGE_METRIC_Advanced_Training_Track_A_Policy_Applications_July2026.md)
- [Track B: Model Calibration And Development](DGE_METRIC_Advanced_Training_Track_B_Model_Development_July2026.md)

## 6. Four-Session Agenda

### Session 1: Setup, VS Code, And AI-Supported Model Navigation

Purpose:

- Establish a common virtual workflow.
- Make VS Code the central working environment.
- Show how AI assistants can support model exploration without replacing verification.

Core blocks:

- Online norms, support channels, and troubleshooting queue.
- Repository orientation: source files, generated files, scripts, scenario inputs, outputs.
- VS Code workflow: search, file navigation, terminals, diff view, extensions.
- AI-supported exploration: tracing variables, locating parameters, explaining execution paths.
- Light Git workflow: branch, diff, commit, and what not to commit.

Hands-on output:

- Each group prepares a one-page execution map for one model run or scenario pipeline.

### Session 2: Scenario Design And Application Of Results

Purpose:

- Connect model use to policy questions and scenario design.
- Let participants practice defining assumptions, expected channels, and outputs.

Core blocks:

- Baseline vs alternative scenario logic.
- Scenario assumptions and naming conventions.
- Examples: PDP8, net-zero, rooftop solar, energy efficiency, financing, or participant-proposed topics.
- Reading model results: GDP, investment, emissions, energy prices, government, trade balance.
- AI-supported drafting of scenario documentation and result narratives.

Hands-on output:

- Each group creates a scenario sheet with assumptions, expected channels, key indicators, and expected policy relevance.

### Session 3: Calibration, Model Modification, And Debugging

Purpose:

- Move from interpreting scenarios to changing and validating the model workflow.
- Address the strongest need for direct technical support.

Core blocks:

- Calibration workflow: data inputs, parameters, targets, diagnostics.
- Controlled code changes in MATLAB and Dynare files.
- Generating and adapting equations or code snippets with AI support.
- Common errors: missing semicolons, macro conditions, generated-file edits, path issues, steady-state/residual failures.
- Debugging protocol: capture error, trace source, make minimal change, inspect diff, rerun, document validation.

Hands-on output:

- Each group implements or diagnoses one controlled change and produces a debug note: issue, root cause, fix, validation evidence.

### Session 4: Guided Open Lab, Collaboration, And Consultation Preparation

Purpose:

- Give participants structured support on their own applications.
- Consolidate model-development skills into useful policy outputs.

Core blocks:

- Strongly guided open lab with typical use cases:
  - Modify one scenario assumption.
  - Update one calibration or parameter input.
  - Add or adjust one output chart/table.
  - Diagnose one model run failure.
  - Draft one policy interpretation slide.
- Team workflow: Git review, shared notes, result documentation, reproducibility checklist.
- Optional consultation focus: prepare questions, scenario evidence, or model outputs relevant for NIEF.
- Wrap-up: next-step commitments and post-training support needs.

Hands-on output:

- Each group presents one small model-use case with a short change note, output evidence, and remaining questions.

## 7. Survey Integration

The survey can keep the organizing team's proposed structure:

1. Full name.
2. Organization / institution.
3. Interest in participating in an advanced training course on DGE-METRIC and Dynare, tentatively scheduled for July 2026:
   - Yes
   - No
   - Possibly, depending on schedule and course content
4. Preferred dates during the week of July 20, 2026, with multiple selections allowed:
   - Monday, July 20, 2026
   - Tuesday, July 21, 2026
   - Wednesday, July 22, 2026
   - Thursday, July 23, 2026
   - Friday, July 24, 2026
5. Topics participants would like to explore in greater depth, with multiple selections allowed.
6. Additional comments, suggestions, or questions for the organizing team.

Recommended wording for the topic question:

> Which topics would you like to explore in greater depth during the advanced training course? Please select all that apply.

Suggested answer options:

- AI-supported model development in VS Code.
- Navigating and understanding the DGE-METRIC codebase.
- Designing policy scenarios and modifying scenario assumptions.
- Applying results to policy questions, including scenario interpretation and communication.
- Calibration workflow, data updates, and parameter changes.
- Model modification, including equations, Dynare files, and MATLAB scripts.
- Debugging common MATLAB/Dynare errors.
- Using Git or version control for team collaboration.
- Guided open lab on participants' own use cases.
- Other topic proposal.

Optional follow-up if the survey tool allows it:

> If you selected several topics, please name your top two priorities.

## 8. Roles And Responsibilities

### Christoph Schult / IWH

- Lead trainer.
- Prepare and deliver the four virtual sessions.
- Provide examples for VS Code, AI-supported development, model modification, calibration, and debugging.
- Adapt final depth based on survey responses.

### GIZ Organizing Team

- Send survey on July 1, 2026.
- Confirm final dates and participant list.
- Provide virtual platform, invitations, shared notes space, and participant communication.
- Share survey results with the trainer early enough to finalize the agenda.

### GIZ Viet Nam / Local Coordination

- Confirm whether NIEF has been contacted and whether a consultation is planned for the week of July 27, 2026.
- Clarify whether outputs from the advanced training should feed directly into NIEF preparation.
- Identify a local or remote training assistant/focal point if possible, for example Ms. Van, especially for setup support, breakout-room support, and participant troubleshooting.

## 9. Preparation Timeline

| Date | Task |
|---:|---|
| July 1, 2026 | Send participant survey. |
| July 6-7, 2026 | Review survey responses and decide final dates. |
| July 8-10, 2026 | Finalize topic emphasis and session agenda. |
| July 13-15, 2026 | Confirm participant technical setup and circulate pre-training checklist. |
| July 16-17, 2026 | Prepare final exercises, templates, and example files. |
| July 20-23, 2026 | Deliver four virtual afternoon sessions. |
| July 24, 2026 | Optional clinic, buffer, or follow-up support. |
| Week of July 27, 2026 | Potential NIEF consultation and/or post-training application support. |

## 10. Materials To Prepare

- VS Code quick-start guide for DGE-METRIC.
- AI-supported development prompt sheet.
- Responsible AI verification checklist.
- Scenario design template.
- Calibration and debugging checklist.
- Git/diff mini-guide for model changes.
- Open-lab use-case template.
- Shared notes document with one section per session and per group.

## 11. Completion Outputs

By the end of the training, each group should have:

- An execution map for one DGE-METRIC workflow.
- A scenario sheet with assumptions, channels, and expected indicators.
- A debug or model-change note with validation evidence.
- One policy-ready chart, table, or short narrative based on a scenario or participant use case.
- A short list of follow-up questions for independent work or potential consultation preparation.

## 12. Open Decisions

- Confirm final delivery dates after survey responses.
- Confirm whether the training should prioritize content/policy applications, model calibration/development, or a balanced approach.
- Confirm NIEF outreach status and timing.
- Decide whether Ms. Van or another colleague can support the virtual sessions as local/technical assistant.
- Decide whether Friday, July 24, 2026 should be reserved as a clinic or left free.
