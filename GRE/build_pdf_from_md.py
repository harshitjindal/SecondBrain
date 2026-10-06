#!/usr/bin/env python3
"""Obsidian-style Markdown (LaTeX math + callouts) -> PDF.

Pipeline: preprocess callouts -> pandoc (Markdown -> HTML, math via KaTeX)
          -> headless Chromium (Playwright) prints the page to PDF.

Setup (once):
    sudo apt install pandoc            # or: brew install pandoc
    pip install playwright && playwright install chromium
    npm install katex                  # local KaTeX (falls back to CDN if absent)

Usage:
    python3 build_pdf.py GRE_Quant_Cheatsheet.md GRE_Quant_Cheatsheet.pdf
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
text = src.read_text(encoding="utf-8")

# 1) Obsidian callouts -> small coloured labels / plain quote
text = re.sub(r"^>\s*\[!SUCCESS\][^\n]*$",
              '<span class="tag ok">Verified</span>', text, flags=re.M | re.I)
text = re.sub(r"^>\s*\[!QUESTION\][^\n]*$",
              '<span class="tag warn">Needs verification</span>', text, flags=re.M | re.I)
text = re.sub(r"^>\s*\[!NOTE\][^\n]*$",
              '<span class="tag new">New</span>', text, flags=re.M | re.I)
text = re.sub(r"^>\s*\[!WARNING\][^\n]*$",
              '<span class="tag warn">Corrected</span>', text, flags=re.M | re.I)
text = re.sub(r"^>\s*\[!abstract\]\s*Overview\s*",
              "> **Overview.** ", text, flags=re.M | re.I)

# 2) Bold that wraps inline math with split markers: **Name (**$x$**)** -> **Name ($x$)**
text = re.sub(r"\*\*([^*\n]*?)\(\*\*(\$[^$\n]+\$)\*\*\)\*\*", r"**\1(\2)**", text)

# 3) Tabs -> 4 spaces so nested lists parse consistently
text = text.expandtabs(4)

CSS = """
@page { size: A4; margin: 16mm 15mm; }
body { font-family: "Helvetica Neue", Arial, "Liberation Sans", sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #1c1c1c; max-width: none; margin: 0; padding: 0; }
h1 { font-size: 17pt; color: #1f3a68; border-bottom: 2px solid #1f3a68;
     padding-bottom: 3px; margin: 20px 0 8px; break-after: avoid; }
header h1.title { font-size: 22pt; border: none; margin: 0 0 6px; }
h3 { font-size: 12pt; color: #2b2b2b; margin: 14px 0 4px; break-after: avoid; }
blockquote { margin: 6px 0 10px; padding: 6px 12px; background: #eef3fb;
             border-left: 4px solid #1f3a68; border-radius: 3px; }
hr { border: none; border-top: 1px solid #ccc; margin: 10px 0; }
ul, ol { margin: 3px 0 6px; padding-left: 22px; }
li { margin: 2px 0; break-inside: avoid; }
p { margin: 4px 0; }
.tag { display: inline-block; font-size: 8pt; font-weight: 700; padding: 1px 7px;
       border-radius: 9px; margin: 0 0 2px; }
.tag.ok   { background: #e3f4e6; color: #1b6b2c; border: 1px solid #9fd3aa; }
.tag.new  { background: #e4ecfb; color: #1f3a68; border: 1px solid #a9bde6; }
.tag.warn { background: #fff1d6; color: #8a5a00; border: 1px solid #e8c36f; }
.katex { font-size: 1.02em; }
"""

here = Path(__file__).resolve().parent
katex_dir = here / "node_modules" / "katex" / "dist"
katex_arg = f"--katex={katex_dir.as_uri()}/" if katex_dir.exists() else "--katex"

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    (d / "in.md").write_text(text, encoding="utf-8")
    (d / "style.css").write_text(CSS, encoding="utf-8")
    html = d / "out.html"
    subprocess.run([
        "pandoc", str(d / "in.md"), "-o", str(html), "--standalone",
        "--from=markdown+tex_math_dollars", katex_arg,
        "--metadata", "title=GRE Quantitative Reasoning Quick Reference (v2)",
        "--metadata", "pagetitle=GRE Quant Cheat Sheet",
        "--css", "style.css", "--wrap=none",
    ], check=True)
    # Drop the duplicate title block (the note already has its own H1 title)
    h = html.read_text(encoding="utf-8")
    h = re.sub(r"<header id=\"title-block-header\">.*?</header>", "", h, flags=re.S)
    html.write_text(h, encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        page.goto(html.as_uri(), wait_until="networkidle")
        page.wait_for_selector(".katex", timeout=20000)   # math rendered
        page.wait_for_timeout(500)
        page.pdf(path=str(out), format="A4", print_background=True,
                 margin={"top": "16mm", "bottom": "16mm", "left": "15mm", "right": "15mm"},
                 display_header_footer=True,
                 header_template="<span></span>",
                 footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#777">'
                                 '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
        b.close()
print(f"Wrote {out}")
