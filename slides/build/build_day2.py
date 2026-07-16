import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidekit as sk

DECK = "DGE-METRIC Online Training — Online Day 2 — Thu 23 Jul 2026"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "DGE-METRIC_Online_Day2_Slides.pptx")

prs = sk.new_deck()
n = [0]
def pn():
    n[0] += 1
    return n[0]

# 1. Title
sk.title_slide(
    prs,
    "DGE-METRIC Online Training",
    "Online Day 2 — Calibration & Scenario Hands-On, then Reserve Requirements: Method & Implementation",
    [
        "Thursday 23 July 2026 · Morning + Afternoon · 2 × 180 minutes",
        "GIZ Vietnam | DGE-METRIC Program | Online Module",
        "This is Training Day 4, delivered online",
    ],
)
pn()

# ============ MORNING SESSION ============
sk.section_slide(prs, "Online Day 2 — Morning", "Calibration & Scenario Hands-On",
                  "Codebase navigation, Git/GitHub Desktop, debugging, AI-assisted VS Code · 180 minutes")

sk.table_slide(
    prs, "This Morning's Agenda — 7 Blocks, 180 Minutes", ["Block", "Min", "What happens"],
    [
        ["1. Objective and setup check", "10", "Restate expected outputs; confirm MATLAB/Dynare/paths working"],
        ["2. Codebase nav & version control", "30", "Trace an equation to its helper; clone + first commit in GitHub Desktop; open in VS Code"],
        ["3. Baseline calibration run", "25", "Guided execution; interpret diagnostics as a group"],
        ["4. Debugging common MATLAB/Dynare errors", "20", "Categorize a failure before fixing it; work a broken example together"],
        ["— Break —", "15", ""],
        ["5. Finance + efficiency scenario run, AI-VS Code demo", "35", "Run your finance scenario vs. base case, and the efficiency scenario vs. PDP8; live AI-assistant demo"],
        ["6. Comparison tables, chart & narrative", "35", "Build tables for both scenario families; one chart + 4-sentence narrative"],
        ["7. Report-out and debrief", "10", "Fast report-out across groups"],
    ],
    col_widths=[3.4, 0.8, 5.3], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Recap & Setup Check", kicker="Block 1 · 10 min",
    items=[
        ("Yesterday: your finance-scenario metadata sheet and the energy-efficiency scenario metadata sheet, both fully documented", 0, False),
        ("Confirm every group still has both sheets before starting", 0, False),
        ("Setup check: MATLAB, Dynare, and repository paths working for every group", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Codebase Navigation & Version Control", kicker="Block 2 · 30 min",
    items=[
        ("ModFiles/ holds Dynare equations — but the parameters/variables they reference are usually set elsewhere", 0, False),
        ("Functions/ holds the MATLAB helpers that compute or set those values", 0, False),
        ("The navigation skill: given an equation, find what it references, and whether that's a calibration input (ExcelFiles/) or a computed value (Functions/)", 0, False),
        ("Version control — no command line required:", 0, True),
        ("Clone the repository and make your first commit using GitHub Desktop's visual interface", 1, False),
        ("Open the same repository in VS Code — the two tools share one Git history; use the Source Control panel alongside GitHub Desktop", 1, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Baseline Calibration & Debugging", kicker="Blocks 3–4 · 45 min",
    items=[
        ("A calibration run is only usable for scenario comparison once its diagnostics pass", 0, True),
        ("Check: residuals, steady-state convergence, accounting identities, output files generated", 0, False),
        ("Debugging as a categorization skill — find the category before you try a fix:", 0, True),
        ("1. Path error — the run can't find a file it needs", 1, False),
        ("2. Missing or locked input — a required workbook isn't where the run expects, or is open elsewhere", 1, False),
        ("3. Non-convergence — the solver doesn't reach a steady state; check initial values before touching tolerances", 1, False),
        ("4. Syntax/structural error — usually caught by Dynare's own error message", 1, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.section_slide(prs, "Short break", "15 minutes", "Every group should have a valid baseline run before we continue")

sk.two_col_slide(
    prs, "Finance + Efficiency Scenario Runs, with AI-Assisted VS Code",
    "What runs against what",
    [
        ("Finance scenario vs. its matching base case (same emissions pathway, one variable differs)", 0, False),
        ("Energy-efficiency scenario vs. the PDP8 baseline (efficiency coefficients differ)", 0, False),
        ("Identical solver options and horizon for both comparisons", 0, False),
    ],
    "AI-assisted VS Code (live demo)",
    [
        ("Locate a function/variable, explain unfamiliar code, draft a small edit for review", 0, False),
        ("General workflow guidance — not a DGE-METRIC-specific claim", 0, False),
        ("Always review AI-suggested edits before applying them", 0, True),
    ],
    kicker="Block 5 · 35 min", page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Comparison Tables, Chart & Narrative", kicker="Block 6 · 35 min",
    items=[
        ("Finance table: public financing rate, renewable capital stock, GDP, investment, emission-tax revenue, renewable generation", 0, False),
        ("Efficiency table: energy intensity, final energy demand, GDP, investment, energy prices/expenditure", 0, False),
        ("The efficiency scenario's GDP effect accounts for the rebound effect — net, not gross, savings", 0, True),
        ("Pick one indicator with clear policy relevance; build one chart and a 4-sentence narrative: result, mechanism, policy implication, caveat", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "This Morning's Output & Debrief", kicker="Block 7 · 10 min",
    items=[
        ("You leave with: a calibration diagnostic note; comparison tables and one chart+narrative covering both the finance and efficiency scenarios; a local repository committed to via GitHub Desktop", 0, False),
        ("Debrief: which transmission channel best explains your finance scenario's difference from its base case? The efficiency scenario's difference from PDP8?", 0, False),
        ("Debrief: did the AI assistant's suggestion need correcting before you trusted it?", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# ============ AFTERNOON SESSION ============
sk.section_slide(prs, "Online Day 2 — Afternoon", "Reserve Requirements — Method and Implementation",
                  "180 minutes")

sk.table_slide(
    prs, "This Afternoon's Agenda — 7 Blocks, 180 Minutes", ["Block", "Min", "What happens"],
    [
        ["1. Frame the question and the caveat", "15", "State the policy question; state the DGE-METRIC/toy-model distinction up front"],
        ["2. Inputs from Days 1–2", "15", "Map which finance- and efficiency-scenario outputs feed a reserve-adequacy analysis"],
        ["3. Step 1 — break-even screening", "25", "Break-even table; the MC = MB accounting logic"],
        ["4. Steps 2–3 — validate, optimize", "25", "\"Not justified\" verdicts; the Step-3 caveat"],
        ["— Break —", "15", ""],
        ["5. Implementation: where this lives in DGE-METRIC", "35", "Post-processing script vs. structural model change — the ModFiles/Functions pattern, applied to reserves"],
        ["6. Draft implementation plan", "35", "Choose a carrier; draft mechanism, DGE-METRIC outputs needed, codebase location, open items"],
        ["7. Wrap and preview", "15", "Confirm plan recorded; preview tomorrow's guided open lab"],
    ],
    col_widths=[3.6, 0.8, 5.1], page_no=pn(), deck_label=DECK,
)

sk.warning_slide(
    prs, "Before We Start: A Scope Note",
    "Today's numbers come from a separate illustrative toy model, not from DGE-METRIC.",
    [
        ("DGE-METRIC's own reserve-requirement analysis has not yet been built", 0, False),
        ("The formula, target indicator, and optimality criterion for DGE-METRIC specifically are still [SME REVIEW NEEDED]", 0, False),
        ("Everything today illustrates the METHOD using a stylized small-open-economy model — treat it as training-stage, not as a Vietnam policy answer", 0, False),
    ], kicker="Block 1 · read this first", page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "The Policy Question & Inputs Needed", kicker="Blocks 1–2 · 30 min",
    items=[
        ("A strategic reserve requirement: a target level of stockpiled/standby capacity held to buffer a supply disruption", 0, False),
        ("\"Optimal\" means MC = MB: marginal cost of one more unit of coverage equals the marginal benefit (avoided crisis losses)", 0, True),
        ("Inputs needed from Days 1–2:", 0, True),
        ("Energy-carrier demand and import dependence under the efficiency scenario vs. PDP8 baseline", 1, False),
        ("GDP, investment, and fiscal paths under the finance scenarios", 1, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Step 1 — Screen: Break-Even Accounting", kicker="Block 3 · 25 min",
    items=[
        ("Compute the annualized cost of holding the reserve, then back out the minimum crisis GDP loss (%) that would make it pay for itself", 0, False),
        ("Baseline GDP (2024): USD 430,000m · crisis probability p: 0.04/yr · break-even divisor: USD 172.0m", 0, False),
        ("Illustrative ranking (lowest to highest break-even bar):", 0, True),
        ("Refined-product tanks (8-day cover) and distributed BESS clear the lowest bar (≈0.16–0.18% of GDP)", 1, False),
        ("90-day imported coal and 6-MTA LNG need the largest crises (≈1.9–2.0% of GDP)", 1, False),
    ], page_no=pn(), deck_label=DECK,
    note="Illustrative toy-model numbers — not DGE-METRIC outputs.",
)

sk.bullets_slide(
    prs, "Steps 2–3 — Validate & Optimize", kicker="Block 4 · 25 min",
    items=[
        ("Step 2 — Validate: feed a 20% and 50% disruption through the toy model's CES production function; read off avoided GDP loss vs. the Step-1 threshold", 0, False),
        ("Illustrative result: every carrier tested comes back \"not justified\" at both shock sizes under the current calibration", 1, False),
        ("Step 3 — Optimize: search over coverage days for the level maximizing Net Reserve Value (insurance benefit − storage cost)", 0, False),
        ("Caveat: the latest run hit the edge of the search grid with a mis-scaled storage-cost figure — treat as provisional", 1, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.section_slide(prs, "Short break", "15 minutes", "Next: where would this live in the DGE-METRIC codebase?")

sk.bullets_slide(
    prs, "Implementation: Where This Would Live in DGE-METRIC", kicker="Block 5 · 35 min",
    items=[
        ("Reusing the structure-vs-calibration pattern from model modification:", 0, True),
        ("Most plausibly: a post-processing script reading existing DGE-METRIC outputs (energy-carrier demand, import dependence, GDP/investment/fiscal paths) — arithmetic on top of run outputs, not a new structural relationship", 0, False),
        ("If a genuinely endogenous crisis-cost channel were needed inside the model itself, that piece would belong in ModFiles/, with calibration in Functions/ or ExcelFiles/", 0, False),
        ("This implementation pattern is itself provisional until the DGE-METRIC formula is confirmed — teach it as an approach, not a confirmed design", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Draft Your Implementation Plan", kicker="Block 6 · 35 min",
    items=[
        ("Choose one carrier from the break-even table", 0, False),
        ("Document: mechanism (specific to your carrier); DGE-METRIC outputs it would need (name the indicator); where the logic would live in the codebase, and why; what remains [SME REVIEW NEEDED]", 0, False),
        ("Record your plan — you'll complete the full analysis note tomorrow morning", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

sk.bullets_slide(
    prs, "Today's Output & What's Next", kicker="Block 7 · 15 min",
    items=[
        ("You leave with: a documented MC = MB break-even walkthrough for one carrier, and an implementation plan for how the analysis would be built in DGE-METRIC", 0, False),
        ("Tomorrow morning: guided open lab — finish the walkthrough by hand for your chosen carrier and write the full reserve-requirement analysis note", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

prs.save(OUT)
print("Saved", OUT, "with", len(prs.slides._sldIdLst), "slides")
