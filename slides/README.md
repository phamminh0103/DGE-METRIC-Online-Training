\
# Slide Decks

Facilitator slide decks for the three online training days, one `.pptx` per day. Branding (GIZ red, logo) follows `../../def.tex`'s GIZ color scheme so the decks read consistently with the on-site `Day 3` deck.

## Files

- [DGE-METRIC_Online_Day1_Slides.pptx](DGE-METRIC_Online_Day1_Slides.pptx) — Online Day 1 (Wed 22 Jul 2026, afternoon only, 1 session — finance & energy-efficiency scenario definition, 13 slides). Opens with a setup check-in (VS Code, GitHub, AI coding assistant) — see `../outreach/setup-guide.md` for the full step-by-step version **[Added 2026-07-14]**.
- [DGE-METRIC_Online_Day2_Slides.pptx](DGE-METRIC_Online_Day2_Slides.pptx) — Online Day 2 (Thu 23 Jul 2026, AM calibration/scenario hands-on + PM reserve requirements method & implementation, 2 sessions, 20 slides)
- [DGE-METRIC_Online_Day3_Slides.pptx](DGE-METRIC_Online_Day3_Slides.pptx) — Online Day 3 (Fri 24 Jul 2026, AM guided open lab + PM calibration modification & sensitivity analysis + course close, 2 sessions, 19 slides)

**Rebuilt 2026-07-13** for the depth-over-breadth curriculum restructuring — see [`../design/decision-log.md`](../design/decision-log.md). Each deck follows the block-by-block trainer-flow timing in the matching `../content/*/facilitator-guide.md` (durations sum to 180 min per session, including breaks) and the source-grounded content in the matching `lesson.md` files. Slide content is a condensed, presentation-ready version of that material — it does not introduce any fact, number, or assumption not already present in those source files.

**Reserve-requirement caveat (now Day 2 PM and Day 3 AM):** per `../../CLAUDE.md` ("Optimal reserve requirement rules"), each deck states up front — on a prominent callout slide — that the reserve-requirement numbers come from a separate illustrative toy model, not DGE-METRIC, and that DGE-METRIC's own reserve-requirement analysis has not yet been built. Do not remove or soften these slides.

## Regenerating

Decks are generated from Python (`python-pptx`), not hand-edited. To regenerate after editing a `lesson.md`/`facilitator-guide.md` source file, update the corresponding content in `build/build_dayN.py` and re-run:

```
cd build
python build_day1.py
python build_day2.py
python build_day3.py
```

- [build/slidekit.py](build/slidekit.py) — shared slide-layout helpers (title slide, section divider, bullets, table, two-column, warning callout), GIZ color constants, and the GIZ logo path.
- [build/build_day1.py](build/build_day1.py), [build/build_day2.py](build/build_day2.py), [build/build_day3.py](build/build_day3.py) — per-day slide content and generation script.

Requires `python-pptx` (`pip install python-pptx`) and Pillow (already a transitive dependency). The GIZ logo is read from `../../pictures/GIZ_Logo.png`, resolved relative to `slidekit.py`'s own location (fixed 2026-07-14 — was previously a hardcoded absolute path from another machine, which broke the build here).

## Status

Rebuilt 2026-07-13 for the depth-over-breadth curriculum restructuring. Clock time/time zone for each day are still unconfirmed (see `../qa/sme-questions.md` item 5) — title slides show duration in minutes, not clock times, consistent with the outreach agenda documents.

**2026-07-14:** Day 1 deck updated with the new setup check-in (see `../design/decision-log.md`) — added a poll slide and a setup-quick-reference slide (Blocks/slides 3–4), renumbered the agenda table and all later block kickers. Day 1 is now 13 slides.
