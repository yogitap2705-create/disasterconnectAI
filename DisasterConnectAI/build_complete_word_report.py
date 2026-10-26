import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

ASSETS_DIR = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\report_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ==============================================================================
# STEP 1: GENERATE ARCHITECTURAL DIAGRAMS IF MISSING
# ==============================================================================
def generate_architectural_diagrams():
    # 1. Gantt Chart
    gantt_path = os.path.join(ASSETS_DIR, "gantt_chart.png")
    if not os.path.exists(gantt_path):
        fig, ax = plt.subplots(figsize=(8, 5.5), dpi=200)
        tasks = [
            "Testing & Implementation",
            "System Coding & AI Engine",
            "System Design",
            "System Analysis",
            "Preliminary Investigation"
        ]
        starts_prop = [4.5, 3.0, 2.0, 1.0, 0.0]
        durations_prop = [1.5, 2.5, 1.5, 1.5, 1.2]
        starts_act = [4.6, 3.1, 2.1, 1.1, 0.0]
        durations_act = [1.4, 2.4, 1.4, 1.4, 1.2]

        y_pos = range(len(tasks))
        ax.barh([y + 0.15 for y in y_pos], durations_prop, left=starts_prop, height=0.25, 
                color='white', edgecolor='black', linewidth=1.5, label='Proposed Time')
        ax.barh([y - 0.15 for y in y_pos], durations_act, left=starts_act, height=0.25, 
                color='#333333', edgecolor='black', linewidth=1.5, label='Actual Time')

        ax.set_yticks(y_pos)
        ax.set_yticklabels(tasks, fontsize=10, fontweight='bold')
        ax.set_xticks([0, 1.2, 2.5, 4.0, 6.0])
        ax.set_xticklabels(["July\n2025", "August\n2025", "September\n2025", "Oct-Nov\n2025", "December\n2025"], fontsize=9)
        ax.set_title("Gantt Chart - DisasterConnectAI Project Timeline", fontsize=13, fontweight='bold', pad=15)
        ax.legend(loc='lower right', framealpha=0.9)
        ax.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(gantt_path, bbox_inches='tight')
        plt.close()

    # 2. Lifecycle
    life_path = os.path.join(ASSETS_DIR, "lifecycle_diagram.png")
    if not os.path.exists(life_path):
        fig, ax = plt.subplots(figsize=(7, 8), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        boxes = {
            "Initialization": (2.5, 10.5), "Requirements": (6.5, 9.0),
            "Planning": (2.5, 7.5), "Design": (6.5, 7.5),
            "Implementation": (6.5, 5.0), "Evaluation": (2.5, 5.0),
            "Verification": (4.5, 3.0), "Deployment": (6.5, 1.0)
        }
        for name, (x, y) in boxes.items():
            rect = patches.FancyBboxPatch((x-1.4, y-0.45), 2.8, 0.9, boxstyle="round,pad=0.2", fc="#F8F9FA", ec="#1A365D", lw=2)
            ax.add_patch(rect)
            ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color="#1A365D")
        def arrow(x1, y1, x2, y2):
            ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(facecolor='#1A365D', edgecolor='#1A365D', width=1.5, headwidth=7, headlength=7))
        arrow(2.5, 10.0, 2.5, 8.0)
        arrow(2.5, 7.5, 5.1, 8.8)
        arrow(6.5, 8.5, 6.5, 8.0)
        arrow(6.5, 7.0, 6.5, 5.5)
        arrow(6.5, 4.5, 4.5, 3.5)
        arrow(4.5, 3.5, 2.5, 4.5)
        arrow(2.5, 5.5, 2.5, 7.0)
        arrow(6.5, 4.5, 6.5, 1.5)
        ax.set_title("Detailed Life Cycle of the Project (Iterative & Incremental)", fontsize=12, fontweight='bold')
        plt.tight_layout()
        plt.savefig(life_path, bbox_inches='tight')
        plt.close()

    # 3. DFD 0
    dfd0_path = os.path.join(ASSETS_DIR, "dfd_level0.png")
    if not os.path.exists(dfd0_path):
        fig, ax = plt.subplots(figsize=(8, 7), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        circle = patches.Circle((5, 5), 1.6, fc="#FFF5F5", ec="#800020", lw=2.5)
        ax.add_patch(circle)
        ax.text(5, 5.2, "DisasterConnectAI", ha='center', va='center', fontsize=11, fontweight='bold', color="#800020")
        ax.text(5, 4.6, "Central System\n(Level 0)", ha='center', va='center', fontsize=9, color="#444")
        modules = [
            ("User & Auth\nManagement", 5, 8.8),
            ("Incident Intake &\nGPS Detection", 8.3, 7.2),
            ("AI Triage &\nThreat Assessment", 8.3, 2.8),
            ("District Volunteer\nAssignment", 5, 1.2),
            ("In-App Tactical\nDispatch System", 1.7, 2.8),
            ("Shelter & Relief\nCamp Locator", 1.7, 7.2)
        ]
        for label, x, y in modules:
            rect = patches.FancyBboxPatch((x-1.3, y-0.5), 2.6, 1.0, boxstyle="square,pad=0.1", fc="#F0F4F8", ec="#2B6CB0", lw=1.8)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A365D")
            ax.annotate('', xy=(5 + (x-5)*0.55, 5 + (y-5)*0.55), xytext=(x - (x-5)*0.35, y - (y-5)*0.35),
                        arrowprops=dict(facecolor='#2B6CB0', edgecolor='#2B6CB0', width=1.2, headwidth=6, headlength=6))
        ax.set_title("Data Flow Diagram - Level 0 (Context Level)", fontsize=13, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(dfd0_path, bbox_inches='tight')
        plt.close()

    # 4. DFD 1
    dfd1_path = os.path.join(ASSETS_DIR, "dfd_level1.png")
    if not os.path.exists(dfd1_path):
        fig, ax = plt.subplots(figsize=(8.5, 9), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 11)
        ax.axis('off')
        center = patches.Circle((5, 5.5), 1.5, fc="#FFF5F5", ec="#800020", lw=2.5)
        ax.add_patch(center)
        ax.text(5, 5.6, "DisasterConnectAI", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#800020")
        ax.text(5, 5.1, "First Level DFD", ha='center', va='center', fontsize=8.5, color="#555")
        left_b = [
            ("User Registration\n& Auth Management", 1.8, 9.5),
            ("Incident Intake &\nGPS Coordinates", 1.8, 7.5),
            ("District Filter &\nJurisdiction Service", 1.8, 5.5),
            ("Volunteer Matching\n& Auto-Dispatch", 1.8, 3.5),
            ("Audit Logs &\nTelemetry Records", 1.8, 1.5),
        ]
        right_b = [
            ("AI Action Plan &\nThreat Assessment", 8.2, 9.5),
            ("Tactical Dispatch Hub\n& Mission Alert", 8.2, 7.5),
            ("Live Interactive Map\nVisualization", 8.2, 5.5),
            ("Relief Camps &\nShelter Capacity", 8.2, 3.5),
            ("Missing Persons &\nFamily Reunification", 8.2, 1.5),
        ]
        for label, x, y in left_b:
            rect = patches.FancyBboxPatch((x-1.5, y-0.45), 3.0, 0.9, boxstyle="square,pad=0.1", fc="#EDF2F7", ec="#2B6CB0", lw=1.5)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color="#1A365D")
            ax.annotate('', xy=(3.8, 5.5 + (y-5.5)*0.3), xytext=(x+1.5, y), arrowprops=dict(facecolor='#2B6CB0', edgecolor='#2B6CB0', width=1, headwidth=5))
        for label, x, y in right_b:
            rect = patches.FancyBboxPatch((x-1.5, y-0.45), 3.0, 0.9, boxstyle="square,pad=0.1", fc="#F7FAFC", ec="#C53030", lw=1.5)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color="#742A2A")
            ax.annotate('', xy=(x-1.5, y), xytext=(6.2, 5.5 + (y-5.5)*0.3), arrowprops=dict(facecolor='#C53030', edgecolor='#C53030', width=1, headwidth=5))
        ax.set_title("First Level Data Flow Diagram (Level 1 DFD)", fontsize=13, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(dfd1_path, bbox_inches='tight')
        plt.close()

    # 5. DFD 2
    dfd2_path = os.path.join(ASSETS_DIR, "dfd_level2.png")
    if not os.path.exists(dfd2_path):
        fig, ax = plt.subplots(figsize=(8, 9), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        rect = patches.FancyBboxPatch((0.5, 9.8), 2.0, 0.8, boxstyle="square,pad=0.1", fc="#E2E8F0", ec="#2D3748", lw=1.8)
        ax.add_patch(rect)
        ax.text(1.5, 10.2, "Citizen / Admin /\nVolunteer", ha='center', va='center', fontsize=8.5, fontweight='bold')
        nodes = [
            ("Login / Auth\nCheck", 4.5, 10.2), ("Verify Role &\nSession Token", 4.5, 8.2),
            ("Incident Intake &\nGPS Geolocation", 4.5, 6.2), ("AI Triage &\nRisk Calculation", 4.5, 4.2),
            ("District Dispatch &\nVolunteer Routing", 4.5, 2.2),
        ]
        outputs = [
            ("Render Command\nDashboard", 8.2, 10.2), ("Plot Incident on\nLive Map", 8.2, 8.2),
            ("Generate AI Survival\nAction Plan", 8.2, 6.2), ("Send Tactical Mission\nDispatch Order", 8.2, 4.2),
            ("Update Mission Status &\nResolve Incident", 8.2, 2.2),
        ]
        for label, x, y in nodes:
            circle = patches.Circle((x, y), 0.75, fc="#FEFCBF", ec="#D69E2E", lw=1.8)
            ax.add_patch(circle)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#744210")
        for label, x, y in outputs:
            r = patches.FancyBboxPatch((x-1.3, y-0.45), 2.6, 0.9, boxstyle="square,pad=0.1", fc="#EBF8FF", ec="#3182CE", lw=1.5)
            ax.add_patch(r)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#2B6CB0")
        ax.annotate('', xy=(3.75, 10.2), xytext=(2.5, 10.2), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(4.5, 8.95), xytext=(4.5, 9.45), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(4.5, 6.95), xytext=(4.5, 7.45), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(4.5, 4.95), xytext=(4.5, 5.45), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(4.5, 2.95), xytext=(4.5, 3.45), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        for i in range(5):
            ax.annotate('', xy=(6.9, nodes[i][2]), xytext=(5.25, nodes[i][2]), arrowprops=dict(facecolor='#3182CE', edgecolor='#3182CE', width=1, headwidth=5))
        ax.set_title("Second Level Data Flow Diagram (Level 2 DFD)", fontsize=13, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(dfd2_path, bbox_inches='tight')
        plt.close()

    # 6. ERD
    erd_path = os.path.join(ASSETS_DIR, "erd_diagram.png")
    if not os.path.exists(erd_path):
        fig, ax = plt.subplots(figsize=(9, 8), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        entities = [("User", 2, 8), ("Disaster", 8, 8), ("Volunteer", 2, 2), ("Notification", 8, 2), ("Shelter", 5, 5)]
        for name, x, y in entities:
            rect = patches.FancyBboxPatch((x-1.1, y-0.5), 2.2, 1.0, boxstyle="square,pad=0.1", fc="#EBF8FF", ec="#2B6CB0", lw=2)
            ax.add_patch(rect)
            ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold', color="#1A365D")
        relations = [("Reports", 5, 8), ("Assigned To", 5, 2), ("Dispatches", 8, 5), ("Registers", 2, 5)]
        for label, x, y in relations:
            diamond = patches.Polygon([[x, y+0.45], [x+0.8, y], [x, y-0.45], [x-0.8, y]], closed=True, fc="#FEFCBF", ec="#B7791F", lw=1.5)
            ax.add_patch(diamond)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#744210")
        def line(x1, y1, x2, y2): ax.plot([x1, x2], [y1, y2], color="#4A5568", lw=1.5)
        line(3.1, 8, 4.2, 8); line(5.8, 8, 6.9, 8); line(3.1, 2, 4.2, 2); line(5.8, 2, 6.9, 2)
        line(2, 7.5, 2, 5.45); line(2, 4.55, 2, 2.5); line(8, 7.5, 8, 5.45); line(8, 4.55, 8, 2.5); line(5, 7.55, 5, 5.5)
        ax.set_title("Entity Relationship Diagram (ERD) - DisasterConnectAI Data Architecture", fontsize=13, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(erd_path, bbox_inches='tight')
        plt.close()

    # 7. Activity
    act_path = os.path.join(ASSETS_DIR, "activity_diagram.png")
    if not os.path.exists(act_path):
        fig, ax = plt.subplots(figsize=(7, 9), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        ax.add_patch(patches.Circle((5, 11.2), 0.35, fc="black", ec="black"))
        steps = [
            ("Citizen Logs In / Registers", 10.0),
            ("Captures Incident & GPS Coordinates", 8.6),
            ("AI Engine Calculates Severity & Risk Score", 7.2),
            ("Incident Plotted on Live GIS Map", 5.8),
            ("Admin Auto-Assigns District Volunteer", 4.4),
            ("Volunteer Receives Tactical Mission Briefing", 3.0),
            ("Rescue Mission Executed & Marked Resolved", 1.6)
        ]
        for label, y in steps:
            rect = patches.FancyBboxPatch((2.2, y-0.45), 5.6, 0.9, boxstyle="round,pad=0.2", fc="#F7FAFC", ec="#800020", lw=1.8)
            ax.add_patch(rect)
            ax.text(5, y, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#800020")
        ax.add_patch(patches.Circle((5, 0.4), 0.35, fc="white", ec="black", lw=1.5))
        ax.add_patch(patches.Circle((5, 0.4), 0.22, fc="black", ec="black"))
        ax.annotate('', xy=(5, 10.45), xytext=(5, 10.85), arrowprops=dict(facecolor='black', width=1.2, headwidth=5))
        for i in range(len(steps)-1):
            ax.annotate('', xy=(5, steps[i+1][1]+0.45), xytext=(5, steps[i][1]-0.45), arrowprops=dict(facecolor='black', width=1.2, headwidth=5))
        ax.annotate('', xy=(5, 0.75), xytext=(5, steps[-1][1]-0.45), arrowprops=dict(facecolor='black', width=1.2, headwidth=5))
        ax.set_title("Activity Diagram - Emergency Response Lifecycle", fontsize=12, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(act_path, bbox_inches='tight')
        plt.close()

    # 8. Use Case
    uc_path = os.path.join(ASSETS_DIR, "usecase_diagram.png")
    if not os.path.exists(uc_path):
        fig, ax = plt.subplots(figsize=(9, 8), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.add_patch(patches.Rectangle((2.8, 0.5), 4.4, 9.0, fc="#FCFDFF", ec="#1A365D", lw=2, linestyle="--"))
        ax.text(5.0, 9.2, "DisasterConnectAI Platform", ha='center', va='center', fontsize=11, fontweight='bold', color="#1A365D")
        def draw_actor(x, y, name):
            ax.add_patch(patches.Circle((x, y+0.4), 0.2, fc="#CBD5E0", ec="black", lw=1.2))
            ax.plot([x, x], [y+0.2, y-0.2], color="black", lw=1.5)
            ax.plot([x-0.25, x+0.25], [y+0.05, y+0.05], color="black", lw=1.5)
            ax.plot([x, x-0.2], [y-0.2, y-0.5], color="black", lw=1.5)
            ax.plot([x, x+0.2], [y-0.2, y-0.5], color="black", lw=1.5)
            ax.text(x, y-0.75, name, ha='center', va='center', fontsize=8.5, fontweight='bold')
        draw_actor(1.2, 7.5, "Citizen")
        draw_actor(1.2, 2.5, "Volunteer")
        draw_actor(8.8, 5.0, "Disaster\nAdministrator")
        use_cases = [
            ("Submit Disaster Report", 8.2), ("Instant SOS & GPS Lock", 7.0),
            ("View Live Incident Map", 5.8), ("Locate Relief Shelters", 4.6),
            ("View Tactical Mission Orders", 3.4), ("Auto-Assign District Force", 2.2),
            ("Resolve & Update Status", 1.0)
        ]
        for label, y in use_cases:
            ax.add_patch(patches.Ellipse((5.0, y), 3.4, 0.7, fc="#EDF2F7", ec="#2B6CB0", lw=1.5))
            ax.text(5.0, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#2C5282")
        ax.plot([1.4, 3.3], [7.5, 8.2], color="#718096", lw=1); ax.plot([1.4, 3.3], [7.5, 7.0], color="#718096", lw=1)
        ax.plot([1.4, 3.3], [7.5, 5.8], color="#718096", lw=1); ax.plot([1.4, 3.3], [7.5, 4.6], color="#718096", lw=1)
        ax.plot([1.4, 3.3], [2.5, 3.4], color="#718096", lw=1); ax.plot([1.4, 3.3], [2.5, 5.8], color="#718096", lw=1)
        ax.plot([1.4, 3.3], [2.5, 1.0], color="#718096", lw=1)
        ax.plot([8.6, 6.7], [5.0, 5.8], color="#718096", lw=1); ax.plot([8.6, 6.7], [5.0, 4.6], color="#718096", lw=1)
        ax.plot([8.6, 6.7], [5.0, 2.2], color="#718096", lw=1); ax.plot([8.6, 6.7], [5.0, 1.0], color="#718096", lw=1)
        ax.set_title("Use Case Diagram - DisasterConnectAI Roles & Capabilities", fontsize=12, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(uc_path, bbox_inches='tight')
        plt.close()

    # 9. Class
    cls_path = os.path.join(ASSETS_DIR, "class_diagram.png")
    if not os.path.exists(cls_path):
        fig, ax = plt.subplots(figsize=(9, 8), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        classes = [
            ("User\n---\n- id: String\n- fullName: String\n- role: String\n- district: String\n---\n+ register()\n+ login()", 1.8, 7.5),
            ("Disaster\n---\n- id: String\n- disasterType: String\n- severity: String\n- aiRiskScore: Number\n- district: String\n---\n+ createReport()\n+ updateStatus()", 5.0, 7.5),
            ("Volunteer\n---\n- id: String\n- skills: String\n- district: String\n- availability: Boolean\n---\n+ acceptMission()\n+ completeTask()", 8.2, 7.5),
            ("Notification\n---\n- recipient: ObjectId\n- subject: String\n- messageHtml: String\n- deliveryStatus: String\n---\n+ sendInApp()\n+ acknowledge()", 2.5, 2.8),
            ("AIEngine\n---\n- geminiModel: String\n- triageRules: Array\n---\n+ assessThreat()\n+ generateSOP()\n+ recommendSupplies()", 7.5, 2.8),
        ]
        for label, x, y in classes:
            rect = patches.FancyBboxPatch((x-1.3, y-1.1), 2.6, 2.2, boxstyle="square,pad=0.1", fc="#FFFFFF", ec="#800020", lw=1.8)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.2, family='monospace', color="#1A202C")
        ax.annotate('', xy=(3.7, 7.5), xytext=(3.1, 7.5), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(6.9, 7.5), xytext=(6.3, 7.5), arrowprops=dict(facecolor='black', width=1, headwidth=5))
        ax.annotate('', xy=(5.0, 6.4), xytext=(2.5, 3.9), arrowprops=dict(facecolor='#800020', edgecolor='#800020', width=1, headwidth=5))
        ax.annotate('', xy=(5.0, 6.4), xytext=(7.5, 3.9), arrowprops=dict(facecolor='#800020', edgecolor='#800020', width=1, headwidth=5))
        ax.set_title("Class Diagram - Core System Entities & Controllers", fontsize=12, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(cls_path, bbox_inches='tight')
        plt.close()

    # 10. Object
    obj_path = os.path.join(ASSETS_DIR, "object_diagram.png")
    if not os.path.exists(obj_path):
        fig, ax = plt.subplots(figsize=(9, 8), dpi=200)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        objects = [
            ("user1 : User\n---\nfullName = 'Rohit Patil'\nrole = 'citizen'\ndistrict = 'Pune'", 2.0, 7.5),
            ("disaster1 : Disaster\n---\ntype = 'Flood'\nseverity = 'High'\nriskScore = 8.8\ndistrict = 'Pune'", 5.0, 7.5),
            ("vol1 : Volunteer\n---\nfullName = 'Sunil Shinde'\ndistrict = 'Pune'\nstatus = 'Assigned'", 8.0, 7.5),
            ("notif1 : Notification\n---\nstatus = 'delivered_in_app'\nacknowledged = true", 5.0, 3.0),
        ]
        for label, x, y in objects:
            rect = patches.FancyBboxPatch((x-1.3, y-0.9), 2.6, 1.8, boxstyle="square,pad=0.1", fc="#FEFCBF", ec="#B7791F", lw=1.8)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.5, family='monospace', color="#744210")
        ax.plot([3.3, 3.7], [7.5, 7.5], color="#4A5568", lw=1.5)
        ax.plot([6.3, 6.7], [7.5, 7.5], color="#4A5568", lw=1.5)
        ax.plot([5.0, 5.0], [6.6, 3.9], color="#4A5568", lw=1.5)
        ax.set_title("Object Diagram - Runtime Operational State Example", fontsize=12, fontweight='bold', pad=10)
        plt.tight_layout()
        plt.savefig(obj_path, bbox_inches='tight')
        plt.close()

generate_architectural_diagrams()
print("Architectural diagrams verified.")

# ==============================================================================
# STEP 2: ASSEMBLE WORD DOCUMENT
# ==============================================================================
doc = docx.Document()

for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

def add_page_border(section):
    sectPr = section._sectPr
    pgBorders = parse_xml(
        f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">'
        f'  <w:top w:val="double" w:sz="12" w:space="24" w:color="000000"/>'
        f'  <w:left w:val="double" w:sz="12" w:space="24" w:color="000000"/>'
        f'  <w:bottom w:val="double" w:sz="12" w:space="24" w:color="000000"/>'
        f'  <w:right w:val="double" w:sz="12" w:space="24" w:color="000000"/>'
        f'</w:pgBorders>'
    )
    sectPr.append(pgBorders)

add_page_border(doc.sections[0])

def p_center(text, size=12, bold=False, italic=False, space_before=0, space_after=6, color=(0,0,0), underline=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    run.font.color.rgb = RGBColor(*color)
    return p

def p_heading1(text, space_before=16, space_after=10, color=(128, 0, 32)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.underline = True
    run.font.color.rgb = RGBColor(*color)
    return p

def p_heading2(text, space_before=12, space_after=6, color=(26, 54, 93)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(*color)
    return p

def p_body(text, space_before=0, space_after=6, bold_prefix="", italic=False):
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
    return p

def p_bullet(text, bold_prefix=""):
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
    return p

def add_image(filename, width_inch=5.5, caption=""):
    full_path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(full_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run()
        run.add_picture(full_path, width=Inches(width_inch))
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = "Times New Roman"
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(90, 90, 90)

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_code_block(title, code_text):
    p_t = doc.add_paragraph()
    p_t.paragraph_format.space_before = Pt(10)
    p_t.paragraph_format.space_after = Pt(2)
    r_t = p_t.add_run(title)
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(10.5)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(128, 0, 32)

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8F9FA")
    set_table_borders(table, color="D0D0D0", sz="4")
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(33, 37, 41)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(4)

print("Starting document creation...")

# ==============================================================================
# TITLE PAGE
# ==============================================================================
p_center("A", size=16, bold=True, space_before=20, space_after=6)
p_center("Project Report On", size=14, bold=True, underline=True, space_after=24)
p_center("DisasterConnectAI:", size=22, bold=True, color=(128, 0, 32), space_after=4)
p_center("Real-Time Intelligent Disaster Management &\nEmergency Response Platform", size=16, bold=True, underline=True, color=(128, 0, 32), space_after=28)

p_center("Designed By:", size=13, bold=True, underline=True, space_after=6)
p_center("Mr. / Miss. [Student Name]", size=12, bold=True, space_after=2)
p_center("Exam Seat Number: [______________]", size=11, italic=True, space_after=24)

p_center("Submitted To:", size=13, bold=True, underline=True, space_after=6)
p_center("K.M.S.P. MANDAL’S", size=12, bold=True, space_after=2)
p_center("SANT RAWOOL MAHARAJ MAHAVIDYALAYA, KUDAL.", size=13, bold=True, space_after=2)
p_center("(NAAC Re-Accreditation “B+” Grade)", size=11, italic=True, space_after=6)
p_center("In the partial fulfillment of", size=11, space_after=2)
p_center("B.Sc. Computer Science (Sem V)", size=12, bold=True, space_after=20)

p_center("Under Guidance of:", size=13, bold=True, underline=True, space_after=6)
p_center("Asst. Prof. Santosh Chougule (M.C.A.)", size=11.5, bold=True, space_after=2)
p_center("Asst. Prof. Prakash Talankar (M.C.A.)", size=11.5, bold=True, space_after=20)

p_center("Through:", size=13, bold=True, underline=True, space_after=6)
p_center("THE HEAD,", size=11, bold=True, space_after=2)
p_center("DEPARTMENT OF COMPUTER SCIENCE,", size=11, bold=True, space_after=2)
p_center("S.R.M. COLLEGE, KUDAL.", size=11, bold=True, space_after=24)

p_center("PROJECT REPORT", size=14, bold=True, space_after=2)
p_center("2025-26", size=13, bold=True, space_after=0)

doc.add_page_break()

# ==============================================================================
# DECLARATION
# ==============================================================================
p_center("DECLARATION", size=18, bold=True, underline=True, space_before=15, space_after=30)
p_body("To,")
p_body("The Head,")
p_body("Department of Computer Science,")
p_body("S. R. M. College, Kudal.")
p_body("Respected Sir,")
p_body("We undersigned, hereby declare that the project on \"DisasterConnectAI\" is developed under the guidance of our lecturer Asst. Prof. Santosh Chougule.", space_after=12)
p_body("The conclusion in this report is based on the data, which is collected by me. I am declaring that this is our original work. I have not copied any materials related to my project.", space_after=12)
p_body("We do undersign that if my work is found to be copied, then I am liable to punishment as per the university rule.", space_after=40)
p_body("DATE:")
p_body("PLACE: KUDAL.")
p_center("(Mr. / Miss. [Student Name])", size=12, bold=True, space_before=30)
doc.add_page_break()

# ==============================================================================
# CERTIFICATE
# ==============================================================================
p_center("K.M.S.P. MANDAL’S", size=13, bold=True, space_before=10, space_after=2)
p_center("SANT RAWOOL MAHARAJ MAHAVIDYALAYA,", size=14, bold=True, space_after=2)
p_center("KUDAL.", size=14, bold=True, space_after=4)
p_center("NAAC RE-ACCREDITATION “B+” GRADE", size=11, bold=True, space_after=24)
p_center("CERTIFICATE", size=18, bold=True, underline=True, space_after=24)

p_body("This is to certify that Mr. / Miss. [Student Name] having Exam Seat number ____________________ has satisfactorily carried out her/his project work entitled:", space_after=14)
p_center("DisasterConnectAI:", size=16, bold=True, color=(128, 0, 32), space_after=2)
p_center("Real-Time Intelligent Disaster Management & Emergency Response Platform", size=13, bold=True, space_after=16)
p_body("As per the syllabus prescribed for B.SC. Computer Science of Mumbai University, Mumbai.", space_after=14)
p_body("It is also certifying that this is her/his own work completed during academic year 2025-26. The work done is satisfactory and is presented as per the specifications.", space_after=50)

sig_table = doc.add_table(rows=1, cols=3)
sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
for cell in sig_table.rows[0].cells:
    cell.width = Inches(2.1)
c0, c1, c2 = sig_table.rows[0].cells
c0.paragraphs[0].text = "Project Guide\n\n\n(Asst. Prof. S. R. Chougule)"
c0.paragraphs[0].runs[0].font.name = "Times New Roman"
c0.paragraphs[0].runs[0].font.bold = True
c1.paragraphs[0].text = "External Examiner\n\n\n(Sign & Date)"
c1.paragraphs[0].runs[0].font.name = "Times New Roman"
c1.paragraphs[0].runs[0].font.bold = True
c2.paragraphs[0].text = "Head of Department\n\n\n(Department Seal)"
c2.paragraphs[0].runs[0].font.name = "Times New Roman"
c2.paragraphs[0].runs[0].font.bold = True

p_body("DATE:", space_before=30)
doc.add_page_break()

# ==============================================================================
# ACKNOWLEDGEMENT
# ==============================================================================
p_center("ACKNOWLEDGEMENT", size=18, bold=True, underline=True, space_before=20, space_after=24)
p_body("It’s my great pleasure to get this opportunity and sincerely thank all the people, who paved the way to create a successful project and helped me immensely during the completion of this project.", space_after=12)
p_body("I would like to express my deepest gratitude to my project guide, Asst. Prof. S. R. Chougule, who provided invaluable insights, domain guidance, and technical direction throughout the development of DisasterConnectAI.", space_after=12)
p_body("I also extend my sincere thanks to Asst. Prof. Prakash Talankar and the Head of the Department of Computer Science for their academic encouragement and state-of-the-art laboratory facilities.", space_after=12)
p_body("And last but not the least! I would like to thank my family, college faculty, and all my classmates for their constant moral support, technical discussions, and testing feedback.", space_after=36)
p_center("Thank You.", size=14, bold=True, space_after=36)
p_center("Mr. / Miss. [Student Name]", size=12, bold=True)
doc.add_page_break()

# ==============================================================================
# INDEX
# ==============================================================================
p_center("INDEX", size=20, bold=True, underline=True, space_before=10, space_after=18)

index_data = [
    ("1.", "I", "Acknowledgment", "iv"),
    ("2.", "II", "Synopsis of the Project\n  • Problem Statement\n  • Objective & Scope\n  • Process Description", "1 - 3"),
    ("3.", "III", "Main Report\n"
                  "  • Objective & Scope of the Project\n"
                  "  • Theoretical Background\n"
                  "  • Survey of Literature\n"
                  "  • Research Analysis and Design\n"
                  "  • System Planning & Gantt Chart\n"
                  "  • Details of Hardware & Software Used\n"
                  "  • Detailed Life Cycle of the Project (Iterative Model)\n"
                  "  • Data Flow Diagrams (Level 0, Level 1, Level 2)\n"
                  "  • Entity Relationship Diagram (ERD)\n"
                  "  • Activity Diagram\n"
                  "  • Class Diagram\n"
                  "  • Object Diagram\n"
                  "  • Use Case Diagram\n"
                  "  • Input and Output Screen Design (Desktop Screen Widescreen Views)\n"
                  "  • Process Involved & Emergency Workflows\n"
                  "  • Methodology Used for Testing (Manual Testing)\n"
                  "  • Test Cases & Test Reports\n"
                  "  • Code of the Project", "4 - 48"),
    ("4.", "IV", "Annexure\n  • Database Collection Schemas (MongoDB)\n  • RESTful API Endpoints Specification", "49 - 52"),
    ("5.", "V", "Conclusion", "53 - 54"),
    ("6.", "VI", "Future Enhancement", "55 - 56"),
    ("7.", "VII", "References & Bibliography", "57 - 58"),
]

idx_table = doc.add_table(rows=1, cols=4)
idx_table.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(idx_table, color="B0B0B0", sz="4")

headers = ["Sr. No.", "Chapter No.", "Title", "Page No."]
for i, h in enumerate(headers):
    cell = idx_table.rows[0].cells[i]
    cell.paragraphs[0].text = h
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell.paragraphs[0].runs[0].font.bold = True
    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
    set_cell_background(cell, "F0F4F8")

widths = [Inches(0.8), Inches(1.1), Inches(3.7), Inches(0.9)]
for row_data in index_data:
    row = idx_table.add_row()
    for col_idx, text in enumerate(row_data):
        cell = row.cells[col_idx]
        cell.width = widths[col_idx]
        p_c = cell.paragraphs[0]
        p_c.text = text
        p_c.runs[0].font.name = "Times New Roman"
        p_c.runs[0].font.size = Pt(10)
        p_c.paragraph_format.space_before = Pt(3)
        p_c.paragraph_format.space_after = Pt(3)
        if col_idx in [0, 1, 3]:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_c.runs[0].font.bold = True

doc.add_page_break()

# ==============================================================================
# CHAPTER II: SYNOPSIS OF THE PROJECT
# ==============================================================================
p_center("CHAPTER II", size=18, bold=True, space_before=150, space_after=12)
p_center("Synopsis of the Project", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("DisasterConnectAI - Project Synopsis")

p_heading2("Problem Statement:")
p_body(
    "Disasters—both natural (such as flash floods, severe landslides, earthquakes, and cyclonic storm surges) and technological/industrial hazards (such as chemical leaks and factory fires)—strike with rapid onset and catastrophic consequences. During such crises, conventional emergency communication channels experience catastrophic failures. Phone lines become congested, 112/108 helplines face extreme wait times, and emergency dispatch centers struggle to filter duplicate, chaotic, and panic-driven public reports.",
    space_after=8
)
p_body("Current emergency handling mechanisms in developing regions suffer from three fatal bottlenecks:", space_after=4)
p_bullet("Lack of Structured Information: Citizens post unverified, panic-driven videos on social media without precise geolocation, trapped civilian counts, or hazard classification.", bold_prefix="1.")
p_bullet("Absence of Automated Triage: District collectorate control rooms are overwhelmed by hundreds of simultaneous calls, leaving them unable to scientifically prioritize life-critical incidents over minor disruptions.", bold_prefix="2.")
p_bullet("Delayed Volunteer Mobilization: Relief volunteers are organized haphazardly over chat groups without structured task orders, district jurisdiction matching, or real-time status tracking.", bold_prefix="3.")

p_heading2("Objective & Scope:")
p_body("DisasterConnectAI is engineered as an enterprise-grade, real-time crisis intelligence and disaster management platform to solve these critical bottlenecks through modern web architecture and artificial intelligence:")
p_bullet("Real-Time Incident Intake & One-Tap SOS: To provide citizens with an instant emergency intake interface that auto-captures high-accuracy GPS coordinates, photo evidence, and danger assessments in under 15 seconds.", bold_prefix="•")
p_bullet("AI-Powered Threat Assessment & Triage Scoring: To leverage an automated AI triage engine that evaluates hazards on a 1-to-10 risk scale, structures citizen narratives into actionable crisis briefs, and generates immediate civilian survival SOPs.", bold_prefix="•")
p_bullet("Statewide District Command & 1-Click Dispatch: To furnish disaster administrators with a real-time command dashboard featuring Maharashtra's 36 districts, live GIS mapping, and 1-click nearest matching volunteer allocation.", bold_prefix="•")
p_bullet("Relief Infrastructure Hub: To provide real-time evacuation shelter registers with live bed occupancy meters, 24/7 statewide emergency directory, family tracing for missing persons, and standard operating crisis checklists.", bold_prefix="•")

p_heading2("Process Description:")
p_body(
    "Traditional disaster management relies heavily on manual coordination: stranded citizens dial emergency helplines or rely on family members; collectorate staff manually write down notes on paper or spreadsheets; and field rescue teams are dispatched through ad-hoc telephone calls. This creates unacceptable latency, miscommunication, and tragic loss of life during the crucial 'Golden Hour' of survival.",
    space_after=8
)
p_body(
    "DisasterConnectAI transforms this fragmented process into an automated, synchronized digital command pipeline. When a citizen submits a disaster report or triggers an Instant SOS, the system's AI engine immediately processes the telemetry: computing severity, generating a tailored survival plan, and plotting the incident on the real-time Leaflet GIS map.",
    space_after=8
)
p_body(
    "District administrators can immediately execute 1-Click Auto Dispatch to allocate the nearest qualified volunteer (e.g., Water Rescue Specialist or Hazmat Technician in Pune or Nashik). Mission orders are immediately transmitted with formatted operational guidelines, while live evacuation shelter capacities guide displaced families to safety.",
    space_after=12
)

doc.add_page_break()

# ==============================================================================
# CHAPTER III: MAIN REPORT
# ==============================================================================
p_center("CHAPTER III", size=18, bold=True, space_before=150, space_after=12)
p_center("Main Report", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("1. Objective and Scope")
p_body("DisasterConnectAI is designed to provide immediate crisis triage, unified volunteer coordination, and real-time situational awareness during catastrophic natural and technological emergencies. Key objectives include:")
p_bullet("Instant Emergency Reporting & GPS Geolocation: Allows affected citizens to submit disaster incidents with live GPS latitude/longitude, category selection, and photo verification in seconds.", bold_prefix="1.")
p_bullet("AI Automated Triage & Priority Scoring: Eliminates administrative bottlenecks by computing dynamic hazard scores (1 to 10), drafting standardized incident summaries, and providing citizens with instant life-saving checklists.", bold_prefix="2.")
p_bullet("Interactive Geospatial Mapping: Integrates high-performance Leaflet GIS to render color-coded severity heatmaps and district incident markers for comprehensive situational awareness.", bold_prefix="3.")
p_bullet("1-Click District Volunteer Allocation: Matches incident districts with registered volunteer skillsets (e.g., Medical First Aid, Flood Rescue, Hazmat Support) for instant dispatch.", bold_prefix="4.")
p_bullet("Statewide Crisis Resource Ecosystem: Unifies evacuation camp bed occupancy gauges, 24/7 district control room helplines, family reunification registry, and interactive SOP checklists into a single responsive web portal.", bold_prefix="5.")

p_heading1("2. Theoretical Background")
p_body(
    "The theoretical foundation of DisasterConnectAI is anchored in multidisciplinary frameworks spanning Disaster Risk Reduction (DRR), the Incident Command System (ICS), the Golden Hour principle in emergency medicine, and Artificial Intelligence Decision Support Systems (DSS).",
    space_after=8
)
p_body(
    "Disaster Risk Reduction & Incident Command System (ICS): ICS is a standardized on-scene emergency management concept designed to provide integrated organizational structure without being hindered by jurisdictional boundaries. DisasterConnectAI digitally instantiates ICS by establishing clear hierarchical roles (Citizen Reporter, Field Volunteer, Incident Commander/Admin) and structured message pipelines.",
    space_after=8
)
p_body(
    "The 'Golden Hour' Concept: Emergency trauma medicine recognizes that the first 60 minutes following catastrophic injury or disaster onset are the most decisive in preventing mortality. Manual call handling and uncoordinated rescue operations invariably consume this window. DisasterConnectAI compresses intake, automated triage, and volunteer dispatch to less than 60 seconds, restoring the Golden Hour to emergency responders.",
    space_after=8
)
p_body(
    "Geographic Information Systems (GIS): Real-time spatial clustering of citizen incident coordinates allows emergency administrators to detect disaster epicenters, track flood propagation, and delineate safe evacuation corridors away from hazard perimeters.",
    space_after=12
)

p_heading1("3. Survey of Literature")
p_body("A thorough literature survey was conducted across existing national and international emergency response platforms:", space_after=6)
p_bullet("National Disaster Management Authority (NDMA) Portals: Government portals in India provide strategic alerts and meteorological advisories but lack interactive, two-way civilian intake, instant volunteer routing, or real-time shelter bed capacity tracking.", bold_prefix="1.")
p_bullet("Social Media-Based Crisis Mapping: While social platforms enable rapid dissemination, they suffer from high noise-to-signal ratios, unverified rumors, lack of structured GIS telemetry, and absence of verifiable dispatch tracking.", bold_prefix="2.")
p_bullet("Traditional SOS Mobile Apps: Existing mobile apps primarily cater to individual personal safety through SMS triggers. They do not support multi-hazard incident intake, district-wide triage, volunteer resource matching, or community evacuation management.", bold_prefix="3.")

p_heading1("4. Research Analysis and Design")
p_heading2("4.1 Introduction")
p_body("To bridge these critical shortcomings, DisasterConnectAI was engineered as a comprehensive full-stack platform uniting citizens, rescue volunteers, and district authorities. It provides an intuitive, high-speed desktop web application, resilient cloud data persistence, and an automated AI triage subsystem.", space_after=8)

p_heading2("4.2 System Requirements Analysis")
p_body("Functional Requirements:")
p_bullet("User Authentication & RBAC: Secure JWT-based registration and login with role-based access control (Citizen, Volunteer, Administrator) and 1-Click quick command access for emergency drills.", bold_prefix="•")
p_bullet("Incident Intake & GPS Lock: Responsive intake form with HTML5 Geolocation API, district dropdown (all 36 Maharashtra districts), image evidence upload via Multer, and Instant SOS trigger.", bold_prefix="•")
p_bullet("AI Triage Subsystem: Automated evaluation of disaster severity, risk scoring (1-10), threat summary generation, and supply recommendations.", bold_prefix="•")
p_bullet("Real-Time GIS Mapping: Leaflet-powered map displaying active incidents with dynamic color-coded markers, popups, and district filters.", bold_prefix="•")
p_bullet("District Volunteer Dispatch: Automated and manual allocation of volunteers based on district matching and specialized skills.", bold_prefix="•")
p_bullet("Evacuation Shelters Registry: Interactive camp locator displaying verified amenities (Food, Water, Medical, Power) and live bed occupancy progress bars.", bold_prefix="•")
p_bullet("Missing Persons Registry: Citizen reporting portal for tracing lost family members with search by district and 1-click 'Mark Safe' status update.", bold_prefix="•")
p_bullet("Emergency Helplines Directory: Comprehensive contact directory for central helplines (112, 108, NDRF 1078, 101) and all 36 Maharashtra district control rooms.", bold_prefix="•")

p_body("Non-Functional Requirements:", space_before=8)
p_bullet("High Availability & Reliability: High system uptime ensuring uninterrupted crisis command and reliable incident submission.", bold_prefix="•")
p_bullet("Performance & Responsiveness: Page load and API response times under 200ms on 4G/5G networks. Vite-optimized bundle sizes.", bold_prefix="•")
p_bullet("Accessibility & Visual Standards: Strict avoidance of informal/colorful emojis in compliance with professional emergency defense standards, utilizing clean monochrome vector icons (FontAwesome/react-icons).", bold_prefix="•")
p_bullet("Widescreen Desktop Interface: Optimized for command centers, desktop monitors, and laptop displays for high-volume operational control.", bold_prefix="•")

p_heading2("4.3 Design of the System")
p_heading2("1.1 System Architecture")
p_body("A clean, decoupled 5-tier layered architecture is implemented for DisasterConnectAI, ensuring scalability, security, and high maintainability:", space_after=6)
p_bullet("Presentation Layer (Client): React 19 single-page application built with Vite, featuring modular components, reactive state management, and Leaflet GIS mapping.", bold_prefix="1.")
p_bullet("API & Routing Layer: Express.js RESTful API providing structured endpoints for auth, incident intake, dispatch, shelters, notifications, and AI chat.", bold_prefix="2.")
p_bullet("Business Logic & Triage Layer: Node.js controllers managing RBAC, district matching algorithms, file upload pipelines, and emergency SOP compilation.", bold_prefix="3.")
p_bullet("AI Intelligence Layer: Dual-engine hybrid architecture integrating Google Gemini generative models with robust rule-based fallback decision matrices.", bold_prefix="4.")
p_bullet("Data Persistence Layer: MongoDB Atlas / Community Server with Mongoose ORM models enforcing strict validation and indexed spatial queries.", bold_prefix="5.")

p_heading2("1.2 Database Design")
p_body("Core collections maintained in the DisasterConnectAI MongoDB database:")
p_bullet("users: Stores user identity, hashed passwords, roles (citizen, volunteer, admin), assigned district, phone, and volunteer specialized skills.", bold_prefix="•")
p_bullet("disasters: Stores incident category, district, location text, GPS coordinates (latitude, longitude), description, image path, AI risk score, AI action plan, status (Pending, In Progress, Resolved), and assigned volunteer reference.", bold_prefix="•")
p_bullet("notifications: Stores recipient ID, disaster reference, subject, formatted HTML briefing, delivery status, and volunteer acknowledgment flag with timestamp.", bold_prefix="•")
p_bullet("shelters: Stores evacuation camp name, district, address, total capacity, occupied beds, status ('Open' / 'Full'), contact phone, and verified amenities flags.", bold_prefix="•")
p_bullet("missingpersons: Stores full name, age, gender, district, last seen location, photo, reporting contact, and status ('Missing' / 'Located Safe').", bold_prefix="•")

doc.add_page_break()

# ==============================================================================
# SYSTEM PLANNING & GANTT CHART
# ==============================================================================
p_heading1("5. System Planning")
p_body("Rigorous project planning was conducted to define milestones, resource allocation, risk mitigation strategies, and delivery schedules across the development life cycle.", space_after=6)
p_bullet("Business Requirements Definition: Analyzed disaster response protocols in Maharashtra districts (Pune, Mumbai, Nashik, Raigad) and identified essential platform capabilities.", bold_prefix="•")
p_bullet("Resource Planning: Assigned roles across UI/UX design, full-stack JavaScript engineering, MongoDB database modeling, AI prompt engineering, and QA testing.", bold_prefix="•")
p_bullet("Communication & Milestone Review: Scheduled weekly sprint reviews and integration tests.", bold_prefix="•")

p_heading2("Gantt Chart:")
p_body("The project timeline detailing proposed vs. actual completion across development phases:")
add_image("gantt_chart.png", width_inch=5.5, caption="Figure 5.1: Gantt Chart - DisasterConnectAI Project Development Timeline")

p_heading1("6. Details of Hardware & Software Used")
p_heading2("Hardware Requirements:")
p_bullet("Processor: 11th Gen Intel(R) Core(TM) i5 / i7 @ 3.20GHz or AMD Ryzen 5 / 7 (or equivalent)", bold_prefix="•")
p_bullet("Clock Speed: 2.50 GHz to 3.80 GHz", bold_prefix="•")
p_bullet("RAM: 8.00 GB (Minimum 4 GB required)", bold_prefix="•")
p_bullet("Storage: 256 GB SSD (Minimum 10 GB free space for development environment, dependencies, and uploads)", bold_prefix="•")
p_bullet("Network Interface: High-speed Wi-Fi / Broadband connection with active internet connectivity", bold_prefix="•")
p_bullet("Client Devices: Desktop PC, laptop, or workstation with high-resolution desktop monitor (1920x1080 or 1440x900)", bold_prefix="•")

p_heading2("Software Requirements:")
p_bullet("Operating System: Windows 11 (64-bit) / Linux Ubuntu 22.04 LTS", bold_prefix="•")
p_bullet("Runtime Environment: Node.js (v18.x or v20.x LTS) with NPM (v9.x or v10.x)", bold_prefix="•")
p_bullet("Database Management System: MongoDB (v6.0+ Community Server or MongoDB Atlas Cloud)", bold_prefix="•")
p_bullet("Code Editor / IDE: Visual Studio Code with ESLint and Prettier plugins", bold_prefix="•")
p_bullet("Web Browsers: Google Chrome (v120+), Microsoft Edge, or Mozilla Firefox", bold_prefix="•")

p_heading2("Languages & Libraries Used:")
p_bullet("JavaScript (ES6+) & JSX: Primary programming language for both backend (Node.js) and frontend (React).", bold_prefix="•")
p_bullet("React 19 & Vite: Fast, reactive component-driven desktop user interface framework.", bold_prefix="•")
p_bullet("Express.js: High-performance minimalist web framework for building REST APIs.", bold_prefix="•")
p_bullet("Mongoose ORM: Schema-based solution for modeling application data in MongoDB.", bold_prefix="•")
p_bullet("Leaflet & React-Leaflet: Open-source interactive desktop-friendly mapping library.", bold_prefix="•")
p_bullet("Google Gemini Generative AI SDK & Axios: HTTP client and AI engine communication.", bold_prefix="•")
p_bullet("Multer: Node.js middleware for multipart/form-data incident photo handling.", bold_prefix="•")

doc.add_page_break()

# ==============================================================================
# DETAILED LIFE CYCLE & PROCESS MODEL
# ==============================================================================
p_heading1("7. Detailed Life Cycle of the Project")
p_heading2("Iterative and Incremental Model:")
p_body(
    "DisasterConnectAI was built using the Iterative and Incremental Software Development Life Cycle (SDLC) model. This methodology combines the benefits of phased prototyping with iterative refinement, making it ideal for high-complexity, mission-critical applications.",
    space_after=8
)
p_body("Key Benefits of the Iterative Model in DisasterConnectAI:")
p_bullet("Rapid Deployment of Core Features: Enabled immediate validation of incident reporting and map rendering early in the project.", bold_prefix="•")
p_bullet("Continuous Feedback Integration: Allowed seamless incorporation of advanced capabilities like real-time shelter capacity tracking and missing persons reunification.", bold_prefix="•")
p_bullet("Early Defect Detection: Facilitated isolated unit and integration testing at each sprint, preventing architectural bottlenecks.", bold_prefix="•")

add_image("lifecycle_diagram.png", width_inch=4.8, caption="Figure 7.1: Detailed Project Life Cycle (Iterative & Incremental SDLC)")

doc.add_page_break()

# ==============================================================================
# DATA FLOW DIAGRAMS
# ==============================================================================
p_heading1("8. Data Flow Diagrams (DFDs)")
p_body(
    "A Data Flow Diagram (DFD) maps the flow of information for any process or system. It utilizes defined symbols like rectangles, circles, and arrows to depict data inputs, outputs, storage points, and routes between each destination.",
    space_after=8
)

p_heading2("Level 0 DFD (Context Level):")
p_body("The Context Level DFD illustrates the overall boundary of DisasterConnectAI, showing primary external entities (Citizens, Administrators, Volunteers) interacting with the central system:")
add_image("dfd_level0.png", width_inch=5.2, caption="Figure 8.1: Data Flow Diagram - Level 0 (Context Level Diagram)")

doc.add_page_break()

p_heading2("First Level DFD (Level 1):")
p_body("The First Level DFD decomposes the central system into its major operational subsystems: User Management, Incident Intake, AI Threat Assessment, District Dispatch, and Resource Registries:")
add_image("dfd_level1.png", width_inch=5.4, caption="Figure 8.2: First Level Data Flow Diagram (Level 1 DFD)")

doc.add_page_break()

p_heading2("Second Level DFD (Level 2):")
p_body("The Second Level DFD provides a granular view of the incident lifecycle from initial authentication, geocoded GPS intake, AI risk computation, and volunteer district routing to field resolution:")
add_image("dfd_level2.png", width_inch=5.2, caption="Figure 8.3: Second Level Data Flow Diagram (Level 2 DFD)")

doc.add_page_break()

# ==============================================================================
# ENTITY RELATIONSHIP DIAGRAM (ERD)
# ==============================================================================
p_heading1("9. Entity Relationship Diagram (ERD)")
p_body("The Entity-Relationship Diagram (ERD) visualizes the logical data model of DisasterConnectAI, illustrating the relationships between entities stored within the MongoDB database.", space_after=6)

p_heading2("Symbols Used to Draw ERD:")
p_bullet("Rectangle: Represents an Entity set (e.g., User, Disaster, Volunteer, Notification, Shelter).", bold_prefix="•")
p_bullet("Ellipse / Oval: Represents Attributes of an entity (e.g., disasterType, aiRiskScore, district).", bold_prefix="•")
p_bullet("Diamond: Represents Relationships connecting entities (e.g., Reports, Dispatches, Manages).", bold_prefix="•")
p_bullet("Lines: Link attributes to entities and entities to relationship diamonds.", bold_prefix="•")

add_image("erd_diagram.png", width_inch=5.4, caption="Figure 9.1: Entity Relationship Diagram (ERD) - DisasterConnectAI Data Architecture")

p_heading2("Entity Attribute Specifications:")
p_body("1. User Entity: user_id (PK), fullName, email, password, role ('citizen' | 'volunteer' | 'admin'), district, phone, skills, createdAt.")
p_body("2. Disaster Entity: disaster_id (PK), disasterType, district, location, latitude, longitude, description, image, aiRiskScore, aiThreatAssessment, aiActionPlan, status, reportedBy (FK), assignedVolunteer (FK), createdAt.")
p_body("3. Notification Entity: notification_id (PK), recipient (FK), disaster (FK), subject, messageHtml, deliveryStatus, acknowledged, acknowledgedAt, createdAt.")
p_body("4. Shelter Entity: shelter_id (PK), name, district, address, capacity, occupied, status, contactPhone, amenities.")
p_body("5. MissingPerson Entity: person_id (PK), fullName, age, gender, district, lastSeenLocation, contactNumber, status ('Missing' | 'Located Safe').")

doc.add_page_break()

# ==============================================================================
# ACTIVITY DIAGRAM
# ==============================================================================
p_heading1("10. Activity Diagram")
p_body("An Activity Diagram models the dynamic operational workflow of the system, depicting the sequence of actions executed from incident intake to resolution.", space_after=6)

p_heading2("Symbols Used to Draw Activity Diagram:")
p_bullet("Filled Black Circle: Represents the initial starting state.", bold_prefix="•")
p_bullet("Rounded Rectangle: Represents an Action or Activity state.", bold_prefix="•")
p_bullet("Directed Arrow: Represents the control flow transition from one activity to another.", bold_prefix="•")
p_bullet("Encircling Ring / Bullseye: Represents the final completion state.", bold_prefix="•")

add_image("activity_diagram.png", width_inch=4.8, caption="Figure 10.1: Activity Diagram - End-to-End Emergency Lifecycle")

doc.add_page_break()

# ==============================================================================
# CLASS DIAGRAM & OBJECT DIAGRAM
# ==============================================================================
p_heading1("11. Class Diagram")
p_body("The Class Diagram expresses the static object-oriented structure of the platform, detailing data attributes, member methods, and associations between controllers, models, and service utilities.", space_after=6)
add_image("class_diagram.png", width_inch=5.4, caption="Figure 11.1: Class Diagram - Core Controllers, Models & AI Engine")

p_heading1("12. Object Diagram", space_before=18)
p_body("An Object Diagram illustrates an instantiated snapshot of the system at a specific execution point in time, showing live runtime attribute values.", space_after=6)
add_image("object_diagram.png", width_inch=5.4, caption="Figure 12.1: Object Diagram - Runtime Incident & Mission State")

doc.add_page_break()

# ==============================================================================
# USE CASE DIAGRAM
# ==============================================================================
p_heading1("13. Use Case Diagram")
p_body("The Use Case Diagram defines the behavioral interactions between system actors (Citizen, Volunteer, Administrator) and the platform's core functional use cases.", space_after=6)

p_heading2("Symbols Used to Draw Use Case Diagram:")
p_bullet("Stick Figure: Represents an external Actor interacting with the system.", bold_prefix="•")
p_bullet("Ellipse: Represents a Use Case (a discrete operational capability).", bold_prefix="•")
p_bullet("Dashed Box: Represents the System Boundary encapsulating all system use cases.", bold_prefix="•")
p_bullet("Connecting Lines: Depict associations between actors and their permissible actions.", bold_prefix="•")

add_image("usecase_diagram.png", width_inch=5.4, caption="Figure 13.1: Use Case Diagram - Role Capabilities Matrix")

doc.add_page_break()

# ==============================================================================
# INPUT & OUTPUT SCREEN DESIGN (DESKTOP WIDESCREEN SCREENS ONLY)
# ==============================================================================
p_heading1("14. Input and Output Screen Design (Desktop Screen Views)")
p_body(
    "The user interface of DisasterConnectAI is purpose-built for desktop command consoles, district operation rooms, and desktop computer workstations. It provides wide 16:9 widescreen layouts, multi-column data views, interactive GIS viewports, and clean vector typography without informal colorful emojis.",
    space_after=10
)

# Screen 1: Command Center
p_heading2("1. Emergency Command Center & Statewide Incident Dispatcher (Desktop View):")
p_body(
    "The flagship desktop command center displays live telemetry metric cards (Active Incidents, Registered Volunteers, Monitored Districts, Operational Readiness), a search and district jurisdiction filter toolbar, and a comprehensive incident table with AI Risk Meters and 1-Click volunteer dispatch controls.",
    space_after=4
)
add_image("desktop_screen_command_center.png", width_inch=5.6, caption="Figure 14.1: Desktop Screen - Emergency Command Center & Statewide Incident Dispatcher")

doc.add_page_break()

# Screen 2: GIS Map
p_heading2("2. Real-Time GIS Spatial Incident & Evacuation Corridors Map (Desktop View):")
p_body(
    "A full-screen interactive desktop GIS map powered by Leaflet, displaying active disaster epicenters, color-coded hazard perimeters (Critical Flood, Chemical Fire, Storm Surge), floating situational layer legends, and dynamic incident popups with GPS coordinates.",
    space_after=4
)
add_image("desktop_screen_gis_map.png", width_inch=5.6, caption="Figure 14.2: Desktop Screen - Real-Time GIS Spatial Incident & Evacuation Map")

doc.add_page_break()

# Screen 3: Incident Intake & SOS
p_heading2("3. Live Incident Intake & Emergency SOS Dispatcher (Desktop View):")
p_body(
    "A widescreen dual-column desktop console featuring the emergency intake form with automated HTML5 GPS geolocator, high-priority Instant SOS trigger, and an automated AI Triage & Decision Matrix generating instant threat scores (8.8/10), survival steps, and supply lists.",
    space_after=4
)
add_image("desktop_screen_incident_intake.png", width_inch=5.6, caption="Figure 14.3: Desktop Screen - Live Incident Intake & Emergency SOS Dispatcher")

doc.add_page_break()

# Screen 4: Relief Shelters
p_heading2("4. Relief Camps & Evacuation Shelters Live Capacity Registry (Desktop View):")
p_body(
    "A responsive 3-column desktop registry tracking relief camps across Maharashtra districts with real-time bed occupancy progress meters, capacity percentages, verified on-site amenities (Meals, Drinking Water, Medical Teams, Power Generators), and evacuation directions.",
    space_after=4
)
add_image("desktop_screen_shelters.png", width_inch=5.6, caption="Figure 14.4: Desktop Screen - Relief Camps & Evacuation Shelters Live Capacity Registry")

doc.add_page_break()

# Screen 5: Missing Persons
p_heading2("5. Family Reunification & Missing Persons Tracing Registry (Desktop View):")
p_body(
    "A desktop tracing portal featuring search by name, district filters, and cards displaying person details, last known landmark, status indicators (Missing, Search Active, Located Safe), and single-click 'Mark Located Safe' status confirmation.",
    space_after=4
)
add_image("desktop_screen_missing_persons.png", width_inch=5.6, caption="Figure 14.5: Desktop Screen - Family Reunification & Missing Persons Tracing Registry")

doc.add_page_break()

# Screen 6: AI Emergency Chatbot
p_heading2("6. 24/7 AI Emergency Response Assistant & Triage Console (Desktop View):")
p_body(
    "A desktop split-screen conversational console featuring an emergency knowledge base on the left (Flash Flood SOPs, Burn First Aid, 72-Hour Survival Kit) and an AI chat stream on the right providing structured, life-saving emergency advice.",
    space_after=4
)
add_image("desktop_screen_ai_chatbot.png", width_inch=5.6, caption="Figure 14.6: Desktop Screen - 24/7 AI Emergency Response Assistant & Triage Console")

doc.add_page_break()

# ==============================================================================
# METHODOLOGY USED FOR TESTING & TEST CASES
# ==============================================================================
p_heading1("15. Methodology Used for Testing")
p_heading2("Manual Testing:")
p_body(
    "Manual Testing is the software testing process in which test cases are executed manually by a test engineer without the use of automated testing frameworks. The primary purpose of manual testing is to verify system stability, uncover edge-case defects, assess usability under duress, and ensure conformance with functional specifications.",
    space_after=8
)
p_body(
    "In a life-critical disaster management system like DisasterConnectAI, manual testing is imperative. While automated scripts can verify API responses, human manual validation is essential to evaluate UI clarity during panic situations, verify map interaction responsiveness, and ensure zero-loss delivery across variable network speeds.",
    space_after=8
)

p_heading2("Testing Life Cycle Steps:")
p_bullet("Requirement Study: Review functional specifications, user roles (Citizen, Volunteer, Admin), and database schemas.", bold_prefix="1.")
p_bullet("Test Case Design: Draft comprehensive test cases covering positive paths, negative inputs, and boundary conditions.", bold_prefix="2.")
p_bullet("Test Environment Setup: Configure MongoDB Atlas, Express backend on port 5000, and Vite frontend on port 5173.", bold_prefix="3.")
p_bullet("Execution of Test Cases: Manually execute intake forms, GPS detection, AI scoring, volunteer assignment, and in-app inbox delivery.", bold_prefix="4.")
p_bullet("Defect Reporting & Triage: Log issues and engineer permanent solutions.", bold_prefix="5.")
p_bullet("Regression & Retesting: Re-execute test cases to guarantee 100% pass rates.", bold_prefix="6.")

doc.add_page_break()

p_heading1("16. Test Cases & Test Reports")
p_body("Comprehensive manual testing results for DisasterConnectAI:")

test_cases_data = [
    ("TC-01", "Citizen User Registration", "Provide valid name, email, password, and district", "User registered, JWT token stored, redirected to dashboard", "Passed"),
    ("TC-02", "Login with Invalid Credentials", "Submit incorrect password or unregistered email", "Appropriate error message displayed; access denied", "Passed"),
    ("TC-03", "1-Click Admin Quick Login", "Click Emergency Command Quick Access on login tab", "Instantly authenticates as admin and opens Command Center", "Passed"),
    ("TC-04", "GPS Coordinate Auto-Detection", "Click 'Detect Location' on incident intake form", "Browser geolocates accurate latitude & longitude in seconds", "Passed"),
    ("TC-05", "One-Tap Instant SOS Trigger", "Click 'Instant SOS' on disaster reporting page", "Auto-fills high-priority alert and locks current GPS coordinates", "Passed"),
    ("TC-06", "AI Threat Assessment & Scoring", "Submit report describing severe flood in Karve Nagar", "AI computes Risk: 8.8/10, generates 4-step survival checklist", "Passed"),
    ("TC-07", "Live GIS Map Incident Plotting", "Open /map after submitting a new disaster incident", "Incident appears with red high-severity pin and interactive popup", "Passed"),
    ("TC-08", "Statewide District Filtering", "Select 'Pune' from District Filter dropdown in Admin", "Table filters to show only Pune incidents matching jurisdiction", "Passed"),
    ("TC-09", "1-Click District Volunteer Dispatch", "Click '1-Click District Dispatch' for unassigned incident", "Auto-assigns matching district volunteer & updates status", "Passed"),
    ("TC-10", "Shelter Bed Capacity Tracking", "Access /shelters registry and inspect bed gauges", "Accurately displays occupancy percentage and amenities badges", "Passed"),
    ("TC-11", "Missing Person Filing & Status", "Submit lost family report & click 'Mark Located Safe'", "Record created, search filters work, status updates to Safe", "Passed"),
    ("TC-12", "Emergency Directory 1-Click Dial", "Click on National Helpline 112 or Pune Control Room", "Triggers tel: prompt to initiate instant voice call", "Passed"),
    ("TC-13", "AI Emergency Chatbot Inquiry", "Ask chatbot 'What are immediate flood survival steps?'", "AI assistant provides structured bullet-point response instantly", "Passed")
]

tc_table = doc.add_table(rows=1, cols=5)
tc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tc_table, color="B0B0B0", sz="4")

tc_headers = ["Test ID", "Description", "Input / Action", "Expected / Actual Output", "Status"]
for i, h in enumerate(tc_headers):
    cell = tc_table.rows[0].cells[i]
    cell.paragraphs[0].text = h
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell.paragraphs[0].runs[0].font.bold = True
    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
    set_cell_background(cell, "EBF8FF")

tc_widths = [Inches(0.8), Inches(1.5), Inches(1.8), Inches(1.9), Inches(0.8)]

for row_data in test_cases_data:
    row = tc_table.add_row()
    for col_idx, text in enumerate(row_data):
        cell = row.cells[col_idx]
        cell.width = tc_widths[col_idx]
        p_c = cell.paragraphs[0]
        p_c.text = text
        p_c.runs[0].font.name = "Times New Roman"
        p_c.runs[0].font.size = Pt(9)
        p_c.paragraph_format.space_before = Pt(3)
        p_c.paragraph_format.space_after = Pt(3)
        if col_idx == 0:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_c.runs[0].font.bold = True
        elif col_idx == 4:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_c.runs[0].font.bold = True
            p_c.runs[0].font.color.rgb = RGBColor(40, 167, 69)

doc.add_page_break()

# ==============================================================================
# CODE OF THE PROJECT
# ==============================================================================
p_heading1("17. Code of the Project")
p_body(
    "Selected production source code listings demonstrating the core architectural components of DisasterConnectAI across backend server, database models, controllers, AI engines, and frontend interfaces:",
    space_after=8
)

# Code 1: backend/server.js
code_server = """// DisasterConnectAI - Main Backend Server (backend/server.js)
const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const path = require("path");
const connectDB = require("./config/db");

dotenv.config();
connectDB();

const app = express();
app.use(cors());
app.use(express.json());
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// Core Enterprise Route Registrations
app.use("/api/auth", require("./routes/authRoutes"));
app.use("/api/disasters", require("./routes/disasterRoutes"));
app.use("/api/notifications", require("./routes/notificationRoutes"));
app.use("/api/shelters", require("./routes/shelterRoutes"));
app.use("/api/missing-persons", require("./routes/missingPersonRoutes"));
app.use("/api/chat", require("./routes/chatRoutes"));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`DisasterConnectAI Server running on port ${PORT}`);
});"""
add_code_block("1. Backend Server Entrypoint (backend/server.js):", code_server)

# Code 2: backend/models/Disaster.js
code_disaster = """// DisasterConnectAI - Disaster Incident Model (backend/models/Disaster.js)
const mongoose = require("mongoose");

const disasterSchema = new mongoose.Schema({
  disasterType: {
    type: String,
    required: true,
  },
  district: {
    type: String,
    required: true,
    default: "Pune",
  },
  location: {
    type: String,
    required: true,
  },
  latitude: {
    type: Number,
  },
  longitude: {
    type: Number,
  },
  description: {
    type: String,
    required: true,
  },
  image: {
    type: String,
  },
  severity: {
    type: String,
    enum: ["Low", "Medium", "High"],
    default: "Medium",
  },
  aiRiskScore: {
    type: Number,
    default: 5,
  },
  aiThreatAssessment: {
    type: String,
  },
  aiActionPlan: [String],
  aiRecommendedSupplies: [String],
  status: {
    type: String,
    enum: ["Pending", "In Progress", "Resolved"],
    default: "Pending",
  },
  reportedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  },
  assignedVolunteer: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model("Disaster", disasterSchema);"""
add_code_block("2. Disaster Incident Schema (backend/models/Disaster.js):", code_disaster)

# Code 3: backend/utils/aiEngine.js
code_ai = """// DisasterConnectAI - Automated AI Triage & Assessment Engine (backend/utils/aiEngine.js)
const { GoogleGenerativeAI } = require("@google/generative-ai");

async function generateDisasterAssessment(disasterType, description, location) {
  try {
    if (process.env.GEMINI_API_KEY) {
      const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
      const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
      const prompt = `Analyze this disaster incident:
Type: ${disasterType}
Location: ${location}
Description: ${description}

Return JSON with:
1. threatAssessment: Concise 2-sentence hazard summary.
2. riskScore: Number 1-10.
3. actionPlan: Array of 4 immediate civilian survival steps.
4. recommendedSupplies: Array of 4 emergency items.`;

      const result = await model.generateContent(prompt);
      const response = await result.response;
      return JSON.parse(response.text());
    }
  } catch (err) {
    console.warn("AI API fallback triggered:", err.message);
  }

  // Resilient Rule-Based Decision Matrix Fallback
  return getRuleBasedAssessment(disasterType, description);
}

function getRuleBasedAssessment(type, desc) {
  const isSevere = /trapped|critical|unconscious|heavy|severe/i.test(desc);
  return {
    threatAssessment: `Active ${type} incident detected. High response priority.`,
    riskScore: isSevere ? 9 : 7,
    actionPlan: [
      "Evacuate to elevated, reinforced RCC structures immediately.",
      "Shut off main circuit breakers and gas cylinders.",
      "Keep mobile communications reserved for life safety calls.",
      "Cooperate with arriving local volunteer rescue forces."
    ],
    recommendedSupplies: ["Drinking Water Tablets", "Trauma First Aid Kit", "Emergency Torch", "Whistle"]
  };
}

module.exports = { generateDisasterAssessment };"""
add_code_block("3. Automated AI Triage & Decision Engine (backend/utils/aiEngine.js):", code_ai)

doc.add_page_break()

# ==============================================================================
# CHAPTER IV: ANNEXURE
# ==============================================================================
p_center("CHAPTER IV", size=18, bold=True, space_before=150, space_after=12)
p_center("Annexure", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("1. Database Structure & Schema Collections")
p_body("DisasterConnectAI uses MongoDB. Below are the primary document schemas:")

schema_json = """// 1. User Document Structure (users collection)
{
  "_id": "67a1b2c3d4e5f6789012345a",
  "fullName": "Rahul Deshmukh",
  "email": "rahul.deshmukh@disasterconnect.ai",
  "role": "volunteer",
  "district": "Pune",
  "phone": "+91 98220 12345",
  "skills": "Flood Rescue & Boat Handling",
  "createdAt": "2025-08-15T09:30:00.000Z"
}

// 2. Disaster Incident Document (disasters collection)
{
  "_id": "67a1b2c3d4e5f6789012345b",
  "disasterType": "Flood",
  "district": "Pune",
  "location": "Karve Nagar, Mutha River Bank",
  "latitude": 18.4912,
  "longitude": 73.8214,
  "description": "Rapid water level rise following Khadakwasla dam discharge. 4 families trapped.",
  "aiRiskScore": 8.8,
  "aiThreatAssessment": "Severe flash flood hazard with rapidly rising water level. Immediate vertical evacuation required.",
  "aiActionPlan": [
    "Move civilians to RCC structures above 2nd floor.",
    "De-energize electrical substations.",
    "Deploy inflatable rescue crafts."
  ],
  "status": "In Progress",
  "reportedBy": "67a1b2c3d4e5f67890123450",
  "assignedVolunteer": "67a1b2c3d4e5f6789012345a",
  "createdAt": "2025-08-15T10:15:00.000Z"
}"""
add_code_block("MongoDB Document Schemas (JSON Representation):", schema_json)

p_heading2("2. RESTful API Endpoints Specification:")
api_table = doc.add_table(rows=1, cols=4)
api_table.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(api_table, color="B0B0B0", sz="4")

api_headers = ["Method", "Endpoint", "Access Role", "Functional Description"]
for i, h in enumerate(api_headers):
    cell = api_table.rows[0].cells[i]
    cell.paragraphs[0].text = h
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell.paragraphs[0].runs[0].font.bold = True
    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
    set_cell_background(cell, "F0F4F8")

api_routes = [
    ("POST", "/api/auth/register", "Public", "Register new citizen or volunteer account"),
    ("POST", "/api/auth/login", "Public", "Authenticate user & return JWT session token"),
    ("GET", "/api/disasters", "All Roles", "Retrieve all disaster reports with volunteer details"),
    ("POST", "/api/disasters", "Citizen / Admin", "Submit disaster report with photo and coordinates"),
    ("PUT", "/api/disasters/:id/assign", "Admin", "Assign volunteer & update tactical dispatch"),
    ("PUT", "/api/disasters/:id/status", "Admin / Volunteer", "Update lifecycle status (Pending, In Progress, Resolved)"),
    ("GET", "/api/shelters", "Public", "Fetch relief shelters with live bed occupancy rates"),
    ("GET", "/api/missing-persons", "Public", "Fetch missing persons registry & search records"),
    ("POST", "/api/chat", "Public", "Query 24/7 AI emergency response chatbot assistant")
]

for row_data in api_routes:
    row = api_table.add_row()
    for col_idx, text in enumerate(row_data):
        cell = row.cells[col_idx]
        p_c = cell.paragraphs[0]
        p_c.text = text
        p_c.runs[0].font.name = "Times New Roman"
        p_c.runs[0].font.size = Pt(8.5)
        p_c.paragraph_format.space_before = Pt(2)
        p_c.paragraph_format.space_after = Pt(2)
        if col_idx == 0:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_c.runs[0].font.bold = True

doc.add_page_break()

# ==============================================================================
# CHAPTER V: CONCLUSION
# ==============================================================================
p_center("CHAPTER V", size=18, bold=True, space_before=150, space_after=12)
p_center("Conclusion", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("Conclusion")
p_body(
    "DisasterConnectAI successfully addresses the urgent necessity for an integrated, real-time, and resilient emergency response platform in the face of escalating natural and technological disasters.",
    space_after=8
)
p_body(
    "By bridging the critical gap between stranded citizens, field volunteers, and district authorities, the application establishes a seamless Incident Command System. Key achievements include:",
    space_after=6
)
p_bullet("Rapid Incident Ingestion: Citizens can report disasters or trigger Instant SOS alerts with automatic high-precision GPS geocoding in under 15 seconds.", bold_prefix="•")
p_bullet("Automated AI Triage: Eliminates manual triage delays by computing dynamic threat scores (1-10) and generating immediate civilian survival checklists.", bold_prefix="•")
p_bullet("Widescreen Desktop Command: Provides emergency control room operators with statewide GIS mapping, multi-district filtering, and 1-click volunteer dispatch.", bold_prefix="•")
p_bullet("Comprehensive Relief Ecosystem: Unifies interactive GIS mapping, relief shelter bed capacity gauges, 24/7 statewide emergency directory, family tracing for missing persons, and crisis SOPs into a single responsive platform.", bold_prefix="•")
p_bullet("Professional Defence-Grade UI: Replaced all informal emojis with clean vector icons, ensuring an austere, high-clarity interface suited for real emergency command operations.", bold_prefix="•")

p_body(
    "During comprehensive manual testing, DisasterConnectAI achieved 100% test pass rates across all operational test cases, proving its reliability, efficiency, and real-world viability. Ultimately, this project demonstrates how modern web engineering and artificial intelligence can be harmonized to protect human lives and bolster community resilience.",
    space_before=12, space_after=12
)

doc.add_page_break()

# ==============================================================================
# CHAPTER VI: FUTURE ENHANCEMENTS
# ==============================================================================
p_center("CHAPTER VI", size=18, bold=True, space_before=150, space_after=12)
p_center("Future Enhancement", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("Future Enhancements")
p_body("While the current version of DisasterConnectAI provides a full-featured crisis response infrastructure, several advanced capabilities are planned for future iterations:")
p_bullet("LoRaWAN & Satellite Mesh Networking: Enabling offline peer-to-peer data relay during total cellular network blackouts, transmitting SOS coordinates directly to emergency gateways via Long Range (LoRa) radio packets.", bold_prefix="1.")
p_bullet("Autonomous Drone Surveillance Feeds: Integrating live video streams from automated aerial drones to verify ground damage and detect stranded survivors using computer vision.", bold_prefix="2.")
p_bullet("Predictive Hydro-Meteorological AI Modeling: Incorporating Doppler radar telemetry and dam water release sensor APIs to forecast flash flooding 3 to 6 hours before river surges occur.", bold_prefix="3.")
p_bullet("Regional Multilingual Voice Interface: Adding real-time voice-driven intake in Marathi, Hindi, and regional dialects to assist illiterate or elderly citizens during extreme panic.", bold_prefix="4.")
p_bullet("Integration with National CAP-Alerts (NDMA / SDMA): Direct bidirectional synchronization with India's Common Alerting Protocol (CAP) for statewide early warning broadcasts.", bold_prefix="5.")
p_bullet("IoT Water-Level & Smoke Sensor Telemetry: Automatic trigger generation from municipal IoT flood gauges placed on bridges and riverbanks across Maharashtra districts.", bold_prefix="6.")
p_bullet("Blockchain-Verified Relief Logistics: Immutable auditing of relief supply distribution (food grains, medicines, blankets) to prevent diversion and ensure transparent humanitarian aid.", bold_prefix="7.")

doc.add_page_break()

# ==============================================================================
# CHAPTER VII: REFERENCES & BIBLIOGRAPHY
# ==============================================================================
p_center("CHAPTER VII", size=18, bold=True, space_before=150, space_after=12)
p_center("References and Bibliography", size=22, bold=True, color=(128, 0, 32), underline=True)
doc.add_page_break()

p_heading1("References and Bibliography")
p_body("When compiling this project report for DisasterConnectAI, a wide variety of official documentation, research literature, and technical standards were consulted:", space_after=12)

p_heading2("Websites & Technical Documentation:")
p_bullet("Node.js Official Documentation: https://nodejs.org/en/docs/", bold_prefix="1.")
p_bullet("React Official Documentation: https://react.dev/", bold_prefix="2.")
p_bullet("MongoDB Atlas & Mongoose Documentation: https://www.mongodb.com/docs/ / https://mongoosejs.com/", bold_prefix="3.")
p_bullet("Leaflet.js Interactive Maps API: https://leafletjs.com/reference.html", bold_prefix="4.")
p_bullet("Google Gemini Generative AI API Documentation: https://ai.google.dev/docs", bold_prefix="5.")
p_bullet("GeeksforGeeks Full Stack Web Development: https://www.geeksforgeeks.org/", bold_prefix="6.")
p_bullet("National Disaster Management Authority (NDMA), Government of India: https://ndma.gov.in/", bold_prefix="7.")
p_bullet("Disaster Management Department, Government of Maharashtra: https://mahadma.gov.in/", bold_prefix="8.")

p_heading2("Books & Research Publications:")
p_bullet("Pressman, R. S. (2014). Software Engineering: A Practitioner's Approach (8th ed.). McGraw-Hill Education.", bold_prefix="1.")
p_bullet("Chodorow, K. (2013). MongoDB: The Definitive Guide (2nd ed.). O'Reilly Media.", bold_prefix="2.")
p_bullet("Flanagan, D. (2020). JavaScript: The Definitive Guide (7th ed.). O'Reilly Media.", bold_prefix="3.")
p_bullet("United Nations Office for Disaster Risk Reduction (UNDRR). (2015). Sendai Framework for Disaster Risk Reduction 2015-2030.", bold_prefix="4.")

# Save master document
OUTPUT_DOCX = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\DisasterConnectAI_Project_Report.docx"
DESKTOP_DOCX = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI_Project_Report.docx"
DOWNLOADS_DOCX = r"C:\Users\ammyp\Downloads\DisasterConnectAI_Project_Report.docx"
ROOT_DOCX = r"C:\DisasterConnectAI\DisasterConnectAI_Project_Report.docx"

doc.save(OUTPUT_DOCX)
print("Saved master Word report:", OUTPUT_DOCX)

import shutil
shutil.copyfile(OUTPUT_DOCX, DESKTOP_DOCX)
shutil.copyfile(OUTPUT_DOCX, DOWNLOADS_DOCX)
shutil.copyfile(OUTPUT_DOCX, ROOT_DOCX)
print("Copied to Desktop, Downloads, and C: drive successfully!")
