"""C997: scrub the WSQ layer from labs/*.md and the LG Markdown mirror (copied from source-wsq)."""
import re
from pathlib import Path

NEW = "Business Transformation with AI Agents"
SUBS = [
    ("Digital Transformation and Business Innovation with Generative AI (GenAI)", NEW),
    ("Digital Transformation and Business Innovation with GenAI", NEW),
    ("TGS-2023037472", "C997"),
    ("**WSQ Course Code:**", "**Course Code:**"),
    ("Version v38 · 9 August 2026", "Version v1.0 · 2 October 2026"),
    ("Version v38", "Version v1.0"),
    ("This Learner Guide accompanies the WSQ course ", "This Learner Guide accompanies the course "),
    ("you will need this for the assessment and for governance.", "you will need this for governance."),
    ("Save every deliverable; the labs are the direct preparation for the Practical Performance tasks.",
     "Save every deliverable; each lab builds on the artifact produced by the previous one."),
    ("live here in the Learner Guide, which you may use during the open-book assessment.",
     "live here in the Learner Guide."),
]
CODES = r"(?:[KA]\d(?:,\s*)?)+"


def scrub(text):
    for a, b in SUBS:
        text = text.replace(a, b)
    text = re.sub(rf"\s*\({CODES}\)$", "", text, flags=re.M)                 # topic strap codes
    text = re.sub(rf"^(\*\*)?Maps to:(\*\*)? {CODES} — ", r"\1Focus:\2 ", text, flags=re.M)
    text = re.sub(rf"^- {CODES} — (\w)", lambda m: "- " + m.group(1).upper(), text, flags=re.M)
    return text


def drop_section(text, heading):
    """Remove a '## heading' section up to the next '## ' heading."""
    return re.sub(rf"^## {re.escape(heading)}\n.*?(?=^## )", "", text, flags=re.M | re.S)


# Labs
for f in Path("labs").glob("*.md"):
    t = scrub(f.read_text())
    if f.name == "README.md":                     # drop the competency-code "Maps to" column
        t = re.sub(r"^\| Lab \| Title \| Maps to \| Tools \|$", "| Lab | Title | Tools |", t, flags=re.M)
        t = t.replace("| --- | --- | --- | --- |", "| --- | --- | --- |")
        t = re.sub(rf"^(\| \d+ \| .*?) \| {CODES} \|", r"\1 |", t, flags=re.M)
    f.write_text(t)

# LG Markdown mirror
f = Path(f"LG-{NEW} (C997).md")
t = scrub(f.read_text())
t = drop_section(t, "Skills Framework Alignment")
t = drop_section(t, "Preparing for the Assessment")
t = t.replace("- [Skills Framework Alignment](#skills-framework-alignment)\n", "")
t = t.replace("- [Preparing for the Assessment](#preparing-for-the-assessment)\n", "")
t = re.sub(r"(\| --- \| --- \| --- \| --- \|\n).*?\n\n",
           r"\1| 1.0 | 2 October 2026 | Initial release of the Business Transformation with AI Agents (C997) Learner "
           r"Guide: 3 topics and 18 connected labs with step-by-step instructions, aligned to the v1.0 99-slide deck. "
           r"| Tertiary Infotech Academy |\n\n", t, count=1, flags=re.S)
f.write_text(t)
print("scrubbed labs + LG md")
