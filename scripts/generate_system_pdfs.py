"""Generate professional PDFs from the system-documentation Markdown sources."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import LongTable, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, TableStyle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "system-documentation"
OUTPUT = SOURCE / "pdf"
VERSION, DATE = "0.2.0", "2026-09-10"
LINK = re.compile(r"\[([^]]+)\]\(([^)]+)\)")


def sources() -> list[Path]:
    return [SOURCE / "README.md", *sorted(SOURCE.glob("[0-1][0-9]-*.md"))]


def inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = LINK.sub(r"<u>\1</u>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)


def footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawString(18 * mm, 10 * mm, f"AI Dataset Foundry {VERSION} · {DATE}")
    canvas.drawRightString(192 * mm, 10 * mm, f"Página {doc.page}")
    canvas.restoreState()


def markdown_table(lines: list[str], styles) -> LongTable:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append([Paragraph(inline(cell), styles["TableCell"]) for cell in cells])
    width = 174 * mm / max(len(row) for row in rows)
    table = LongTable(rows, colWidths=[width] * len(rows[0]), repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f766e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#cbd5e1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def build(source: Path, destination: Path) -> None:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Cover", parent=styles["Title"], fontSize=24, leading=29,
                              textColor=colors.HexColor("#0f766e"), alignment=TA_CENTER))
    styles.add(ParagraphStyle(name="BodyDoc", parent=styles["BodyText"], fontSize=9.2, leading=12.2,
                              textColor=colors.HexColor("#1e293b"), spaceAfter=6))
    styles.add(ParagraphStyle(name="BulletDoc", parent=styles["BodyDoc"], leftIndent=12,
                              firstLineIndent=-7, bulletIndent=3))
    styles.add(ParagraphStyle(name="CodeDoc", fontName="Courier", fontSize=6.8, leading=8.5,
                              leftIndent=6, rightIndent=6, borderWidth=.5, borderPadding=5,
                              borderColor=colors.HexColor("#cbd5e1"), backColor=colors.HexColor("#f8fafc")))
    styles.add(ParagraphStyle(name="TableCell", parent=styles["BodyText"], fontSize=6.8, leading=8.2))
    for key, size, color in (("Heading1", 18, "#0f766e"), ("Heading2", 13, "#155e75"), ("Heading3", 10.5, "#334155")):
        styles[key].fontSize, styles[key].leading = size, size + 3
        styles[key].textColor, styles[key].spaceBefore = colors.HexColor(color), 10

    lines = source.read_text(encoding="utf-8").splitlines()
    title = next((line[2:] for line in lines if line.startswith("# ")), source.stem)
    story = [Spacer(1, 38 * mm), Paragraph(inline(title), styles["Cover"]), Spacer(1, 8 * mm),
             Paragraph(f"AI Dataset Foundry<br/>Versión {VERSION}<br/>{DATE}<br/>Fuente: {source.name}", styles["BodyDoc"]), PageBreak()]
    index, in_code, code = 0, False, []
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            if in_code:
                story.extend([Preformatted("\n".join(code), styles["CodeDoc"]), Spacer(1, 5)])
                code, in_code = [], False
            else:
                in_code = True
            index += 1
            continue
        if in_code:
            code.append(line)
            index += 1
            continue
        if line.startswith("|") and index + 1 < len(lines) and lines[index + 1].startswith("|"):
            block = []
            while index < len(lines) and lines[index].startswith("|"):
                block.append(lines[index])
                index += 1
            story.extend([markdown_table(block, styles), Spacer(1, 7)])
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), styles["Heading3"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline(line[3:]), styles["Heading2"]))
        elif line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), styles["Heading1"]))
        elif re.match(r"^[-*] ", line):
            story.append(Paragraph("• " + inline(line[2:]), styles["BulletDoc"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline(line), styles["BulletDoc"]))
        elif line.strip():
            story.append(Paragraph(inline(line), styles["BodyDoc"]))
        else:
            story.append(Spacer(1, 3))
        index += 1
    destination.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(destination), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=16*mm, bottomMargin=17*mm, title=title,
                      author="AI Dataset Foundry contributors").build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    items = sources()
    if len(items) != 20:
        raise SystemExit(f"Expected 20 Markdown sources, found {len(items)}")
    if not args.check:
        for source in items:
            build(source, OUTPUT / f"{source.stem}.pdf")
    missing = [source.name for source in items if not (OUTPUT / f"{source.stem}.pdf").is_file()]
    short = [source.name for source in items if source.stat().st_size < 300]
    if missing or short:
        raise SystemExit(f"PDF check failed: missing={missing}, short_sources={short}")
    print(f"[OK] {len(items)} Markdown sources and PDFs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
