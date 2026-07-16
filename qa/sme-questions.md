\
# SME / User Questions

**Status update, 2026-07-08:** the user approved `../design/curriculum-map.md` and `../design/agenda.md`, unblocking full lesson content per `../CLAUDE.md` Step 7 (see `../design/decision-log.md`). Full content has now been drafted for all five sessions. Approving the curriculum and agenda does **not** resolve the source-grounding gaps below — each remains open and is flagged inline in the drafted content as `[SME REVIEW NEEDED]` or as an explicit assumption to confirm. Items are grouped by topic; each includes why it matters.

## 1. Delivery status of on-site Training Day 3

A full presenter guide for an in-person "Day 3" (calibration, repository walkthrough, IO calibration pipeline, baseline calibration hands-on, generic scenario design, baseline-vs-alternative hands-on, chart/narrative) already exists at `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`, with compiled slide decks dated June 2026.

- **Was this Day 3 already delivered in person to this participant cohort?**
  - If yes: Online Day 1 afternoon should be a short recap/bridge only (per the audience assumption in `CLAUDE.md`), not a re-teaching of calibration mechanics, and Online Day 2 morning's calibration hands-on can move faster / focus on the finance-scenario layer specifically.
  - If no: clarify why the online course is numbered as continuing from Training Day 3 rather than starting at Day 1, and confirm the Online Day 1/Day 2-morning content should fully carry the calibration teaching load described in the Day 3 plan.

## 2. Reserve-requirement methodology for DGE-METRIC (blocking)

`CLAUDE.md` requires Training Day 5 morning to teach participants how to use DGE-METRIC outputs to determine optimal reserve requirements, and explicitly prohibits inventing the formula or optimality criterion.

- No DGE-METRIC-specific reserve-requirement formula, target indicator, or institutional rule was found in `docs/`, the Day 3 plan, or `CLAUDE.md` itself.
- A related methodology exists, but only on a separate stylized small-open-economy toy model (marginal-cost-equals-marginal-benefit screening → shock validation → Monte Carlo welfare optimization over reserve coverage days). That methodology is documented elsewhere as illustrative/training-stage, explicitly pending a full DGE-METRIC production-network run to compute per-carrier expected GDP loss from a supply disruption.
- **Questions for SME:**
  1. Does DGE-METRIC (as opposed to the toy model) currently have any reserve-requirement variables, calibration targets, or output indicators at all?
  2. Should Training Day 5 morning teach the toy-model methodology explicitly labeled as a preview/proxy (with the DGE-METRIC integration caveat stated up front), or should it wait until DGE-METRIC itself supports this?
  3. If DGE-METRIC support is not yet built, should the module instead focus on defining the policy question and required inputs (conceptual), deferring the actual computation to a future session?

**Content approach taken (2026-07-08):** rather than leaving the module fully blocked, Training Day 5 morning content now teaches the policy question conceptually and walks through the existing `Toy Model SOE MC/` break-even and Monte-Carlo welfare methodology (`email_optimal_reserve_requirements.md`, `reserve_breakeven_table.md`) **explicitly and repeatedly labeled as an illustrative proxy on a stylized small-open-economy model, not a DGE-METRIC output**, per the SME-question-2 option of teaching the toy-model methodology as a labeled preview. The actual DGE-METRIC reserve-requirement formula, target indicator, and optimality criterion are still marked `[SME REVIEW NEEDED]` throughout — see `../content/training-day-04/afternoon-reserve-requirements-method/` (method + implementation framing, since 2026-07-13) and `../content/training-day-05/morning-reserve-requirements-open-lab/` (hands-on application). This still blocks the module from citing DGE-METRIC-specific numbers; it does not block the conceptual/methodological teaching content.

## 3. Repository access for hands-on sessions

- The `docs/` subfolder of `DGE-METRIC-VietNam` is mirrored locally, but `ExcelFiles/` in this Dropbox copy is empty. The Day 3 plan references specific workbooks (`ModelCalibration5Sectorsand1Regions.xlsx`, `ModelBaseline5Sectorsand1Regions.xlsx`, `ModelScenarios5Sectorsand1Regions.xlsx`) and a GitHub repository (`schultkr/DGE-METRIC-VietNam`) as the live model source.
- The Day 3 plan also references an `Training/Day3_Calibration/IO_Calibration/` pipeline (`run_pipeline.m`, `split_utilities_sector.m`, `aggregate_for_dge.m`, config files) not verified present in this Dropbox location.
- **Question:** where will online participants access the live model repository (calibration workbooks, `.mod`/`.m` files, IO calibration pipeline) for the Day 2-morning and Day 3-morning hands-on sessions? Confirm the canonical repository location and access method (GitHub clone, shared drive, etc.) before drafting hands-on exercise files.

## 4. Numeric finance-scenario assumptions beyond the existing matrix

`financing_pathway.md` documents a baseline public financing rate of 8%, a concessional-loan reduction of 3pp, and a revenue-recycling rule. `CLAUDE.md` prohibits inventing additional numeric finance assumptions.

- **Question:** are there additional finance-scenario variants planned for this training beyond the existing PDP8/NZ × Base/Concessional/Recycle matrix (e.g. public vs. private financing shares, external financing), or should the online training use exactly the existing six-scenario matrix?

## 5. Schedule logistics — **RESOLVED 2026-07-08**

`CLAUDE.md` does not specify calendar dates, clock times, or time zone for Online Day 1/2/3, and an earlier planning document (`../DGE_METRIC_Advanced_Training_Plan_July2026.md`) describes a different four-session, VS-Code/AI-focused training tentatively for the week of July 20–24, 2026.

**Resolution:** per the pre-survey (item 7) and the user's decision, this course keeps its 3-day/2-morning+3-afternoon structure, anchored to the three most-preferred days of that same week: **Wednesday 22, Thursday 23, Friday 24 July 2026** (Online Day 1/2/3 respectively). See `../design/decision-log.md`. Clock time and time zone are still **`[SME REVIEW NEEDED]`**.

## 6. Older `Online_Training_Agenda.md` and detailed-plan documents — **PARTIALLY RESOLVED 2026-07-08**

Two older planning documents in this folder (`Online_Training_Agenda.md`; `DGE_METRIC_Online_Training_Detailed_Plan.md`) describe a VS Code / Git / AI-assistant-centric training (4–5 sessions), not the calibration/finance/pathways/reserve-requirement structure in `CLAUDE.md`.

**Resolution:** the pre-survey (item 7) shows real, substantial demand for exactly this model-development content among this course's actual registrants — it is not a separate audience. Per the user's decision, the relevant topics (codebase navigation, model modification, debugging, Git, AI-assisted VS Code development, guided open lab) have been folded into this course's five sessions rather than left to a separate track. Whether `Online_Training_Agenda.md` and `DGE_METRIC_Online_Training_Detailed_Plan.md` themselves should now be archived (since their content is superseded/absorbed) is still open — `[SME REVIEW NEEDED]`.

## 7. Pre-survey findings (`pre survey.xlsx`), reviewed 2026-07-08 — bears directly on items 5 and 6

A real participant pre-survey exists in this folder (`../pre survey.xlsx`, 2 sheets: raw responses + a topic/date tally). It was collected 2026-07-01 to 2026-07-04 from ~17 registrants across real organizations (RCEE; Vietnam Petroleum Institute — VPI ×2; National Institute for Economics and Finance / Ministry of Finance ×4; Electric Power University ×2; Institute for Policy and Strategy Studies (IPSS) ×3; Institute of Energy; Institute of Science and Technology for Energy and Environment; School of Economics and Management, HUST; Vietnam Academy of Science and Technology; Energy and Environment Consultancy JSC; CEGR; CIEM). This resolves part of item 5 (real target week exists) but reopens item 6 (topic scope) in a way that needs a decision, not just archiving.

**Interest:** 83.3% "Yes", 16.7% "Possibly (depending on schedule/content)", 0% "No" — strong confirmed demand.

**Date preference** (responses per day, week of **July 20–24, 2026**, multi-select): Mon 20/07 — 9; Tue 21/07 — 10; Wed 22/07 — 12; Thu 23/07 — 13; Fri 24/07 — 17 (of ~16–17 respondents). Later in the week is clearly preferred. `[SME REVIEW NEEDED: the raw response label for Monday reads "Morning afternoon, 20/07/2026" while Tue–Fri read "<Day> afternoon, <date>" — confirm whether Monday was offered as a full day (AM+PM) and Tue–Fri as afternoon-only, or whether this is a label artifact and all five days were afternoon-only options]`.

**Format ambiguity:** the response sheet includes a column header `"Zalo Confirm (2nd voting for op[tion] 2.5 days in-person)"`, implying a second round of voting considered a **2.5-day in-person** alternative to whatever online/multi-day format was first proposed. `[SME REVIEW NEEDED: confirm final decision — online across the surveyed week, or in-person/hybrid over 2.5 days — before finalizing `design/agenda.md`, the facilitator guides, or outreach materials with specific dates]`.

**Topic demand** (count of respondents selecting each topic, out of ~17; free text translated from Vietnamese):

| Rank | Topic | Count | In current curriculum? |
|---:|---|---:|---|
| 1 | Applying model results to policy questions and communicating findings | 17 | Yes — chart/narrative rule, all sessions |
| 2 | Calibration workflow, data updates, parameter changes | 15 | Yes — Day 1 PM / Day 2 AM |
| 2 | Designing policy scenarios and modifying assumptions | 15 | Yes — finance-scenario matrix (Day 1 PM/Day 2 AM); energy pathways (Day 2 PM) |
| 4 | Navigating and understanding the DGE-METRIC codebase | 14 | Partial — folder-role recap only, not deep code navigation |
| 4 | Model modification: equations, Dynare files, MATLAB scripts | 14 | **No** — not currently covered |
| 6 | Debugging common MATLAB/Dynare errors | 8 | Partial — troubleshooting tables exist but are calibration/run-focused, not general debugging |
| 6 | AI-supported model development in VS Code | 8 | **No** — not currently covered |
| 6 | Guided open lab on participants' own use cases | 8 | **No** — not currently covered |
| 9 | Git / version control and team collaboration | 7 | **No** — not currently covered |
| 10 | Other (write-in): climate change / external shocks on growth | 1 | Partial — energy pathways touch this indirectly |

**This does not overlap cleanly with the built curriculum.** Three topics match well (policy communication, calibration, scenario design). Five topics with real, substantial demand (codebase navigation, model/equation editing, debugging, Git, AI-assisted VS Code development, open lab) are **not covered at all** in the five drafted sessions — these are exactly the topics in the older, previously-flagged `DGE_METRIC_Advanced_Training_Plan_July2026.md` / Track A / Track B documents (item 6). Energy transition pathways and reserve requirements — half of the built curriculum — are **not asked about in the survey at all**.

**Qualitative requests (free text, translated), applicable regardless of scope decision:**
- Provide a teaching assistant / co-facilitator (raised twice, independently).
- Provide manuals and instructional videos for later self-service reference (raised twice, independently).
- Explain variable meanings and relationships more thoroughly, not just mechanics.
- Consider introducing Octave as a MATLAB-license-free alternative.
- Confirm registration materials/logistics are fully sent and confirmed to participating units ahead of time.
- Pair technical instruction with concrete policy applications throughout (already this course's design intent — reinforces the existing chart-and-narrative rule).
- One respondent wants deeper Vietnam-specific model calibration/extension.

**Decision (2026-07-08):** see `../design/decision-log.md` — add model-development topics alongside the existing curriculum; keep the 3-day/2-AM+3-PM structure anchored to Wed–Fri 22–24 July 2026; keep delivery online. Still open: the Monday label ambiguity (moot now that Monday/Tuesday are no longer used), the 2.5-day in-person alternative, and clock time/time zone (item 5).

**2026-07-13 note:** the curriculum was restructured the same week (see item 8 below). Two rows in the topic-demand table above are now stale: "Designing policy scenarios and modifying assumptions" — energy pathways (Day 2 PM) no longer exist as a separate pathway-design session, though the underlying pre-survey demand is still met via the energy-efficiency scenario and the finance matrix. "Model modification: equations, Dynare files, MATLAB scripts" (14 votes) is still covered, but repurposed onto reserve requirements (Day 2 PM) rather than energy pathways.

## 8. [New 2026-07-13] Open items from the depth-over-breadth restructuring

See `../design/decision-log.md` 2026-07-13 entry for the full restructuring rationale (finance + energy-efficiency scenario definition on Day 1 PM; reserve-requirement method + implementation on Day 2 PM; guided open lab on Day 3 AM; calibration modification + sensitivity analysis on Day 3 PM, replacing the wrap-up).

- **Scope cut, not yet institutionally confirmed:** DER (Distributed Energy Resources) and LNG-to-Hydrogen/CCS pathways are dropped from this iteration by user decision, not by SME/institutional sign-off. If either topic has independent stakeholder demand beyond the pre-survey (e.g. from VPI or Electric Power University, both represented in the pre-survey respondent list), flag before treating this cut as final.
- **`CLAUDE.md` is now out of sync** with the required session map, learning outcome #5, and the "wrap-up must not be a new technical module" rule. Documented as a deliberate exception in `decision-log.md`, but `CLAUDE.md` itself was not edited — confirm with the course owner whether it should be updated to match, or left as the stable baseline with exceptions layered on top (as has been the practice since the 2026-07-08 extension too).
- **Reserve-requirement implementation framing (Day 2 PM) is itself unverified**: the "most plausibly a post-processing script, not a structural model change" framing is a reasonable teaching pattern, not a confirmed design — it should be revisited once the actual DGE-METRIC reserve-requirement formula (item 2, still blocking) is confirmed.
- **Structural-parameter baseline values and file locations for the new Day 3 PM sensitivity-analysis content** (discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs) are not confirmed in the reviewed sources — see `[SME REVIEW NEEDED]` markers throughout `../content/training-day-05/afternoon-calibration-modification-sensitivity/`.
- **IO calibration pipeline location** (item 3's existing open question) now also blocks Day 3 PM's calibration-internals content, not just Day 2 AM's hands-on run.
