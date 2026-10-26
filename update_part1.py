import re

part1_path = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\report_content_part1.py"
with open(part1_path, "r", encoding="utf-8") as f:
    text = f.read()

# We need to replace the preliminary pages up to INDEX
# Let us find where TITLE starts and where INDEX starts
title_marker = "# PRELIMINARY: TITLE PAGE (Page 1)"
index_marker = "# PRELIMINARY: INDEX / TABLE OF CONTENTS (Pages 5 - 6)"

pos_title = text.find(title_marker)
pos_index = text.find(index_marker)

assert pos_title != -1, "Title marker not found"
assert pos_index != -1, "Index marker not found"

new_preliminary = """# PRELIMINARY: TITLE PAGE (Page 1)
    # ==============================================================================
    p_center("Project Report On", size=13, italic=True, space_before=20, space_after=6)
    p_center("DisasterConnectAI", size=26, bold=True, space_before=4, space_after=6, color=(128, 0, 32))
    p_center("An Intelligent Geolocation-Enabled Disaster Response, Incident Triage,\nand Volunteer Mobilization System",
             size=13, bold=True, space_before=4, space_after=20, color=(26, 54, 93))

    p_center("Designed By:", size=12, bold=True, space_after=2)
    p_center("Miss. Yogita Dilip Padvekar", size=15, bold=True, color=(128, 0, 32), space_after=18)

    p_center("Submitted To:", size=11, bold=True, space_after=2)
    p_center("K.M.S.P. MANDAL’S", size=12, bold=True, space_after=2)
    p_center("SANT RAWOOL MAHARAJ MAHAVIDYALAYA, KUDAL", size=16, bold=True, color=(128, 0, 32), space_after=4)
    p_center("(NAAC Re-Accreditation “B+” Grade)", size=11, italic=True, space_after=4)
    p_center("In the partial fulfillment of the requirements for the Degree of", size=11, italic=True, space_after=2)
    p_center("B.Sc. Computer Science (Sem V)", size=14, bold=True, space_after=18, color=(26, 54, 93))

    p_center("Under Guidance of:", size=11, italic=True, space_after=2)
    p_center("Asst. Prof. Santosh Chougule (M.C.A.)         Asst. Prof. Prakash Talankar (M.C.A.)", size=12, bold=True, space_after=18)

    p_center("Through:", size=11, italic=True, space_after=2)
    p_center("THE HEAD, DEPARTMENT OF COMPUTER SCIENCE,\nS.R.M. COLLEGE, KUDAL.", size=12, bold=True, space_after=16)

    p_center("PROJECT REPORT", size=13, bold=True, space_after=2)
    p_center("ACADEMIC YEAR: 2026 - 2027", size=12, bold=True, space_before=4)

    doc.add_page_break()

    # ==============================================================================
    # PRELIMINARY: DECLARATION (Page 2)
    # ==============================================================================
    p_center("DECLARATION", size=18, bold=True, underline=True, color=(128, 0, 32), space_before=16, space_after=20)

    p_body("To,\nThe Head,\nDepartment of Computer Science,\nS. R. M. College, Kudal.", space_after=12)
    p_body("Respected Sir,", space_after=10)

    decl_text = (
        "We undersigned, hereby declare that the project on \\"DisasterConnectAI\\" is developed "
        "under the guidance of our lecturer Asst. Prof. Santosh Chougule and Asst. Prof. Prakash Talankar.\\n\\n"
        "The conclusion in this report is based on the data, which is collected by me. I am declaring that this "
        "is our original work. I have not copied any materials related to my project from any unauthorized source.\\n\\n"
        "We do undersign that if my work is found to be copied, then I am liable to punishment as per the university rule."
    )
    p_body(decl_text, space_after=50)

    p_body("DATE: ____________________\\nPLACE: KUDAL.", bold_prefix="", space_after=40)

    p_center("____________________________________________", size=10, bold=True, space_after=4)
    p_center("(Miss. Yogita Dilip Padvekar)", size=13, bold=True, space_after=2)
    p_center("Candidate, B.Sc. Computer Science (Sem V)", size=11, italic=True)

    doc.add_page_break()

    # ==============================================================================
    # PRELIMINARY: CERTIFICATE (Page 3)
    # ==============================================================================
    p_center("K.M.S.P. MANDAL’S", size=12, bold=True, space_before=10, space_after=2)
    p_center("SANT RAWOOL MAHARAJ MAHAVIDYALAYA, KUDAL", size=16, bold=True, color=(128, 0, 32), space_after=4)
    p_center("NAAC RE-ACCREDITATION “B+” GRADE", size=11, bold=True, space_after=4)
    p_center("DEPARTMENT OF COMPUTER SCIENCE", size=13, bold=True, color=(26, 54, 93), space_after=16)

    p_center("CERTIFICATE", size=18, bold=True, underline=True, color=(128, 0, 32), space_after=20)

    cert_text = (
        "This is to certify that Miss. Yogita Dilip Padvekar having Exam Seat number ____________________ "
        "have satisfactorily carried out her project work entitled \\"DisasterConnectAI\\" as per the syllabus "
        "prescribed for B.Sc. Computer Science of Mumbai University, Mumbai.\\n\\n"
        "It is also certifying that this is her own work completed during academic year 2026 - 2027. "
        "The work done is satisfactory and is presented as per the specifications."
    )
    p_body(cert_text, space_after=50)

    p_center("____________________                ____________________                ____________________", size=10, bold=True, space_after=4)
    p_center("   Project Guide                      External Examiner                    Head of Department   ", size=11, bold=True, space_after=2)
    p_center("(Asst. Prof. S. Chougule)                                                  (Dept. of Computer Science)", size=9, italic=True, space_after=40)

    p_body("DATE: ____________________\\nPLACE: KUDAL.", bold_prefix="", space_after=10)

    doc.add_page_break()

    # ==============================================================================
    # CHAPTER I: ACKNOWLEDGMENT (Page 4)
    # ==============================================================================
    p_center("CHAPTER I", size=18, bold=True, space_before=30, space_after=8)
    p_center("Acknowledgment", size=22, bold=True, color=(128, 0, 32), underline=True, space_after=24)

    p_body(
        "It’s my great pleasure to get this opportunity and sincerely thank all the people, who have paved "
        "the way to create a successful project and helped me a lot during the completion of this project.", space_after=14
    )
    p_body(
        "I would like to thank my project guide, Asst. Prof. Santosh Chougule (M.C.A.) and Asst. Prof. Prakash Talankar (M.C.A.), "
        "who provided important information, technical advice, and guided me throughout the project completion.", space_after=14
    )
    p_body(
        "I am immensely thankful to The Head, Department of Computer Science, S.R.M. College, Kudal, and our Principal, "
        "Dr. S. D. Kulkarni, for providing access to computing laboratory infrastructure, internet connectivity, "
        "and continuous academic encouragement.", space_after=14
    )
    p_body(
        "And last but not the least! I would like to thank all my classmates, parents, and friends for their continuous "
        "support and cooperation throughout my studies.", space_after=36
    )

    p_body("Thank You.\\n\\nMiss. Yogita Dilip Padvekar", bold_prefix="", italic=True)

    doc.add_page_break()

    """

# Replace the preliminary part
new_text = text[:pos_title] + new_preliminary + text[pos_index:]

# Clean up corrupted bullets in index if any
new_text = new_text.replace("  ? ", "  • ").replace("   ", "  • ")

with open(part1_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("report_content_part1.py updated successfully with Miss. Yogita Dilip Padvekar preliminary pages!")
