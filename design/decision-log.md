\
# Decision Log

Record of SME/user decisions that unblock or redirect work. Newest first.

---

## 2026-07-14 — Detailed-agenda docx rebranded to GIZ red

**What happened:** the user asked for "the same theme for the slides as for the detailed agenda." Checking the actual docx theme found it was Word's generic default (Calibri/Cambria, blue `accent1` `4F81BD`) — never GIZ-branded, unlike every slide deck (GIZ red `CC071E`, per `def.tex` and `slidekit.py`). Asked the user which direction via `AskUserQuestion`; confirmed: rebrand the docx to match the slides, not the reverse.

**Action taken:** using `python-docx` (plus a small zip-level patch for the theme XML, since python-docx doesn't expose theme color editing directly):
- `Title`/`Heading 1`/`Heading 2`/`Heading 3` styles recolored to GIZ red (`CC071E`); the `Title` style's bottom border recolored to match (was theme-linked blue).
- Theme's `accent1` updated from `4F81BD` to `CC071E` so any accent-linked elements stay consistent.
- All 5 session tables: header row now GIZ-red fill with white bold text, body rows alternating white/light-gray (`F5F5F5`) — mirrors `slides/build/slidekit.py`'s `table_slide()` exactly.
- GIZ logo (`../../pictures/GIZ_Logo.png`) added to the page header.

**Why this is durable:** the rebranded file is also the `--reference-doc` pandoc uses to regenerate itself from `detailed-agenda.md` (see `outreach/README.md`), so the branding carries forward automatically on future content edits — no extra step required.

**Not done:** the two archived docx variants (`outreach/Archiv/`) were left untouched — they're no longer regenerated per the 2026-07-13 retirement note, so rebranding them would be dead effort.

---

## 2026-07-14 — Day 1 opens with a setup check-in; VS Code/GitHub/AI-assistant install moved earlier

**What happened:** the user asked that Online Day 1 begin with an installation/setup check-in confirming all participants have VS Code and GitHub installed, and an AI coding assistant enabled (Claude Code, GitHub Copilot, or another LLM coding assistant), rather than leaving these three tools to be installed live during Day 2 AM's from-scratch walkthrough.

**Why:** per the user, verifying setup is done before diving into content avoids losing Day 2 AM hands-on time to individual installation troubleshooting. Confirmed via `AskUserQuestion`: check-in placed as the new first block of Session 1 (before the welcome/recap block), framed as a quick poll with a troubleshooting buffer (pair with a neighbor, install links, flag the facilitator — fixed in the break, not live).

**What did not change:** Day 2 AM still teaches full Git/GitHub Desktop and VS Code workflows from scratch (cloning, committing, Source Control panel, AI-assisted editing) — per `../CLAUDE.md`'s "Before you join" precedent, no *experience* is assumed, only that the tools are present and open. MATLAB/Dynare remain the only tools that must be fully working (not just installed) before Day 1.

**Timing adjustment:** to keep Session 1 at 180 min after adding a 10-min check-in block, "Welcome, recap & where things live" was trimmed 15→10 min and "Why financing design matters" was trimmed 20→15 min. No other block changed.

**Deviation from `../CLAUDE.md`:** the "Format"/prerequisites framing implicitly extended by the 2026-07-08 decision (below) stated GitHub Desktop and VS Code "can be installed then or in advance" (Day 2, optional early). This decision makes VS Code, a GitHub account, and an AI coding assistant **required** before Day 1. `CLAUDE.md` itself was not edited, consistent with prior practice — this is a documented layered decision.

**Action taken:** updated `outreach/detailed-agenda.md` (new Session 1 block, "Format" and "Before you join" sections, revision note) and regenerated the single active `outreach/DGE-METRIC_Online_Training_Agenda_Detailed.docx`; updated `design/agenda.md` (Online Day 1 learning objectives and key content); updated `outreach/README.md` (file inventory correction — only one `.docx` is now active, the other two live in `outreach/Archiv/`); updated `slides/build/build_day1.py` and regenerated `slides/DGE-METRIC_Online_Day1_Slides.pptx` with a new setup-check-in slide and renumbered agenda table.

**Follow-up same day:** the user asked for clear step-by-step setup instructions, not just a poll — added `outreach/setup-guide.md` (VS Code install, GitHub account, enabling Claude Code/GitHub Copilot/another assistant in VS Code, confirming the existing MATLAB/Dynare install, and optionally adding MathWorks' MATLAB extension to VS Code for `.m` file editing). Linked from `detailed-agenda.md`'s "Before you join" and `design/agenda.md`. Added a second Day 1 slide ("Setup Quick Reference") immediately after the check-in poll, condensing the guide for in-session reference. While rebuilding the deck, fixed an unrelated portability bug in `slides/build/slidekit.py`: `LOGO_PATH` was a hardcoded absolute path from a different machine (`C:\Users\schul\...`), which made the build fail entirely on this machine — changed to resolve relative to `slidekit.py`'s own location.

---

## 2026-07-13 — Curriculum restructured: depth over breadth per afternoon

**What happened:** the user directed a restructuring of the outreach detailed agenda, then asked for it to be propagated through the whole repository. Each afternoon now goes deep on one topic instead of surveying several:

- **Day 1 PM** (was: calibration/finance prep + codebase nav + Git): now finance-scenario **and** energy-efficiency-scenario detailed definition. Codebase navigation and Git/GitHub Desktop moved to Day 2 AM.
- **Day 2 AM** (was: calibration/finance hands-on + debugging + AI-VS Code): unchanged core, but now also runs the energy-efficiency scenario alongside the finance matrix, and absorbs codebase navigation + Git/GitHub Desktop from Day 1 PM.
- **Day 2 PM** (was: energy transition pathways + model modification): now reserve-requirement **method and implementation** — the model-modification framing (structural equation vs. calibration helper) is repurposed from pathways onto reserve requirements.
- **Day 3 AM** (was: optimal reserve requirements core method + guided open lab in one session): now purely the guided open lab, hands-on, applying Day 2 PM's method to a self-chosen carrier.
- **Day 3 PM** (was: wrap-up — synthesis, three checklists, group reflection, exit ticket, remaining questions, next steps): now calibration internals, how to modify calibration inputs/structural parameters, and one-at-a-time sensitivity analysis, ending in a **30-minute close** (independent-use checklist + exit ticket only — no full synthesis, no group reflection, no separate remaining-questions block).

**Scope cut:** the Distributed Energy Resources (Scenario A) and LNG-to-Hydrogen/CCS (Scenario C) pathways are dropped from this iteration. Energy efficiency (Scenario B) is the one fully-worked pathway example, now folded into the finance-scenario definition/hands-on flow rather than run as its own pathway-design session.

**Why:** the user judged that four topics done in depth (finance scenarios, energy-efficiency scenarios, reserve requirements, calibration/sensitivity) serve participants better than six topics done at survey depth. Confirmed via `AskUserQuestion` on two specific forks before drafting: (a) drop DER/LNG-H2 rather than condense or relocate them — recommended and accepted; (b) fold the wrap-up into a short close at the end of Day 3 PM rather than dropping it entirely or moving it to Day 3 AM — recommended and accepted.

**Deviations from `../CLAUDE.md` this decision creates** (documented here rather than silently edited into the base governance document, consistent with how the 2026-07-08 pre-survey extension was handled below):
- "Required session map" no longer matches: Day 2 PM is reserve requirements, not energy transition pathways; Day 3 AM is the guided lab, not the reserve-requirement core method; Day 3 PM is a new technical module (calibration/sensitivity), not solely a wrap-up.
- "Required learning outcomes" #5 ("Design and compare alternative energy transition pathways") is no longer met as written — narrowed to one worked pathway (energy efficiency) folded into outcome #4 instead of a standalone multi-pathway comparison. A new outcome (modify calibration inputs/parameters; run a sensitivity analysis) is added that has no corresponding numbered entry in `CLAUDE.md`.
- "Prohibited behavior" states "treat the wrap-up afternoon as a new technical module" — Day 3 PM is now deliberately a new technical module, with only a 30-minute close retained from the original wrap-up structure. This is a direct, acknowledged exception, not an oversight.
- `CLAUDE.md` itself was **not** edited, matching the precedent set 2026-07-08 below. If this restructuring should become the new baseline rather than a documented exception, `CLAUDE.md`'s session map, learning outcome #5, and the wrap-up prohibition need explicit updating — flagged to the user rather than done unilaterally.

**Action taken:** renamed and rewrote all five `content/training-day-*/` session folders (`lesson.md`, `facilitator-guide.md`, `exercise.md`, `expected-outputs.md`, and session templates) to the new structure; updated `course-brief.md`, `curriculum-map.md`, `agenda.md`; updated `scenarios/` logs and templates (energy-transition renamed to energy-efficiency; reserve-requirements template split into an implementation-plan stage and an open-lab analysis stage); updated `qa/sme-questions.md`; regenerated `outreach/detailed-agenda.md` and both agenda `.docx` files, `outreach/DGE-METRIC_Online_Training_Agenda_policy_reframed.docx`, and `outreach/course-flyer.html`; rebuilt all three `slides/*.pptx` decks. The reserve-requirement scope caveat (illustrative `Toy Model SOE MC` proxy, not DGE-METRIC — see `../qa/sme-questions.md` item 2, still open) is preserved and carried into its new location (Day 2 PM framing, Day 3 AM lab).

---

## 2026-07-08 — Pre-survey reviewed; schedule and curriculum scope reopened

**What happened:** the user asked to revise the Online Training using `../pre survey.xlsx`, a real participant pre-survey (~17 respondents, real organizations, collected 2026-07-01–07-04) for "the advanced training course on DGE-METRIC and Dynare scheduled for July 2026." Full findings logged in [`../qa/sme-questions.md`](../qa/sme-questions.md) item 7.

**Why this matters:** the survey supplies a real target week (July 20–24, 2026) and a real, ranked topic-demand list — but that topic list only partially overlaps the five-session curriculum drafted and approved 2026-07-08 (this same day, earlier). Three topics match (calibration, scenario design, policy communication/charting). Five topics with strong demand (codebase navigation, equation/Dynare/MATLAB-script editing, debugging, Git, AI-assisted VS Code development, guided open lab) are not covered at all — they match the previously-shelved `DGE_METRIC_Advanced_Training_Plan_July2026.md` / Track A / Track B documents instead (`qa/sme-questions.md` item 6). Energy transition pathways and reserve requirements — half the built curriculum — are not mentioned in the survey at all. The survey also raises a live format question (a "2nd voting for option of 2.5 days in-person" column suggests an in-person alternative may still be under consideration, not settled as online).

**Not yet decided:** whether to (a) fold model-development topics into the existing calibration/finance/pathway/reserve curriculum, (b) keep the curriculum as-is and treat the survey as evidence for a separate track, or (c) restructure around the survey's demonstrated demand; and whether the event is online (as designed) or in-person/hybrid over 2.5 days. Asked the user directly rather than guessing, given how much downstream content this decision touches (`design/agenda.md`, all five `facilitator-guide.md` files, `outreach/`).

**Action taken so far:** none to session content or schedule pending the answer above. Recorded findings only.

**Resolution (same day, user decision):**
1. **Curriculum scope:** add the model-development topics (codebase navigation deep-dive, model modification via equations/Dynare/MATLAB scripts, debugging, Git/version control, AI-assisted VS Code development, guided open lab) *alongside* the existing calibration/finance/pathway/reserve curriculum — not instead of it, not as a separate untouched track.
2. **Schedule format:** keep the existing 3-day, 2-morning + 3-afternoon structure; anchor it to the 3 most-preferred days from the survey rather than all 5 — **Wednesday 22, Thursday 23, and Friday 24 July 2026** (12, 13, and 17 responses respectively, vs. 9–10 for Mon/Tue). Online Day 1 = Wed 22 (PM only), Online Day 2 = Thu 23 (AM+PM), Online Day 3 = Fri 24 (AM+PM).
3. **Delivery mode:** online, as designed. The "2.5-day in-person" alternative referenced in the survey's Zalo-confirm column remains unresolved and is left flagged in `qa/sme-questions.md` item 7 rather than blocking further work.

**Action taken:** revised `course-brief.md`, `curriculum-map.md`, and `agenda.md` with real dates; added new content blocks (retimed within the existing 180-min sessions, not extending them further) to all five sessions' `lesson.md`/`facilitator-guide.md`/`exercise.md`/`expected-outputs.md`; updated `outreach/` materials with real dates and the expanded topic list; addressed the qualitative survey requests (teaching assistant, manuals/videos, Octave note) where they fit naturally rather than inventing new infrastructure to satisfy them. `CLAUDE.md` itself was **not** edited — it remains the base governance document; this extension is layered on top and documented here rather than silently rewriting it.

---

## 2026-07-08 — Curriculum map and agenda approved

**Decision:** The user confirmed that `curriculum-map.md` and `agenda.md` are approved as drafted.

**Effect:** Unblocks `../CLAUDE.md` "First tasks for Claude Code" Step 7 — full lesson content may now be drafted for all five sessions (Training Day 3 PM, Day 4 AM, Day 4 PM, Day 5 AM, Day 5 PM).

**Not decided by this approval:** approving the curriculum/agenda structure does not resolve the source-grounding gaps already logged in `../qa/sme-questions.md`. In particular:

- Item 2 (reserve-requirement methodology) remains open. No DGE-METRIC-specific formula exists. Content for Training Day 5 morning is drafted using the conceptual policy-question framing plus the existing `ToyModelSOEMC` break-even/Monte-Carlo methodology, explicitly labeled as an illustrative proxy pending a DGE-METRIC production-network run — per `../CLAUDE.md` "Optimal reserve requirement rules". See [[reserve-requirement-content-approach]].
- Item 1 (on-site Day 3 delivery status), item 3 (hands-on repository access), item 4 (finance assumptions beyond the six-scenario matrix), and item 5 (schedule/dates/time zone) remain open and are flagged inline in the drafted content as `[SME REVIEW NEEDED]` or explicit open questions.

**Action taken:** Drafted full lesson content (lesson, facilitator guide, exercise, expected outputs, and session-specific templates) for all five sessions, plus scenario/pathway logs and templates. Content is grounded in the sources listed in `curriculum-map.md`, `../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`, `../../06_HandsOn_Materials/Day3/`, `../../../DGE-METRIC-VietNam/docs/`, and `../../../Toy Model SOE MC/`.
