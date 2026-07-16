\
# Online Training Agenda

Three afternoon sessions, two morning sessions. Each afternoon is a design/definition session (no model run); each morning is hands-on, applying the previous afternoon's work. Naming follows `../CLAUDE.md`: Training Day 3 = Online Day 1, Training Day 4 = Online Day 2, Training Day 5 = Online Day 3. No morning session is scheduled for Online Day 1.

**Dates: Wednesday 22 – Friday 24 July 2026** (set 2026-07-08 from the participant pre-survey — see `../qa/sme-questions.md` item 7 and `decision-log.md`). Exact clock time and time zone are still `[SME REVIEW NEEDED]`.

**Restructured 2026-07-13** — see `decision-log.md` for the full rationale and the resulting deviations from `../CLAUDE.md`'s required session map, learning outcome #5, and the wrap-up rule (Day 3 PM is now a new technical module, by explicit user decision). Each session's revised or moved content is marked **[Revised 2026-07-13]**.

**Revised 2026-07-14** — Online Day 1 now opens with a setup check-in (VS Code, GitHub, AI coding assistant); see `decision-log.md` 2026-07-14 entry. Marked **[Revised 2026-07-14]** below.

---

## Training Day 3 — Online Day 1 — Wednesday 22 July 2026 (Afternoon only)

### Session: Finance Scenarios & Energy-Efficiency Scenarios — Detailed Definition

**Purpose:** define, in full detail, the six-scenario finance matrix and the energy-efficiency/DSM scenario — the two scenario families Online Day 2 morning runs hands-on. This is a prep/design session: no model run happens today.

**Prerequisites from on-site training:** repository access; prior exposure to `docs/index.md`, `docs/running.md`; if Training Day 3 (calibration/scenario, in-person) was already delivered, this session can move faster through the recap portions — see open question in `course-brief.md`.

**Learning objectives:**
- **[Revised 2026-07-14]** Confirm VS Code, a GitHub account, and an AI coding assistant (Claude Code, GitHub Copilot, or another LLM coding assistant) are installed/enabled — a setup check-in, not instruction in using them.
- Explain why financing design (interest rate, revenue recycling) is a first-order determinant of transition speed and cost, independent of the emissions pathway chosen.
- Read and fully document the six-scenario finance matrix to be run tomorrow morning.
- Explain the energy-efficiency/DSM scenario's narrative, core modeling channels, and quantified savings/investment figures.
- Draft a complete scenario metadata block (per `../CLAUDE.md` "Scenario design rules") for both a finance scenario and the efficiency scenario.

**Key content (source-grounded):**
- **[Revised 2026-07-14 — new opening block, 10 min]** Setup check-in: quick poll on VS Code, GitHub (account, GitHub Desktop if already installed), and an AI coding assistant in VS Code. Anyone not ready pairs with a neighbor and gets pointed to install links; gaps are fixed in the first break, not live. This moves the "installed" bar for these three tools from "Day 2 AM, from scratch" to "confirmed before Day 1" — Day 2 AM still teaches full Git/GitHub Desktop/VS Code workflows from scratch, this check-in only confirms presence. To hold the session at 180 min, "Welcome, recap" trimmed 15→10 min and "Why financing design matters" trimmed 20→15 min. Step-by-step participant instructions (VS Code, GitHub, Claude Code/Copilot/other, and optionally adding MATLAB file support in VS Code) are in `../outreach/setup-guide.md` **[Added 2026-07-14]**.
- Brief pointer to where these assumptions live in the repository (`docs/financing_pathway.md`, `docs/energy_efficiency_pathway.md`, `ExcelFiles/`) — full codebase navigation and Git/GitHub Desktop are taught tomorrow morning, not today **[Revised 2026-07-13 — moved from this session to Online Day 2 AM to make room for scenario-definition depth]**.
- Financing logic from `../../../DGE-METRIC-VietNam/docs/financing_pathway.md`: baseline public financing rate (8%), concessional-loan variant (−3pp), revenue-recycling variant (cap-and-trade revenue → renewable subsidy), and the six-scenario matrix (`PDP8-Base`, `NZ-Base`, `PDP8-Concessional`, `NZ-Concessional`, `PDP8-Recycle`, `NZ-Recycle`).
- **[Revised 2026-07-13]** Energy-efficiency & demand-side-management scenario, from `../../../DGE-METRIC-VietNam/docs/energy_efficiency_pathway.md`: lower energy intensity of production, reduced peak electricity demand, slower final-energy demand growth, lower fossil-fuel/electricity imports; 2030 savings potential ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households; quantified investment need ≈USD 361 million/year (≈0.076% of 2024 GDP); documented rebound effect (higher efficiency raises productivity/GDP, partly offsetting direct energy savings). Previously taught as one of three pathways in a separate Day 2 PM session; now the sole pathway example, elevated to full scenario-metadata depth alongside finance.

**Participant output:** a completed finance-scenario metadata sheet (assigned scenario from the six-scenario matrix) and a completed energy-efficiency scenario metadata sheet, both ready to run tomorrow morning.

**Preparation for next session:** Online Day 2 morning runs the baseline calibration, then runs and interprets both the finance matrix and the efficiency scenario hands-on.

---

## Training Day 4 — Online Day 2 — Thursday 23 July 2026 (Morning + Afternoon)

### Session: Calibration & Scenario Hands-On — Codebase Navigation, Git/GitHub Desktop, Debugging, AI-Assisted VS Code (Morning)

**Purpose:** run baseline calibration, inspect diagnostics, run the finance matrix and the energy-efficiency scenario, and build the codebase-navigation and version-control fluency needed to do so independently.

**Learning objectives:**
- Execute a baseline calibration run and read diagnostics.
- **[Revised 2026-07-13 — moved from Day 1 PM]** Locate a specific equation in `ModFiles/` and trace it to the MATLAB helper in `Functions/` that computes its inputs.
- **[Revised 2026-07-13 — moved from Day 1 PM]** Clone a repository and commit via GitHub Desktop; use VS Code's Source Control panel alongside it.
- Categorize a MATLAB/Dynare failure (path, missing/locked input, non-convergence, syntax) before attempting a fix.
- Run the six-scenario finance matrix and the energy-efficiency scenario, and interpret GDP, investment, fiscal, emissions, and efficiency-specific effects.
- Use an AI coding assistant in VS Code to help locate, explain, or edit a calibration/scenario script.

**Key content (source-grounded):**
- Baseline calibration run per `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md` (Session 4) and `../../06_HandsOn_Materials/Day3/HandsOn1_Baseline_Calibration.md`.
- Codebase navigation deep-dive and Git/GitHub Desktop + VS Code basics — content unchanged from the 2026-07-08 pre-survey addition, only its timing moved (was Day 1 PM, now here, immediately before it's used hands-on).
- Debugging common MATLAB/Dynare errors as a taught skill: categorizing path errors, missing/locked inputs, non-convergence, and syntax errors.
- AI-assisted development in VS Code: using an AI coding assistant to help locate, explain, or edit a calibration/scenario script, demonstrated live.
- Baseline-vs-alternative comparison per Session 6 of the Day 3 plan and `HandsOn2_Baseline_vs_Alternative.md`, applied to **both** the finance-scenario matrix and the energy-efficiency scenario (vs. PDP8 baseline) **[Revised 2026-07-13 — efficiency scenario execution added here; previously the efficiency scenario was only designed, not run, in the old Day 2 PM pathway session]**.
- Minimum comparison variables: GDP, investment, emissions, plus finance-specific indicators (`financing_pathway.md`) and efficiency-specific indicators (energy intensity, final energy demand).

**Participant output:** one calibration diagnostic note (including one debugged issue if encountered); one comparison chart and policy narrative covering both the finance scenario and the efficiency scenario; a local repository cloned and committed to via GitHub Desktop.

### Session: Reserve Requirements — Method and Implementation (Afternoon)

**Purpose:** teach the MC = MB reserve-requirement method and how such an analysis would be implemented in the DGE-METRIC codebase once the formula is confirmed. This is a design/prep session: no model run happens today (the toy-model illustrative calculation is worked by hand tomorrow morning).

**Status:** the DGE-METRIC-specific formula remains blocked — `[SME REVIEW NEEDED: confirm reserve-requirement formula, target indicator, and optimality criterion for DGE-METRIC]`. No DGE-METRIC-specific reserve-requirement formula, variable list, or institutional rule was found in `docs/`, the Day 3 plan, or `CLAUDE.md`. A related three-step methodology (break-even screening → shock validation → Monte Carlo welfare optimization) exists on a separate stylized toy model (`Toy Model SOE MC/`), explicitly marked elsewhere as illustrative pending a full DGE-METRIC production-network run — it must not be presented as DGE-METRIC's answer without SME confirmation. See `../qa/sme-questions.md` item 2. The conceptual/illustrative-proxy content itself is not blocked and is drafted in full.

**Learning objectives:**
- State the reserve-requirement policy question: how much strategic reserve of an energy carrier is worth holding, given its cost and the crisis losses it avoids.
- Identify which finance-scenario and efficiency-scenario outputs from Days 1–2 feed a reserve-adequacy analysis.
- Explain the three-step MC = MB methodology (break-even accounting → shock validation → Monte Carlo welfare optimization) using illustrative toy-model numbers, correctly labeled as such.
- **[Revised 2026-07-13]** Explain the implementation pattern: which parts of a reserve-requirement analysis would be a post-processing script reading existing DGE-METRIC outputs, versus a structural addition to `ModFiles/`/`Functions/` — the same structure-vs-calibration distinction previously taught for pathway model modification, now applied here (pathways themselves are out of scope this iteration — see below).

**Key content (source-grounded):**
- The policy question and MC = MB logic, and the illustrative `Toy Model SOE MC` three-step methodology — content carried over unchanged from the previous Day 3 AM session (see `qa/sme-questions.md` item 2, `Toy Model SOE MC/email_optimal_reserve_requirements.md`, `reserve_breakeven_table.md`): baseline GDP (2024) USD 430,000m, crisis probability 4%/yr, break-even divisor USD 172.0m; illustrative ranking from refined-product tanks/distributed BESS (≈0.16–0.18% break-even GDP loss) to 90-day imported coal / 6-MTA LNG (≈1.9–2.0%); Step 2 "not justified" verdicts at 20%/50% shock sizes under current toy-model calibration; Step 3's provisional, mis-scaled corner-solution caveat.
- **[Revised 2026-07-13 — new]** Implementation framing, reusing the pattern previously taught for pathway model modification (`docs/RTS_pathway.md`, `docs/energy_efficiency_pathway.md` structure-vs-calibration distinction, now generalized): a reserve-requirement analysis most plausibly lives as a post-processing script reading DGE-METRIC scenario/pathway outputs (energy-carrier demand, import dependence, GDP/investment/fiscal paths) rather than as a new structural equation block — though this is itself provisional until the DGE-METRIC formula is confirmed.
- Inputs needed: energy-carrier demand and import dependence from the efficiency scenario (Day 1 PM/Day 2 AM); GDP, investment, and fiscal paths from the finance scenarios (Day 1 PM/Day 2 AM).

**Participant output:** a documented implementation plan for one self-chosen energy carrier: mechanism, DGE-METRIC outputs it would need, where the logic would live in the codebase, and what remains `[SME REVIEW NEEDED]`.

**Preparation for next session:** Online Day 3 morning is a guided open lab — participants finish the MC = MB walkthrough by hand for their chosen carrier and write up the full reserve-requirement analysis note, using today's implementation plan as the starting point.

---

## Training Day 5 — Online Day 3 — Friday 24 July 2026 (Morning + Afternoon)

### Session: Guided Open Lab — Applying the Reserve-Requirement Method (Morning)

**Purpose:** hands-on application of yesterday afternoon's MC = MB method to a self-chosen energy carrier, finishing the reserve-requirement analysis note. **[Revised 2026-07-13]** Previously this session also carried the core-method walkthrough (break-even table, Steps 1–3) in the same 180 minutes as the open lab; that conceptual content moved to Day 2 PM, freeing this entire session for the hands-on lab.

**Learning objectives:**
- Apply the MC = MB break-even and validation logic by hand to a self-chosen carrier.
- Correctly distinguish illustrative-proxy numbers from anything that would need to be a DGE-METRIC output.
- Produce a complete reserve-requirement analysis note: inputs, walkthrough, sensitivity notes, caveats.

**Key content:** same illustrative `Toy Model SOE MC` numbers as yesterday afternoon; no new conceptual content introduced (per `../CLAUDE.md`-style discipline against re-teaching in an applied session) — this session is entirely guided practice.

**Before this session runs:** state to participants, verbally and on the first slide: *"Today's numbers come from a separate illustrative toy model, not from DGE-METRIC. DGE-METRIC's own reserve-requirement analysis has not yet been built."* Do not soften or drop this framing — it is a `../../../CLAUDE.md` requirement (see "Optimal reserve requirement rules": do not invent the reserve-requirement formula or optimality criterion).

**Participant output:** one completed reserve-requirement analysis note per group, for a self-chosen carrier, documenting inputs, sensitivity, trade-offs, and caveats.

**Preparation for next session:** Online Day 3 afternoon shifts topic entirely, to calibration internals and sensitivity analysis — no dependency on this session's specific carrier choice.

### Session: Calibration Internals — Modification & Sensitivity Analysis, + Course Close (Afternoon)

**Purpose:** teach calibration internals in depth, how to modify calibration data inputs and structural parameters, and how to run a one-at-a-time sensitivity analysis — then close the course with a short independent-use checklist and exit ticket. **[Revised 2026-07-13]** This entire session is new; it replaces the previous wrap-up-only session. Per the user's explicit decision (see `decision-log.md`), this is a deliberate exception to `../CLAUDE.md`'s rule that the final afternoon must not be a new technical module.

**Learning objectives:**
- Explain the calibration workbook structure: data inputs vs. structural parameters.
- Explain the IO calibration pipeline and its validation/audit checks.
- Modify a calibration data input and a structural parameter, and know which files each requires touching.
- Design and document a one-at-a-time sensitivity-analysis plan for one structural parameter.
- Complete the course's independent-use checklist and exit ticket.

**Key content (source-grounded):**
- Calibration workbook structure and structural parameters (discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs) per `../../../DGE-METRIC-VietNam/docs/calibration.md`.
- IO calibration pipeline (`run_pipeline.m` → `split_utilities_sector.m` → `aggregate_for_dge.m`, with validation/audit CSV outputs) per `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md` Session 3. **Not verified present in this Dropbox copy** — `[SME REVIEW NEEDED: confirm live location of the IO_Calibration pipeline folder for this cohort — see qa/sme-questions.md item 3]`.
- How to modify calibration: a data-input change touches `ExcelFiles/`; a structural-parameter change touches a `Functions/` helper (or the calibration workbook, depending on how the parameter is set) — re-run and re-validate against the accounting-coherence checks before trusting the result.
- **[New 2026-07-13]** Sensitivity analysis method: one-at-a-time parameter perturbation — perturb one structural parameter by a defined amount, re-run, compare against the unperturbed baseline, and record the result in a sensitivity log. This is general good-practice methodology, not a DGE-METRIC-specific procedure documented in the reviewed sources — taught and flagged as such.
- Short close (30 min, replacing the previous full wrap-up structure): independent-use checklist (trimmed to the single combined checklist, dropping the separate reproducibility and policy-communication checklists as standalone blocks — their content is folded into the single checklist) and exit ticket (unchanged four items). Group reflection and a separate remaining-questions block are dropped from live time; open institutional questions are listed in `qa/sme-questions.md` for asynchronous follow-up instead.

**Participant output:** a sensitivity-analysis plan for one structural parameter (parameter, perturbation range, expected effect, output indicators to check); a completed independent-use checklist; a completed exit ticket.
