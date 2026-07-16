\
# Outreach Materials

Participant-facing and promotional materials for the DGE-METRIC online training. Distinct from `../design/agenda.md`, which is the internal facilitator planning document (with source citations and open SME items) — these files are written for an external audience and deliberately omit internal jargon and citations.

## Files

- [participant-agenda.md](participant-agenda.md) — original summary-level agenda (pre-2026-07-13 curriculum: energy pathways incl. DER/LNG-to-Hydrogen, wrap-up as its own session). Kept as a historical/alternate source; **no longer the source for any `.docx` below.**
- [detailed-agenda.md](detailed-agenda.md) — **current source of truth**, block-by-block (5 sessions × relative-minute blocks, each summing to 180 min). Revised 2026-07-13: each afternoon now goes deep on one topic (Day 1 PM finance + energy-efficiency scenario definition, Day 2 PM reserve-requirement method + implementation, Day 3 PM calibration modification + sensitivity analysis + short close) instead of surveying several; DER and LNG-to-Hydrogen pathways are out of scope for this iteration; codebase navigation and Git/GitHub Desktop moved to Day 2 AM; the standalone wrap-up session was folded into a 30-min close at the end of Day 3 PM. Revised again 2026-07-14: Day 1 now opens with a setup check-in (VS Code, GitHub, AI coding assistant), and installing those three tools moved from "Day 2 AM, from scratch" to a prerequisite confirmed before Day 1.
- [DGE-METRIC_Online_Training_Agenda_Detailed.docx](DGE-METRIC_Online_Training_Agenda_Detailed.docx) — the single active `.docx`, generated from `detailed-agenda.md`. The two sibling variants (`DGE-METRIC_Online_Training_Agenda.docx` and `..._policy_reframed.docx`) were moved to `Archiv/` per this file's earlier "consider retiring" notes and are no longer regenerated. **Rebranded 2026-07-14** to GIZ red (was Word's generic default blue/Calibri theme) so it matches the slide decks: Title/Heading styles recolored to GIZ red (`CC071E`), the theme's `accent1` updated to match, table header rows now GIZ-red with white bold text and alternating white/light-gray body rows (mirrors `slidekit.py`'s `table_slide`), and the GIZ logo added to the page header. Because this file is also used as the `--reference-doc` for its own regeneration, the branding carries forward automatically — no extra step needed after future `detailed-agenda.md` edits.
- [course-flyer.html](course-flyer.html) — one-page visual flyer, updated 2026-07-13 to the current curriculum. Published as a shareable Artifact: https://claude.ai/code/artifact/78287972-4391-4e2a-9480-12c28fee53f8

Regenerate the active `.docx` after editing `detailed-agenda.md` (do not hand-edit the docx), using itself as the style reference so formatting round-trips:

```
pandoc detailed-agenda.md --reference-doc=DGE-METRIC_Online_Training_Agenda_Detailed.docx -o DGE-METRIC_Online_Training_Agenda_Detailed_NEW.docx
mv DGE-METRIC_Online_Training_Agenda_Detailed_NEW.docx DGE-METRIC_Online_Training_Agenda_Detailed.docx
```

## Status

**Dates confirmed 2026-07-08: Wednesday 22 – Friday 24 July 2026**, set from the participant pre-survey (see [`../qa/sme-questions.md`](../qa/sme-questions.md) item 7 and [`../design/decision-log.md`](../design/decision-log.md)).

**2026-07-13: curriculum restructured, and the restructuring has now been propagated everywhere** — `../design/agenda.md`, `../design/curriculum-map.md`, `../design/course-brief.md`, all `../content/*/lesson.md`/`facilitator-guide.md`/`exercise.md`/`expected-outputs.md` files (folders renamed to match), `../scenarios/` logs and templates, `../qa/sme-questions.md`, all three files above, `course-flyer.html`, and all three `../slides/*.pptx` decks are in sync as of this date. See [`../design/decision-log.md`](../design/decision-log.md) 2026-07-13 entry for the full rationale, including the deliberate, documented deviations from `../CLAUDE.md` (session map, learning outcome #5, and the wrap-up rule) that this restructuring introduces — `CLAUDE.md` itself was not edited, matching prior practice.

**2026-07-14: detailed-agenda docx rebranded to GIZ red.** The active `.docx` previously used Word's generic default theme (blue accent, Calibri/Cambria) with no GIZ branding at all, unlike the slide decks. Recolored headings/title/table headers to GIZ red and added the GIZ logo to the page header so the two artifact types read as one system. See `../design/decision-log.md`.

**2026-07-14: Day 1 setup check-in added.** Day 1 (Online Day 1 PM) now opens with a dedicated block confirming VS Code, GitHub, and an AI coding assistant are installed/enabled, and the "Before you join" prerequisites were expanded accordingly (previously only MATLAB/Dynare were required before Day 1; VS Code/GitHub/AI-assistant install now moves earlier too, though full from-scratch instruction stays on Day 2 AM). Propagated to `detailed-agenda.md`, the active `.docx`, `../design/agenda.md`, `../design/decision-log.md`, and the Day 1 slide deck.

Clock time, time zone, and registration link/contact are **still not confirmed** and remain "to be confirmed" in all files.
