"""C997 Learner Guide: explicit rewrite of the WSQ LG (TGS-2023037472 v38) as the non-WSQ twin."""
import re, shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LG-Digital Transformation and Business Innovation with GenAI.docx"
OUT = "courseware/LG-Business Transformation with AI Agents (C997).docx"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)
retitle_all(d)
t_ctrl = d.tables[0]

# Cover
set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C997")
set_text(para_by_text(d, "Version 38"), "Version 1.0")

# Document version control -> single v1.0 row
for r in list(t_ctrl.rows)[2:]:
    t_ctrl._tbl.remove(r._tr)
for c, v in zip(t_ctrl.rows[1].cells, [
        "1.0", "2 October 2026",
        "Initial release of the Business Transformation with AI Agents (C997) Learner Guide: 3 topics and "
        "18 connected labs with step-by-step instructions, aligned to the v1.0 99-slide deck.",
        "Tertiary Infotech Academy"]):
    set_cell(c, v)

# TOC
def toc(start):
    hits = [p for p in d.paragraphs if p.text.startswith(start) and "\t" in p.text]
    assert len(hits) == 1, start
    return hits[0]
delete(toc("Skills Framework Alignment\t"))
delete(toc("Preparing for the Assessment\t"))

# Introduction
p = para_by_text(d, "This Learner Guide accompanies the WSQ course")
set_text(p, p.text.replace("the WSQ course ", "the course ").replace("(TGS-2023037472)", "(C997)"))

p = para_by_text(d, "Use this guide alongside the course slides")
set_text(p, p.text.replace(", which you may use during the open-book assessment.", "."))

# Skills Framework Alignment section and the closing assessment section go
delete_range(d, "Skills Framework Alignment", "Before You Start")
delete_range(d, "Preparing for the Assessment", "Glossary")

# Sentence-level assessment references
p = para_by_text(d, "Record which tool produced which artifact")
set_text(p, "Record which tool produced which artifact — you will need this for governance.")
p = para_by_text(d, "Save every deliverable;")
set_text(p, "Save every deliverable; each lab builds on the artifact produced by the previous one.")

# Competency codes: topic straps "(K1, K2, A1, A2)" and "Maps to: K1, A2 — ..." lines
strip_codes_all(d)
MAPS = re.compile(r"^Maps to: (?:[KA]\d(?:,\s*)?)+ — ")
for p in d.paragraphs:
    if MAPS.match(p.text):
        set_text(p, MAPS.sub("Focus: ", p.text))

d.core_properties.title = "LG-Business Transformation with AI Agents (C997)"
d.save(OUT)
print("saved", OUT)
