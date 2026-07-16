\
# Facilitator Guide — Training Day 3 (Online Day 1) Afternoon — Wednesday 22 July 2026

Companion to [`lesson.md`](lesson.md). Use this for live delivery timing and trainer flow.

`[SME REVIEW NEEDED: confirm start/end clock time and time zone for 22 July 2026 — see ../../../qa/sme-questions.md item 5]`. Durations below are relative minute blocks, not fixed clock times.

## Session length

180 minutes total.

**Restructured 2026-07-13**: this session was previously "Calibration and Finance-Scenario Prep" (repository recap, codebase navigation, Git basics, finance matrix). Codebase navigation and Git/GitHub Desktop moved to Online Day 2 AM; the freed time now goes to defining the energy-efficiency scenario at the same depth as the finance matrix. See [`../../../design/decision-log.md`](../../../design/decision-log.md).

**Revised 2026-07-14**: added a 10-minute setup check-in as the new opening block (VS Code, GitHub, AI coding assistant — see decision-log 2026-07-14 entries). "Welcome, recap" and "Why financing design matters" were each trimmed by 5 minutes to hold the session at 180 minutes.

## Trainer flow

| Block | Duration | Content | Source |
|---|---:|---|---|
| 1. Setup check-in | 10 min | Quick poll: VS Code installed, GitHub account exists, an AI coding assistant enabled in VS Code (Claude Code, GitHub Copilot, or other). Not ready? Pair with a neighbor, flag the facilitator, fix in the break | `outreach/setup-guide.md` |
| 2. Welcome, recap & where things live | 10 min | Rapid recap of on-site training outcomes; state what today, tomorrow morning, and Thursday afternoon will each produce; point to where financing and efficiency assumptions live in the repository | Day 3 plan Session 1; `docs/financing_pathway.md`; `docs/energy_efficiency_pathway.md` |
| 3. Why financing design matters | 15 min | Three reasons financing design is a first-order determinant of transition speed and cost | `docs/financing_pathway.md` |
| 4. The six-scenario finance matrix, in full detail | 35 min | Baseline rate, concessional variant, revenue-recycling variant walked through mechanism by mechanism; the six-scenario matrix and the comparison rule | `docs/financing_pathway.md` |
| 5. Draft finance-scenario metadata sheet | 25 min | Groups assigned one of six scenarios; document in full using `scenario-template.md` | This lesson, Part 10 |
| Break | 15 min | | |
| 6. The energy-efficiency scenario, in full detail | 35 min | Narrative, core channels, 2030 savings potential (7.4%/5.1%/11.6%), investment need (~USD 361m/yr), rebound effect | `docs/energy_efficiency_pathway.md` |
| 7. Draft efficiency-scenario metadata sheet | 30 min | Groups document the efficiency scenario using `efficiency-scenario-template.md` | This lesson, Part 10 |
| 8. Wrap and preview | 5 min | Confirm both metadata sheets are recorded; preview tomorrow morning's hands-on run of both scenarios | |

## Facilitation prompts

- "Why would a policymaker care whether GDP moved because of financing cost or because of an efficiency gain — don't these look the same on a GDP chart?"
- "What's the one variable that's different between your assigned finance scenario and its base case — and only that one thing?"
- "Where does the efficiency scenario's rebound effect show up in your expected-effects field, and why does leaving it out overstate the scenario's benefit?"

## Quality gate

- Reject any finance metadata sheet whose "expected mechanism" references a variable outside the finance matrix (public financing rate, revenue recycling) — this is a scenario-definition session for the finance matrix specifically.
- Reject an efficiency metadata sheet that omits the rebound effect or inflates the quantified savings/investment figures beyond what `energy_efficiency_pathway.md` documents.
- Do not let Block 2 or Block 5 expand into a full repository walkthrough — that content now lives in tomorrow morning's session; a pointer to the relevant doc file is enough here.

## Risk checks

- If several participants show up without VS Code, GitHub, or an AI coding assistant installed, do not let Block 1 expand into a live installation walkthrough — pair them with a ready neighbor, point them to `outreach/setup-guide.md`, and resolve individually in the first break so Block 2 starts on time.
- If a participant cannot locate the repository or is unsure of prior-training coverage, do not attempt to re-teach the full Day 3 in-person session live — flag it for asynchronous follow-up and continue with the recap pace for the group.
- If the open question on prior Day 3 delivery (`qa/sme-questions.md` item 1) resolves to "not yet delivered," escalate: Parts 2–3 of the lesson need to expand into full first-time instruction, which does not fit in 180 minutes — flag to the course owner before the session runs.
