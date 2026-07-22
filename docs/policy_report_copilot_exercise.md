# Policy Report Exercise — From Scenario Output to a Council-Ready Brief (Copilot Edition)

A hands-on exercise in **VS Code + GitHub Copilot**, built on Section 6 ("Scenario Design
Framework") of the DGE-METRIC Technical Report. Unlike the arithmetic worked problem sets
elsewhere in `docs/`, this exercise is about the *workflow* of using an AI pair-programmer
responsibly on a real reporting task — not about hand calculation.

You will (1) run the model yourself to produce your own scenario output, (2) generate a small
MATLAB script that produces two comparison figures from that output, (3) turn those figures into
a short written policy brief, and (4) package the whole recipe as a reusable Copilot **prompt
file** so the next scenario pair takes minutes, not an hour.

Everything in this exercise uses **your own simulated output** — the figures and the brief you
write are only as good as the run that produced them, and running it yourself is what makes the
verification steps below meaningful rather than an exercise in checking numbers you already know.

Prerequisite: Copilot and Copilot Chat installed and signed in — see
[worksheets/setup/GitHub_Copilot_Setup_Guide.md](../worksheets/setup/GitHub_Copilot_Setup_Guide.md)
if you haven't done this yet.

## Learning objectives

By the end of this exercise you should be able to:

1. Run the model to produce a scenario comparison you will actually use downstream, instead of
   treating simulation output as a given.
2. Choose the right Copilot **mode** (Ask vs. Edit vs. Agent) for a given step of a reporting task.
3. Turn a plotting spec into a working MATLAB script by prompting Copilot with the *right context*,
   not just a bare request.
4. Verify AI-generated code and AI-generated prose against ground truth instead of trusting it by
   default.
5. Translate model internals into policy language a non-technical reader can act on.
6. Package a multi-step workflow as a reusable Copilot **prompt file** — the closest Copilot
   equivalent to a saved "skill" — and explain how that differs from an always-on custom
   instructions file.

## Setup: what you're working with

- Repository/folder: `Code/dge-metric-model` inside *this* training repository — your own local
  copy of the DGE-METRIC model. All paths below are relative to that folder unless stated
  otherwise.
- Governance files already present there for Copilot to read automatically: `AGENTS.md` and
  `.github/copilot-instructions.md` — both say the same thing: never hand-edit generated Dynare
  output, keep source edits inside `ModFiles/`, `Functions/`, `scripts/`, `docs/`, and input
  workbooks under `ExcelFiles/`.
- Reporting-script style reference, already in `scripts/reporting/GenerateEESimulationResultsFigures.m`
  — read it (Part 1), don't copy it wholesale.
- Target prose style: [policy_report_brief.md](policy_report_brief.md) /
  [policy_report_brief.docx](policy_report_brief.docx), in this same `docs/` folder — note this is
  the training repo's top-level `docs/`, not anything inside `Code/dge-metric-model`, since it's
  training material, not model code. Skim it now; you'll be asked to match its tone in Part 3.

### Step 0 — Produce your own scenario output (do this before Part 1)

Nothing in this exercise uses pre-baked results. In MATLAB, with `Code/dge-metric-model` as your
working directory, run:

```matlab
RunSimulations
```

This repo's copy of `RunSimulations.m` is already configured with
`activeScenarioGroups = {'Reference', 'EE'}`, so a single run produces everything this exercise
needs: `ExcelFiles/Output/Baseline.csv`, `EE_Directive10.csv`, `EE_Directive10_NoBESS.csv`, and
`EE_PDP8_PV_BESS_NoBESS.csv`. This will take a while — use the time to read Part 1 and Part 2
below so you know what you're aiming for once it finishes.

Confirm before continuing: do all four CSVs listed above exist under `ExcelFiles/Output/`, and
does `Baseline.csv` have a `Year` column running from 2026 to 2050? If a run errors out partway,
re-check `activeScenarioGroups` wasn't accidentally edited, then re-run.

## Part 1 — Ask mode: orient yourself before you generate anything

**Concept:** Copilot Chat's **Ask** mode is read-only — it answers questions and reads whatever
files you point it at, but does not edit anything. Use it first, always, on unfamiliar code: it's
cheaper to be wrong in chat than in a file.

### Try it yourself

Open `scripts/reporting/GenerateEESimulationResultsFigures.m` in the editor, open Copilot Chat,
switch to **Ask** mode, and reference the open file (in most Copilot Chat versions this is
automatic for the active editor tab, or use `#file` / `#codebase` depending on your version).
Prompt:

> Explain what CSV columns this script requires, what one figure of its output represents, and
> what "5-year block" means in its deviation charts.

**Verification, not just acceptance:** Copilot's answer should match what you read directly in
the script (`requiredVars` near the top, and the `five_year_deviation_blocks` helper near the
bottom). If it doesn't — for instance if it invents a column that isn't in `requiredVars` — that's
a live example of why every part of this exercise insists on checking AI output against source,
not against how confident it sounds.

## Part 2 — Agent mode: generate a new plotting script

**Concept:** Copilot Chat's **Agent** mode can read multiple files, run terminal commands, and
iterate on its own output across several turns — appropriate here because the task needs to
inspect a CSV's actual columns, write a script, and likely fix a runtime error. Ask mode alone
cannot run MATLAB for you.

### Task

Switch to **Agent** mode. Ask Copilot to create a new script,
`scripts/reporting/GeneratePolicyBriefFigures.m`, that:

- Reads `ExcelFiles/Output/Baseline.csv` and `ExcelFiles/Output/EE_Directive10.csv` — the two
  files your own Step 0 run just produced.
- Produces exactly two figures, saved as both `.png` and `.svg` to
  `docs/figures/Policy_Brief_Exercise/` (inside `Code/dge-metric-model`, the same place
  `GenerateEESimulationResultsFigures.m` writes its own output — not the training repo's
  top-level `docs/` where the brief in Setup lives):
  1. GDP level deviation of EE_Directive10 vs. Baseline, 5-year block averages (percent).
  2. Energy intensity deviation of EE_Directive10 vs. Baseline, 5-year block averages
     (index-point deviation; negative = improved efficiency — same sign convention as Figure 6.1
     in the technical report).
- Follows the conventions already used in `GenerateEESimulationResultsFigures.m`: error out (not
  silently skip) if a required CSV or column is missing; use the repo root resolved from
  `mfilename`, not a hardcoded path; call `setup_paths()` before anything else.

A prompt template to adapt (fill in the blanks, don't paste it verbatim — writing your own
sentences around it is part of the exercise):

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

- [ ] Do both figures actually appear in `Code/dge-metric-model/docs/figures/Policy_Brief_Exercise/`?
- [ ] Does the GDP figure's sign match what you'd expect (Directive 10 should show *some*
      nonzero deviation, not a flat line — a flat line usually means a column was read wrong)?
- [ ] Did Copilot's script duplicate the whole file, or actually reuse the existing helper
      functions where it said it would? Open the diff/generated file and check — this is the
      single most-skipped verification step, and the one most likely to hide a stale copy of a
      helper that quietly diverges from the original next time someone edits it.

## Part 3 — Turning plots into a written brief

**Concept:** the same assistant, a different job: translating model internals into policy
language. This is an Edit/Ask-mode task, not an Agent-mode one — you're producing prose, not
running code.

### Task

With both new figures open (or their file paths given to Copilot as context), and the training
repo's top-level [`docs/policy_report_brief.md`](policy_report_brief.md) (not anything inside
`Code/dge-metric-model`) open as a style reference, prompt Copilot to draft a
roughly 250-word section extending that brief with a new subsection covering your two figures —
matching its tone (no `exo_...` variable names, no equations, plain policy language) and its
convention of stating the sign/read-direction of each chart explicitly.

### Verify before you accept it

- [ ] Every specific number or direction claimed in the draft ("X improved by roughly Y") — can
      you trace it back to the actual bar heights in your two figures? Check at least two
      sentences by eye.
- [ ] Does the draft accidentally reintroduce a variable name or equation, breaking the "no code
      internals" style of the target brief?
- [ ] Does it repeat the operational-status caveat from `policy_report_brief.md` (a scenario being
      documented isn't the same as it being the one that was actually run) where relevant, or
      does it overstate certainty?

## Part 4 — Packaging the recipe as a reusable "skill"

**Concept — Copilot's answer to a saved "skill":** GitHub Copilot doesn't call this feature
"Skills," but it has a direct equivalent: a **prompt file**
(`.github/prompts/<name>.prompt.md`), a saved, reusable instruction set you invoke on demand
(typically by typing `/<name>` in Copilot Chat) instead of retyping the whole Part 2 + Part 3
spec every time you want a brief for a *different* scenario pair.

This is a different mechanism from `.github/copilot-instructions.md`, which
`Code/dge-metric-model` already has:

| | `.github/copilot-instructions.md` | `.github/prompts/*.prompt.md` |
|---|---|---|
| When it applies | Automatically, on every Copilot request in this repo | Only when you invoke it by name |
| What it's for | Always-on background rules (e.g. "never hand-edit generated Dynare output") | An on-demand, parameterized recipe for a specific repeated task |
| Analogy | House rules | A named macro/shortcut |

### Task

Create `Code/dge-metric-model/.github/prompts/policy-brief.prompt.md` (on a branch or your own
fork of this training repo — do not commit directly to `main`) that captures the Part 2 + Part 3
recipe as a template, with the scenario names, output subfolder, and figure specs left as
placeholders the next user fills in. Test it by invoking it for a *different* scenario pair than
the one you just did by hand (e.g. `Baseline` vs. `EE_PDP8_PV_BESS_NoBESS` — both already sitting
in your `ExcelFiles/Output/` from Step 0) and confirm it produces figures + draft prose with
noticeably less back-and-forth than Parts 2–3 took the first time.

## Self-check questions

1. Why does Part 1 use Ask mode and Part 2 use Agent mode — what would go wrong (or just not
   work) if you swapped them?
2. What's one thing you found in verification (Parts 2 or 3) that Copilot got subtly wrong or
   invented? If nothing did, what specifically did you check to be sure?
3. What's the practical difference between putting a rule in `copilot-instructions.md` versus a
   `prompt.md` file — if you wanted "always translate `exo_` variable names to plain language in
   any policy-facing prose," which one would you add it to, and why?
4. Section 6.4 of the technical report warns that a scenario being defined doesn't mean it's
   switched on by default. Where in this exercise did that caveat actually matter — could you
   have cited a scenario result that was never produced by the current default run configuration?

## One-paragraph summary

Turning model output into a policy-ready brief is a three-step pipeline — orient (Ask mode),
build (Agent mode), and translate (Ask/Edit mode) — and every step needs a verification check that
does not depend on how confident the AI's output sounds: cross-reference the script against the
CSV it reads, cross-reference the prose against the figure it describes. Once the recipe works
once, a Copilot **prompt file** turns it into a reusable, named shortcut — the practical
equivalent of a saved "skill" — kept separate from the repo's always-on
`copilot-instructions.md` rules, which apply automatically rather than on request.
