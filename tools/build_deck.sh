#!/bin/sh
# Rebuild the C997 deck from the WSQ source: convert_deck.py, then fix_deck.py.
set -e
cd "$(dirname "$0")/.."
OUT="courseware/Business Transformation with AI Agents (C997)-v1.0.pptx"
python3 ~/.claude/skills/wsq-to-non-wsq/scripts/convert_deck.py \
  --src "source-wsq/courseware/Digital Transformation and Business Innovation with GenAI-v38.pptx" --out "$OUT" \
  --old-title "Digital Transformation and Business Innovation with Generative AI (GenAI)" \
  --new-title "Business Transformation with AI Agents" \
  --old-code TGS-2023037472 --new-code C997 \
  --sub "Digital Transformation and Business Innovation with GenAI=>Business Transformation with AI Agents" \
  --sub "Version v38  ·  9 August 2026=>Version v1.0  ·  2 October 2026" \
  --wsq-slides 2,8,9,10,17,18,19,104,105
python3 tools/fix_deck.py
