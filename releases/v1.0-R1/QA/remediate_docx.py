"""Surgical OOXML remediation for AME v1.0 publication tables and Appendix C."""
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

DOCX = Path(__file__).resolve().parents[1] / "Master" / "AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}
ET.register_namespace("w", W)

def q(tag):
    return f"{{{W}}}{tag}"

def set_attr(el, name, value):
    el.set(q(name), str(value))

def ensure(parent, tag):
    child = parent.find(f"w:{tag}", NS)
    if child is None:
        child = ET.SubElement(parent, q(tag))
    return child

def move_to(parent, child, index):
    current = list(parent).index(child)
    if current != index:
        parent.remove(child); parent.insert(index, child)

def set_cell_text(tc, text, size_half_points=18, bold=False):
    tc_pr = ensure(tc, "tcPr")
    for p in list(tc.findall("w:p", NS)):
        tc.remove(p)
    p = ET.SubElement(tc, q("p"))
    p_pr = ET.SubElement(p, q("pPr"))
    spacing = ET.SubElement(p_pr, q("spacing"))
    set_attr(spacing, "before", 0); set_attr(spacing, "after", 0)
    r = ET.SubElement(p, q("r"))
    r_pr = ET.SubElement(r, q("rPr"))
    fonts = ET.SubElement(r_pr, q("rFonts"))
    set_attr(fonts, "ascii", "Calibri"); set_attr(fonts, "hAnsi", "Calibri")
    size = ET.SubElement(r_pr, q("sz")); set_attr(size, "val", size_half_points)
    size_cs = ET.SubElement(r_pr, q("szCs")); set_attr(size_cs, "val", size_half_points)
    if bold:
        ET.SubElement(r_pr, q("b"))
    t = ET.SubElement(r, q("t")); t.set(f"{{{XML}}}space", "preserve"); t.text = text

def format_table(tbl, widths, font_half_points):
    rows = tbl.findall("w:tr", NS)
    if not rows or any(len(r.findall("w:tc", NS)) != len(widths) for r in rows):
        raise RuntimeError("Unexpected table shape")
    total = sum(widths)
    tbl_pr = ensure(tbl, "tblPr")
    move_to(tbl, tbl_pr, 0)
    tbl_w = ensure(tbl_pr, "tblW"); set_attr(tbl_w, "type", "dxa"); set_attr(tbl_w, "w", total)
    tbl_ind = ensure(tbl_pr, "tblInd"); set_attr(tbl_ind, "type", "dxa"); set_attr(tbl_ind, "w", 120)
    layout = ensure(tbl_pr, "tblLayout"); set_attr(layout, "type", "fixed")
    borders = ensure(tbl_pr, "tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        edge = ensure(borders, side); set_attr(edge, "val", "single"); set_attr(edge, "sz", 4); set_attr(edge, "color", "B7C3D0")
    margins = ensure(tbl_pr, "tblCellMar")
    for side, val in (("top", 80), ("bottom", 80), ("start", 100), ("end", 100)):
        m = ensure(margins, side); set_attr(m, "type", "dxa"); set_attr(m, "w", val)
    grid = ensure(tbl, "tblGrid")
    move_to(tbl, grid, 1)
    for child in list(grid): grid.remove(child)
    for width in widths:
        c = ET.SubElement(grid, q("gridCol")); set_attr(c, "w", width)
    for ri, row in enumerate(rows):
        tr_pr = ensure(row, "trPr")
        move_to(row, tr_pr, 0)
        # Remove fixed heights so content can expand and split safely.
        for h in list(tr_pr.findall("w:trHeight", NS)): tr_pr.remove(h)
        if ri == 0:
            ET.SubElement(tr_pr, q("tblHeader"))
        for ci, tc in enumerate(row.findall("w:tc", NS)):
            tc_pr = ensure(tc, "tcPr")
            move_to(tc, tc_pr, 0)
            tc_w = ensure(tc_pr, "tcW"); set_attr(tc_w, "type", "dxa"); set_attr(tc_w, "w", widths[ci])
            va = ensure(tc_pr, "vAlign"); set_attr(va, "val", "center")
            if ri == 0:
                shd = ensure(tc_pr, "shd"); set_attr(shd, "val", "clear"); set_attr(shd, "fill", "E8EEF5")
            for p in tc.findall("w:p", NS):
                p_pr = ensure(p, "pPr")
                move_to(p, p_pr, 0)
                spacing = ensure(p_pr, "spacing"); set_attr(spacing, "before", 0); set_attr(spacing, "after", 0); set_attr(spacing, "line", 240); set_attr(spacing, "lineRule", "auto")
                for r in p.findall("w:r", NS):
                    r_pr = ensure(r, "rPr")
                    move_to(r, r_pr, 0)
                    fonts = ensure(r_pr, "rFonts"); set_attr(fonts, "ascii", "Calibri"); set_attr(fonts, "hAnsi", "Calibri")
                    sz = ensure(r_pr, "sz"); set_attr(sz, "val", font_half_points)
                    szcs = ensure(r_pr, "szCs"); set_attr(szcs, "val", font_half_points)
                    if ri == 0 and r_pr.find("w:b", NS) is None: ET.SubElement(r_pr, q("b"))

with ZipFile(DOCX, "r") as source:
    files = {name: source.read(name) for name in source.namelist()}

root = ET.fromstring(files["word/document.xml"])

# Final status is applied only after the remediation render has passed inspection.
for node in root.findall(".//w:t", NS):
    if node.text:
        node.text = node.text.replace("Publication Ready — Canonical and Frozen", "Publication Ready — Remediation Verified")
        node.text = node.text.replace("Publication Remediation in Progress — Release on Hold", "Publication Ready — Remediation Verified")
        node.text = node.text.replace(
            "Detailed Deliverable identities are governed by Section 9 and detailed exit criteria by Sections 13–15.",
            "This is a derived matrix only. Section 13 exclusively governs Milestone titles, mappings, dependencies and Exit Criteria. Detailed Deliverable identities are governed by Section 9, and completion and acceptance are governed by Sections 14–15.",
        )

tables = root.findall(".//w:tbl", NS)
if len(tables) != 9:
    raise RuntimeError(f"Expected 9 tables, found {len(tables)}")

# Extract text only, then rebuild every table from clean schema-ordered OOXML. The source
# tables contain malformed layout residue that cannot be made portable by property edits.
table_data = []
for table in tables:
    table_data.append([
        ["".join(n.text or "" for n in tc.findall(".//w:t", NS)) for tc in row.findall("w:tc", NS)]
        for row in table.findall("w:tr", NS)
    ])

# Appendix C is a derived matrix. Replace its stale M1–M6 rows from authoritative Section 13.
matrix = [
    ("Milestone 1 — Expense Platform Complete", "Completed Project Expense workflow, API, authorization and financial controls", "End-to-end lifecycle, permitted/prohibited action, role, authorization and financial-control evidence"),
    ("Milestone 2 — Operator Workspace Complete", "Completed Operator Workspace and Operator-facing role-aware frontend integration", "Complete Operator journey, role-access, action-control, lifecycle and workspace-review evidence"),
    ("Milestone 3 — Evidence Layer Complete", "Completed Evidence Workflow and integrated Project Expense and evidence data flow", "Evidence association, classification, access, restriction, lifecycle-linkage and integrated data-flow evidence"),
    ("Milestone 4 — Investor Transparency Complete", "Completed Investor Transparency experience, operational and Investor reporting, and role-aware frontend integration", "Investor journey, role-access, disclosure/restriction, reporting, source-record comparison and authority-labelling evidence"),
    ("Milestone 5 — Beta Candidate Complete", "All Minimum Deliverables and the integrated controlled Beta demonstration", "End-to-end demonstration, integrated journeys, QA, security, deployment, documentation, traceability and completion-reporting evidence"),
]
table_data[5] = [["Milestone", "Principal result", "Evidence focus"], *[list(x) for x in matrix]]

width_sets = [
    [900, 2700, 1000, 2400, 1400, 1300],
    [3300, 1300, 5100],
    [2500, 5700, 1500],
    [2800, 6900],
    [3900, 3000, 2800],
    [2300, 3900, 3500],
    [2600, 7100],
    [2200, 3800, 3700],
    [2200, 3700, 3800],
]
font_sizes = [16, 17, 17, 18, 18, 18, 18, 18, 18]
body = root.find("w:body", NS)
rebuilt = []
for old, data, widths, size in zip(tables, table_data, width_sets, font_sizes):
    table = ET.Element(q("tbl"))
    for ri, values in enumerate(data):
        tr = ET.SubElement(table, q("tr"))
        for value in values:
            tc = ET.SubElement(tr, q("tc")); set_cell_text(tc, value, size, ri == 0)
    format_table(table, widths, size)
    index = list(body).index(old); body.remove(old); body.insert(index, table); rebuilt.append(table)

files["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
with NamedTemporaryFile(delete=False, suffix=".docx", dir=DOCX.parent) as tmp:
    tmp_path = Path(tmp.name)
with ZipFile(tmp_path, "w", ZIP_DEFLATED) as target:
    for name, data in files.items(): target.writestr(name, data)
tmp_path.replace(DOCX)
print(DOCX)
