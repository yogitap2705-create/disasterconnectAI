import os

# Script to expand report_content_part1.py and report_content_part3.py
# with extensive academic case studies, 8 detailed use case specifications,
# and 8 UI component tables for each Windows screen.

print("Expanding report_content_part1.py and report_content_part3.py...")

# 1. Update report_content_part1.py
with open("report_content_part1.py", "r", encoding="utf-8") as f:
    p1 = f.read()

case_studies_and_use_cases = """
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
"""

use_case_specs = """
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
"""

# Inject into part 1
target_lit = 'p_bullet("Static Shelter Information: Most municipal websites list shelter addresses without real-time telemetry indicating remaining bed capacity or medical doctor availability.", bold_prefix="4.")'
if target_lit in p1:
    p1 = p1.replace(target_lit, target_lit + "\\n" + case_studies_and_use_cases)
    print("Injected Case Studies into report_content_part1.py")

target_nfr = 'add_styled_table(nfr_headers, nfr_rows, [1.0, 1.5, 3.2, 1.8], bg_header="1A365D", align_center_cols=[0, 1])'
if target_nfr in p1:
    p1 = p1.replace(target_nfr, target_nfr + "\\n" + use_case_specs)
    print("Injected Use Cases into report_content_part1.py")

with open("report_content_part1.py", "w", encoding="utf-8") as f:
    f.write(p1)
print("Updated report_content_part1.py successfully!")

# 2. Update report_content_part3.py
with open("report_content_part3.py", "r", encoding="utf-8") as f:
    p3 = f.read()

# Tables for each of the 8 Windows screens
screen_tables_code = '''
    # UI Component Table for Screen 1
    p_heading3("Table 17.1: UI Component & Control Specification - Windows Screen 1 (Command Center)")
    tbl1_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl1_rows = [
        ["CMD-WIN-01", "Window Control", "Minimize (—)", "onWindowMinimize()", "Desktop Window State", "OS-level hook"],
        ["CMD-WIN-02", "Window Control", "Maximize (□)", "onWindowMaximize()", "Desktop Viewport Size", "1920x1080 standard"],
        ["CMD-WIN-03", "Window Control", "Close (✕)", "onWindowClose()", "App Process State", "Confirmation dialog"],
        ["CMD-KPI-01", "Metric Card", "Active Emergencies", "onClickFilterActive()", "Disaster.count({status: !Resolved})", "Real-time auto-refresh"],
        ["CMD-KPI-02", "Metric Card", "Volunteers Deployed", "onClickFilterVolunteers()", "User.count({role: volunteer})", "District scoped"],
        ["CMD-KPI-03", "Metric Card", "Relief Camps Active", "onClickFilterShelters()", "Shelter.count({isActive: true})", "Taluka aggregated"],
        ["CMD-KPI-04", "Metric Card", "AI Triage Latency", "onHoverTelemetry()", "Telemetry.geminiLatencyMs", "95th percentile benchmark"],
        ["CMD-TBL-01", "Data Table", "Incident Dispatch Table", "onRowSelect(incidentId)", "Disaster.find({district})", "RBAC DEOC Officer"],
        ["CMD-ACT-01", "Action Trigger", "DISPATCHED Button", "onClickTriggerDispatch()", "Disaster.status = 'Assigned'", "Audit logged with timestamp"]
    ]
    add_styled_table(tbl1_headers, tbl1_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 2
    p_heading3("Table 17.2: UI Component & Control Specification - Windows Screen 2 (GIS Map)")
    tbl2_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl2_rows = [
        ["GIS-WIN-01", "Windows Omnibox", "Address Bar (https://...)", "onNavigate()", "Router URL /map", "HTTPS TLS 1.3 enforced"],
        ["GIS-LYR-01", "Layer Checkbox", "Flash Floods (L5)", "onToggleLayer('flood')", "Disaster.severity === 'Critical'", "Dynamic leaflet layer"],
        ["GIS-LYR-02", "Layer Checkbox", "Landslide Blockades (L4)", "onToggleLayer('landslide')", "Disaster.type === 'Landslide'", "Dynamic leaflet layer"],
        ["GIS-LYR-03", "Layer Checkbox", "Safe Shelters", "onToggleLayer('shelter')", "Shelter.find({isActive: true})", "Cluster marker group"],
        ["GIS-PIN-01", "Map Marker", "Incident Threat Pin", "onMarkerClick(incId)", "Disaster.location.coordinates", "WGS-84 coordinate validation"],
        ["GIS-COR-01", "Polyline", "Evacuation Corridor Vector", "onCorridorClick(corId)", "Corridor.waypointCoordinates", "Verified passable road network"],
        ["GIS-CTL-01", "Map Control", "Zoom In / Out (+ / -)", "onMapZoom()", "Leaflet.zoomLevel (9 to 18)", "Viewport boundary lock"]
    ]
    add_styled_table(tbl2_headers, tbl2_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 3
    p_heading3("Table 17.3: UI Component & Control Specification - Windows Screen 3 (Incident Intake & SOS)")
    tbl3_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl3_rows = [
        ["INTK-WIZ-01", "Progress Stepper", "1. Details -> 2. GPS -> 3. Photo", "onStepChange()", "IntakeWizard.currentStep", "Linear step validation"],
        ["INTK-CAT-01", "Select Dropdown", "Disaster Category", "onCategoryChange()", "Disaster.disasterType", "Mandatory enum field"],
        ["INTK-SEV-01", "Slider / Radio", "Severity Level (L1 to L5)", "onSeverityChange()", "Disaster.severity", "Integer range 1 to 5"],
        ["INTK-GPS-01", "Telemetry Card", "Automatic GPS Lock", "onFetchGeolocation()", "navigator.geolocation.coords", "WGS-84 precision <5m"],
        ["INTK-TXT-01", "Textarea Input", "Emergency Description", "onNarrativeChange()", "Disaster.description", "Sanitized string 10-2000 ch"],
        ["INTK-CNT-01", "Number Input", "Trapped Persons Count", "onCountChange()", "Disaster.trappedCount", "Integer >= 0"],
        ["INTK-MED-01", "Dropzone Bay", "Photo / Video Evidence", "onFileUpload()", "Disaster.mediaUrls", "Max 50MB, MIME validation"],
        ["INTK-SOS-01", "Crimson Button", "BROADCAST SOS DISPATCH", "onSubmitSOS()", "Disaster.create() & socket.emit", "Immediate server dispatch"]
    ]
    add_styled_table(tbl3_headers, tbl3_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 4
    p_heading3("Table 17.4: UI Component & Control Specification - Windows Screen 4 (Shelters Registry)")
    tbl4_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl4_rows = [
        ["SHLT-FLT-01", "Filter Bar", "Filter District / Taluka", "onTalukaFilter()", "Shelter.taluka", "Jurisdiction restriction"],
        ["SHLT-CRD-01", "Desktop Card", "Shelter Overview Card", "onSelectShelter()", "Shelter.name, address, phone", "3-column responsive grid"],
        ["SHLT-MTR-01", "Progress Bar", "Bed Capacity Meter", "onHoverCapacity()", "Shelter.occupiedBeds / totalCapacity", "Color changes at >90%"],
        ["SHLT-MED-01", "Status Tag", "Doctor On-Site (MBBS)", "onToggleDoctorStatus()", "Shelter.medicalPost", "Verified medical badge"],
        ["SHLT-RAT-01", "Status Tag", "Food Rations Days", "onUpdateRations()", "Shelter.foodRationsDays", "Alert triggered when <3 days"],
        ["SHLT-ACT-01", "Action Button", "DIRECT EVACUEES HERE", "onDirectEvacuees()", "Disaster.assignedShelterId", "Route mapped via Leaflet"]
    ]
    add_styled_table(tbl4_headers, tbl4_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 5
    p_heading3("Table 17.5: UI Component & Control Specification - Windows Screen 5 (Missing Persons)")
    tbl5_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl5_rows = [
        ["MISS-SRCH-01", "Search Omnibox", "Search Name or Location", "onSearchQueryChange()", "MissingPerson.fullName regex", "Debounced search 300ms"],
        ["MISS-FLT-01", "Dropdown Filter", "Status (Missing, Safe)", "onStatusFilter()", "MissingPerson.status", "Enum filter selector"],
        ["MISS-CRD-01", "Profile Card", "Person Photo & Dossier", "onOpenDossierModal()", "MissingPerson.photoUrl, age, gender", "Biometric card container"],
        ["MISS-SGT-01", "Modal Form", "Submit Sighting Info", "onSubmitSighting()", "MissingPerson.sightingHistory", "Citizen verified submission"],
        ["MISS-REG-01", "Primary Button", "+ REGISTER MISSING PERSON", "onOpenRegisterModal()", "MissingPerson.create()", "Authentication required"]
    ]
    add_styled_table(tbl5_headers, tbl5_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 6
    p_heading3("Table 17.6: UI Component & Control Specification - Windows Screen 6 (AI Emergency Chatbot)")
    tbl6_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl6_rows = [
        ["CHAT-PRM-01", "Prompt Pill", "Flash Flood Survival Checklist", "onSelectPrompt()", "ChatSession.promptTemplate", "Verified SDMA protocol"],
        ["CHAT-PRM-02", "Prompt Pill", "Nearest Shelter in Kudal", "onQueryNearestShelter()", "Shelter.geoNear query", "Haversine lookup"],
        ["CHAT-DIR-01", "Sidebar Box", "Emergency Helplines (1070/112)", "onDirectCall()", "Telephone URI tel:1070", "Official government lines"],
        ["CHAT-MSG-01", "Chat Turn", "Citizen Emergency Query", "onSendMessage()", "ChatSession.messages.push()", "Multi-turn context preserved"],
        ["CHAT-BOT-01", "AI Response", "DisasterConnect AI Guidance", "onRenderMarkdown()", "Gemini.generateContent.text", "Sub-1500ms streaming"],
        ["CHAT-ACT-01", "Action Pill", "LOCK ROOFTOP GPS BEACON", "onTransmitBeacon()", "Disaster.updateBeaconGPS()", "Direct SDRF alert emitted"]
    ]
    add_styled_table(tbl6_headers, tbl6_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 7
    p_heading3("Table 17.7: UI Component & Control Specification - Windows Screen 7 (Volunteer Assignment)")
    tbl7_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl7_rows = [
        ["VOL-DIST-01", "Jurisdiction Filter", "Select District / Taluka", "onDistrictChange()", "Session.jurisdictionDistrict", "Authorized DEOC officer only"],
        ["VOL-INC-01", "Left Queue Pane", "Pending Incidents Table", "onSelectIncident(id)", "Disaster.find({status: 'Reported'})", "Sorted by AI Risk Score"],
        ["VOL-LST-01", "Right Volunteer Pane", "Verified District Volunteers", "onFilterVolunteers()", "User.find({role: 'volunteer'})", "Haversine proximity sorted"],
        ["VOL-SKL-01", "Skill Badge", "Swift Water Rescue Certified", "onFilterBySkill()", "Volunteer.skills", "SDRF certified credentials"],
        ["VOL-ASN-01", "Crimson Action", "ASSIGN TO INCIDENT", "onClickAssign()", "Disaster.assignedVolunteer = volId", "WebSocket mission alert fired"]
    ]
    add_styled_table(tbl7_headers, tbl7_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])

    # UI Component Table for Screen 8
    p_heading3("Table 17.8: UI Component & Control Specification - Windows Screen 8 (Analytics & Audit)")
    tbl8_headers = ["Component ID", "Element Type", "Control Label / Title", "Event Handler", "Bound Data Field", "Security / Validation"]
    tbl8_rows = [
        ["AUD-BAR-01", "Bar Chart", "Disaster Proportion Breakdown", "onSelectCategory()", "Disaster.aggregate(groupBy category)", "Normalized percentage bars"],
        ["AUD-CRV-01", "Line Chart", "Hourly Reporting Velocity", "onHoverTimePoint()", "Disaster.aggregate(hourlyCounts)", "Peak inundation highlight"],
        ["AUD-TBL-01", "Audit Table", "System Telemetry Stream", "onSortAuditLogs()", "AuditLog.find().sort({timestamp:-1})", "Immutable write-only collection"],
        ["AUD-EXP-01", "Export Button", "[EXPORT AUDIT PACK CSV]", "onExportAuditCSV()", "AuditLog.export()", "SHA-256 integrity hash attached"]
    ]
    add_styled_table(tbl8_headers, tbl8_rows, [1.0, 1.2, 1.6, 1.4, 1.4, 0.9], bg_header="1A365D", align_center_cols=[0, 1])
'''

# Find insertion point before Section 18 in part 3
target_s18 = 'p_heading1("18. Operational Emergency Workflows & SDMA SOP Protocols")'
if target_s18 in p3:
    p3 = p3.replace(target_s18, screen_tables_code + "\\n\\n    " + target_s18)
    print("Injected 8 UI Component Tables into report_content_part3.py")

with open("report_content_part3.py", "w", encoding="utf-8") as f:
    f.write(p3)
print("Updated report_content_part3.py successfully!")
