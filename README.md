# FoP Sessions 8 & 9 – Materials

**Course:** Fundamentals of Programming (FoP)  
**Program:** B.S. in Management and Public Policy  
**Sessions:** 8 (Tuples, Sets & Dictionaries) and 9 (Functions – Basics)  
**Duration per session:** 90 minutes  

---

## What’s included

| File | Purpose |
|------|--------|
| **Session8_Tuples_Sets_Dictionaries.pptx** | Slides for Session 8. Upload to **Google Slides** (File → Import → Upload). |
| **Session9_Functions_Basics.pptx** | Slides for Session 9. Upload to Google Slides. |
| **Session8_Master.ipynb** | Instructor/reference notebook for Session 8. Open in **Google Colab** (File → Upload notebook). |
| **Session8_Student.ipynb** | Student notebook – fill-in code during class. Share link via Colab (File → Share). |
| **Session9_Master.ipynb** | Instructor/reference notebook for Session 9. |
| **Session9_Student.ipynb** | Student notebook – fill-in code during class. |
| **REFERENCES.txt** | Reference books used in the course (also on the last slide of each PPT). |

Each PPT ends with a **References** slide (Downey, Matthes, Müller & Guido, GeeksforGeeks, W3Schools).

---

## Workflow

1. **Before the session (early instructions)**  
   - Upload the **Student** notebook for that session to Google Colab.  
   - Share the Colab link (View only or Make a copy) so students can open and duplicate it.  
   - Optionally share the PPT link (Google Slides) so they can follow along.

2. **During the session (90 min)**  
   - Present using the PPT (in Google Slides).  
   - Use the **Master** notebook as your reference; students work in the **Student** notebook and run code on the fly.
   - **In-class:** Students solve 2–3 practice problems during the session; the rest are **homework** (Master has solutions for all).

3. **Practice problems (each session)**  
   - **Session 8:** Section 4 (feedback) + 5.1–5.2 = in-class; 5.3–5.7 = homework (5.7 is a challenge: releases by scheme/district using tuples, sets, dicts).  
   - **Session 9:** Section 5 (summarize_grants) + 6.1–6.2 = in-class; 6.3–6.6 = homework (format_cr, scheme_status, count_above, lookup_indicator, report_line, merge_totals).  
   - **Master** notebooks contain full solutions for every practice problem.

**Solution Colab for students?** Use **one Master notebook** as your single source of truth (you solve/check there). Do *not* share the Master with students during the assignment. Optionally, **after** the homework deadline, you can duplicate the Master, rename it (e.g. `Session8_Solutions.ipynb`), remove any extra commentary, and share that link so students can self-check — this reduces repeat "how do I do 5.7?" and speeds up your grading.

4. **Regenerating PPTs (optional)**  
   - Edit `build_pptx.py` if you change slide content.  
   - From this folder run:  
     `python3 -m venv .venv && .venv/bin/pip install python-pptx && .venv/bin/python build_pptx.py`  
   - New `.pptx` files will be written in this folder.

---

## References (from course outline)

- **Text:** Downey, A. (2012). *Think Python*. O'Reilly Media, Inc.  
- **Ref:** Matthes, E. (2023). *Python Crash Course*.  
- **Ref:** Müller, A. C., & Guido, S. (2016). *Introduction to machine learning with Python*. O'Reilly Media, Inc.  
- **Online:** GeeksforGeeks Python, W3Schools Python  
