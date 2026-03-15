"""
Generate Session 8 and Session 9 PowerPoint files for FoP (Fundamentals of Programming).
Upload the .pptx to Google Slides for editing/presenting.
"""
from pptx import Presentation
from pptx.util import Inches

OUTPUT_DIR = "."

def add_title_slide(prs, title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle

def add_content_slide(prs, title, bullets):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    body = slide.placeholders[1].text_frame
    for b in bullets:
        p = body.add_paragraph()
        p.text = b
        p.level = 0

def add_ref_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "References"
    body = slide.placeholders[1].text_frame
    refs = [
        "Downey, A. (2012). Think Python. O'Reilly Media, Inc.",
        "Matthes, E. (2023). Python Crash Course: A hands-on, project-based introduction to programming.",
        "Müller, A. C., & Guido, S. (2016). Introduction to machine learning with Python: a guide for data scientists. O'Reilly Media, Inc.",
        "GeeksforGeeks Python: https://www.geeksforgeeks.org/python/",
        "W3Schools Python: https://www.w3schools.com/python/",
    ]
    for r in refs:
        p = body.add_paragraph()
        p.text = r
        p.level = 0

def build_session8_pptx():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    add_title_slide(prs,
        "Session 8: Tuples, Sets & Dictionaries",
        "FoP – B.S. in Management and Public Policy | 90 min"
    )
    add_content_slide(prs, "Learning objectives", [
        "Organize data using tuples, sets, and dictionaries.",
        "Choose the right structure for policy and management data (schemes, beneficiaries, surveys).",
        "Apply to real-world tasks: unique stakeholders, scheme lookups, survey response counts.",
    ])
    add_content_slide(prs, "Tuples – management & policy use", [
        "Immutable ordered sequence: (scheme_name, year, budget) — e.g. one fixed record.",
        "Use when: order matters and data should not change (e.g. policy snapshot, KPI row).",
        "Unpacking: scheme_name, year, budget = policy_record.",
    ])
    add_content_slide(prs, "Sets – unique entities", [
        "Unordered collection of unique elements: e.g. unique beneficiary IDs, districts, departments.",
        "Use when: counting distinct stakeholders, regions covered, or removing duplicate responses.",
        "Operations: union (combined coverage), intersection (common beneficiaries), difference.",
    ])
    add_content_slide(prs, "Dictionaries – key–value lookups", [
        "Key–value pairs: scheme_id → details, department → head, indicator → target.",
        "Use when: looking up policy details, program metadata, or survey codes by ID.",
        ".keys(), .values(), .items() for reporting and iteration.",
    ])
    add_content_slide(prs, "When to use which? (management & policy)", [
        "Tuple: one fixed record (e.g. scheme name, financial year, allocated amount).",
        "Set: unique beneficiaries, unique districts in a program, unique response categories.",
        "Dict: scheme_id → full details; department → contact; indicator_code → definition.",
    ])
    add_content_slide(prs, "Practical in-class (Colab)", [
        "Session 8 Student notebook: tuples (policy record), sets (unique regions/beneficiaries), dicts (scheme lookup).",
        "Hands-on: e.g. count unique districts in a program, build a scheme lookup table.",
        "All examples use business management and public policy contexts.",
    ])
    add_content_slide(prs, "Session 8 – Recap", [
        "Tuples: immutable, ordered.",
        "Sets: unique, unordered, fast membership.",
        "Dictionaries: key–value, fast lookup by key.",
    ])
    add_ref_slide(prs)

    path = f"{OUTPUT_DIR}/Session8_Tuples_Sets_Dictionaries.pptx"
    prs.save(path)
    print(f"Saved: {path}")

def build_session9_pptx():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    add_title_slide(prs,
        "Session 9: Functions – Basics",
        "FoP – B.S. in Management and Public Policy | 90 min"
    )
    add_content_slide(prs, "Learning objectives", [
        "Define and call functions with parameters and return values.",
        "Write reusable code for policy and management tasks (formatting, summaries, lookups).",
        "Apply functions: budget display, scheme summaries, indicator lookups, report snippets.",
    ])
    add_content_slide(prs, "Why functions? (management & policy)", [
        "Reuse: format budget in lakhs/crores, format scheme names, or build report lines repeatedly.",
        "Structure: break reporting into clear steps (e.g. get_scheme_summary, format_for_display).",
        "Easier to maintain when definitions change (e.g. currency, rounding rules).",
    ])
    add_content_slide(prs, "Defining a function", [
        "def function_name(parameter1, parameter2):",
        "    '''Optional docstring — e.g. \"Format budget in lakhs for display\"'''",
        "    # body",
        "    return result",
    ])
    add_content_slide(prs, "Parameters and return", [
        "Parameters: e.g. scheme name and year, or a list of grant amounts.",
        "return: e.g. formatted string, summary dict, or lookup result.",
        "Without return: function returns None (avoid for data you need to use).",
    ])
    add_content_slide(prs, "Scope", [
        "Variables inside a function are local (e.g. temp totals, formatted strings).",
        "Variables in the notebook are global; prefer passing data in and returning results.",
        "Keeps policy/data inputs explicit and outputs clear for reporting.",
    ])
    add_content_slide(prs, "Practical in-class (Colab)", [
        "Session 9 Student notebook: functions for policy/scheme formatting, grant averages, scheme lookup.",
        "Hands-on: e.g. format_budget(amount), summarize_grants(list), get_scheme_by_id(dict, id).",
        "All examples aligned with business management and public policy.",
    ])
    add_content_slide(prs, "Session 9 – Recap", [
        "def name(params): ... return value",
        "Use functions for reusable formatting, summaries, and lookups in policy/management data.",
        "Structure programs with small, named steps for clarity and maintenance.",
    ])
    add_ref_slide(prs)

    path = f"{OUTPUT_DIR}/Session9_Functions_Basics.pptx"
    prs.save(path)
    print(f"Saved: {path}")

if __name__ == "__main__":
    build_session8_pptx()
    build_session9_pptx()
    print("Done. Upload .pptx files to Google Slides as needed.")
