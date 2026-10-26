import re

# ==============================================================================
# 1. UPDATE ASSEMBLE_MASTER_REPORT.PY
# ==============================================================================
asm_path = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\assemble_master_report.py"
with open(asm_path, "r", encoding="utf-8") as f:
    text = f.read()

# Margins: Left margin 1.5 inches for hole punch binding
old_margin = """# 1. Margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)"""

new_margin = """# 1. Margins (Left margin 1.5 inches for punch / binding space as requested)
for section in doc.sections:
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.5)
    section.right_margin = Inches(1)"""

if old_margin in text:
    text = text.replace(old_margin, new_margin)
    print("Updated margins in assemble_master_report.py to Left=1.5 inches!")
else:
    print("Warning: old_margin pattern not found")

# Sub head: 14 pt (p_heading2)
text = text.replace('run.font.size = Pt(13)', 'run.font.size = Pt(14)')
# Sub-sub head: 13 pt (p_heading3)
text = text.replace('run.font.size = Pt(11.5)', 'run.font.size = Pt(13)')

# Normal font size: 12 pt (p_body and p_bullet)
# Replace Pt(11) in p_body and p_bullet
body_pattern = """def p_body(text, space_before=0, space_after=6, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.italic = italic
    return p"""

new_body_pattern = """def p_body(text, space_before=0, space_after=6, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.italic = italic
    return p"""

if body_pattern in text:
    text = text.replace(body_pattern, new_body_pattern)
    print("Updated p_body font size to 12 pt!")
else:
    print("Warning: body_pattern not found")

bullet_pattern = """def p_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    return p"""

new_bullet_pattern = """def p_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p"""

if bullet_pattern in text:
    text = text.replace(bullet_pattern, new_bullet_pattern)
    print("Updated p_bullet font size to 12 pt!")
else:
    print("Warning: bullet_pattern not found")

# Table column width scaling to fit printable width 5.75 inches
old_tbl_w = """    # Column Widths
    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = Inches(w)"""

new_tbl_w = """    # Column Widths (Auto-scaled to fit within printable width: 5.75 inches)
    tot_w = sum(col_widths)
    max_avail_w = 5.75
    scale = (max_avail_w / tot_w) if tot_w > max_avail_w else 1.0
    scaled_widths = [w * scale for w in col_widths]
    for row in table.rows:
        for i, w in enumerate(scaled_widths):
            row.cells[i].width = Inches(w)"""

if old_tbl_w in text:
    text = text.replace(old_tbl_w, new_tbl_w)
    print("Updated table column scaling to fit within 5.75 inches!")

with open(asm_path, "w", encoding="utf-8") as f:
    f.write(text)

print("assemble_master_report.py successfully updated!")
