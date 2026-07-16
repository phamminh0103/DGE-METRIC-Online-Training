# DGE-METRIC Online Training (Training Day 3–5)

Online continuation of the on-site DGE-METRIC training, numbered Training Day 3–5 / Online Day 1–3. See [`CLAUDE.md`](CLAUDE.md) for the full project brief and working rules.

> This repository is a published copy of the working course-development folder. The raw participant pre-survey (`pre survey.xlsx`, containing names and personal emails) is deliberately excluded — see [`.gitignore`](.gitignore) — and stays in the internal working copy only.

**Dates: Wednesday 22 – Friday 24 July 2026.** Set 2026-07-08 from a real participant pre-survey, which also surfaced strong demand for model-development topics (codebase navigation, Git, debugging, AI-assisted VS Code development, model modification) now folded into the five sessions alongside the original calibration/finance/pathway/reserve curriculum. See [`qa/sme-questions.md`](qa/sme-questions.md) item 7 and [`design/decision-log.md`](design/decision-log.md).

**Curriculum restructured 2026-07-13**: each afternoon now goes deep on one topic instead of surveying several. Distributed Energy Resources and LNG-to-Hydrogen pathways are out of scope for this iteration; energy efficiency is the one fully-worked pathway example. This is a deliberate, documented exception to some of `CLAUDE.md`'s rules (session map, learning outcome #5, the wrap-up rule) — see [`design/decision-log.md`](design/decision-log.md) 2026-07-13 entry and [`qa/sme-questions.md`](qa/sme-questions.md) item 8 before relying on `CLAUDE.md` alone to describe the current course.

## Start here

- [Course brief](design/course-brief.md)
- [Curriculum map](design/curriculum-map.md) — learning outcomes to sessions to sources
- [Agenda](design/agenda.md) — full session-by-session plan
- [Decision log](design/decision-log.md) — approvals and content-approach decisions
- [Open SME/user questions](qa/sme-questions.md)
- [Assessment plan](design/assessment-plan.md)
- [Style guide](design/style-guide.md)

## Session content

| Date | Online day | Session | Folder |
|---|---:|---|---|
| Wed 22 Jul 2026 | 1 | Afternoon: Finance & energy-efficiency scenarios — detailed definition | [`content/training-day-03/afternoon-finance-efficiency-scenarios/`](content/training-day-03/afternoon-finance-efficiency-scenarios/) |
| Thu 23 Jul 2026 | 2 | Morning: Calibration & scenario hands-on **+ codebase nav, Git/GitHub Desktop, debugging, AI-assisted VS Code** | [`content/training-day-04/morning-calibration-scenario-hands-on/`](content/training-day-04/morning-calibration-scenario-hands-on/) |
| Thu 23 Jul 2026 | 2 | Afternoon: Reserve requirements — method and implementation | [`content/training-day-04/afternoon-reserve-requirements-method/`](content/training-day-04/afternoon-reserve-requirements-method/) |
| Fri 24 Jul 2026 | 3 | Morning: Guided open lab — applying the reserve-requirement method | [`content/training-day-05/morning-reserve-requirements-open-lab/`](content/training-day-05/morning-reserve-requirements-open-lab/) |
| Fri 24 Jul 2026 | 3 | Afternoon: Calibration internals — modification & sensitivity analysis, + course close | [`content/training-day-05/afternoon-calibration-modification-sensitivity/`](content/training-day-05/afternoon-calibration-modification-sensitivity/) |

Renamed 2026-07-13 from `afternoon-calibration-finance`, `morning-calibration-finance-hands-on`, `afternoon-energy-transition-pathways`, `morning-optimal-reserve-requirements`, and `afternoon-wrap-up` respectively — see [`design/decision-log.md`](design/decision-log.md).

## Scenario, pathway, and activity logs

- [`scenarios/finance/`](scenarios/finance/), [`scenarios/energy-efficiency/`](scenarios/energy-efficiency/) *(renamed 2026-07-13 from `energy-transition/`)*, [`scenarios/reserve-requirements/`](scenarios/reserve-requirements/)
- [`activities/`](activities/)

## Slide decks

- [`slides/`](slides/) — one facilitator `.pptx` per online day, generated from the content above

## Outreach (participant-facing / advertising)

- [`outreach/detailed-agenda.md`](outreach/detailed-agenda.md) — block-by-block agenda, current source of truth for the `.docx` files shared with participants
- [`outreach/course-flyer.html`](outreach/course-flyer.html) — one-page visual flyer for advertising the course

## Other files in this folder

The remaining top-level files (`DGE_METRIC_Advanced_Training_Plan*`, `DGE_METRIC_Advanced_Training_Track_A/B_*`, `DGE_METRIC_Online_Training_Detailed_Plan.md`, `Online_Training_Agenda.md`) are earlier planning documents for a different VS Code/Git/AI-assistant-centric track. Whether they should be archived or kept as a separate track is open — see [`qa/sme-questions.md`](qa/sme-questions.md) item 6.
