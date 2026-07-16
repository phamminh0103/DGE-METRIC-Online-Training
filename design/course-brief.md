\
# Course Brief: DGE-METRIC Online Training (Training Day 3–5)

## Purpose

This repository develops the online continuation of the on-site DGE-METRIC training. It picks up numbering at **Training Day 3** and runs through **Training Day 5**, delivered online as **Online Day 1, 2, and 3**. It is not a new course and must not be renumbered as if starting at Day 1 (see [`../CLAUDE.md`](../CLAUDE.md), "Prohibited behavior").

The topic is applied use of DGE-METRIC for scenario analysis, calibration, energy transition analysis, finance scenarios, and determination of optimal reserve requirements.

## Continuity with the on-site training

A detailed presenter guide for an in-person **Training Day 3** already exists at
[`../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`](../../Day%203/DGE_METRIC_Training_Day3_Session_Plan.md). It covers repository orientation, the IO calibration workflow, a baseline calibration hands-on, generic scenario design, a baseline-vs-alternative hands-on, and chart/narrative practice — supported by existing hands-on sheets in
[`../../06_HandsOn_Materials/Day3/`](../../06_HandsOn_Materials/Day3/).

**This online course restructures that same Day 3 material into the online prep/apply format** required by `CLAUDE.md` (afternoon prepares the next morning), and extends it with two topics the existing Day 3 plan does not yet cover in depth: finance-scenario design specifically (rate/subsidy mechanisms) and energy transition pathway design, before moving to the new Day 5 topic of optimal reserve requirements.

**Open question:** whether the in-person Day 3 session was already delivered to this cohort as a full stand-alone day, in which case Online Day 1 should be a short recap/bridge rather than a re-teaching of calibration mechanics. See [`../qa/sme-questions.md`](../qa/sme-questions.md).

## Audience

Participants who already attended the previous on-site training (Training Day 1–2, and possibly Day 3). Do not repeat introductory macroeconomic or DGE theory beyond a short recap. Focus on applied model use, hands-on workflows, interpretation, reproducibility, and policy communication.

## Primary goal

Enable participants to use DGE-METRIC independently for calibrated baseline analysis, policy scenario design, scenario comparison, interpretation of model outputs, and communication of policy trade-offs.

## Structure at a glance

Three afternoon sessions, two morning sessions, held **Wednesday 22 – Friday 24 July 2026** (see [`../qa/sme-questions.md`](../qa/sme-questions.md) item 7 for how these dates were set from the participant pre-survey; clock time and time zone are still `[SME REVIEW NEEDED]`). Each afternoon is a design/definition session (no model run); each morning is hands-on, applying the previous afternoon's work.

**Scope extended 2026-07-08:** a real pre-registration survey of this course's own participants (`../pre survey.xlsx`) showed strong, specific demand for model-development skills — codebase navigation, editing equations/Dynare/MATLAB scripts, debugging, Git, and AI-assisted development in VS Code — alongside the originally-scoped calibration/finance/pathway/reserve content. Per the user's decision (see [`decision-log.md`](decision-log.md)), these were folded into the existing five sessions rather than treated as a separate track.

**Curriculum restructured 2026-07-13:** each afternoon now goes deep on one topic instead of surveying several — see [`decision-log.md`](decision-log.md) 2026-07-13 entry for the full rationale and the resulting deviations from `../CLAUDE.md`'s session map, learning outcome #5, and wrap-up rule. In brief: the Distributed Energy Resources and LNG-to-Hydrogen pathways are out of scope for this iteration (energy efficiency remains the one fully-worked pathway example); codebase navigation and Git/GitHub Desktop moved to Day 2 AM; the standalone wrap-up session is now a 30-minute close at the end of Day 3 PM.

**Setup check-in added 2026-07-14:** Online Day 1 (Day 3 PM) now opens with a 10-minute check-in confirming VS Code, GitHub, and an AI coding assistant (Claude Code, GitHub Copilot, or another) are installed/enabled — installing these moved from "Day 2 AM, from scratch" to a prerequisite confirmed before Day 1. Step-by-step participant instructions (including MATLAB/Dynare and optionally adding MATLAB file support to VS Code) are in [`../outreach/setup-guide.md`](../outreach/setup-guide.md). Day 2 AM still teaches full Git/GitHub Desktop/VS Code workflows from scratch — see [`decision-log.md`](decision-log.md) 2026-07-14 entries.

| Training day | Date | Online day | Session | Main focus | Primary sources |
|---|---|---:|---|---|---|
| Day 3 | Wed 22 Jul 2026 | Online Day 1 | Afternoon | Finance-scenario **and** energy-efficiency-scenario detailed definition | `docs/financing_pathway.md`; `docs/energy_efficiency_pathway.md`; pre-survey topic 4 |
| Day 4 | Thu 23 Jul 2026 | Online Day 2 | Morning | Calibration and scenario hands-on (finance + efficiency), **+ codebase navigation, Git/GitHub Desktop, debugging, and AI-assisted VS Code work** | Day 3 session plan (Sessions 4–6); `HandsOn1`/`HandsOn2`; `docs/index.md`; pre-survey topics 4, 6, 7, 9 |
| Day 4 | Thu 23 Jul 2026 | Online Day 2 | Afternoon | Reserve requirements — method and implementation | [SME REVIEW NEEDED: DGE-METRIC reserve-requirement formula and data — see qa/sme-questions.md]; `docs/index.md` (ModFiles/ vs. Functions/ pattern); pre-survey topics 4, 8 |
| Day 5 | Fri 24 Jul 2026 | Online Day 3 | Morning | Guided open lab — applying the reserve-requirement method to a self-chosen carrier | Same as Day 4 PM; pre-survey topic 8 |
| Day 5 | Fri 24 Jul 2026 | Online Day 3 | Afternoon | Calibration internals, modification, and sensitivity analysis, + short close | `docs/calibration.md`; Day 3 session plan (Session 3, IO calibration pipeline) |

Full detail: [`agenda.md`](agenda.md). Outcome-to-source mapping: [`curriculum-map.md`](curriculum-map.md).

## Source grounding used for this brief

- `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`
- `../../06_HandsOn_Materials/Day3/README.md`, `HandsOn1_Baseline_Calibration.md`, `HandsOn2_Baseline_vs_Alternative.md`, `HandsOn3_Group_Chart_and_Narrative.md`
- `../../../DGE-METRIC-VietNam/docs/index.md`, `running.md`, `calibration.md`, `scenario.md`, `financing_pathway.md`, `pathways.md`

## Open questions

See [`../qa/sme-questions.md`](../qa/sme-questions.md) for all items requiring SME or user confirmation, in particular the reserve-requirement methodology for Day 5, the status of the in-person Day 3 delivery, clock time/time zone for the confirmed dates, and whether a "2.5-day in-person" alternative format (mentioned in the pre-survey) is still under consideration.
