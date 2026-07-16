# CLAUDE.md

## Project purpose

This repository develops a three-day online training that continues the previous on-site DGE-METRIC training. The online course must start with Training Day 3, not Day 1. Use the following naming throughout:

- Training Day 3 = Online Day 1
- Training Day 4 = Online Day 2
- Training Day 5 = Online Day 3

The training topic is the use of the Dynamic General Equilibrium model, specifically DGE-METRIC, for scenario analysis, calibration, energy transition analysis, finance scenarios, and determination of optimal reserve requirements.

## Primary training goal

Enable participants to use the DGE-METRIC model independently for calibrated baseline analysis, policy scenario design, scenario comparison, interpretation of model outputs, and communication of policy trade-offs.

## Audience assumptions

Participants have already attended the previous on-site training. Do not repeat introductory macroeconomic or DGE model theory unless needed for a short recap. Focus on applied model use, hands-on workflows, interpretation, reproducibility, and policy communication.

## Course structure

The online training has three afternoon sessions and two morning sessions.

Important sequencing rule:

- Each afternoon session should prepare participants for the following morning session.
- The final afternoon session must be a wrap-up, not a new full technical module.
- Do not create a morning session for Online Day 1 unless explicitly requested.

### Required session map

| Training day | Online day | Session | Main focus | Purpose |
|---|---:|---|---|---|
| Training Day 3 | Online Day 1 | Afternoon | Calibration and finance scenarios | Reconnect to the previous on-site training, review repository structure, prepare calibration and finance-scenario inputs for the next morning. |
| Training Day 4 | Online Day 2 | Morning | Calibration and finance scenario hands-on | Run baseline calibration, inspect diagnostics, run baseline vs. finance alternatives, and interpret GDP, investment, fiscal, and policy effects. |
| Training Day 4 | Online Day 2 | Afternoon | Energy transition pathways | Design different energy transition pathways and prepare assumptions, files, and expected mechanisms for the next morning. |
| Training Day 5 | Online Day 3 | Morning | Optimal reserve requirements | Use model outputs from scenarios/pathways to determine and interpret optimal reserve requirements. |
| Training Day 5 | Online Day 3 | Afternoon | Wrap-up | Consolidate calibration, scenario design, energy pathways, reserve-requirement analysis, reproducibility, and independent-use checklist. |

## Required learning outcomes

By the end of the online training, participants should be able to:

1. Navigate the DGE-METRIC repository and identify the role of major folders and files.
2. Explain the calibration workflow from source data to DGE-ready inputs.
3. Run a baseline calibration and interpret diagnostics.
4. Design finance scenarios using transparent assumptions and metadata.
5. Design and compare alternative energy transition pathways.
6. Use scenario outputs to support determination of optimal reserve requirements.
7. Compare baseline and alternative outputs using GDP, investment, emissions, fiscal indicators, policy indicators, and reserve-related indicators.
8. Produce reproducible charts and short policy narratives with caveats.
9. Document assumptions, file edits, model runs, diagnostics, and interpretation clearly enough for another analyst to reproduce.

## Repository layout to create or maintain

Use this structure for the online training repository unless an existing structure already exists. If the repository already contains a DGE-METRIC model layout, preserve it and add training material around it rather than reorganizing the model code.

```text
/
  README.md
  CLAUDE.md
  LICENSE

  source/
    previous-onsite-training/
    dge-metric-reference/
    sme-notes/
    data-dictionaries/

  design/
    course-brief.md
    curriculum-map.md
    agenda.md
    assessment-plan.md
    style-guide.md
    decision-log.md

  content/
    training-day-03/
      afternoon-calibration-finance/
        README.md
        lesson.md
        facilitator-guide.md
        exercise.md
        scenario-template.md
        expected-outputs.md
    training-day-04/
      morning-calibration-finance-hands-on/
        README.md
        lesson.md
        facilitator-guide.md
        exercise.md
        expected-outputs.md
      afternoon-energy-transition-pathways/
        README.md
        lesson.md
        facilitator-guide.md
        exercise.md
        pathway-template.md
        expected-outputs.md
    training-day-05/
      morning-optimal-reserve-requirements/
        README.md
        lesson.md
        facilitator-guide.md
        exercise.md
        expected-outputs.md
      afternoon-wrap-up/
        README.md
        synthesis.md
        independent-use-checklist.md
        exit-ticket.md
        final-qa.md

  scenarios/
    finance/
      README.md
      scenario-log.md
      assumptions-template.md
    energy-transition/
      README.md
      pathway-log.md
      assumptions-template.md
    reserve-requirements/
      README.md
      reserve-analysis-template.md

  activities/
    calibration-diagnostics/
    scenario-comparison/
    chart-and-narrative/
    reserve-requirements/

  assets/
    figures/
    slides/
    screenshots/

  qa/
    sme-questions.md
    review-checklist.md
    accessibility-checklist.md
    pilot-feedback.md
    final-review.md

  scripts/
    course-checks/
    export/
```

If the repository includes the DGE-METRIC model itself, expect and respect the following model-side folders:

```text
  docs/
  ExcelFiles/
  Functions/
  ModFiles/
  scripts/
  Training/
```

Model-side roles:

- `docs/`: documentation, model notes, and figures.
- `ExcelFiles/`: Excel-based baseline, calibration, scenario, and output workbooks.
- `Functions/`: MATLAB helper functions for steady state, initialization, diagnostics, and simulation utilities.
- `ModFiles/`: Dynare model blocks, equations, and display-oriented equation files.
- `scripts/`: maintenance and workflow scripts used to run or support the model.
- `Training/`: training resources and slide-support materials.

## Source-grounding rules

Never invent model details, parameter values, country assumptions, file names, or scenario results.

Use this source priority:

1. Existing repository files.
2. Source documents in `source/`.
3. Approved design files in `design/`.
4. SME notes or user-provided instructions.
5. External references only when explicitly requested and cited.

When a fact, parameter, equation, data source, or model command is missing, write:

```text
[SME REVIEW NEEDED: describe the missing item]
```

When a file path or command is uncertain, inspect the repository before proposing changes.

## Training design rules

For every session, create materials with the following structure:

1. Session purpose.
2. Prerequisites from the previous on-site training.
3. Learning objectives.
4. Short recap or bridge from the previous session.
5. Conceptual explanation.
6. Hands-on task.
7. Expected output.
8. Debrief questions.
9. Common errors and troubleshooting.
10. Documentation or reporting task.
11. Preparation for the next session, except the final wrap-up.

For the final afternoon wrap-up, use this structure instead:

1. Synthesis of calibration, scenarios, energy pathways, and reserve requirements.
2. Independent-use checklist.
3. Reproducibility checklist.
4. Policy-communication checklist.
5. Group reflection.
6. Exit ticket.
7. Remaining SME or institutional questions.
8. Next steps for participants.

## Calibration rules

Calibration material must emphasize accounting coherence and reproducibility.

Include the following topics when relevant:

- IO calibration workflow.
- Source data to DGE-ready input format.
- Sector mapping and aggregation.
- Fossil and renewable utility split.
- Import decomposition into intermediate and final-use components.
- Baseline calibration run.
- Convergence and residual diagnostics.
- Comparison of model moments to target moments.
- Calibration diagnostic note.

When creating calibration exercises, require participants to record:

- Input file edited or inspected.
- Assumption changed or confirmed.
- Command or script used.
- Diagnostic checked.
- Interpretation of the diagnostic.
- Whether the run is acceptable for scenario analysis.

Calibration validation checks should include, where applicable:

- Output conservation.
- Import conservation.
- Value-added consistency.
- Sectoral labor compensation plausibility.
- Non-negativity of final matrices.

## Scenario design rules

Scenarios must be designed from the calibrated benchmark. Do not modify unrelated baseline parameters to force a desired result.

Every scenario must include a metadata block with:

- Scenario label.
- Policy mechanism.
- Exact file edits.
- Exact variables changed.
- Time path.
- Start year and end year.
- Transition profile.
- Expected effects.
- Key output indicators.
- Caveats.
- Person or group responsible.
- Date created or revised.

Scenario labels should be stable, descriptive, and machine-readable. Use lowercase kebab-case, for example:

```text
finance-green-credit-high-2030
energy-netzero-accelerated-2040
reserve-requirement-optimal-baseline
```

## Finance scenario rules

Finance scenarios for Online Day 1 and Online Day 2 morning should focus on how financing assumptions affect model outcomes.

Possible finance scenario themes include:

- Financing of transition investment.
- Green credit or concessional finance.
- Public vs. private financing shares.
- Fiscal burden of subsidies or guarantees.
- Investment crowding-in or crowding-out.
- External financing and macroeconomic trade-offs.

Do not create numerical finance assumptions unless they are present in the repository or approved by the user/SME. Mark missing assumptions for SME review.

Finance scenario outputs should compare, where available:

- GDP path.
- Investment path.
- Sectoral output.
- Fiscal indicators.
- Debt or financing burden indicators.
- Welfare or household impact indicators.
- Emissions if finance affects transition investment.

## Energy transition pathway rules

Energy transition pathway material for Online Day 2 afternoon should focus on scenario design and preparation for the following morning.

Pathways may include, subject to source support:

- Baseline or current-policy pathway.
- Gradual transition pathway.
- Accelerated renewable pathway.
- Fossil phase-down pathway.
- Carbon-pricing pathway.
- Subsidy or investment-support pathway.
- Efficiency-improvement pathway.

Each pathway must document:

- Policy mechanism.
- Energy-sector assumptions.
- Affected sectors.
- Time path.
- Expected mechanisms.
- Expected output indicators.
- Caveats and data limitations.

Energy transition outputs should compare, where available:

- GDP.
- Investment.
- Emissions.
- Energy-sector output.
- Fiscal or policy indicators.
- Distributional or sectoral transition burden.

## Optimal reserve requirement rules

Training Day 5 morning must teach participants how to use model outputs to inform determination of optimal reserve requirements.

Reserve-requirement content should connect model scenarios to reserve adequacy and policy design. It should be framed as applied analysis, not as a black-box number.

When creating this module, include:

- Definition of the reserve-requirement policy question.
- Inputs needed from baseline and alternative scenarios.
- Link between macro-financial conditions and reserve needs.
- How finance scenarios and energy transition pathways affect reserve requirements.
- Comparison of reserve-related indicators across scenarios.
- Sensitivity analysis.
- Interpretation of trade-offs.
- Policy narrative with caveats.

Do not invent the reserve-requirement formula or optimality criterion. If the formula, variables, or institutional rule are missing, write:

```text
[SME REVIEW NEEDED: confirm reserve-requirement formula, target indicator, and optimality criterion]
```

Reserve-requirement outputs may include, depending on model support:

- Optimal reserve requirement estimate.
- Reserve adequacy gap.
- Scenario-specific reserve demand.
- Fiscal or macroeconomic cost of higher reserves.
- Investment and GDP trade-offs.
- Sensitivity to financing and energy pathway assumptions.

## Chart and policy narrative rules

Every major hands-on session should produce one chart and one short policy narrative.

The chart must include:

- Clear title.
- Baseline and scenario labels.
- Units.
- Time period.
- Data source or output file.
- Short note on assumptions.

The policy narrative must include:

1. Main quantitative result.
2. Economic mechanism.
3. Policy implication.
4. One caveat.
5. Next analytical step.

## Assessment and participant outputs

Use practical assessment rather than theoretical exams.

Required participant outputs:

- Calibration diagnostic note.
- Finance scenario sheet.
- Energy pathway sheet.
- Baseline vs. alternative scenario comparison chart.
- Reserve-requirement analysis note.
- Final independent-use checklist.
- Exit ticket.

The final exit ticket should ask participants to write:

1. One calibration insight they will use.
2. One scenario-design practice they will keep.
3. One reserve-requirement or policy-analysis habit they will apply.
4. One remaining question for future support.

## Accessibility and online-learning rules

Design for self-paced review and live online delivery.

- Use clear headings and short sections.
- Avoid long dense paragraphs.
- Provide step-by-step instructions for hands-on tasks.
- Add alt text for all figures and screenshots.
- Provide transcripts or speaker notes for recorded explanations.
- Make activities possible with low bandwidth when feasible.
- Provide expected outputs so participants can self-check.
- Include troubleshooting tips for each model run.
- Avoid unnecessary animation or visual complexity.

## Git and reproducibility rules

Keep training content reproducible.

- Use Git branches for large changes.
- Commit after each completed session or module.
- Keep source files separate from generated outputs.
- Do not overwrite model outputs without archiving or documenting the run.
- Store scenario assumptions in scenario logs.
- Store SME decisions in `design/decision-log.md`.
- Store open questions in `qa/sme-questions.md`.
- Use relative links in Markdown.

## Commands and verification

Before editing, inspect the repository:

```bash
git status
find . -maxdepth 3 -type f | sort | head -200
```

Before committing training content, run available checks. If commands do not exist, propose them instead of assuming they exist.

Suggested checks:

```bash
# Markdown and link checks, if available
markdownlint .

# Course/site build, if the repository uses a static site generator
npm run build

# Custom course checks, if implemented
python scripts/course-checks/check_structure.py
python scripts/course-checks/check_links.py
python scripts/course-checks/check_scenario_metadata.py
```

Do not run long MATLAB, Dynare, or model-calibration jobs without explicit approval. Ask before running anything that may take significant time, overwrite outputs, or require licensed software.

## Claude working style

When asked to create or revise training content:

1. Inspect relevant files first.
2. Summarize the current state.
3. Identify missing information.
4. Propose a short plan.
5. Create or edit files only after the plan is clear.
6. Keep content source-grounded.
7. Mark uncertain items as SME review needed.
8. End with changed files, open questions, and recommended next action.

When asked to create a new session, use this output pattern:

```text
Session: [Training Day X / Online Day Y / Morning or Afternoon]
Focus: [topic]
Participant output: [deliverable]
Files to create or edit:
- ...
Open SME questions:
- ...
```

## Prohibited behavior

Do not:

- Renumber the online course as Day 1 if it should continue as Training Day 3.
- Create unsupported parameter values.
- Invent model commands, formulas, or outputs.
- Mix baseline calibration changes with policy scenario changes.
- Treat the wrap-up afternoon as a new technical module.
- Delete or reorganize the DGE-METRIC model folders without permission.
- Hide caveats in policy narratives.
- Present a scenario as policy advice without documenting assumptions.

## First tasks for Claude Code

When this repository is first opened, do the following:

1. Inspect repository structure.
2. Create or update `design/course-brief.md`.
3. Create or update `design/curriculum-map.md`.
4. Create or update `design/agenda.md` using the required three-afternoon/two-morning structure.
5. Create or update `qa/sme-questions.md` with missing assumptions, especially for finance scenarios and optimal reserve requirements.
6. Create skeleton folders for Training Day 3, Training Day 4, and Training Day 5.
7. Do not draft full lesson content until the agenda and curriculum map are approved.
