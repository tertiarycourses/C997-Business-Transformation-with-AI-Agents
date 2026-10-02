"""C997 Lesson Plan: explicit rewrite of the WSQ LP (TGS-2023037472 v38) as the 2-day non-WSQ twin."""
import shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LP-Digital Transformation and Business Innovation with GenAI.docx"
OUT = "courseware/LP-Business Transformation with AI Agents (C997).docx"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)
retitle_all(d)
t_ctrl, t_info, t_day1, t_day2, t_labs = d.tables

# Cover
set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C997")
set_text(para_by_text(d, "Version 38"), "Version 1.0")

# Document version control -> single v1.0 row
for r in list(t_ctrl.rows)[2:]:
    t_ctrl._tbl.remove(r._tr)
for c, v in zip(t_ctrl.rows[1].cells, [
        "1.0", "2 October 2026",
        "Initial release of the Business Transformation with AI Agents (C997) lesson plan: two 9:30am – 5:30pm "
        "days (15 instructional hours) covering all 3 topics and 18 connected labs, mapped to the v1.0 99-slide deck.",
        "Tertiary Infotech Academy"]):
    set_cell(c, v)

# TOC: Assessment and Skills Framework Alignment sections go
def toc(start):
    hits = [p for p in d.paragraphs if p.text.startswith(start) and "\t" in p.text]
    assert len(hits) == 1, start
    return hits[0]
delete(toc("Assessment\t"))
delete(toc("Skills Framework Alignment\t"))

# Course Information
def kv(key):
    return next(r for r in t_info.rows if r.cells[0].text == key)
set_cell(kv("WSQ Course Reference").cells[0], "Course Code")
set_cell(kv("Course Code").cells[1], "C997")
set_cell(kv("Duration").cells[1], "2 days · 7.5 instructional hours per day (15 hours)")
set_cell(kv("Daily Timing").cells[1], "9:30 am – 5:30 pm (one 30-minute lunch; refreshments taken during activity time)")
t_info._tbl.remove(kv("Skills Framework")._tr)

# Assessment + Skills Framework Alignment sections (heading through the K6 bullet)
delete_range(d, "Assessment", "Course Schedule")

# Schedules: 450 teaching minutes + one 30-minute lunch, closing on 5:30pm.
# Day 1: the WSQ teaching rows already total 450 (30/60/105/75/105/75); its 60-min lunch + two
#        15-min teas collapse into one 30-min lunch.
# Day 2: the WSQ non-assessment content rows (60/120/75/45 = 300) rescaled proportionally onto the
#        420 left after the 15-min recap and 15-min close: 85/165/105/65. The 165-min lab block is
#        split around lunch (Lab 9 | Lab 10).
c1 = [strip_codes(r.cells[2].text) for r in t_day1.rows]
rebuild_rows(t_day1, [
    (1, ["9:30–10:00", "30 min", "Welcome, trainer and learner introductions, ground rules, learning outcomes and course outline", "2–13"]),
    (2, ["10:00–11:00", "60 min", c1[2], "14–23"]),
    (4, ["11:00–12:45", "105 min", c1[4], "24–27"]),
    (5, ["12:45–13:15", "30 min", "Lunch break", "—"]),
    (6, ["13:15–14:30", "75 min", c1[6].replace(" Digital attendance (PM).", ""), "28–29"]),
    (8, ["14:30–16:15", "105 min", c1[8], "30–49"]),
    (9, ["16:15–17:30", "75 min", c1[9], "50–53"]),
])
c2 = [strip_codes(r.cells[2].text) for r in t_day2.rows]
rebuild_rows(t_day2, [
    (1, ["9:30–9:45", "15 min", "Day 1 recap and Q&A", "—"]),
    (2, ["9:45–11:10", "85 min", c2[2], "54–55"]),
    (4, ["11:10–12:40", "90 min", "STAGE 5 — Hands-on: Lab 9: Create the AI Voiceover", "56–57"]),
    (5, ["12:40–13:10", "30 min", "Lunch break", "—"]),
    (4, ["13:10–14:25", "75 min", "STAGE 6 — Hands-on: Lab 10: Generate the Background Soundtrack with Suno", "58–59"]),
    (6, ["14:25–16:10", "105 min", c2[6].replace("Digital attendance (PM). ", "") + ". Topic 2 recap", "60–64"]),
    (8, ["16:10–17:15", "65 min", c2[8], "65–91"]),
    (9, ["17:15–17:30", "15 min", "Course summary, next steps, Q&A and course feedback", "92–99"]),
])
for p in [p for p in d.paragraphs if p.text.startswith("Total training time:")]:
    set_text(p, "Total instructional time: 450 minutes (7.5 hours), 9:30 am – 5:30 pm with a 30-minute lunch.")

d.core_properties.title = "LP-Business Transformation with AI Agents (C997)"
d.save(OUT)
print("saved", OUT)
