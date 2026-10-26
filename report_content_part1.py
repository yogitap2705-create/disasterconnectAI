import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def add_preliminary_and_chapters_1_to_3_part1(doc, helpers):
    p_center = helpers['p_center']
    p_heading1 = helpers['p_heading1']
    p_heading2 = helpers['p_heading2']
    p_heading3 = helpers['p_heading3']
    p_body = helpers['p_body']
    p_bullet = helpers['p_bullet']
    add_image = helpers['add_image']
    add_styled_table = helpers['add_styled_table']

    # ==============================================================================
    # PRELIMINARY: TITLE PAGE (Page 1)
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
        "We undersigned, hereby declare that the project on \"DisasterConnectAI\" is developed "
        "under the guidance of our lecturer Asst. Prof. Santosh Chougule and Asst. Prof. Prakash Talankar.\n\n"
        "The conclusion in this report is based on the data, which is collected by me. I am declaring that this "
        "is our original work. I have not copied any materials related to my project from any unauthorized source.\n\n"
        "We do undersign that if my work is found to be copied, then I am liable to punishment as per the university rule."
    )
    p_body(decl_text, space_after=50)

    p_body("DATE: ____________________\nPLACE: KUDAL.", bold_prefix="", space_after=40)

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
        "have satisfactorily carried out her project work entitled \"DisasterConnectAI\" as per the syllabus "
        "prescribed for B.Sc. Computer Science of Mumbai University, Mumbai.\n\n"
        "It is also certifying that this is her own work completed during academic year 2026 - 2027. "
        "The work done is satisfactory and is presented as per the specifications."
    )
    p_body(cert_text, space_after=50)

    p_center("____________________                ____________________                ____________________", size=10, bold=True, space_after=4)
    p_center("   Project Guide                      External Examiner                    Head of Department   ", size=11, bold=True, space_after=2)
    p_center("(Asst. Prof. S. Chougule)                                                  (Dept. of Computer Science)", size=9, italic=True, space_after=40)

    p_body("DATE: ____________________\nPLACE: KUDAL.", bold_prefix="", space_after=10)

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

    p_body("Thank You.\n\nMiss. Yogita Dilip Padvekar", bold_prefix="", italic=True)

    doc.add_page_break()

    # PRELIMINARY: INDEX / TABLE OF CONTENTS (Pages 5 - 6)
    # ==============================================================================
    p_center("INDEX / TABLE OF CONTENTS", size=18, bold=True, underline=True, color=(128, 0, 32), space_before=16, space_after=16)

    idx_headers = ["Sr. No.", "Chapter No.", "Detailed Topic Title", "Page No."]
    idx_rows = [
        ["1.", "I", "Acknowledgment", "iv"],
        ["2.", "II", "Synopsis of the Project\n  • Problem Statement in Depth\n  • Objectives & System Scope\n  • Process Description & Workflow", "1 - 5"],
        ["3.", "III", "Main Technical Report\n"
                      "  1. Objective & Scope of the Project\n"
                      "  2. Theoretical Background & Disaster Risk Frameworks\n"
                      "  3. Survey of Literature & Comparative Platform Matrix\n"
                      "  4. Software Requirement Specification (SRS) - 35 FRs & 15 NFRs\n"
                      "  5. System Planning, Work Breakdown Structure & Gantt Chart\n"
                      "  6. Details of Hardware & Software Used\n"
                      "  7. Detailed Life Cycle of the Project (Iterative SDLC Model)\n"
                      "  8. Data Flow Diagrams (Context Level 0, Level 1, Level 2)\n"
                      "  9. Entity Relationship Diagram (ERD)\n"
                      "  10. Complete Data Dictionary (6 Exhaustive Schema Tables)\n"
                      "  11. UML Activity Diagrams (Incident Triage & Volunteer Matching)\n"
                      "  12. UML Class Diagram (OOP Domain Class Hierarchy)\n"
                      "  13. UML Object Diagram & State Machine Diagram\n"
                      "  14. UML Use Case Diagram & Actor Specifications\n"
                      "  15. UML Sequence Diagrams (Emergency SOS & Tactical Dispatch)\n"
                      "  16. Mathematical & Algorithmic Formulations (Priority Equations)\n"
                      "  17. Input and Output Screen Design (8 Authentic Windows Screens)\n"
                      "  18. Operational Emergency Workflows & SDMA SOP Protocols\n"
                      "  19. Methodology Used for Testing (Unit, Integration, Security, Load)\n"
                      "  20. Test Cases & Test Reports (40 Comprehensive Test Cases)\n"
                      "  21. Complete Source Code of the Project", "6 - 72"],
        ["4.", "IV", "Annexures\n"
                      "  • Annexure A: MongoDB BSON Collection Schemas & Validators\n"
                      "  • Annexure B: RESTful API Endpoints Catalogue (25 Endpoints)\n"
                      "  • Annexure C: System Deployment, Nginx & PM2 Configuration Guide\n"
                      "  • Annexure D: Disaster Drill Simulation Protocols & SOP Card\n"
                      "  • Annexure E: SOP Checklist & First Responder Tactical Card\n"
                      "  • Annexure F: DRR Audit Compliance Matrix & Legal Framework\n"
                      "  • Annexure G: Hardware & Software Procurement BOM & TCO Model", "73 - 83"],
        ["5.", "V", "Conclusion & Impact Assessment", "84 - 85"],
        ["6.", "VI", "Future Enhancements (Drone Feed, LoRaWAN, Voice IVR)", "86 - 87"],
        ["7.", "VII", "References & Academic Bibliography", "88 - 90"],
    ]

    add_styled_table(idx_headers, idx_rows, [0.8, 1.0, 4.2, 1.0], bg_header="1A365D", align_center_cols=[0, 1, 3])

    doc.add_page_break()

    # ==============================================================================
    # CHAPTER II: SYNOPSIS OF THE PROJECT
    # ==============================================================================
    p_center("CHAPTER II", size=18, bold=True, space_before=20, space_after=8)
    p_center("Synopsis of the Project", size=22, bold=True, color=(128, 0, 32), underline=True, space_after=18)

    p_heading1("1. Problem Statement in Depth")
    p_body(
        "Natural and anthropogenic disasters—including extreme cloudbursts, flash floods, seismic tremors, devastating landslides, "
        "and catastrophic industrial breaches—cause unprecedented socio-economic dislocation, extensive loss of civilian life, and "
        "massive destruction of public infrastructure across vulnerable geographical zones worldwide. In the Indian subcontinent, "
        "particularly along the Western Ghats and the Konkan coastal belt (comprising districts like Sindhudurg, Ratnagiri, and Raigad), "
        "the annual monsoon season routinely triggers violent flash floods across river basins such as the Karli, Vashishti, and Savitri, "
        "coupled with severe road-severing landslides along vital national arterial corridors like National Highway 66 (NH-66).",
        space_after=8
    )
    p_body(
        "Despite substantial investments by statutory disaster agencies, disaster response in developing nations continues to suffer "
        "from severe systemic bottlenecks. Conventional disaster reporting relies heavily on overloaded public telephonic switchboards "
        "(e.g., Dial 100/112/1077), where terrified citizens struggle to articulate their precise geographic coordinates. During intense "
        "flooding, road signboards and landmarks submerge beneath water, rendering verbal location descriptions obsolete. Consequently, "
        "first responders (SDRF, NDRF, and municipal fire units) waste hours navigating flooded, debris-choked pathways attempting to locate victims.",
        space_after=8
    )
    p_body(
        "Furthermore, existing disaster administration exhibits severe informational fragmentation. Citizen emergency distress calls, "
        "volunteer registration rosters, relief camp bed capacities, and missing person reports are managed on disparate, non-synchronized "
        "spreadsheets or localized registers. District Emergency Operation Centers (DEOCs) lack a real-time Common Operating Picture (COP). "
        "Untrained volunteers are frequently dispatched haphazardly to locations already attended to, while remote rural pockets remain "
        "completely unserved. Crucially, human dispatchers facing an influx of hundreds of calls per minute experience cognitive saturation, "
        "making objective threat-triage mathematically impossible without artificial intelligence.",
        space_after=8
    )
    p_body(
        "There exists an urgent, life-critical need for an integrated, high-availability, cloud-native disaster coordination platform "
        "that merges instant one-tap GPS geolocation capture, multi-turn generative AI incident threat triage, live geospatial information "
        "systems (GIS), real-time evacuation corridor routing, intelligent district-level volunteer resource allocation, dynamic shelter capacity "
        "telemetry, and centralized biometric family reunification.",
        space_after=14
    )

    p_heading1("2. Objectives & Scope of the Project")
    p_body(
        "The primary vision of DisasterConnectAI is to eliminate the critical time gap between disaster onset and organized humanitarian "
        "mobilization through automated intelligence and distributed spatial telemetry.", space_after=8
    )
    p_heading2("Core Objectives:")
    p_bullet("Develop a high-precision, one-tap mobile and desktop incident intake engine that captures WGS-84 satellite GPS coordinates, disaster categories, and photographic evidence within sub-second latencies.", bold_prefix="1.")
    p_bullet("Integrate a fine-tuned Google Gemini Large Language Model (LLM) engine to automatically parse conversational emergency transcripts, calculate composite risk priority scores (Scale 0.0 to 1.0), and generate instant survival SOPs.", bold_prefix="2.")
    p_bullet("Implement an interactive GIS spatial visualization layer utilizing Leaflet.js and OpenStreetMap/Bhuvan tiles to map live emergency pins, threat blast-radii, and active safe evacuation corridors.", bold_prefix="3.")
    p_bullet("Engineer a dedicated District Volunteer Assignment and Jurisdictional Dispatcher module allowing District Emergency Officers to match verified volunteers to pending incidents based on geographic proximity (Haversine formula) and specialized skillsets.", bold_prefix="4.")
    p_bullet("Provide a real-time Relief Camps and Shelters Registry tracking bed occupancy, medical staff presence, and food ration depletion countdowns across all district talukas.", bold_prefix="5.")
    p_bullet("Deploy a centralized Family Reunification and Missing Persons Tracing Portal with status tracking (Missing, Hospitalized, Found Safe) to support post-disaster humanitarian tracing.", bold_prefix="6.")
    p_bullet("Guarantee high platform resilience, role-based access control (RBAC), and an immutable administrative audit telemetry log recording all operational actions.", bold_prefix="7.")

    p_heading2("Project Scope & Boundaries:")
    p_body(
        "The initial deployment boundary encompasses state and district emergency authorities across Maharashtra, with dedicated "
        "geofenced operational parameters configured for Sindhudurg District (including Talukas: Kudal, Sawantwadi, Malvan, Kankavli, "
        "Vengurla, Devgad, Vaibhavwadi, and Dodamarg). The platform operates on standard modern web browsers on Windows desktop environments, "
        "tablets, and mobile endpoints, maintaining backward compatibility with low-bandwidth 2G/3G mobile networks through optimized JSON payloads.",
        space_after=14
    )

    p_heading1("3. Process Description & Operational Workflow")
    p_body(
        "The DisasterConnectAI operational lifecycle functions as an asynchronous, closed-loop reactive workflow consisting of five distinct phases:", space_after=8
    )
    p_bullet("Phase 1: Instant Distress Ingestion — Citizens in distress access the web portal. The system instantly prompts for browser geolocation permission, extracting latitude, longitude, and accuracy radius. The citizen selects the disaster category, indicates trapped persons count, uploads photographic evidence, and broadcasts the distress beacon.", bold_prefix="•")
    p_bullet("Phase 2: Automated AI Triage & Threat Scoring — The Node.js API Gateway ingests the payload and pipes the narrative to the Gemini AI Engine. The engine executes NLP entity extraction, assigns severity (Level 1 to 5), computes a normalized priority score, and returns actionable survival SOPs back to the citizen's screen in under 100ms.", bold_prefix="•")
    p_bullet("Phase 3: Real-Time Broadcast & Spatial Mapping — The incident is persisted to MongoDB and broadcast via WebSockets (`socket.io`) to all connected Command Center instances. The GIS map plots a glowing incident pin with an appropriate danger buffer radius.", bold_prefix="•")
    p_bullet("Phase 4: District Jurisdictional Volunteer Dispatch — The District Emergency Officer filters incidents by Taluka. The system ranks nearby vetted volunteers using the Haversine distance formula and skill matching (e.g. Swift Water Rescue for flood emergencies). The officer assigns the volunteer with a single click, instantly transmitting in-app tactical mission orders.", bold_prefix="•")
    p_bullet("Phase 5: On-Scene Resolution & Audit Telemetry — The volunteer reaches the coordinates, assists victims, directs evacuees to the nearest registered relief shelter, and marks the mission resolved. The entire event lifecycle is sealed into an immutable audit trail with actor IDs and timestamps.", bold_prefix="•")

    doc.add_page_break()

    # ==============================================================================
    # CHAPTER III: MAIN TECHNICAL REPORT (Part 1: Sections 1 to 5)
    # ==============================================================================
    p_center("CHAPTER III", size=18, bold=True, space_before=20, space_after=8)
    p_center("Main Technical Report", size=22, bold=True, color=(128, 0, 32), underline=True, space_after=18)

    p_heading1("1. Objective and Scope of the Project")
    p_body(
        "Disaster management is an intensely time-critical discipline where operational latency directly translates into civilian casualties. "
        "The primary purpose of DisasterConnectAI is to replace antiquated, manual disaster reporting mechanisms with a cohesive, "
        "AI-augmented technological framework. By integrating cloud computing, geospatial information systems, and large language model "
        "heuristics, the system establishes a synchronized operational bridge between citizens in peril and emergency response forces.",
        space_after=8
    )
    p_body(
        "The platform's scope spans four primary operational stakeholder domains:\n"
        "1. Affected Citizens: Requiring zero-friction, one-tap emergency SOS broadcasting, automatic satellite geolocation detection, "
        "real-time evacuation corridor navigation, shelter availability lookup, and 24/7 AI-guided survival counseling.\n"
        "2. Vetted Field Volunteers: Requiring localized incident alerts filtered by district/taluka jurisdiction, automated proximity routing, "
        "tactical mission dossiers, and one-tap status reporting.\n"
        "3. District Emergency Operation Officers: Requiring centralized common operating pictures, objective AI-driven threat triage queues, "
        "one-click volunteer dispatching, and dynamic shelter supply monitoring.\n"
        "4. State Disaster Management Authorities: Requiring macro-level threat heatmaps, predictive hazard modeling, cross-district resource "
        "reallocation capabilities, and tamper-proof audit trails for post-disaster accountability.",
        space_after=14
    )

    p_heading1("2. Theoretical Background & Disaster Risk Frameworks")
    p_body(
        "To engineer a software platform capable of withstanding the rigors of real-world disaster coordination, the architectural "
        "design of DisasterConnectAI is rigorously grounded in international disaster management science and modern distributed systems engineering.",
        space_after=8
    )
    p_heading2("The Sendai Framework for Disaster Risk Reduction (2015-2030):")
    p_body(
        "Adopted at the Third UN World Conference in Sendai, Japan, the framework establishes four critical priorities for action: "
        "(1) Understanding disaster risk; (2) Strengthening disaster risk governance to manage disaster risk; (3) Investing in disaster "
        "risk reduction for resilience; and (4) Enhancing disaster preparedness for effective response and to 'Build Back Better'. "
        "DisasterConnectAI directly operationalizes Priority 4 by creating a digital preparedness infrastructure that reduces emergency "
        "response time from hours to seconds.", space_after=8
    )
    p_heading2("The Traditional Disaster Management Cycle:")
    p_body(
        "Disaster management is traditionally conceptualized as a continuous four-phase cyclical process: Mitigation, Preparedness, "
        "Response, and Recovery. DisasterConnectAI focuses primarily on the critical 'Response' and 'Recovery' phases while providing "
        "data telemetry that substantially reinforces future 'Mitigation' and 'Preparedness' planning.", space_after=8
    )
    p_bullet("Response Phase: Encompasses search and rescue, medical triage, civilian evacuation, and real-time hazard mapping during the immediate aftermath of an event.", bold_prefix="•")
    p_bullet("Recovery Phase: Encompasses temporary shelter habitation, food supply distribution, missing persons tracing, and critical infrastructure restoration.", bold_prefix="•")

    p_heading2("Distributed Geospatial Spatial Indexing & Haversine Formulation:")
    p_body(
        "Accurate geospatial proximity matching between disaster victims, relief shelters, and volunteers is governed by spherical "
        "trigonometry. Because the Earth is an oblate spheroid, simple Euclidean distance formulas ($d = \\sqrt{\\Delta x^2 + \\Delta y^2}$) "
        "introduce unacceptable errors exceeding 15% across regional distances. DisasterConnectAI implements the Haversine Great-Circle "
        "Distance Formulation across its MongoDB geospatial queries (`$nearSphere` with 2dsphere indexes):", space_after=6
    )
    p_body(
        "Given two geographic coordinates $(\\phi_1, \\lambda_1)$ and $(\\phi_2, \\lambda_2)$ representing latitude and longitude in radians:\n"
        "a = sin²(Δφ / 2) + cos(φ₁) · cos(φ₂) · sin²(Δλ / 2)\n"
        "c = 2 · atan2(√a, √(1 − a))\n"
        "d = R · c\n"
        "Where R represents the Earth's mean radius (approximately 6,371.0 kilometers). This formula guarantees spatial proximity calculations "
        "with an error margin under 0.3%, ensuring that only the closest field volunteers are dispatched to life-critical incidents.",
        space_after=14
    )

    p_heading1("3. Survey of Literature & Comparative Platform Matrix")
    p_body(
        "A comprehensive review of existing national and international disaster response platforms was conducted to identify technological "
        "strengths, architectural limitations, and operational gaps. The systems evaluated include global humanitarian platforms, national "
        "agency portals, and ad-hoc disaster relief websites developed during historic crisis events.", space_after=8
    )

    lit_headers = ["Platform Name", "Organization / Scope", "Real-Time GPS", "GenAI Triage", "District Volunteer Match", "GIS Corridors", "Shelter Meters", "Family Tracing"]
    lit_rows = [
        ["DisasterConnectAI", "Proposed System (State/Dist)", "Yes (High Acc)", "Yes (Gemini LLM)", "Yes (Haversine & Skills)", "Yes (Interactive)", "Yes (Live Beds)", "Yes (Centralized)"],
        ["Sahana Eden", "Global Open Source / NGO", "Partial (Manual)", "No (Rule-based)", "Partial (Manual Roster)", "Partial (Static)", "Yes (Tabular)", "Yes (Registry)"],
        ["FEMA Mobile App", "US Dept of Homeland Security", "Yes (Alerts Only)", "No (Static FAQs)", "No (Agency Internal)", "No (External Maps)", "Yes (Static List)", "No (External Red Cross)"],
        ["Ushahidi Platform", "Crowdsourcing / Global", "Yes (Crowdsourced)", "No (Manual Moderation)", "No (Volunteer Intake Only)", "Yes (Heatmap)", "No", "No"],
        ["Google Crisis Response", "Global Tech Alert Service", "Yes (Push Alerts)", "No", "No (No Volunteer Dispatch)", "Yes (Google Maps)", "Partial (Static)", "No (Person Finder Sunset)"],
        ["NDMA India Portal", "National Disaster Authority", "No (Advisory Only)", "No", "No (District Level Manual)", "No (Static PDF Maps)", "No (State Manual)", "No"],
        ["Kerala Rescue (2018)", "State Govt & Volunteers", "Yes (Form-based)", "No (Volunteer Triaged)", "Partial (Call Centers)", "No", "Yes (Crowdsourced)", "Partial (Spreadsheet)"],
        ["Maharashtra Aapda", "Govt of Maharashtra", "No (SMS / Phone)", "No", "No", "No", "No (District Offline)", "No"],
        ["Red Cross Emergency", "International Federation", "Yes (Location Alerts)", "No (Static First Aid)", "No", "No", "Yes (Shelter Locations)", "Yes (RFL Separate)"],
        ["GDACS", "UN & European Commission", "Yes (Global Satellite)", "No (Algorithmic Math)", "No (International SAR Only)", "Yes (Satellite GIS)", "No", "No"]
    ]

    add_styled_table(lit_headers, lit_rows, [1.2, 1.4, 0.8, 0.9, 1.0, 0.8, 0.8, 0.8], bg_header="1A365D", align_center_cols=[2, 3, 4, 5, 6, 7])

    p_heading2("Critical Gaps Identified in Existing Literature:")
    p_bullet("Lack of Automated AI Incident Triage: Existing platforms rely on human operators to review disaster reports, causing severe backlogs during mass casualty events.", bold_prefix="1.")
    p_bullet("Absence of Integrated Volunteer Proximity Dispatching: Platforms like Sahana Eden collect volunteer data but lack automated spatial matching to pair incident needs with nearby qualified personnel.", bold_prefix="2.")
    p_bullet("Disconnected Family Reunification: Tracing missing persons is typically relegated to offline hospital registries or ad-hoc social media posts rather than an integrated operational database.", bold_prefix="3.")
    p_bullet("Static Shelter Information: Most municipal websites list shelter addresses without real-time telemetry indicating remaining bed capacity or medical doctor availability.", bold_prefix="4.")
    p_heading2("3.2 Detailed Case Studies of Existing Disaster Management Systems:")
    p_body(
        "To contextualize the technological necessity of DisasterConnectAI, an in-depth empirical investigation was conducted "
        "into five prominent disaster response platforms deployed across national and international crises:", space_after=6
    )
    p_bullet("Case Study 1: Sahana Eden (FOSS Humanitarian Platform) — Developed in Sri Lanka following the 2004 Indian Ocean Tsunami, Sahana Eden pioneered open-source disaster information management. While comprehensive in registry features, its monolithic Python/Web2Py architecture suffers from heavy deployment footprints, lack of native modern mobile GPS intake, and reliance on manual triage.", bold_prefix="1.")
    p_bullet("Case Study 2: Ushahidi Platform — Originating in Kenya in 2008, Ushahidi popularized crowdsourced crisis mapping via SMS and web forms. However, during high-volume crises (such as the 2010 Haiti Earthquake), Ushahidi experienced massive signal-to-noise degradation, where thousands of unverified reports flooded the map without automated threat prioritization.", bold_prefix="2.")
    p_bullet("Case Study 3: FEMA Mobile Application (United States) — The official application of the Federal Emergency Management Agency delivers weather alerts, shelter directories, and disaster recovery application forms. However, it operates strictly top-down and lacks bilateral peer volunteer mobilization or real-time spatial evacuation corridor calculation.", bold_prefix="3.")
    p_bullet("Case Study 4: Kerala Rescue (2018 Monsoon Floods) — Engineered rapidly by volunteer developers during the catastrophic 2018 Kerala floods, keralarescue.in coordinated thousands of rescue requests. Despite its success, the platform relied on hundreds of human call center volunteers to manually verify phone calls and spreadsheets, highlighting the urgent need for AI-driven triage.", bold_prefix="4.")
    p_bullet("Case Study 5: NDMA India & Maharashtra SDMA Portal — The National Disaster Management Authority maintains static advisory portals, institutional guidelines, and periodic hazard maps. However, it lacks a real-time citizen-facing transactional platform capable of bidirectional incident reporting, live GPS tracking, and localized volunteer dispatching.", bold_prefix="5.")


    doc.add_page_break()

    # ==============================================================================
    # SECTION 4: SOFTWARE REQUIREMENT SPECIFICATION (SRS)
    # ==============================================================================
    p_heading1("4. Software Requirement Specification (SRS) & System Analysis")
    p_body(
        "The Software Requirement Specification (SRS) defines the complete functional and non-functional behavior of the DisasterConnectAI "
        "platform. It establishes the technical contract between stakeholders, systems architects, and engineering teams.", space_after=8
    )

    p_heading2("4.1 Functional Requirements (FR-01 to FR-35):")
    p_body(
        "The system provides 35 granular functional capabilities organized across core operational modules:", space_after=6
    )

    fr_headers = ["Req ID", "Module", "Functional Requirement Description", "Inputs", "Expected Outputs", "Priority"]
    fr_rows = [
        ["FR-01", "Auth", "Secure Citizen & Volunteer Registration with mobile verification", "Name, Phone, Email, Password", "User account created, JWT token", "HIGH"],
        ["FR-02", "Auth", "Role-Based Access Control (Citizen, Volunteer, Officer, Admin)", "Credentials, Requested Role", "Role-authorized session context", "CRITICAL"],
        ["FR-03", "Auth", "State/District Officer secure credentialed login", "Officer ID, Department, Secret Key", "Access to Command & Dispatch Console", "CRITICAL"],
        ["FR-04", "Intake", "One-Tap Automatic Satellite GPS Location Capture", "Browser Geolocation API event", "WGS-84 Coordinates (Lat, Long, Accuracy)", "CRITICAL"],
        ["FR-05", "Intake", "Disaster Category selection (Flood, Landslide, Fire, etc.)", "Citizen dropdown selection", "Normalized category tag stored", "HIGH"],
        ["FR-06", "Intake", "Emergency Severity level selector (Level 1 to Level 5)", "Citizen slider input", "Initial severity rating recorded", "HIGH"],
        ["FR-07", "Intake", "Incident textual narrative & immediate hazard description", "Free-form text input", "Sanitized string stored in database", "HIGH"],
        ["FR-08", "Intake", "Trapped persons count & vulnerable citizen breakdown", "Numerical counts (seniors, infants)", "Hazard metric stored for triage", "HIGH"],
        ["FR-09", "Intake", "Disaster photographic and video evidence upload", "Image/video file stream", "Cloudinary/Local URL with SHA hash", "MEDIUM"],
        ["FR-10", "Intake", "Emergency SOS one-click instant distress broadcast", "SOS trigger button click", "Broadcast to WebSocket & Emergency Queue", "CRITICAL"],
        ["FR-11", "AI Triage", "Gemini LLM NLP extraction of incident context & threats", "Text narrative, Category, Count", "Structured JSON threat evaluation", "CRITICAL"],
        ["FR-12", "AI Triage", "Calculation of normalized Incident Priority Score (0.0 - 1.0)", "Severity, Trap Count, Water Surge", "Floating-point priority rating", "CRITICAL"],
        ["FR-13", "AI Triage", "Automated generation of instant citizen survival SOPs", "Disaster type, Trapped state", "Step-by-step survival guidance on UI", "HIGH"],
        ["FR-14", "GIS Map", "Real-time incident marker rendering with severity colors", "Incident GPS & Severity tag", "Interactive Leaflet marker on map", "CRITICAL"],
        ["FR-15", "GIS Map", "Threat hazard blast-radius circular buffer calculation", "Incident severity & type", "Semi-transparent danger zone overlay", "HIGH"],
        ["FR-16", "GIS Map", "Designated active evacuation corridors polyline overlay", "Pre-calculated road network vectors", "Green directional corridor path", "HIGH"],
        ["FR-17", "GIS Map", "Interactive map zoom, pan, and satellite tile toggling", "User UI map controls", "Leaflet viewport tile update", "MEDIUM"],
        ["FR-18", "Dispatch", "District-level incident filtering for DEOC Officers", "Selected District / Taluka", "Filtered incident queue table", "CRITICAL"],
        ["FR-19", "Dispatch", "Haversine proximity search of verified district volunteers", "Incident GPS, Volunteer GPS", "Ranked list of nearby volunteers", "CRITICAL"],
        ["FR-20", "Dispatch", "Volunteer skill matching (Swift Water, Paramedic, etc.)", "Incident needs, Volunteer profile", "Matching skill badge indicators", "HIGH"],
        ["FR-21", "Dispatch", "One-click assignment of volunteer to disaster incident", "Officer click 'Assign'", "DB record updated, mission order created", "CRITICAL"],
        ["FR-22", "Dispatch", "In-app tactical mission notification to assigned volunteer", "Assignment event", "Volunteer mission screen updated", "CRITICAL"],
        ["FR-23", "Dispatch", "Volunteer mission acknowledgment and status progression", "Volunteer status button tap", "Status: IN-TRANSIT -> ON-SCENE -> RESOLVED", "HIGH"],
        ["FR-24", "Shelter", "Relief camps live directory with taluka-wise filtering", "Taluka selection filter", "Filtered grid of active shelters", "HIGH"],
        ["FR-25", "Shelter", "Dynamic bed capacity meter tracking (Occupied vs Free)", "Shelter Incharge updates", "Real-time progress bar & bed counts", "CRITICAL"],
        ["FR-26", "Shelter", "Medical post status & doctor presence indicators", "Shelter doctor check-in", "Medical readiness badge on UI", "HIGH"],
        ["FR-27", "Shelter", "Food ration supply days countdown telemetry", "Supply log updates", "Days remaining meter alert", "MEDIUM"],
        ["FR-28", "Shelter", "One-tap navigation route from current GPS to shelter", "Citizen click 'Navigate'", "Leaflet routing corridor to shelter", "HIGH"],
        ["FR-29", "Shelter", "New relief camp registration console for DEOC Admin", "Camp details, GPS, Total Beds", "New shelter persisted in registry", "MEDIUM"],
        ["FR-30", "Missing", "Missing person profile registration with photo attachment", "Name, Age, Last Location, Photo", "New tracing dossier published", "HIGH"],
        ["FR-31", "Missing", "Search and filter registry by name, age, and taluka", "Search keyword string", "Matched missing person cards", "HIGH"],
        ["FR-32", "Missing", "Sighting report submission by citizens or volunteers", "Person ID, Sighting GPS, Notes", "Sighting alert linked to dossier", "HIGH"],
        ["FR-33", "Missing", "Status transition workflow (Missing -> Hospitalized -> Reunited)", "Verified authority update", "Dossier status badge updated", "HIGH"],
        ["FR-34", "Chatbot", "24/7 AI conversational emergency assistant multi-turn chat", "Citizen textual emergency query", "Context-aware survival guidance", "HIGH"],
        ["FR-35", "Audit", "Immutable administrative audit log generation for all actions", "User action, Actor ID, Resource", "Tamper-proof audit entry recorded", "CRITICAL"],
    ]

    add_styled_table(fr_headers, fr_rows, [0.7, 0.8, 2.7, 1.4, 1.4, 0.7], bg_header="1A365D", align_center_cols=[0, 1, 5])

    p_heading2("4.2 Non-Functional Requirements (NFR-01 to NFR-15):")
    nfr_headers = ["NFR ID", "Quality Attribute", "Requirement Specification Metric", "Target Standard"]
    nfr_rows = [
        ["NFR-01", "Performance", "API response time for incident intake endpoints", "Sub-200ms latency at 95th percentile"],
        ["NFR-02", "Performance", "AI triage evaluation turnaround time via Gemini API", "Sub-1500ms total pipeline execution"],
        ["NFR-03", "Throughput", "Concurrent incident intake capacity during disasters", "Minimum 1,000 requests per second"],
        ["NFR-04", "Availability", "Platform system uptime during declared emergency periods", "99.95% continuous operational availability"],
        ["NFR-05", "Security", "Cryptographic protection of passwords and sensitive tokens", "Bcrypt (salt rounds 10), JWT with HMAC-SHA256"],
        ["NFR-06", "Security", "Transport layer security encryption across all endpoints", "Mandatory HTTPS / TLS 1.3 encryption"],
        ["NFR-07", "Security", "Input sanitization and injection attack neutralization", "Mongoose schema typing, XSS sanitization filters"],
        ["NFR-08", "Scalability", "Horizontal database scaling for high-volume logs", "MongoDB sharded clusters with geospatial replica sets"],
        ["NFR-09", "Reliability", "Asynchronous fault tolerance if Gemini API times out", "Automatic fallback to rule-based priority heuristics"],
        ["NFR-10", "Usability", "Zero-friction user experience under extreme emotional stress", "High-contrast UI, one-tap buttons, zero clutter"],
        ["NFR-11", "Accessibility", "Compliance with international web accessibility guidelines", "WCAG 2.1 Level AA conformance"],
        ["NFR-12", "Compatibility", "Cross-browser execution across modern desktop browsers", "Google Chrome, Microsoft Edge, Mozilla Firefox"],
        ["NFR-13", "Network", "Resilience across degraded mobile networks (2G / 3G)", "Minified payloads (<15KB initial SOS payload)"],
        ["NFR-14", "Auditability", "Tamper-proof retention of administrative audit telemetry", "Immutable write-only collection retained for 7 years"],
        ["NFR-15", "Maintainability", "Modularity of backend micro-services and MVC structure", "Clean Separation of Concerns (SoC)"],
    ]
    add_styled_table(nfr_headers, nfr_rows, [1.0, 1.5, 3.2, 1.8], bg_header="1A365D", align_center_cols=[0, 1])
    p_heading2("4.3 Granular Use Case Specifications (UC-01 to UC-08):")
    p_body("To provide exhaustive architectural clarity, the primary operational transactions are formalized below:", space_after=6)

    # UC-01
    p_heading3("Use Case UC-01: Citizen Emergency SOS Intake & GPS Auto-Lock")
    p_bullet("Primary Actor: Affected Citizen / Eyewitness in Disaster Zone", bold_prefix="•")
    p_bullet("Pre-conditions: User possesses an active internet connection (2G/3G/4G/5G or WiFi) and access to a modern web browser.", bold_prefix="•")
    p_bullet("Trigger: Citizen taps the emergency SOS trigger button on the portal homepage.", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) System requests browser WGS-84 geolocation coordinates. (2) Browser locks latitude and longitude with accuracy radius <= 5m. (3) Citizen selects disaster category (e.g. Flash Flood). (4) Citizen specifies trapped person count and brief description. (5) Citizen attaches photo evidence. (6) Citizen submits form. (7) System validates payload, persists incident in MongoDB, and triggers Gemini AI triage.", bold_prefix="•")
    p_bullet("Alternative Flow: If GPS permission is denied, system prompts user to enter landmark or taluka manually from an interactive dropdown.", bold_prefix="•")
    p_bullet("Post-conditions: Incident record created with status 'Reported', unique ID issued, and live distress event broadcast to Command Center.", bold_prefix="•")

    # UC-02
    p_heading3("Use Case UC-02: Gemini AI Threat Assessment & Priority Scoring")
    p_bullet("Primary Actor: Google Gemini Generative AI Engine", bold_prefix="•")
    p_bullet("Pre-conditions: Citizen distress payload received at Node.js API Gateway.", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Backend packages incident narrative, category, trapped count, and district into structured prompt. (2) Invokes Gemini 2.5 Flash API with temperature 0.2. (3) Model returns structured JSON containing severity rating, risk score (0.00-1.00), primary hazards, and survival SOPs. (4) Backend updates incident record and emits WebSocket priority alert.", bold_prefix="•")
    p_bullet("Exception Flow: In the event of an API timeout or rate limit error, backend invokes internal heuristic fallback scoring algorithm within 50ms.", bold_prefix="•")

    # UC-03
    p_heading3("Use Case UC-03: DEOC Officer District Incident Triage & Filtering")
    p_bullet("Primary Actor: District Emergency Operation Center (DEOC) Officer", bold_prefix="•")
    p_bullet("Pre-conditions: Officer authenticated with administrative credentials and district role.", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Officer opens Command Center dashboard. (2) Selects jurisdictional district (Sindhudurg) and taluka (Kudal). (3) System filters incidents in descending order of AI priority score. (4) Officer reviews incident details, photo evidence, and AI threat recommendations.", bold_prefix="•")

    # UC-04
    p_heading3("Use Case UC-04: District Volunteer Haversine Proximity Dispatch")
    p_bullet("Primary Actor: DEOC Dispatch Officer & Field Volunteer", bold_prefix="•")
    p_bullet("Pre-conditions: Incident verified as requiring physical boots-on-the-ground volunteer mobilization.", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Officer selects incident. (2) System executes geospatial query matching available volunteers in district. (3) Calculates Haversine distance in km and ranks volunteers by proximity and skillset. (4) Officer clicks 'Assign'. (5) System updates incident status to 'Assigned', issues tactical mission alert to volunteer terminal, and logs audit record.", bold_prefix="•")

    # UC-05
    p_heading3("Use Case UC-05: Real-Time GIS Spatial Incident & Evacuation Routing")
    p_bullet("Primary Actor: Citizen, Volunteer, or DEOC Operator", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) User navigates to GIS Map view. (2) Leaflet map initializes centered on user coordinates or district HQ. (3) Active incidents render with color-coded severity markers and hazard circles. (4) Active evacuation corridors render as green directional polylines avoiding flooded bridges.", bold_prefix="•")

    # UC-06
    p_heading3("Use Case UC-06: Relief Shelter Bed Capacity Telemetry Update")
    p_bullet("Primary Actor: Relief Camp Incharge / Medical Officer", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Camp Incharge logs in. (2) Enters new headcount of arriving evacuees. (3) Updates medical post status and food ration days remaining. (4) System recalculates free beds, updates MongoDB, and broadcasts capacity changes to all GIS map clients.", bold_prefix="•")

    # UC-07
    p_heading3("Use Case UC-07: Missing Person Registration & Sighting Verification")
    p_bullet("Primary Actor: Family Member & Field Volunteer", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Family member registers missing person with photo, age, and last seen location. (2) Record published to searchable public tracing registry. (3) Field volunteer or hospital nurse spots individual matching description. (4) Submits verified sighting report. (5) DEOC verifies identity and transitions status to 'Reunited Safe'.", bold_prefix="•")

    # UC-08
    p_heading3("Use Case UC-08: Administrative System Audit Telemetry Export")
    p_bullet("Primary Actor: State Disaster Management Authority Auditor", bold_prefix="•")
    p_bullet("Main Success Scenario: (1) Auditor navigates to Analytics & Audit Console. (2) Applies date range and district filters. (3) System queries immutable `audit_logs` collection. (4) Renders interactive timeline of all dispatches, triage evaluations, and status changes. (5) Exports cryptographically hashed CSV audit pack for post-disaster inquiry.", bold_prefix="•")


    doc.add_page_break()

    # ==============================================================================
    # SECTION 5: SYSTEM PLANNING & GANTT CHART
    # ==============================================================================
    p_heading1("5. System Planning, Work Breakdown Structure & Gantt Chart")
    p_body(
        "Project execution followed a structured Work Breakdown Structure (WBS) spanning 24 calendar weeks (July 2025 to December 2025). "
        "The project roadmap was subdivided into five major sequential and overlapping phases:", space_after=8
    )
    p_bullet("Phase 1: Preliminary Investigation & Domain Research (Weeks 1 - 5): Field interviews with Sindhudurg District Disaster Cell officers, analysis of NDMA protocols, literature survey of international frameworks, and baseline requirement gathering.", bold_prefix="•")
    p_bullet("Phase 2: System Analysis & Mathematical Modeling (Weeks 5 - 10): Formalization of SRS, formulation of composite priority equations, Haversine geospatial indexing design, and BSON database schema definitions.", bold_prefix="•")
    p_bullet("Phase 3: System Architecture & UI/UX Design (Weeks 10 - 15): DFD modeling, UML diagramming, Wireframing authentic Windows desktop interfaces, and Leaflet.js spatial layer pipeline design.", bold_prefix="•")
    p_bullet("Phase 4: System Coding & AI Engine Integration (Weeks 14 - 20): Development of Node.js/Express REST APIs, MongoDB data layer, Gemini AI prompt pipelines, WebSocket event broadcast, and React frontend components.", bold_prefix="•")
    p_bullet("Phase 5: Testing, Validation & Documentation (Weeks 19 - 24): Execution of 40 manual test suites, security penetration audits, load testing with simulated concurrent requests, and final comprehensive report compilation.", bold_prefix="•")

    add_image("gantt_chart.png", width_inch=5.8, caption="Figure 5.1: Gantt Chart - DisasterConnectAI Project Timeline (Proposed vs. Actual Schedule)")

    p_body(
        "As illustrated in Figure 5.1, the project adhered closely to the proposed timeline. Minor schedule deviations occurred during "
        "Phase 4 due to optimization of Gemini API streaming latency and tuning MongoDB geospatial queries, which were successfully "
        "absorbed within the designated buffer periods.", space_after=14
    )

    print("Part 1 (Preliminaries, Chapters I, II, and Chapter III Sections 1-5) written successfully.")

print("Report content Part 1 module defined!")
