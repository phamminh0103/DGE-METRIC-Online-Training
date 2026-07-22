# Policy Report Exercise — From Scenario Output to a Council-Ready Brief (Copilot Edition)

A hands-on exercise in **VS Code + GitHub Copilot**, built on Section 6 of the DGE-METRIC Technical Report. 

You will (1) generate a small MATLAB script that produces two comparison figures from real model output, (2) turn those figures into a short written policy brief, and (3) package the whole recipe as a reusable Copilot **prompt file** so the next scenario pair takes minutes, not an hour.

Prerequisite: Copilot and Copilot Chat installed and signed in — see
[worksheets/setup/GitHub_Copilot_Setup_Guide.md](../worksheets/setup/GitHub_Copilot_Setup_Guide.md)
if you haven't done this yet.

Target style: [docs/policy_report_brief.md](policy_report_brief.md) /
[docs/policy_report_brief.docx](policy_report_brief.docx) — a distilled, non-technical version of
Section 6. Skim it now; you'll be asked to match its tone in Part 3.

## Learning objectives

By the end of this exercise you should be able to:

1. Choose the right Copilot **mode** (Ask vs. Edit vs. Agent) for a given step of a reporting task.
2. Turn a plotting spec into a working MATLAB script by prompting Copilot with the *right context*, not just a bare request.
3. Verify AI-generated code and AI-generated prose against ground truth instead of trusting it by default.
4. Translate model internals into policy language a non-technical reader can act on.
5. Package a multi-step workflow as a reusable Copilot **prompt file** — the closest Copilot equivalent to a saved "skill" — and explain how that differs from an always-on custom instructions file.

## Setup: what you're working with

- Scenario output already exists for this exercise — you do not need to run MATLAB/Dynare
  simulations first. Confirm these two files are present:
  `ExcelFiles/Output/Baseline.csv` and `ExcelFiles/Output/EE_Directive10.csv`.
- Existing script to read (not copy) for conventions:`scripts/reporting/GenerateEESimulationResultsFigures.m`.
- Output figures go in `docs/figures/` (create a scenario-named subfolder, following the existing `EE_Simulation_Results/` / `Finance_Simulation_Results/` pattern).
- Repository rules Copilot should already be following automatically in this repo: `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` — all three say the same thing: never hand-edit generated Dynare output, keep source edits inside `ModFiles/`, `Functions/`, `scripts/`, `docs/`, and input workbooks under `ExcelFiles/`.

## Part 1 — Ask mode: orient yourself before you generate anything

**Concept:** Copilot Chat's **Ask** mode is read-only — it answers questions and reads whatever files you point it at, but does not edit anything. Use it first, always, on unfamiliar code: it's cheaper to be wrong in chat than in a file.

### Try it yourself

Open `scripts/reporting/GenerateEESimulationResultsFigures.m` in the editor, open Copilot Chat, switch to **Ask** mode, and reference the open file (in most Copilot Chat versions this is automatic for the active editor tab, or use `#file` / `#codebase` depending on your version).
Prompt:

> Explain what CSV columns this script requires, what one figure of its output represents, and
> what "5-year block" means in its deviation charts.

**Verification, not just acceptance:** Copilot's answer should match what you read directly in the script (`requiredVars` near the top, and the `five_year_deviation_blocks` helper near the bottom). If it doesn't — for instance if it invents a column that isn't in `requiredVars` — that's a live example of why Part 5 of this exercise insists on checking AI output against source, not against how confident it sounds.

## Part 2 — Agent mode: generate a new plotting script

**Concept:** Copilot Chat's **Agent** mode can read multiple files, run terminal commands, and iterate on its own output across several turns — appropriate here because the task needs to inspect a CSV's actual columns, write a script, and likely fix a runtime error. Ask mode alone cannot run MATLAB for you.

### Task

Switch to **Agent** mode. Ask Copilot to create a new script,
`scripts/reporting/GeneratePolicyBriefFigures.m`, that:

- Reads `ExcelFiles/Output/Baseline.csv` and `ExcelFiles/Output/EE_Directive10.csv`.
- Produces exactly two figures, saved as both `.png` and `.svg` to
  `docs/figures/Policy_Brief_Exercise/`:
  1. GDP level deviation of EE_Directive10 vs. Baseline, 5-year block averages (percent).
  2. Energy intensity deviation of EE_Directive10 vs. Baseline, 5-year block averages (index-point deviation; negative = improved efficiency — same sign convention as Figure 6.1 in the technical report).
- Follows the conventions already used in`GenerateEESimulationResultsFigures.m`: error out (not silently skip) if a required CSV or column is missing; use the repo root resolved from `mfilename`, not a hardcoded path; call `setup_paths()` before anything else.

A prompt template to adapt (fill in the blanks, don't paste it verbatim — writing your own sentences around it is part of the exercise):

```
Using scripts/reporting/GenerateEESimulationResultsFigures.m as the style reference for
structure, error-handling, and figure formatting, write a new script
scripts/reporting/GeneratePolicyBriefFigures.m that produces exactly two figures for
Baseline vs EE_Directive10: [figure 1 spec], [figure 2 spec]. Save PNG and SVG to
docs/figures/Policy_Brief_Exercise/. Reuse the same five-year-block bar-chart helpers if
they can be reused as-is; otherwise explain what you had to change and why.
```

### Run it and verify

Run the script in MATLAB. Then check, without just trusting the run succeeded:

- [ ] Do both figures actually appear in `docs/figures/Policy_Brief_Exercise/`?
- [ ] Does the GDP figure's sign match what you'd expect (Directive 10 should show *some* nonzero deviation, not a flat line — a flat line usually means a column was read wrong)?
- [ ] Did Copilot's script duplicate the whole file, or actually reuse the existing helper
  functions where it said it would? Open the diff/generated file and check — this is the single most-skipped verification step, and the one most likely to hide a stale copy of a helper that quietly diverges from the original next time someone edits it.

## Part 3 — Turning plots into a written brief

**Concept:** the same assistant, a different job: translating model internals into policy
language. This is an Edit/Ask-mode task, not an Agent-mode one — you're producing prose, not running code.

### Task

With both new figures open (or their file paths given to Copilot as context), and
`docs/policy_report_brief.md` open as a style reference, prompt Copilot to draft a
roughly 250-word section extending that brief with a new subsection covering your two figures — matching its tone (no `exo_...` variable names, no equations, plain policy language) and its convention of stating the sign/read-direction of each chart explicitly.

### Verify before you accept it

- [ ] Every specific number or direction claimed in the draft ("X improved by roughly Y") — can you trace it back to the actual bar heights in your two figures? Check at least two sentences by eye.
- [ ] Does the draft accidentally reintroduce a variable name or equation, breaking the "no code internals" style of the target brief?
- [ ] Does it repeat the operational-status caveat from `policy_report_brief.md` (a scenario being documented isn't the same as it being the one that was actually run) where relevant, or does it overstate certainty?

## Part 4 — Packaging the recipe as a reusable "skill"

**Concept — Copilot's answer to a saved "skill":** GitHub Copilot doesn't call this feature "Skills," but it has a direct equivalent: a **prompt file**
(`.github/prompts/<name>.prompt.md`), a saved, reusable instruction set you invoke on demand (typically by typing `/<name>` in Copilot Chat) instead of retyping the whole Part 2 + Part 3 spec every time you want a brief for a *different* scenario pair. This is a different mechanism from `.github/copilot-instructions.md`, which this repository already has:

|                 | `.github/copilot-instructions.md`                                         | `.github/prompts/*.prompt.md`                                 |
| --------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| When it applies | Automatically, on every Copilot request in this repo                        | Only when you invoke it by name                                 |
| What it's for   | Always-on background rules (e.g. "never hand-edit generated Dynare output") | An on-demand, parameterized recipe for a specific repeated task |
| Analogy         | House rules                                                                 | A named macro/shortcut                                          |

### Task

Create `.github/prompts/policy-brief.prompt.md` (in the `DGE-METRIC` repo, on a branch or your own fork — do not commit directly to `main`) that captures the Part 2 + Part 3 recipe as a template, with the scenario names, output subfolder, and figure specs left as placeholders the next user fills in. Test it by invoking it for a *different* scenario pair than the one you just did by hand (e.g. `Baseline` vs. `EE_PDP8_PV_BESS_NoBESS`) and confirm it produces figures + draft prose with noticeably less back-and-forth than Parts 2–3 took the first time.

## Self-check questions

1. Why does Part 1 use Ask mode and Part 2 use Agent mode — what would go wrong (or just not work) if you swapped them?
2. What's one thing you found in verification (Parts 2 or 3) that Copilot got subtly wrong or invented? If nothing did, what specifically did you check to be sure?
3. What's the practical difference between putting a rule in `copilot-instructions.md` versus a
   `prompt.md` file — if you wanted "always translate `exo_` variable names to plain language in any policy-facing prose," which one would you add it to, and why?
4. Section 6.4 of the technical report warns that a scenario being defined doesn't mean it's switched on by default. Where in this exercise did that caveat actually matter — could you have cited a scenario result that was never produced by the current default run configuration?

## One-paragraph summary

Turning model output into a policy-ready brief is a three-step pipeline — orient (Ask mode), build (Agent mode), and translate (Ask/Edit mode) — and every step needs a verification check that does not depend on how confident the AI's output sounds: cross-reference the script against the CSV it reads, cross-reference the prose against the figure it describes. Once the recipe works once, a Copilot **prompt file** turns it into a reusable, named shortcut — the practical equivalent of a saved "skill" — kept separate from the repo's always-on `copilot-instructions.md` rules, which apply automatically rather than on request.
