\
# Training Day 3 (Online Day 1) — Afternoon: Finance & Energy-Efficiency Scenarios — Detailed Definition

**Date: Wednesday 22 July 2026.** Status: approved for delivery. **Restructured 2026-07-13** — see [`../../../design/decision-log.md`](../../../design/decision-log.md). This session absorbs and elevates content previously split across the old Day 1 PM (finance) and Day 2 PM (energy-efficiency, as one of three pathways) sessions. Codebase navigation and Git/GitHub Desktop, previously taught here, moved to Online Day 2 AM.

**Revised 2026-07-14** — see decision-log 2026-07-14 entries: the session now opens with a 10-minute setup check-in (VS Code, GitHub, an AI coding assistant), and installing those three tools moved from "Day 2 AM, from scratch" to a prerequisite confirmed before today. "Welcome, recap" and "Why financing design matters" were each trimmed by 5 minutes to make room. Full participant-facing install steps are in [`../../../outreach/setup-guide.md`](../../../outreach/setup-guide.md).

## 1. Session purpose

Define, in full detail, the six-scenario finance matrix and the energy-efficiency/demand-side-management scenario — the two scenario families Online Day 2 morning runs and interprets hands-on. This is a prep/design session: no model run happens today.

## 2. Prerequisites from the previous on-site training

- Repository access to `DGE-METRIC-VietNam` (or the shared copy used for this cohort).
- Prior exposure to `docs/index.md` and `docs/running.md`.
- Prior exposure to repository navigation, the calibration workflow, and generic scenario design, per [`../../../../Day 3/DGE_METRIC_Training_Day3_Session_Plan.md`](../../../../Day%203/DGE_METRIC_Training_Day3_Session_Plan.md) Sessions 2–3, 5.

`[SME REVIEW NEEDED: confirm whether the in-person "Day 3" session was already delivered to this specific cohort — see `../../../qa/sme-questions.md` item 1]`.

## 3. Learning objectives

By the end of this session, participants can:

1. **[Added 2026-07-14]** Confirm VS Code, a GitHub account, and an AI coding assistant are installed/enabled — a setup check-in, not instruction in using them.
2. Explain why financing design (interest rate, revenue recycling) is a first-order determinant of transition speed and cost, independent of the emissions pathway chosen.
3. Read and fully document the six-scenario finance matrix to be run tomorrow morning.
4. Explain the energy-efficiency/DSM scenario's narrative, core modeling channels, and quantified savings/investment figures.
5. Draft a complete scenario metadata block, per `../../../CLAUDE.md` "Scenario design rules," for both a finance scenario and the efficiency scenario.

## 4. Recap / bridge from the previous session

### 4.0 Setup check-in (10 min) — [Added 2026-07-14]

Before the recap: a quick poll, not a teaching block.

- **VS Code** installed and opens.
- **GitHub** account exists (GitHub Desktop installed too, if participants got to it).
- An **AI coding assistant** is enabled in VS Code — Claude Code, GitHub Copilot, or another LLM coding assistant.

Anyone not ready pairs with a neighbor, gets pointed to the quick-install steps, and flags the facilitator — gaps get fixed in the first break, not live in front of the group. Full step-by-step instructions (including how to enable Claude Code or GitHub Copilot, and how to optionally add MATLAB `.m`-file support to VS Code) are in [`../../../outreach/setup-guide.md`](../../../outreach/setup-guide.md) — participants should have worked through it before today. Full Git/GitHub Desktop and VS Code *usage* is still taught from scratch on Online Day 2 AM; this check-in only confirms the tools are present and open.

Rapid recap (5 minutes), drawing on Day 3 plan Sessions 1–2:

- Days 1–2 (or in-person Day 3, if already delivered): policy interpretation of DGE-METRIC outputs and core model mechanics.
- Where these assumptions live in the repository: `docs/financing_pathway.md`, `docs/energy_efficiency_pathway.md`, `ExcelFiles/`. Full codebase navigation and Git/GitHub Desktop are taught tomorrow morning (Online Day 2 AM), immediately before they're used hands-on — not repeated here.

## 5. Conceptual explanation

### 5.1 Why financing design matters

Source-grounded in [`docs/financing_pathway.md`](../../../../../DGE-METRIC-VietNam/docs/financing_pathway.md):

1. **Affordability of public investment** — lower borrowing rates reduce the debt-service burden of transition investment.
2. **Investment crowd-in** — recycling emission-tax revenue into renewable capital can fund additional capacity without new borrowing.
3. **Policy credibility** — transparent, pre-announced financing rules improve implementation certainty for investors.

### 5.2 The finance-scenario matrix, in full detail

Baseline facts (do not alter without SME/user confirmation):

| Indicator | Value | Source |
|---|---:|---|
| Public investment financing rate (baseline) | 8% | `financing_pathway.md` |
| Concessional financing shock | −3 percentage points (effective 5%) | `financing_pathway.md` |
| Revenue-recycling baseline | None (emission-tax revenue not earmarked) | `financing_pathway.md` |
| Revenue-recycling variant | Cap-and-trade revenue fully redirected to renewable capital subsidy: τ^{K,F}_Renewable,t = Rev^{C&T}_t | `financing_pathway.md` |

Six-scenario matrix to be run and compared tomorrow morning:

| Scenario ID | Emissions pathway | Public financing rate | Revenue recycling |
|---|---|---:|---|
| PDP8-Base | PDP8 | 8% | No |
| NZ-Base | Net Zero | 8% | No |
| PDP8-Concessional | PDP8 | 5% | No |
| NZ-Concessional | Net Zero | 5% | No |
| PDP8-Recycle | PDP8 | 8% | Yes |
| NZ-Recycle | Net Zero | 8% | Yes |

Comparison principle: concessional and recycling variants are each compared against the base case **with the same emissions pathway** (do not cross-compare PDP8-Concessional against NZ-Base). Cross-pathway comparison (PDP8 vs. NZ) is a separate, secondary question.

### 5.3 The energy-efficiency & demand-side-management scenario, in full detail

Source-grounded in [`docs/energy_efficiency_pathway.md`](../../../../../DGE-METRIC-VietNam/docs/energy_efficiency_pathway.md):

- **Narrative**: prioritized efficiency gains in industry and transport, plus demand-side management (DSM) that flattens peak loads and slows total electricity demand growth, lowering system costs and fuel import needs.
- **Core modeling channels**: lower energy intensity of production; reduced peak electricity demand; slower final-energy demand growth; lower fossil-fuel and electricity imports.
- **Key assumptions and required inputs**: sector-specific efficiency gains (industry, transport) mapped to energy input coefficients; DSM load-shifting assumptions and their effect on required generation capacity; investment costs and who bears them; fuel-import elasticity with respect to electricity demand; explicit rebound-effect assumption (none, or partial).
- **Quantified potential**: 2030 savings potential ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households; quantified annual investment need ≈USD 361 million/year (≈0.076% of 2024 GDP, USD 476.3 bn). A rebound effect is documented: higher efficiency raises productivity and GDP, and the resulting extra activity partly offsets direct energy savings.
- **Reference trajectory**: compared against the PDP8 baseline — front-loaded, investment-driven decarbonization; renewable share rising to ~80–90% by mid-century.

## 6. Hands-on task (paper/worksheet — no model run today)

See [`exercise.md`](exercise.md) for full instructions. In brief:

1. Group task: read the six-scenario finance matrix and draft a complete scenario metadata sheet for your assigned scenario, using [`scenario-template.md`](scenario-template.md).
2. Group task: draft a complete scenario metadata sheet for the energy-efficiency scenario, using [`efficiency-scenario-template.md`](efficiency-scenario-template.md), covering mechanism, sector-specific assumptions, affected sectors, time path, expected effects, indicators, caveats.

## 7. Expected output

See [`expected-outputs.md`](expected-outputs.md). Participants leave with:

- A completed finance-scenario metadata sheet for their assigned scenario.
- A completed energy-efficiency scenario metadata sheet.

## 8. Debrief questions

- For your assigned finance scenario, what is the single variable that changes relative to its base case, and why does isolating one variable at a time matter for interpretation?
- What is the rebound effect in the energy-efficiency scenario, and why does it matter for interpreting tomorrow's results?
- Which indicators would distinguish a "financing effect" from an "efficiency effect" if both scenarios moved GDP in the same direction?

## 9. Common errors and troubleshooting

- **Confusing "baseline" with "PDP8-Base"**: the emissions-pathway baseline (PDP8) and the finance baseline (8%, no recycling) are two different things — PDP8-Base is baseline on *both* dimensions.
- **Comparing across emissions pathways by mistake**: concessional/recycling variants are compared within the same emissions pathway only.
- **Treating financing rate and revenue recycling as substitutes**: they are separate, independently switchable levers in the matrix, not alternative labels for the same mechanism.
- **Leaving the rebound effect out of the efficiency scenario's expected-effects field**: the source documents it explicitly; omitting it overstates the scenario's net energy savings.
- **Inventing a number not in the source documents**: mark it `[SME REVIEW NEEDED: ...]` instead — this applies equally to the finance matrix and the efficiency scenario.

## 10. Documentation or reporting task

Each participant/group records, in the relevant scenario log:

- Finance scenario: scenario ID, emissions pathway, financing-rate/recycling setting, one-sentence expected mechanism — in [`../../../scenarios/finance/scenario-log.md`](../../../scenarios/finance/scenario-log.md).
- Efficiency scenario: the full metadata block — in [`../../../scenarios/energy-efficiency/efficiency-scenario-log.md`](../../../scenarios/energy-efficiency/efficiency-scenario-log.md).

## 11. Preparation for the next session

Online Day 2 morning runs the baseline calibration, then runs and interprets both the finance matrix and the energy-efficiency scenario hands-on (GDP, investment, fiscal, emissions, and efficiency-specific effects). Participants should arrive with both completed metadata sheets.
