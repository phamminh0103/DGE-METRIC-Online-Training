**DGE-METRIC Online Training — Detailed Agenda**

Finance & Energy-Efficiency Scenarios, Reserve Requirements, and Calibration & Sensitivity Analysis

**GIZ Vietnam | DGE-METRIC Program | Online Module | 22–24 July 2026**

Continuing your DGE-METRIC training online — this course picks up directly from the on-site training (Training Days 1–2, and Day 3 if already completed) and moves into applied, hands-on model use. This document expands the course schedule into a block-by-block agenda for each of the five sessions.

**2026-07-13 revision:** each afternoon now goes deep on one topic rather than surveying several. Day 1 PM defines finance and energy-efficiency scenarios in full detail; Day 2 PM covers the reserve-requirement method and how it would be implemented; Day 3 PM covers calibration internals, how to modify them, and sensitivity analysis. To make room for that depth, the Distributed Energy Resources and LNG-to-Hydrogen pathways are out of scope for this iteration (energy-efficiency remains the one fully-worked pathway example); codebase navigation and Git/GitHub Desktop moved from Day 1 PM to Day 2 AM, right before they're needed hands-on; and the closing wrap-up is now a short block at the end of Day 3 PM rather than its own session.

**2026-07-14 revision:** Day 1 now opens with a setup check-in (VS Code, GitHub, an AI coding assistant), and installing these three tools moves from "introduced from scratch on Day 2 AM" to a **prerequisite confirmed before Day 1**. Day 2 AM still teaches full Git/GitHub Desktop and VS Code workflows from scratch — this check-in only confirms the tools are present and open, not that participants already know how to use them. See `../design/decision-log.md` (2026-07-14 entry) for rationale.

# Who this is for

Participants who have already attended the on-site DGE-METRIC training. This course does not repeat introductory macroeconomic or DGE modeling theory — it focuses on using the model independently: calibration, scenario design, interpretation, and policy communication.

# What you will be able to do afterward

- Navigate the DGE-METRIC repository — including tracing an equation to the code that computes it.
- Run a baseline calibration, read its diagnostics with confidence, and debug common MATLAB/Dynare errors systematically.
- Design and fully document a finance scenario and an energy-efficiency scenario, with transparent, source-grounded assumptions.
- Modify calibration data inputs and structural parameters, and run a basic one-at-a-time sensitivity analysis across parameter values.
- Explain the optimal-reserve-requirement method (MC = MB) and how such an analysis would be implemented in the DGE-METRIC codebase once the formula is confirmed.
- Use GitHub Desktop for basic version control, working alongside VS Code, and an AI coding assistant in VS Code to help navigate and edit model files.
- Produce reproducible charts and concise policy briefs that translate model results into actionable recommendations, including caveats.

# Format

- 3 online sessions across 3 days: Wednesday 22 – Friday 24 July 2026 — 2 mornings and 3 afternoons of live content (5 sessions total, see detailed schedule below).
- Total live time: approximately 15 hours (each session runs about 3 hours / 180 minutes).
- Each afternoon is a design/definition session (no model run); each morning is hands-on, applying the previous afternoon's work.
- Day 3 PM ends with a short independent-use checklist and exit ticket instead of a separate wrap-up session.
- Software needed: MATLAB and Dynare, installed and working before Day 1; VS Code, a GitHub account, and an AI coding assistant (Claude Code, GitHub Copilot, or another LLM coding assistant) also installed/enabled before Day 1 and confirmed in Day 1's opening check-in; full GitHub Desktop and VS Code workflows are still taught from scratch on Day 2 morning (see "Before you join" below).
- Each session includes at least one short break; exact clock time and time zone are still to be confirmed, so times below are given as elapsed minutes from the start of each session rather than clock times.

# Detailed Schedule

*Wednesday 22 – Friday 24 July 2026. Exact clock time and time zone: to be confirmed.*

## Session 1 — Wednesday 22 July, Afternoon (180 min)

**Finance scenarios & energy-efficiency scenarios — detailed definition**

You'll produce: a fully documented finance-scenario metadata sheet (your assigned scenario from the six-scenario matrix) and a fully documented energy-efficiency scenario metadata sheet — both ready to run tomorrow morning.

| Block | Duration | What you'll do |
|---|---:|---|
| 1. Setup check-in — VS Code, GitHub, AI coding assistant | 10 min | Quick poll: confirm VS Code is installed and opens, a GitHub account exists (GitHub Desktop installed if you got to it), and an AI coding assistant is enabled in VS Code (Claude Code, GitHub Copilot, or another LLM coding assistant). Anyone not ready: pair with a neighbor who is, grab the quick-install links, and flag the facilitator — gaps get fixed in the first break, not live in front of the group. |
| 2. Welcome, recap & where things live | 10 min | Rapid recap of on-site training outcomes; state what today, tomorrow morning, and Thursday afternoon will each produce; point to where financing and efficiency assumptions live in the repository (`docs/financing_pathway.md`, `docs/energy_efficiency_pathway.md`, `ExcelFiles/`). |
| 3. Why financing design matters | 15 min | Three reasons financing design is a first-order determinant of transition speed and cost: affordability of public investment, investment crowd-in via revenue recycling, and policy credibility. |
| 4. The six-scenario finance matrix, in full detail | 35 min | Baseline public financing rate (8%), concessional-loan variant (−3pp), and revenue-recycling variant, walked through mechanism by mechanism; the six-scenario matrix (PDP8/NZ × Base/Concessional/Recycle) and the comparison rule — concessional/recycling variants compare within the same emissions pathway only. |
| 5. Draft your finance-scenario metadata sheet | 25 min | Your group is assigned one of the six scenarios and documents it in full: label, mechanism, file edits needed, variables changed, time path, expected effects, indicators to check, caveats, owner, date. |
| Break | 15 min | |
| 6. The energy-efficiency & demand-side-management scenario, in full detail | 35 min | Narrative and core modeling channels (lower energy intensity, reduced peak demand, lower fuel/electricity imports); quantified 2030 savings potential (≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households); quantified investment need (≈USD 361 million/year, ≈0.076% of 2024 GDP); the documented rebound effect. |
| 7. Draft your energy-efficiency scenario metadata sheet | 30 min | In groups, document the efficiency scenario using the same metadata structure as Block 5: mechanism, sector-specific assumptions and required inputs, affected sectors, time path, expected effects, indicators, caveats. |
| 8. Wrap and preview | 5 min | Confirm both metadata sheets are recorded; preview tomorrow morning's hands-on run of both scenarios. |

## Session 2 — Thursday 23 July, Morning (180 min)

**Calibration & scenario hands-on — codebase navigation, Git/GitHub Desktop, debugging, AI-assisted VS Code**

You'll produce: a calibration diagnostic note; a comparison chart and policy narrative covering both your finance scenario and the energy-efficiency scenario; a local repository cloned and committed to via GitHub Desktop.

| Block | Duration | What you'll do |
|---|---:|---|
| 1. Objective and setup check | 10 min | Restate today's expected outputs; confirm MATLAB, Dynare, and repository paths are working. |
| 2. Codebase navigation & version control with GitHub Desktop + VS Code | 30 min | Locate one equation in `ModFiles/` and trace it to the MATLAB helper in `Functions/` that computes it; clone the repository and make your first commit using GitHub Desktop's visual interface — no command line required; open the same repository in VS Code and use its Source Control panel alongside GitHub Desktop. |
| 3. Baseline calibration run | 25 min | Guided execution of the baseline calibration; interpret diagnostics (residuals, convergence, accounting identities) as a group. |
| 4. Debugging common MATLAB/Dynare errors | 20 min | Categorize a failure before trying a fix — path errors, missing/locked inputs, non-convergence, syntax errors — and work through one deliberately broken example together. |
| Break | 15 min | |
| 5. Run your finance scenario + the efficiency scenario, with AI-assisted VS Code | 35 min | Run your assigned finance scenario against its matching base case, and run the energy-efficiency scenario against the PDP8 baseline, under identical settings; live demo of using an AI coding assistant in VS Code to locate, explain, and edit the script you're working with. |
| 6. Comparison table, chart & narrative | 35 min | Build a comparison table covering GDP, investment, emissions, and the finance- and efficiency-specific indicators from yesterday's metadata sheets; turn it into one policy-facing chart with a short narrative: result, mechanism, policy implication, caveat. |
| 7. Report-out and debrief | 10 min | Fast report-out across groups; debrief questions. |

## Session 3 — Thursday 23 July, Afternoon (180 min)

**Reserve requirements — method and implementation**

You'll produce: a documented MC = MB break-even walkthrough for one energy carrier, and an implementation plan describing how a reserve-requirement analysis would be built in the DGE-METRIC codebase.

*A note on scope: today's method is illustrated using a separate, stylized model, not DGE-METRIC itself — DGE-METRIC's own reserve-requirement analysis has not yet been built. Treat any specific number used today as illustrative of the method, not as a DGE-METRIC output or a Vietnam-specific policy figure.*

| Block | Duration | What you'll do |
|---|---:|---|
| 1. Frame the question and the scope note | 15 min | State the reserve-adequacy policy question: how much strategic reserve of an energy carrier is worth holding, given its cost and the crisis losses it avoids; restate the scope note above. |
| 2. Connect Day 1–2 outputs | 15 min | Map which of your finance-scenario and efficiency-scenario outputs from Wednesday and Thursday morning would feed into a reserve-adequacy analysis (energy-carrier demand, import dependence, GDP/investment/fiscal paths). |
| 3. Break-even screening (Step 1) | 25 min | Walk through a break-even table and the marginal-cost-equals-marginal-benefit accounting logic used to screen reserve levels across carriers. |
| 4. Validation and optimization (Steps 2–3) | 25 min | Walk through how a screening result would be validated (shock test) and optimized (Monte Carlo welfare search), and discuss why illustrative results should not be read as settled conclusions. |
| Break | 15 min | |
| 5. Implementation: where this would live in DGE-METRIC | 35 min | Worked pattern: which parts of a reserve-requirement analysis would be a post-processing script reading existing DGE-METRIC scenario/pathway outputs, versus a structural addition to `ModFiles/`/`Functions/` — the same structure-vs-calibration distinction used for model modification, applied to reserve requirements; what DGE-METRIC output variables would be needed once the formula is confirmed. |
| 6. Draft your implementation plan | 35 min | Choose one carrier from the break-even table; draft an implementation plan documenting the mechanism, the DGE-METRIC outputs it would need, where the logic would live in the codebase, and what remains `[SME REVIEW NEEDED]` before this could run against DGE-METRIC. |
| 7. Wrap and preview | 15 min | Confirm your implementation plan is recorded; preview tomorrow morning's guided lab, where you finish the analysis for your chosen carrier. |

## Session 4 — Friday 24 July, Morning (180 min)

**Guided open lab — applying the reserve-requirement method**

You'll produce: a completed reserve-requirement analysis note for your chosen carrier — inputs, the MC = MB walkthrough, sensitivity considerations, and caveats.

| Block | Duration | What you'll do |
|---|---:|---|
| 1. Recap method and implementation plan | 15 min | Recap yesterday afternoon's MC = MB logic and your group's implementation plan; confirm your chosen carrier and, where relevant, your own Day 1 pathway/scenario work. |
| 2. Guided open lab, part 1 | 90 min | Work the break-even and validation logic by hand for your chosen carrier; identify which carrier(s) clear the lowest break-even bar and explain why in plain language; the facilitator circulates rather than presenting one worked example for the whole room. |
| Break | 15 min | |
| 3. Guided open lab, part 2 — write it up | 45 min | Finish your reserve-requirement analysis note: inputs used, the walkthrough, sensitivity notes (what would have to change for a conclusion to flip), and an explicit list of what is still `[SME REVIEW NEEDED]` before this could inform an actual decision. |
| 4. Report-out and debrief | 15 min | Fast report-out across groups; discuss trade-offs in a policy context. |

## Session 5 — Friday 24 July, Afternoon (180 min)

**Calibration internals — modification & sensitivity analysis, + course close**

You'll produce: a sensitivity-analysis plan for one structural parameter (parameter, perturbation range, expected effect, output indicators to check); your personal independent-use checklist; a completed exit ticket.

| Block | Duration | What you'll do |
|---|---:|---|
| 1. Recap calibration workflow and why it matters | 10 min | Recap the calibration workflow from source data to DGE-ready inputs, and why accounting coherence is the precondition for trusting any scenario comparison. |
| 2. Calibration internals | 30 min | Data inputs vs. structural parameters (discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs); the calibration workbook structure; the IO calibration pipeline (`run_pipeline.m` → `split_utilities_sector.m` → `aggregate_for_dge.m`) and its validation/audit outputs. |
| 3. How to modify calibration | 25 min | Changing a data input vs. a structural parameter — which files change (`ExcelFiles/` vs. a `Functions/` helper), how to re-run and re-validate against the accounting-coherence checks before trusting the result. |
| Break | 15 min | |
| 4. Sensitivity analysis method | 30 min | One-at-a-time parameter perturbation: pick one structural parameter, perturb it by a defined amount, re-run, and compare outputs against the unperturbed baseline; why isolating one parameter at a time matters for interpretation; how to keep a sensitivity-analysis log. General good-practice methodology — flagged where it is not itself a DGE-METRIC-specific procedure. |
| 5. Draft your sensitivity-analysis plan | 30 min | In groups, pick one structural parameter, define a perturbation range, state your expected effect and which output indicators you'd check, and note any input you can't source and must mark `[SME REVIEW NEEDED]`. |
| 6. Report-out | 10 min | Fast report-out across groups. |
| 7. Course close | 30 min | Independent-use checklist (self-assessment: can you run, modify, and interpret a calibration and scenario on your own?); exit ticket (one calibration insight, one scenario-design practice, one reserve-requirement/policy-analysis habit, one remaining question); a short list of open institutional questions and next steps. |

# Before you join

- Confirm MATLAB and Dynare are installed and working.
- Confirm you can access the DGE-METRIC repository (access method to be confirmed by the course team).
- Install VS Code and confirm it opens.
- Create a GitHub account if you don't already have one (GitHub Desktop can wait until Day 2 morning if you run out of time).
- Enable an AI coding assistant in VS Code — Claude Code, GitHub Copilot, or another LLM coding assistant of your choice.
- Step-by-step instructions for all of the above (including how to add MATLAB file support inside VS Code, optional) are in `setup-guide.md`.
- No pre-reading is required; a short recap opens Day 1.
- No Git, GitHub Desktop, or VS Code *experience* is required — using them is taught from scratch on Day 2 morning, using GitHub Desktop's visual interface rather than the command line. Day 1 only checks that the tools above are installed, not that you know how to use them yet.

# How to register

*To be confirmed — registration link or contact person.*

# Questions

*To be confirmed — course contact name and email.*

# A note on support

Several participants asked about a teaching assistant, manuals/videos for later reference, and whether Octave could substitute for MATLAB. These are being followed up on separately and are not yet confirmed — please direct questions to the course contact above.

*This course continues numbering from the on-site training (Training Days 1–2/3), delivered online as Online Days 1–3. Block timings above are relative to each session's start and will be mapped to confirmed clock times once the time zone question is resolved.*
