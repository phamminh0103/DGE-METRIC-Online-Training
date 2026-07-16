\
# Style Guide

Applies to all content under `../content/`, `../scenarios/`, and `../activities/`. Derived directly from `../CLAUDE.md` "Accessibility and online-learning rules" and "Source-grounding rules" — this file does not add new rules, it operationalizes existing ones for anyone drafting content.

## Structure

- Every standard session uses the 11-part structure in `../CLAUDE.md` "Training design rules"; the final wrap-up uses the 8-part wrap-up structure instead.
- Use clear headings (numbered, matching the 11-part or 8-part structure) and short sections. Avoid long dense paragraphs.
- Hands-on tasks are step-by-step, numbered, with an explicit deliverable statement at the end.

## Source grounding

- Every numeric claim (parameter value, financing rate, savings potential, cost figure) must cite its source document or be marked `[SME REVIEW NEEDED: describe the missing item]`.
- Follow the source priority order in `../CLAUDE.md`: existing repository files → `source/` documents → approved `design/` files → SME/user instructions → external references (only if explicitly requested and cited).
- Never blend an illustrative/proxy result (e.g. `Toy Model SOE MC` reserve-requirement numbers) with a DGE-METRIC-specific claim without an explicit label distinguishing the two.

## Accessibility

- Provide alt-text-equivalent context for every figure or screenshot reference (a one-line description of what it shows, not just a filename).
- Provide expected outputs (`expected-outputs.md`) for every session so participants can self-check without live facilitator support.
- Include a troubleshooting section ("Common errors and troubleshooting") for every hands-on session.
- Avoid unnecessary animation or visual complexity in any chart or slide asset.
- Design hands-on steps so they remain possible with low bandwidth where feasible (e.g. text-based diagnostics before requiring live video).

## Charts and policy narratives

Every chart: clear title, baseline and scenario labels, units, time period, data source/output file, short note on assumptions. Every narrative: main quantitative result, economic mechanism, policy implication, one caveat, next analytical step. Never hide a caveat.

## Cross-linking

Use relative Markdown links between files (e.g. `../../design/course-brief.md`), consistent with `../CLAUDE.md` "Git and reproducibility rules". Link every session's `README.md` back to `course-brief.md`, `curriculum-map.md`, and its `agenda.md` entry.

## Tone

Write for an audience that already attended the on-site training: skip introductory theory, lead with recap/bridge framing, and focus on applied workflow, interpretation, and reproducibility.
