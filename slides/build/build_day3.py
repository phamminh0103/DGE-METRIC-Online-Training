import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidekit as sk

DECK = "DGE-METRIC Online Training — Online Day 3 — Fri 24 Jul 2026"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "DGE-METRIC_Online_Day3_Slides.pptx")

prs = sk.new_deck()
n = [0]
def pn():
    n[0] += 1
    return n[0]

sk.title_slide(
    prs,
    "DGE-METRIC Online Training",
    "Online Day 3 — Guided Open Lab, then Calibration Internals: Modification & Sensitivity Analysis",
    [
        "Friday 24 July 2026 · Morning + Afternoon · 2 × 180 minutes",
        "GIZ Vietnam | DGE-METRIC Program | Online Module",
        "This is Training Day 5, delivered online — the final day of the course",
    ],
)
pn()

# ============ MORNING SESSION ============
sk.section_slide(prs, "Online Day 3 — Morning", "Guided Open Lab",
                  "Applying the reserve-requirement method · 180 minutes")

sk.table_slide(
    prs, "This Morning's Agenda — 5 Blocks, 180 Minutes (+1 break)", ["Block", "Min", "What happens"],
    [
        ["1. Recap method and implementation plan", "15", "Recap yesterday's MC = MB logic and your implementation plan; confirm chosen carrier"],
        ["2. Guided open lab, part 1", "90", "Work the break-even and validation logic by hand for your chosen carrier"],
        ["— Break —", "15", ""],
        ["3. Guided open lab, part 2 — write it up", "45", "Finish your reserve-requirement analysis note: inputs, walkthrough, sensitivity, open items"],
        ["4. Report-out and debrief", "15", "Fast report-out across groups"],
    ],
    col_widths=[3.6, 0.8, 5.1], page_no=pn(), deck_label=DECK,
)

sk.warning_slide(
    prs, "Before We Start: Restate the Scope Note",
    "Today's numbers come from a separate illustrative toy model, not from DGE-METRIC.",
    [
        ("DGE-METRIC's own reserve-requirement analysis has not yet been built — no new conceptual content today, this is guided practice", 0, False),
        ("If asked for \"the\" optimal reserve number for Vietnam: restate this caveat rather than answering with a toy-model figure as if it were final", 0, True),
    ], kicker="Block 1", page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Recap: Method and Implementation Plan", kicker="Block 1 · 15 min",
    items=[
        ("Yesterday afternoon: the three-step MC = MB methodology (screen → validate → optimize) using illustrative Toy Model SOE MC numbers", 0, False),
        ("Baseline GDP (2024) USD 430,000m; crisis probability p = 0.04/yr; break-even divisor USD 172.0m", 0, False),
        ("Your group's implementation plan: chosen carrier, mechanism, DGE-METRIC outputs needed, codebase location", 0, False),
        ("Today: no new concepts — apply this by hand, in full, for your carrier", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Guided Open Lab — Work the Logic by Hand", kicker="Block 2 · 90 min",
    items=[
        ("Confirm: Break-even GDP loss % ≈ Annual cost ÷ 172.0 for your carrier", 0, False),
        ("Confirm the Step-2 verdict (justified / marginal / not justified) at 20% and 50% shock sizes", 0, False),
        ("If you have a Day 2 AM efficiency-scenario comparison: would it increase or decrease exposure to disruption in your carrier?", 0, False),
        ("List two DGE-METRIC outputs that would be needed to redo Steps 1–2 properly, once a reserve module exists", 0, False),
        ("Sensitivity: roughly how much larger would crisis probability or shock size need to be for the verdict to flip?", 0, False),
        ("Facilitator circulates rather than presenting one worked example — multiple carriers are in play at once", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.section_slide(prs, "Short break", "15 minutes", "Next: write up the full analysis note")

sk.bullets_slide(
    prs, "Write Up Your Reserve-Requirement Analysis Note", kicker="Block 3 · 45 min",
    items=[
        ("Combine: yesterday's implementation plan (mechanism, DGE-METRIC outputs, codebase location) + today's completed MC = MB walkthrough", 0, False),
        ("Add: an explicit list of what is still [SME REVIEW NEEDED] before this could inform an actual decision", 0, False),
        ("Every specific number must be labeled as an illustrative Toy Model SOE MC proxy result, not a DGE-METRIC output", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "This Morning's Output & Debrief", kicker="Block 4 · 15 min",
    items=[
        ("You leave with: one completed reserve-requirement analysis note per group, for your chosen carrier", 0, False),
        ("Debrief: in your own words, what does MC = MB mean for a strategic reserve, using your carrier as an example?", 0, False),
        ("Debrief: why does the source material insist on calling the Step 2 \"not justified\" results illustrative rather than final?", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# ============ AFTERNOON SESSION ============
sk.section_slide(prs, "Online Day 3 — Afternoon", "Calibration Internals",
                  "Modification & sensitivity analysis, + course close · 180 minutes")

sk.table_slide(
    prs, "This Afternoon's Agenda — 7 Blocks, 180 Minutes (+1 break)", ["Block", "Min", "What happens"],
    [
        ["1. Recap calibration workflow", "10", "Brief course-arc recap; why accounting coherence is the precondition for everything"],
        ["2. Calibration internals", "30", "Data inputs vs. structural parameters; workbook structure; the IO calibration pipeline"],
        ["3. How to modify calibration", "25", "Data-input change (ExcelFiles/) vs. structural-parameter change (Functions/); re-validate"],
        ["— Break —", "15", ""],
        ["4. Sensitivity analysis method", "30", "One-at-a-time parameter perturbation; why isolating one parameter matters"],
        ["5. Draft sensitivity-analysis plan", "30", "Groups pick one structural parameter and draft a plan"],
        ["6. Report-out", "10", "Fast report-out across groups"],
        ["7. Course close", "30", "Independent-use checklist; exit ticket"],
    ],
    col_widths=[3.4, 0.8, 5.3], page_no=pn(), deck_label=DECK,
)

sk.table_slide(
    prs, "The Course Arc", ["Day", "Focus", "What it produced"],
    [
        ["Day 1 PM", "Finance & efficiency scenario definition", "Two completed scenario metadata sheets"],
        ["Day 2 AM", "Codebase nav, Git, calibration & scenario hands-on", "Calibration diagnostic; finance + efficiency comparison charts"],
        ["Day 2 PM", "Reserve requirements — method & implementation", "Implementation plan for a self-chosen carrier"],
        ["Day 3 AM", "Guided open lab", "Completed reserve-requirement analysis note"],
    ],
    col_widths=[1.4, 3.6, 4.4], kicker="Block 1 · 10 min", page_no=pn(), deck_label=DECK, font_size=13,
    note="Today closes the loop back to calibration — the foundation everything else this week depended on.",
)

sk.bullets_slide(
    prs, "Calibration Internals", kicker="Block 2 · 30 min",
    items=[
        ("Data inputs pinning down the steady state: sectoral employment, value-added, labour cost, export, import, emission shares", 0, False),
        ("Structural parameters: discount factor, depreciation, elasticities of substitution, tax rates, adjustment costs", 0, False),
        ("Calibration credibility rests on accounting coherence — value-added shares, intermediate-input shares, and import decomposition must sum consistently", 0, True),
        ("The IO calibration pipeline: run_pipeline.m → split_utilities_sector.m → aggregate_for_dge.m, with validation/audit CSV outputs", 0, False),
        ("Quality checks: output conservation, import conservation, value-added consistency, non-negativity", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "How to Modify Calibration", kicker="Block 3 · 25 min",
    items=[
        ("Changing a data input (e.g. a sectoral value-added share): edit the calibration workbook in ExcelFiles/, then re-run the pipeline and re-check validation/audit outputs", 0, False),
        ("Changing a structural parameter (e.g. an elasticity of substitution): typically set via a Functions/ helper or a named range in the workbook — confirm the exact location before editing", 0, False),
        ("Either change requires re-running the full calibration-to-baseline chain and re-validating accounting coherence", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.section_slide(prs, "Short break", "15 minutes", "Next: sensitivity analysis method")

sk.bullets_slide(
    prs, "Sensitivity Analysis Method", kicker="Block 4 · 30 min",
    items=[
        ("One-at-a-time (OAT) parameter perturbation: pick one structural parameter, perturb it by a defined amount, re-run, compare against the unperturbed baseline", 0, False),
        ("Why isolate one parameter at a time: perturbing two at once means you can't attribute the output change to either individually", 0, True),
        ("What to check: the same accounting-coherence diagnostics, plus the output indicators most likely to respond to your chosen parameter", 0, False),
        ("Keep a sensitivity log: parameter, baseline value, perturbed value, diagnostic result, output difference", 0, False),
        ("General good-practice methodology — not itself a DGE-METRIC-specific procedure documented in the reviewed sources", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Draft Your Sensitivity-Analysis Plan", kicker="Blocks 5–6 · 40 min",
    items=[
        ("Pick one structural parameter from docs/calibration.md's list", 0, False),
        ("Document: parameter and baseline value (or [SME REVIEW NEEDED]); the perturbation and why it's reasonable; expected effect with a mechanism, not just \"it will change\"; accounting-coherence checks you'd re-run", 0, False),
        ("Only one parameter perturbed — not a combination", 0, True),
        ("Fast report-out across groups", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Course Close", kicker="Block 7 · 30 min",
    items=[
        ("Independent-use checklist — a single combined self-assessment covering calibration/codebase, scenario design, reserve requirements, and reproducibility", 0, False),
        ("Exit ticket — submit in writing:", 0, True),
        ("One calibration insight you'll use going forward", 1, False),
        ("One scenario-design practice you'll keep", 1, False),
        ("One reserve-requirement or policy-analysis habit you'll apply", 1, False),
        ("One remaining question for future support", 1, False),
        ("Open institutional/SME questions are tracked in qa/sme-questions.md for asynchronous follow-up, not worked live here", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# closing
sk.section_slide(prs, "Thank you", "Congratulations on completing DGE-METRIC Online Training",
                  "Questions and independent-use support: course contact to be confirmed")

prs.save(OUT)
print("Saved", OUT, "with", len(prs.slides._sldIdLst), "slides")
