\
# Curriculum Map

Maps each learning outcome to the session(s) that build it and the source material that grounds it. No numeric assumption, formula, or parameter is asserted here beyond what the cited source documents. **Revised 2026-07-13** — see [`decision-log.md`](decision-log.md) for the restructuring rationale and the resulting deviations from `../CLAUDE.md` (outcome #5 in particular is no longer met as originally written).

| # | Learning outcome | Built in | Primary source |
|---:|---|---|---|
| 1 | Navigate the DGE-METRIC repository and identify major folders/files | Online Day 2 AM | `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md` (Session 2, repository walkthrough); `../../../DGE-METRIC-VietNam/docs/index.md` |
| 2 | Explain the calibration workflow from source data to DGE-ready inputs | Online Day 2 AM (run) → Online Day 3 PM (internals, modification) | `../../../DGE-METRIC-VietNam/docs/calibration.md`; Day 3 plan Session 3 (IO calibration pipeline) |
| 3 | Run a baseline calibration and interpret diagnostics | Online Day 2 AM | Day 3 plan Session 4; `../../06_HandsOn_Materials/Day3/HandsOn1_Baseline_Calibration.md` |
| 4 | Design a finance scenario and an energy-efficiency scenario using transparent assumptions and metadata | Online Day 1 PM (define) → Online Day 2 AM (run, compare) | `../../../DGE-METRIC-VietNam/docs/financing_pathway.md` (PDP8/NZ × Base/Concessional/Recycle matrix); `../../../DGE-METRIC-VietNam/docs/energy_efficiency_pathway.md` |
| 5 *(revised scope)* | Modify calibration data inputs and structural parameters, and run a one-at-a-time sensitivity analysis | Online Day 3 PM | `../../../DGE-METRIC-VietNam/docs/calibration.md`; Day 3 plan Session 3. *Was: "design and compare alternative energy transition pathways" — DER and LNG-to-Hydrogen dropped 2026-07-13, see decision-log.* |
| 6 | Explain the optimal-reserve-requirement method (MC = MB) and how it would be implemented in DGE-METRIC | Online Day 2 PM (method + implementation plan) → Online Day 3 AM (apply, hands-on) | [SME REVIEW NEEDED: confirm reserve-requirement formula, target indicator, and optimality criterion for DGE-METRIC — see `../qa/sme-questions.md`]; illustrative `Toy Model SOE MC` methodology used as a labeled proxy |
| 7 | Compare baseline and alternative outputs across GDP, investment, emissions, fiscal, policy, and reserve indicators | Online Day 1 PM (define indicators), Day 2 AM (compare) | `../../../DGE-METRIC-VietNam/docs/scenario.md` (indicator list); Day 3 plan Session 6 (minimum comparison variables) |
| 8 | Produce reproducible charts and short policy narratives with caveats | Online Day 2 AM | Day 3 plan Session 7; `../../06_HandsOn_Materials/Day3/HandsOn3_Group_Chart_and_Narrative.md` |
| 9 | Document assumptions, edits, runs, diagnostics, and interpretation reproducibly | Every session (documentation task) | Day 3 plan Session 3 (file-impact map), Session 4 (diagnostic note) |

## Topic-to-source detail

### Finance and energy-efficiency scenarios (Online Day 1 PM / Day 2 AM)

- Finance scenario matrix (existing, not invented): baseline public financing rate 8%; concessional variant −3pp (effective ~5%); revenue-recycling variant redirects cap-and-trade revenue to renewable subsidies. Six scenarios: `PDP8-Base`, `NZ-Base`, `PDP8-Concessional`, `NZ-Concessional`, `PDP8-Recycle`, `NZ-Recycle`. Source: `financing_pathway.md`.
- Energy-efficiency & demand-side-management scenario: lower energy intensity, reduced peak demand, lower fuel/electricity imports; 2030 savings potential ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households; quantified investment need ≈USD 361 million/year (≈0.076% of 2024 GDP); documented rebound effect. Source: `energy_efficiency_pathway.md`.
- Repository roles: `docs/`, `ExcelFiles/`, `Functions/`, `ModFiles/`, `scripts/`, `Training/` — as listed in `../CLAUDE.md` and confirmed live in the Day 3 plan's repository walkthrough. Codebase navigation (equation → helper trace) is now taught Online Day 2 AM, immediately before it's used hands-on.

### Codebase navigation, Git/GitHub Desktop, debugging, AI-assisted VS Code (Online Day 2 AM)

- Equation-to-helper-function navigation skill: given an equation in `ModFiles/`, identify which parameters/variables it references and whether each is a direct calibration input (`ExcelFiles/`) or computed by a `Functions/` helper. Source: `docs/index.md`.
- Version control taught via GitHub Desktop's visual interface plus VS Code's Source Control panel — general practice, not DGE-METRIC-specific.
- Debugging as a categorization skill (path / missing-or-locked input / non-convergence / syntax) — source: `docs/running.md`; existing troubleshooting tables in `HandsOn1`/`HandsOn2`.
- AI-assisted VS Code — general workflow guidance, not a DGE-METRIC-specific claim.

### Reserve requirements — method and implementation (Online Day 2 PM / Day 3 AM)

- No DGE-METRIC-specific reserve-requirement formula or optimality rule currently exists in the repository sources reviewed (`docs/`, Day 3 plan, `CLAUDE.md`).
- A related methodology (marginal-cost-equals-marginal-benefit screening → shock validation → Monte Carlo welfare optimization) exists but only on a separate stylized small-open-economy toy model (`Toy Model SOE MC/`), not on DGE-METRIC itself, and is explicitly described elsewhere as illustrative/training-stage pending a DGE-METRIC production-network run.
- **[Added 2026-07-13] Implementation framing**: the same structure-vs-calibration distinction used for model modification (a structural relationship belongs in `ModFiles/`; the calibration/parameterization that feeds it belongs in `Functions/`/`ExcelFiles/`) is applied to reserve requirements — teaching where a reserve-adequacy analysis would live in the codebase (most plausibly a post-processing script reading existing DGE-METRIC outputs) once the formula is confirmed, not inventing the formula itself.
- Per `../CLAUDE.md`, this gap must not be filled by invention. Flagged as `[SME REVIEW NEEDED]` in `agenda.md` and `../qa/sme-questions.md` item 2 (still open).

### Calibration internals, modification, and sensitivity analysis (Online Day 3 PM)

- Calibration workbook structure: data inputs (sectoral employment, value-added, labour cost, export, import, emission shares) vs. structural parameters (discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs). Source: `docs/calibration.md`.
- IO calibration pipeline: `run_pipeline.m` → `split_utilities_sector.m` → `aggregate_for_dge.m`, with validation/audit CSV outputs. Source: Day 3 plan Session 3. **Not verified present in this Dropbox copy** — see `../qa/sme-questions.md`.
- **[Added 2026-07-13] Sensitivity analysis method**: one-at-a-time structural-parameter perturbation, re-run, compare against the unperturbed baseline. This is general good-practice methodology, not a DGE-METRIC-specific procedure documented anywhere in the reviewed sources — taught as such, not presented as an existing DGE-METRIC feature.

## Cross-cutting rules applied

- Scenario metadata blocks (label, mechanism, file edits, variables, time path, expected effects, indicators, caveats, owner, date) are required for every scenario introduced in content, per `../CLAUDE.md` "Scenario design rules".
- Scenario labels follow lowercase kebab-case, e.g. `finance-pdp8-concessional`, `efficiency-dsm-baseline`, `reserve-requirement-optimal-baseline`.

## Learning outcomes added 2026-07-08 (pre-survey demand), status as of 2026-07-13

| # | Added outcome | Built in | Primary source | Pre-survey votes |
|---:|---|---|---|---:|
| A | Navigate the DGE-METRIC codebase beyond folder roles — locate a specific equation in `ModFiles/`, trace it to the MATLAB helper that computes it in `Functions/` | Online Day 2 AM *(moved from Day 1 PM, 2026-07-13)* | `docs/index.md` repository map; `ModFiles/`, `Functions/` roles confirmed live in Day 3 plan Session 2 | 14 |
| B | Make a small, deliberate model modification and understand what re-running requires | *(scope narrowed 2026-07-13 — see decision-log)* | `docs/RTS_pathway.md`, `docs/energy_efficiency_pathway.md` — RTS wedge no longer taught (DER dropped); efficiency shifter retained as the modification pattern, taught via the reserve-requirement implementation framing instead of a dedicated pathway session | 14 |
| C | Diagnose and resolve common MATLAB/Dynare errors systematically | Online Day 2 AM | `docs/running.md`; existing troubleshooting tables in `HandsOn1`/`HandsOn2` | 8 |
| D | Use an AI coding assistant inside VS Code to help navigate, explain, or edit DGE-METRIC files | Online Day 2 AM | General VS Code / AI-assistant practice — no DGE-METRIC-specific source | 8 |
| E | Apply the course's methods to a participant's own use case in a guided, less-scripted setting | Online Day 3 AM *(now the session's sole focus, not shared with the core-method walkthrough)* | Built from participants' own Day 1–2 scenario work | 8 |
| F | Use GitHub Desktop (+ VS Code) for basic version control and reproducible collaboration on scenario files | Online Day 2 AM *(moved from Day 1 PM, 2026-07-13)*; reinforced in Day 3 PM's short close | General Git/GitHub Desktop practice — no DGE-METRIC-specific source | 7 |

Outcomes A–F are taught at an introductory, workflow level (not a substitute for a dedicated software-engineering course).
