---
title: "Vietnam Energy-Transition Scenarios: A Short Guide for Policy Readers"
subtitle: "Distilled from DGE-METRIC Technical Report, Section 6 — Scenario Design Framework"
---

# Vietnam Energy-Transition Scenarios: A Short Guide for Policy Readers

*Distilled from DGE-METRIC Technical Report, Section 6 — Scenario Design Framework.
This brief is written for a policy audience: no equations, no code variable names.*

## Why there is a family of scenarios, not just one

Every scenario in this study starts from the same place: a policy-consistent baseline built
around Vietnam's 8th Power Development Plan (PDP8). From that common starting point, three
separate questions are asked, each answered by its own branch of scenarios:

1. **What if emissions were capped outright?** — the Net-Zero branch.
2. **What if households and firms used less energy per unit of output?** — the Energy
   Efficiency branch.
3. **What if the cost of financing clean-energy investment were lower — or higher?** — the
   Green Finance branch.

Because every scenario shares the same starting calibration and the same underlying economy,
any difference in outcomes between two scenarios can be attributed to the specific policy change
being tested, not to some other hidden difference in assumptions.

## Branch 1 — Net-Zero: how much does fuel-switching and efficiency actually save?

The Net-Zero scenario puts a binding, economy-wide limit on emissions, enforced through a
carbon-pricing mechanism. On its own, that only says emissions come down — it does not say
*how*. To find out, two stripped-down variants are run alongside it:

- One that removes the ability of industries to become cleaner per unit of fuel burned.
- One that removes both that *and* the ability to use energy more efficiently overall.

Comparing all three tells a simple story: if fuel-switching and efficiency gains were *not*
available, how much more would have to be done through carbon pricing, restructuring which
sectors produce what, and faster renewable buildout? Read together, the three Net-Zero variants
give a ceiling on how costly the transition could be if technology cooperated less than assumed.

## Branch 2 — Energy Efficiency: what if demand for energy simply fell?

This branch layers efficiency and rooftop-solar assumptions on top of the PDP8 baseline —
industry and services becoming more efficient, more distributed rooftop solar, and battery
storage to make use of it. Several named variants (aligned to different policy programs, e.g.
Directive 10) and a "no battery storage" counterfactual for each let readers see how much of the
benefit depends specifically on storage being deployed alongside solar, versus efficiency gains
on their own.

## Branch 3 — Green Finance: what does cheaper capital buy?

Concessional loans, blended finance, green bonds, and guarantees are not modeled item by item.
Instead they are represented the way they show up in a firm's investment decision: a lower cost
of capital, a lower price for new energy-capital goods, and a larger volume of public investment.
Three financing "architectures" are compared:

| Architecture | Description | Weighted average cost of finance |
|---|---|---|
| Balanced (GF_A) | Mixed public/private financing | 6.43% |
| Market-led (GF_B) | Private capital does more of the work | 7.37% |
| Public-led (GF_C) | Public/concessional capital does more of the work | 5.07% |

Each is tested against both the PDP8 baseline and the Net-Zero cap, so readers can see the
financing effect on its own and combined with a binding emissions constraint.

**A caveat worth repeating in any briefing:** these results show what a financing architecture
*could* achieve if fully and smoothly deployed at the assumed cost. The model cannot verify
whether the underlying interest-rate reductions are realistic or institutionally achievable at
that scale — that judgment belongs to finance-sector experts, not to the model.

## A caveat about which scenarios you're actually looking at

Not every scenario described in the technical documentation is switched on by default when the
model is run. Some are fully built and ready but simply excluded from the default run list;
others are still individually commented out. Before citing a specific number in front of a
minister or donor, always confirm which exact scenario configuration produced it — "the model
shows a scenario exists" is not the same claim as "the model was run and produced this number."

## How to read the comparison charts

Figures accompanying this brief show *deviation from the Baseline*, not the raw scenario path
itself, usually averaged over five-year blocks (2026–2030, 2031–2035, and so on). A negative bar
on an energy-intensity chart means energy use per unit of output *improved* relative to Baseline;
a positive bar on a GDP-share chart means that category grew *larger* as a share of the economy
than it would have under Baseline alone. Always read the axis label and the sign before drawing a
conclusion from the shape of a bar.

---

*Source: DGE-METRIC Technical Report, Section 6 ("Scenario Design Framework"),
`docs/reports/TECHNICAL_REPORT.md` in the DGE-METRIC repository. This document is a simplified
derivative for training purposes and is not a substitute for the technical report.*
