#!/usr/bin/env python3
"""
Build native HTML pages for every markdown document in this repository, so
the GitHub Pages site can be read end-to-end without jumping to GitHub's own
markdown viewer.

For each `NN-name.md` (and a few unnumbered docs: README.md, CHANGELOG.md),
this script:
  1. Runs pandoc with a table-of-contents and the shared page template
     (tools/page-template.html) to produce `NN-name.html` at the repo root.
  2. Rewrites every occurrence of another tracked markdown filename (in link
     hrefs, inline code, or plain text) to point at its `.html` counterpart,
     so cross-references between documents stay inside the Pages site.

Run from the repo root: python3 tools/build-pages.py
Requires: pandoc on PATH.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "tools", "page-template.html")

# (source markdown filename, nav breadcrumb label, page <title>)
DOCS = [
    ("00-how-to-use-this-research.md", "Miten tätä tutkimusta käytetään", "Miten tätä tutkimusta käytetään"),
    ("01-whitepaper.md", "Alkuteksti", "Alkuteksti"),
    ("02-source-register.md", "Lähderekisteri", "Lähderekisteri"),
    ("03-workbook-global-baseline.md", "Globaali perustaso -työkirja", "Globaali perustaso -työkirja"),
    ("04-workbook-ai-working-capacity-conversion.md", "Tekoälytyökapasiteetin muuntotyökirja", "Tekoälytyökapasiteetin muuntotyökirja"),
    ("05-workbook-token-factory-scenarios.md", "Tokenitehtaan skenaariotyökirja", "Tokenitehtaan skenaariotyökirja"),
    ("06-investment-thesis-notes.md", "Sijoitusteesin muistiinpanot", "Sijoitusteesin muistiinpanot"),
    ("07-workbook-humanoid-working-capacity.md", "Humanoidirobottien työkapasiteettityökirja", "Humanoidirobottien työkapasiteettityökirja"),
    ("08-workbook-localized-scenario-eur-finland.md", "Paikallistettu skenaariotyökirja (EUR/Suomi)", "Paikallistettu skenaariotyökirja (EUR/Suomi)"),
    ("09-appendix-glossary.md", "Sanasto", "Sanasto"),
    ("10-appendix-source-register-formatted.md", "Lähderekisteri (muotoiltu)", "Lähderekisteri (muotoiltu)"),
    ("11-appendix-assumption-register.md", "Oletusrekisteri", "Oletusrekisteri"),
    ("12-executive-brief.md", "Johdon tiivistelmä", "Johdon tiivistelmä"),
    ("13-slide-deck-outline.md", "Diaesityksen jäsennys", "Diaesityksen jäsennys"),
    ("14-shortform-general.md", "Lyhytmuoto: yleinen selittäjä", "Lyhytmuoto: yleinen selittäjä"),
    ("15-shortform-ownership.md", "Lyhytmuoto: omistus", "Lyhytmuoto: omistus"),
    ("16-shortform-value.md", "Lyhytmuoto: arvo", "Lyhytmuoto: arvo"),
    ("17-visual-asset-briefs.md", "Visuaalisten resurssien briiffit", "Visuaalisten resurssien briiffit"),
    ("20-appendix-known-limitations.md", "Tunnetut rajoitteet", "Tunnetut rajoitteet"),
    ("README.md", "README", "README"),
    ("CHANGELOG.md", "Muutosloki", "Muutosloki"),
]

# Filenames eligible for cross-reference rewriting (all tracked docs, by basename).
MD_FILENAMES = {name for name, _, _ in DOCS}


def rewrite_cross_references(html, current_filename):
    """Rewrite href="NN-name.md" and bare `NN-name.md` mentions in the
    rendered HTML to point at the corresponding .html file instead."""
    def replace_href(match):
        fname = match.group(1)
        if fname in MD_FILENAMES:
            return f'href="{fname[:-3]}.html"'
        return match.group(0)

    html = re.sub(r'href="([\w.-]+\.md)"', replace_href, html)

    # Bare filename mentions inside <code>NN-name.md</code> (from backtick
    # spans in the source markdown) — relink the code span itself.
    def replace_code_span(match):
        fname = match.group(1)
        if fname in MD_FILENAMES:
            return f'<code><a href="{fname[:-3]}.html">{fname}</a></code>'
        return match.group(0)

    html = re.sub(r'<code>([\w.-]+\.md)</code>', replace_code_span, html)
    return html


def build_one(src_filename, nav_label, title):
    src_path = os.path.join(ROOT, src_filename)
    if not os.path.exists(src_path):
        print(f"  SKIP (not found): {src_filename}")
        return False

    out_filename = src_filename[:-3] + ".html"
    out_path = os.path.join(ROOT, out_filename)

    cmd = [
        "pandoc", src_path,
        "-f", "markdown",
        "-t", "html5",
        "--template", TEMPLATE,
        "--toc", "--toc-depth=2",
        "-V", f"navlabel={nav_label}",
        "-V", f"ghsource={src_filename}",
        "-M", f"title={title}",
        "-o", out_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  FAILED: {src_filename}\n{result.stderr}")
        return False

    with open(out_path, encoding="utf-8") as f:
        html = f.read()
    html = rewrite_cross_references(html, src_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  built {out_filename}")
    return True


def main():
    print("Building HTML pages from markdown sources...")
    ok = 0
    for src_filename, nav_label, title in DOCS:
        if build_one(src_filename, nav_label, title):
            ok += 1
    print(f"\n{ok}/{len(DOCS)} pages built.")
    return 0 if ok == len(DOCS) else 1


if __name__ == "__main__":
    sys.exit(main())
