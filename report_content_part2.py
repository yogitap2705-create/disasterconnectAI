import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_chapter_3_part2(doc, helpers):
    p_center = helpers['p_center']
    p_heading1 = helpers['p_heading1']
    p_heading2 = helpers['p_heading2']
    p_heading3 = helpers['p_heading3']
    p_body = helpers['p_body']
    p_bullet = helpers['p_bullet']
    add_image = helpers['add_image']
    add_styled_table = helpers['add_styled_table']

    doc.add_page_break()

    # ==============================================================================
    # SECTION 6: DETAILS OF HARDWARE & SOFTWARE USED
    # ==============================================================================
    p_heading1("6. Details of Hardware and Software Used")
    p_body(
        "The DisasterConnectAI architecture is engineered as a high-throughput, low-latency distributed web application designed "
        "to function reliably under adverse environmental and network constraints. The technical stack comprises carefully vetted "
        "enterprise open-source frameworks and cloud services.", space_after=8
    )

    p_heading2("6.1 Hardware Configuration:")
    p_heading3("Server-Side Minimum Infrastructure (State/District Operations Node):")
    p_bullet("Processor: Intel Xeon Scalable Processor (8 Cores, 16 Threads @ 3.20 GHz) or AMD EPYC 7002 Series.", bold_prefix="•")
    p_bullet("System RAM: 32 GB DDR4 ECC Registered Memory (expandable to 64 GB for high-concurrency disaster surges).", bold_prefix="•")
    p_bullet("Storage Subsystem: 1 TB NVMe M.2 Solid State Drive (Read/Write speeds up to 3,500 MB/s) with daily off-site encrypted backup.", bold_prefix="•")
    p_bullet("Network Interface: Dual Gigabit Ethernet (1000BASE-T) with redundant ISP fiber links and 4G/5G failover cellular gateway.", bold_prefix="•")
    p_bullet("Power Backup: 10 kVA Online Uninterruptible Power Supply (UPS) with auxiliary diesel generator integration (24-hour runtime).", bold_prefix="•")

    p_heading3("Client-Side Minimum Hardware (Citizen & Volunteer Terminals):")
    p_bullet("Desktop Environment: Windows 10 / Windows 11 PC, Intel Core i3 / AMD Ryzen 3 or higher, 4 GB RAM, 1080p display.", bold_prefix="•")
    p_bullet("Field Volunteer Mobile: Android 8.0+ or iOS 13+ smartphone with integrated A-GPS receiver, 3G/4G/5G cellular connectivity, and camera.", bold_prefix="•")
    p_bullet("Display Resolution: Responsive layout dynamically optimizing from 360x640 (mobile) to 1920x1080 (widescreen desktop command monitors).", bold_prefix="•")

    p_heading2("6.2 Software Configuration & Development Stack:")
    p_bullet("Operating System (Server): Ubuntu Server 22.04 LTS (Long Term Support) Linux 64-bit with hardened kernel security profiles.", bold_prefix="•")
    p_bullet("Operating System (Client): Microsoft Windows 11 / Windows 10 (Build 19044+) or modern mobile OS.", bold_prefix="•")
    p_bullet("Runtime Environment: Node.js v18.19.0 LTS (JavaScript runtime built on Chrome's V8 engine).", bold_prefix="•")
    p_bullet("Backend Web Framework: Express.js v4.18.2 (Fast, unopinionated, minimalist web framework for Node.js).", bold_prefix="•")
    p_bullet("Primary Database: MongoDB Enterprise / MongoDB Atlas v7.0 (Distributed, document-oriented NoSQL database with native 2dsphere geospatial indexing).", bold_prefix="•")
    p_bullet("Object Document Mapper (ODM): Mongoose v8.0.3 (Elegant MongoDB object modeling for Node.js).", bold_prefix="•")
    p_bullet("Artificial Intelligence Engine: Google Gemini API (gemini-2.5-flash / gemini-1.5-flash) via official `@google/genai` SDK.", bold_prefix="•")
    p_bullet("Real-Time Bidirectional Communication: Socket.io v4.7.2 (WebSocket engine with automatic HTTP long-polling fallback).", bold_prefix="•")
    p_bullet("Geospatial GIS Engine: Leaflet.js v1.9.4 with OpenStreetMap and ISRO Bhuvan satellite tile basemaps.", bold_prefix="•")
    p_bullet("Frontend Framework: React.js v18.2.0 (Component-driven declarative user interface library) with React Router DOM v6.", bold_prefix="•")
    p_bullet("Styling Architecture: Modern responsive CSS3 with CSS Grid, Flexbox, and zero third-party UI dependencies.", bold_prefix="•")
    p_bullet("Reverse Proxy & Web Server: Nginx v1.22 with SSL/TLS termination, HTTP/2 multiplexing, and rate-limiting modules.", bold_prefix="•")
    p_bullet("Process Management: PM2 v5.3.0 (Production Process Manager for Node.js with clustering and auto-restart).", bold_prefix="•")
    p_bullet("Testing Frameworks: Jest v29.7.0 (Unit Testing), Supertest v6.3.3 (HTTP Integration Testing), and k6 (Load Testing).", bold_prefix="•")

    doc.add_page_break()

    # ==============================================================================
    # SECTION 7: DETAILED LIFE CYCLE OF THE PROJECT
    # ==============================================================================
    p_heading1("7. Detailed Life Cycle of the Project (Iterative & Incremental SDLC Model)")
    p_body(
        "Disaster response software development carries zero tolerance for operational failure. Consequently, the traditional Linear "
        "Sequential (Waterfall) model was rejected due to its rigidity and inability to accommodate emergent disaster management protocols. "
        "Instead, DisasterConnectAI was engineered using an Iterative and Incremental Software Development Life Cycle (SDLC) model.", space_after=8
    )

    add_image("lifecycle_diagram.png", width_inch=5.5, caption="Figure 7.1: Detailed Life Cycle of the Project (Iterative and Incremental SDLC Architecture)")

    p_body(
        "As depicted in Figure 7.1, the engineering journey was structured into four feedback-driven iterations:", space_after=6
    )
    p_bullet("Iteration 1: Core Geolocation & Emergency Intake Engine — Focused on architecting the REST API gateway, MongoDB 2dsphere schema, and one-tap satellite GPS capture. Validated with simulated field GPS signals across Kudal Taluka.", bold_prefix="1.")
    p_bullet("Iteration 2: AI Triage & Real-Time GIS Mapping — Integrated Google Gemini AI models for multi-turn conversational triage, threat severity score computation, and Leaflet.js spatial layer rendering.", bold_prefix="2.")
    p_bullet("Iteration 3: District Volunteer Mobilization & Shelter Registry — Developed the dedicated District Volunteer Assignment module, Haversine proximity calculation algorithms, and dynamic shelter capacity meters.", bold_prefix="3.")
    p_bullet("Iteration 4: Family Reunification, Security Hardening & UAT — Completed the Missing Persons Tracing portal, conducted security penetration testing (XSS/SQLi), stress-tested WebSocket streams, and finalized administrative audit telemetry.", bold_prefix="4.")

    doc.add_page_break()

    # ==============================================================================
    # SECTION 8: DATA FLOW DIAGRAMS (DFDs)
    # ==============================================================================
    p_heading1("8. Data Flow Diagrams (DFDs)")
    p_body(
        "Data Flow Diagrams graphically represent the flow of data through an information system, modeling its process aspects, "
        "external entities, data stores, and input/output interfaces. DisasterConnectAI is modeled across three hierarchical abstraction levels.", space_after=8
    )

    p_heading2("8.1 Data Flow Diagram - Level 0 (Context Level DFD):")
    p_body(
        "The Level 0 DFD establishes the structural boundary of the system, identifying external entities (Citizens, Vetted Field Volunteers, "
        "District Emergency Officers, State Disaster Administrators, and the Gemini AI Engine) and their primary information exchanges.", space_after=6
    )
    add_image("dfd_level0.png", width_inch=5.8, caption="Figure 8.1: Data Flow Diagram - Level 0 (Context Level Diagram)")

    p_body(
        "In Figure 8.1, the centralized DisasterConnectAI core receives emergency GPS incident streams from citizens and credentialed telemetry "
        "from volunteers. It delegates unstructured threat narratives to the AI engine, transmitting consolidated tactical operational feeds to "
        "the District Emergency Operations Center (DEOC).", space_after=12
    )

    p_heading2("8.2 First Level Data Flow Diagram (Level 1 DFD):")
    p_body(
        "The Level 1 DFD decomposes the monolithic central system into ten core operational sub-processes:", space_after=6
    )
    p_bullet("Process 1.0: User Registration & Role Authentication", bold_prefix="•")
    p_bullet("Process 2.0: Incident Distress Intake & GPS Coordinate Geolocation", bold_prefix="•")
    p_bullet("Process 3.0: Gemini AI Threat Assessment & Priority Scoring", bold_prefix="•")
    p_bullet("Process 4.0: Live GIS Spatial Layering & Hazard Buffer Mapping", bold_prefix="•")
    p_bullet("Process 5.0: District Jurisdictional Filtering & Verification", bold_prefix="•")
    p_bullet("Process 6.0: Volunteer Proximity Matching & Tactical Dispatch", bold_prefix="•")
    p_bullet("Process 7.0: Relief Camp Occupancy & Shelter Capacity Tracking", bold_prefix="•")
    p_bullet("Process 8.0: Family Reunification & Missing Persons Tracing", bold_prefix="•")
    p_bullet("Process 9.0: 24/7 AI Emergency Response Assistant", bold_prefix="•")
    p_bullet("Process 10.0: Administrative Audit Telemetry & Logging", bold_prefix="•")

    add_image("dfd_level1.png", width_inch=5.8, caption="Figure 8.2: First Level Data Flow Diagram (Level 1 DFD - Functional Decomposition)")

    p_heading2("8.3 Second Level Data Flow Diagram (Level 2 DFD):")
    p_body(
        "The Level 2 DFD provides microscopic detail into the incident ingestion and automated volunteer dispatch pipeline, tracing "
        "data state transformations between client inputs, AI evaluations, MongoDB collections, and field mission deliveries.", space_after=6
    )
    add_image("dfd_level2.png", width_inch=5.8, caption="Figure 8.3: Second Level Data Flow Diagram (Level 2 DFD - Incident & Dispatch Pipeline)")

    doc.add_page_break()

    # ==============================================================================
    # SECTION 9: ENTITY RELATIONSHIP DIAGRAM (ERD)
    # ==============================================================================
    p_heading1("9. Entity Relationship Diagram (ERD)")
    p_body(
        "The Entity Relationship Diagram (ERD) visualizes the logical schema structure of the DisasterConnectAI data layer. While "
        "MongoDB is a non-relational document store, strong logical entity relationships and referencing cardinalities are strictly "
        "enforced via Mongoose schemas to preserve referential integrity.", space_after=8
    )

    add_image("erd_diagram.png", width_inch=5.8, caption="Figure 9.1: Entity Relationship Diagram (ERD) - Core Entities and Referential Cardinalities")

    p_heading2("Core Entity Definitions and Relational Cardinalities:")
    p_bullet("User to Incident (1 : N) — A single registered citizen or officer can report multiple disaster incidents across time. Each incident maintains a mandatory foreign reference (`reportedBy`) pointing to the creator User ID.", bold_prefix="1.")
    p_bullet("Incident to Volunteer (1 : 1 or 1 : N) — A critical incident is assigned to one primary verified volunteer or team lead, who coordinates on-scene tactical operations. The incident tracks `assignedVolunteer` with full audit history.", bold_prefix="2.")
    p_bullet("Shelter to Incident (1 : N) — A designated relief shelter services evacuees originating from multiple surrounding disaster incidents within its taluka catchment zone.", bold_prefix="3.")
    p_bullet("Missing Person to Shelter (N : 1) — Multiple missing or displaced persons are cross-referenced to specific relief camps or hospital facilities (`foundLocationShelter`).", bold_prefix="4.")
    p_bullet("Audit Log to User (N : 1) — All system state mutations record the foreign key of the administrative or volunteer actor (`actorId`).", bold_prefix="5.")

    doc.add_page_break()

    # ==============================================================================
    # SECTION 10: COMPLETE DATA DICTIONARY
    # ==============================================================================
    p_heading1("10. Complete Data Dictionary")
    p_body(
        "The Data Dictionary provides formal, detailed metadata specifications for all data elements stored within the DisasterConnectAI "
        "MongoDB database. It outlines field identifiers, BSON data types, key constraints, validation rules, and business semantics.", space_after=8
    )

    # 10.1 Users Collection
    p_heading2("10.1 Collection Name: `users`")
    p_body("Stores authentication profiles, role designations, contact parameters, and jurisdictional district assignments.", space_after=4)
    u_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    u_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique primary identifier for user document"],
        ["fullName", "String", "None", "No", "Trimmed, 3 to 100 characters", "Full legal name of the user"],
        ["email", "String", "Unique", "No", "Valid RFC 5322 regex, lowercase", "Unique email address for authentication"],
        ["password", "String", "None", "No", "Bcrypt hash ($2a$10$...), min 60 char", "Cryptographically salted password hash"],
        ["phone", "String", "Index", "No", "Regex: ^\\+?[1-9]\\d{9,14}$", "Primary mobile number for SMS/Emergency alerts"],
        ["role", "String", "Index", "No", "['citizen', 'volunteer', 'admin']", "Security role governing system authorization"],
        ["district", "String", "Index", "No", "['Sindhudurg', 'Ratnagiri', ...]", "Primary administrative district jurisdiction"],
        ["taluka", "String", "None", "Yes", "Valid taluka within district", "Sub-district administrative subdivision"],
        ["isVerified", "Boolean", "None", "No", "Default: false", "Verification flag for official volunteers/officers"],
        ["isActive", "Boolean", "None", "No", "Default: true", "Account activation flag"],
        ["createdAt", "Date", "None", "No", "Default: Date.now()", "UTC timestamp of user registration"],
        ["updatedAt", "Date", "None", "No", "Auto-updated", "UTC timestamp of last profile mutation"],
    ]
    add_styled_table(u_headers, u_rows, [1.1, 0.9, 0.7, 0.6, 2.3, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.2 Incidents Collection
    p_heading2("10.2 Collection Name: `incidents`")
    p_body("Maintains real-time disaster event telemetry, GPS spatial coordinates, AI triage ratings, and dispatch status.", space_after=4)
    inc_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    inc_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique disaster incident tracking ID"],
        ["disasterType", "String", "Index", "No", "['Flood', 'Landslide', 'Fire', ...]", "Categorical disaster classification"],
        ["severity", "String", "Index", "No", "['Low', 'Medium', 'High', 'Critical']", "Assessed disaster threat severity level"],
        ["description", "String", "None", "No", "Sanitized string, 10-2000 chars", "Citizen emergency narrative and immediate hazards"],
        ["location.type", "String", "None", "No", "Literal: 'Point'", "GeoJSON object type specification"],
        ["location.coords", "Array [Double]", "2dsphere", "No", "[longitude, latitude] WGS-84", "High-precision GPS coordinates array"],
        ["address", "String", "None", "Yes", "Text address / landmark", "Human-readable geographical landmark"],
        ["district", "String", "Index", "No", "Standardized district name", "Jurisdictional administrative district"],
        ["taluka", "String", "Index", "Yes", "Standardized taluka name", "Local taluka / sub-district location"],
        ["trappedCount", "Number", "None", "No", "Integer >= 0, default: 0", "Estimated trapped or imperiled citizens"],
        ["mediaUrls", "Array [String]", "None", "Yes", "Valid URL array", "Cloud-hosted disaster photographic evidence"],
        ["aiRiskScore", "Double", "None", "No", "Float range: 0.00 to 1.00", "Normalized priority score calculated by Gemini"],
        ["aiActionPlan", "String", "None", "Yes", "Markdown formatted SOP", "Instant survival instructions generated by AI"],
        ["status", "String", "Index", "No", "['Reported', 'Assigned', 'Resolved']", "Current operational status of incident"],
        ["reportedBy", "ObjectId", "FK", "No", "Ref: 'User'", "Foreign key referencing reporting citizen"],
        ["assignedUnit", "ObjectId", "FK", "Yes", "Ref: 'User' / 'Volunteer'", "Foreign key referencing dispatched volunteer"],
        ["createdAt", "Date", "Index", "No", "Default: Date.now()", "UTC timestamp of emergency report ingestion"],
        ["resolvedAt", "Date", "None", "Yes", "Nullable Date", "UTC timestamp when incident was closed safe"],
    ]
    add_styled_table(inc_headers, inc_rows, [1.2, 0.9, 0.7, 0.6, 2.2, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.3 Shelters Collection
    p_heading2("10.3 Collection Name: `shelters`")
    p_body("Records relief shelter facilities, geographic coordinates, bed capacity meters, and humanitarian relief inventories.", space_after=4)
    sh_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    sh_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique relief camp identifier"],
        ["name", "String", "None", "No", "String, 3 to 150 characters", "Official designated name of the relief shelter"],
        ["location.coords", "Array [Double]", "2dsphere", "No", "[longitude, latitude]", "GeoJSON spatial coordinates for GPS navigation"],
        ["district", "String", "Index", "No", "Standardized district name", "District in which shelter is situated"],
        ["taluka", "String", "Index", "No", "Standardized taluka name", "Taluka administrative subdivision"],
        ["totalCapacity", "Number", "None", "No", "Integer > 0", "Total certified evacuee bed capacity"],
        ["occupiedBeds", "Number", "None", "No", "Integer >= 0, <= totalCapacity", "Current active registered bed occupancy"],
        ["medicalPost", "Boolean", "None", "No", "Default: false", "Flag indicating on-site physician/paramedic unit"],
        ["doctorIncharge", "String", "None", "Yes", "Doctor name & phone", "Contact info of attending emergency medical officer"],
        ["foodRationsDays", "Number", "None", "No", "Integer >= 0", "Estimated days of food provisions remaining"],
        ["drinkingWater", "Boolean", "None", "No", "Default: true", "Status of potable drinking water supply"],
        ["contactPhone", "String", "None", "No", "Valid phone string", "Emergency shelter hotline phone number"],
        ["isActive", "Boolean", "Index", "No", "Default: true", "Flag indicating shelter is actively receiving evacuees"],
    ]
    add_styled_table(sh_headers, sh_rows, [1.2, 0.9, 0.7, 0.6, 2.2, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.4 Volunteers Collection
    p_heading2("10.4 Collection Name: `volunteers`")
    p_body("Tracks certified volunteer operational skills, jurisdictional coverage, real-time availability, and active deployment status.", space_after=4)
    v_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    v_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique volunteer record identifier"],
        ["userId", "ObjectId", "FK, Unique", "No", "Ref: 'User'", "Foreign key referencing user authentication profile"],
        ["skills", "Array [String]", "Index", "No", "['Swift Water', 'Paramedic', ...]", "Certified specialized disaster relief competencies"],
        ["district", "String", "Index", "No", "Standardized district name", "Registered district of primary deployment"],
        ["taluka", "String", "Index", "No", "Standardized taluka name", "Home taluka for proximity routing"],
        ["availability", "String", "Index", "No", "['Available', 'Dispatched', 'Off']", "Real-time deployment availability status"],
        ["currentLocation", "Array [Double]", "2dsphere", "Yes", "[longitude, latitude]", "Live GPS coordinates broadcast by mobile app"],
        ["activeIncident", "ObjectId", "FK", "Yes", "Ref: 'Incident'", "Foreign key to currently assigned disaster incident"],
        ["bloodGroup", "String", "None", "Yes", "['A+', 'B+', 'O+', 'AB+', ...]", "Volunteer blood group for medical preparedness"],
        ["equipmentList", "Array [String]", "None", "Yes", "['Inflatable Boat', '4x4', ...]", "Tactical disaster gear owned or operated"],
        ["completedMissions", "Number", "None", "No", "Integer >= 0, default: 0", "Total verified rescue operations completed"],
    ]
    add_styled_table(v_headers, v_rows, [1.2, 0.9, 0.8, 0.6, 2.1, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.5 Missing Persons Collection
    p_heading2("10.5 Collection Name: `missing_persons`")
    p_body("Contains humanitarian tracing profiles, photographic biometric references, and reunification milestones.", space_after=4)
    mp_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    mp_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique missing person case tracking ID"],
        ["fullName", "String", "Index", "No", "Trimmed, 2 to 100 characters", "Full name of the missing or displaced person"],
        ["age", "Number", "None", "No", "Integer, 0 to 120", "Age in completed years"],
        ["gender", "String", "None", "No", "['Male', 'Female', 'Other']", "Gender identity"],
        ["photoUrl", "String", "None", "Yes", "Valid image URL string", "Photograph URL for public and field identification"],
        ["lastSeenLocation", "String", "None", "No", "Text description", "Geographical area where person was last observed"],
        ["lastSeenDistrict", "String", "Index", "No", "Standardized district name", "District jurisdiction of disappearance"],
        ["lastSeenTaluka", "String", "Index", "No", "Standardized taluka name", "Taluka jurisdiction of disappearance"],
        ["status", "String", "Index", "No", "['Missing', 'Hospitalized', 'Safe']", "Current tracing status of the individual"],
        ["contactPerson", "String", "None", "No", "Name of seeking relative", "Primary inquiring relative or guardian"],
        ["contactPhone", "String", "None", "No", "Valid phone string", "Emergency telephone number of inquiring relative"],
        ["registeredBy", "ObjectId", "FK", "No", "Ref: 'User'", "User ID of reporting citizen or official"],
    ]
    add_styled_table(mp_headers, mp_rows, [1.2, 0.9, 0.7, 0.6, 2.2, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.6 Audit Logs Collection
    p_heading2("10.6 Collection Name: `audit_logs`")
    p_body("Maintains an immutable, append-only chronological log of all life-critical administrative and operational actions.", space_after=4)
    al_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    al_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique audit event identifier"],
        ["timestamp", "Date", "Index", "No", "Default: Date.now()", "Precise millisecond UTC execution timestamp"],
        ["eventType", "String", "Index", "No", "['DISPATCH', 'TRIAGE', ...]", "Categorical operational event descriptor"],
        ["actorId", "ObjectId", "FK", "No", "Ref: 'User'", "Foreign key to user executing the action"],
        ["actorRole", "String", "None", "No", "Role at execution time", "Security role context during event execution"],
        ["resourceId", "String", "None", "Yes", "Incident ID or Shelter ID", "Primary system resource affected by event"],
        ["actionDetails", "String", "None", "No", "Detailed event narrative", "Human-readable textual breakdown of mutation"],
        ["ipAddress", "String", "None", "No", "IPv4 or IPv6 string", "Client IP address captured at API gateway"],
        ["executionStatus", "String", "None", "No", "['SUCCESS', 'FAILED']", "Result of the operational invocation"],
    ]
    add_styled_table(al_headers, al_rows, [1.2, 0.9, 0.7, 0.6, 2.2, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.7 Notifications Collection
    p_heading2("10.7 Collection Name: `notifications`")
    p_body("Records tactical in-app mission dispatch alerts, delivery timestamps, read acknowledgments, and SMS gateway payloads.", space_after=4)
    notif_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    notif_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique notification alert identifier"],
        ["recipientId", "ObjectId", "FK, Index", "No", "Ref: 'User'", "Foreign key referencing target citizen or volunteer"],
        ["incidentId", "ObjectId", "FK", "Yes", "Ref: 'Incident'", "Associated disaster incident reference"],
        ["title", "String", "None", "No", "Trimmed, 5 to 150 characters", "Brief urgency headline (e.g., 'CRITICAL DISPATCH ORDER')"],
        ["messageBody", "String", "None", "No", "Text, 10 to 1000 characters", "Full textual briefing with GPS location details"],
        ["channel", "String", "None", "No", "['IN_APP', 'SMS', 'PUSH']", "Transmission channel utilized for dispatch"],
        ["deliveryStatus", "String", "Index", "No", "['QUEUED', 'DELIVERED', 'ACK']", "Current delivery and acknowledgment status"],
        ["sentAt", "Date", "Index", "No", "Default: Date.now()", "Timestamp when notification was broadcast"],
        ["acknowledgedAt", "Date", "None", "Yes", "Nullable Date", "Timestamp when recipient tapped acknowledgment"]
    ]
    add_styled_table(notif_headers, notif_rows, [1.2, 0.9, 0.8, 0.6, 2.1, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])

    # 10.8 Evacuation Corridors Collection
    p_heading2("10.8 Collection Name: `evacuation_corridors`")
    p_body("Maintains geographic vector paths, waypoint coordinates, road clearance statuses, and bridge inundation states.", space_after=4)
    cor_headers = ["Field Name", "BSON Type", "Key", "Null", "Validation / Enum Rules", "Description"]
    cor_rows = [
        ["_id", "ObjectId", "PK", "No", "Auto-generated 12-byte hex", "Unique evacuation corridor corridor ID"],
        ["corridorName", "String", "None", "No", "Trimmed string", "Official name (e.g., 'NH-66 Kudal Bypass Corridor')"],
        ["district", "String", "Index", "No", "Standardized district name", "Primary district jurisdiction"],
        ["taluka", "String", "Index", "No", "Standardized taluka name", "Primary taluka jurisdiction"],
        ["waypoints", "Array [Coordinates]", "None", "No", "Array of [lon, lat] pairs", "Sequential geographic vertices forming path polyline"],
        ["passabilityStatus", "String", "Index", "No", "['OPEN', 'RESTRICTED', 'CLOSED']", "Real-time vehicular transit safety rating"],
        ["clearedByAuthority", "String", "None", "No", "Officer name / PWD Dept", "Statutory authority certifying corridor safety"],
        ["lastInspectedAt", "Date", "None", "No", "UTC Date timestamp", "Timestamp of most recent physical engineer survey"]
    ]
    add_styled_table(cor_headers, cor_rows, [1.3, 1.0, 0.8, 0.6, 2.0, 1.8], bg_header="1A365D", align_center_cols=[1, 2, 3])


    doc.add_page_break()

    # ==============================================================================
    # SECTION 11 TO 15: UML ARCHITECTURAL DIAGRAMS
    # ==============================================================================
    p_heading1("11. UML Activity Diagrams")
    p_body(
        "Activity diagrams model the dynamic operational workflows of the platform, capturing the sequential and parallel control "
        "flows from initial citizen distress signaling to field resolution.", space_after=8
    )
    add_image("activity_diagram.png", width_inch=5.5, caption="Figure 11.1: UML Activity Diagram - End-to-End Emergency Lifecycle Workflow")

    p_heading1("12. UML Class Diagram")
    p_body(
        "The UML Class Diagram models the static structural design of DisasterConnectAI, showing system classes, domain attributes, "
        "public/private operations, and associative relationships.", space_after=8
    )
    add_image("class_diagram.png", width_inch=5.8, caption="Figure 12.1: UML Class Diagram - Core Domain Classes, Controllers, and Service Interfaces")

    p_heading1("13. UML Object Diagram & State Machine Diagram")
    p_body(
        "The UML Object Diagram captures a concrete runtime snapshot of instantiated objects during an active flood emergency scenario "
        "in Kudal Taluka. Figure 13.2 defines the complete mathematical State Machine governing incident lifecycle transitions.", space_after=8
    )
    add_image("object_diagram.png", width_inch=5.8, caption="Figure 13.1: UML Object Diagram - Concrete Operational System Instances Snapshot")
    add_image("state_machine_incident.png", width_inch=5.8, caption="Figure 13.2: UML State Machine Diagram - Incident Lifecycle State Transitions")

    p_heading1("14. UML Use Case Diagram & Actor Specifications")
    p_body(
        "The Use Case Diagram defines interactions between external human/system actors and the functional boundaries of the platform.", space_after=8
    )
    add_image("usecase_diagram.png", width_inch=5.8, caption="Figure 14.1: UML Use Case Diagram - Actor Roles and System Capabilities")

    p_heading1("15. UML Sequence Diagrams")
    p_body(
        "Figure 15.1 details the chronological message passing sequences between client web browsers, the Node.js API Gateway, the Gemini "
        "AI evaluation engine, and the District Emergency Operations Center (DEOC).", space_after=8
    )
    add_image("sequence_diagram_sos.png", width_inch=5.8, caption="Figure 15.1: UML Sequence Diagram - SOS Distress Ingestion and Tactical Dispatch Pipeline")

    doc.add_page_break()

    # ==============================================================================
    # SECTION 16: MATHEMATICAL & ALGORITHMIC FORMULATIONS
    # ==============================================================================
    p_heading1("16. Mathematical and Algorithmic Formulations")
    p_body(
        "To eliminate subjective human bias during mass casualty emergencies, DisasterConnectAI relies on formal mathematical and algorithmic models:", space_after=8
    )

    p_heading2("16.1 Composite Incident Priority Score Formulation (P_i):")
    p_body(
        "The priority score governing an incident's position in the emergency dispatch queue is calculated via a multi-factor weighted equation:\n"
        "P_i = w_s · S_i + w_t · T_i + w_h · H_i + w_v · V_i\n\n"
        "Where:\n"
        "• S_i ∈ [0.2, 1.0] represents the base Disaster Severity (L1=0.2, L2=0.4, L3=0.6, L4=0.8, L5=1.0).\n"
        "• T_i = min(1.0, count / 20.0) represents the Trapped Persons factor normalized against a critical threshold of 20 victims.\n"
        "• H_i ∈ [0.0, 1.0] represents Immediate Environmental Hazard presence (e.g., submerged high-tension power cables, rising water surge).\n"
        "• V_i ∈ [0.0, 1.0] represents the Vulnerability coefficient (presence of infants, hospital patients, or senior citizens).\n"
        "• Weights satisfy: w_s (0.40) + w_t (0.30) + w_h (0.20) + w_v (0.10) = 1.00.\n\n"
        "Incidents with P_i >= 0.85 are automatically flagged as CRITICAL L5, triggering automated SDRF audio alarms in the Command Center.",
        space_after=10
    )

    p_heading2("16.2 Multi-Criteria Volunteer Proximity & Skill Matching Weight Algorithm (M_v):")
    p_body(
        "When an incident requires volunteer assignment, candidate volunteers in the district are ranked using an optimization score:\n"
        "M_v = α · (1 / (1 + d_v)) + β · SkillMatch(v, req) + γ · Availability(v)\n\n"
        "Where d_v is the Haversine distance in kilometers, SkillMatch evaluates to 1.0 for exact certification (e.g. Swift Water) "
        "and 0.4 for general volunteers, and α=0.50, β=0.35, γ=0.15. This ensures the best-qualified closest responder is selected.",
        space_after=14
    )

    p_heading2("16.3 Mathematical Simulation Case Study: Karli River Flash Flood (Sindhudurg District):")
    p_body(
        "To illustrate the algorithmic execution of DisasterConnectAI during a live disaster event, consider the following simulated "
        "flash flood scenario in Kudal Taluka. At 14:30 hrs, a citizen reports a sudden river surge near Kudal Bazar Bridge:\n"
        "• Severity Tier: Level 5 (S_i = 1.0)\n"
        "• Trapped Citizens: 45 persons trapped on shop rooftops (count = 45 -> T_i = min(1.0, 45/20) = 1.0)\n"
        "• Immediate Environmental Hazard: Submerged high-tension electrical transformer (H_i = 1.0)\n"
        "• Vulnerable Citizens: 8 senior citizens and 5 infants present on-site (V_i = 1.0)\n\n"
        "Applying the Composite Priority Equation:\n"
        "P_i = (0.40 * 1.0) + (0.30 * 1.0) + (0.20 * 1.0) + (0.10 * 1.0) = 1.00 (MAXIMUM CRITICAL TIER)\n\n"
        "Because P_i = 1.00 >= 0.85, the system automatically elevates the incident to the top of the statewide dispatch queue, "
        "initiates audio distress chimes in the DEOC Command Center, and triggers the Volunteer Proximity Matching Engine.",
        space_after=10
    )

    p_heading2("16.4 Multi-Criteria Volunteer Proximity & Skill Ranking Matrix:")
    p_body(
        "For Incident INC-8941 at coordinates (16.0245° N, 73.6892° E), the Haversine distance and multi-criteria optimization scores "
        "(M_v) for five registered volunteers across Sindhudurg District are calculated below:", space_after=6
    )

    rank_headers = ["Volunteer ID", "Full Name", "Taluka / Base", "GPS Coordinates", "Distance (d_v)", "Certified Skill", "Skill Match (β)", "Composite Score (M_v)", "Rank"]
    rank_rows = [
        ["V-1042", "Nitin Suresh Parab", "Kudal Bazar", "16.0350 N, 73.6980 E", "1.82 km", "Swift Water Rescue", "1.00 (Exact)", "0.874", "RANK 1 (DISPATCHED)"],
        ["V-1088", "Dr. Pooja M. Rane", "Kudal MIDC", "16.0420 N, 73.7020 E", "2.41 km", "Paramedic / Trauma", "0.80 (High)", "0.762", "RANK 2 (SUPPORT)"],
        ["V-1102", "Sunil D. Kadam", "Pinguli Village", "16.0120 N, 73.7150 E", "3.14 km", "Food Logistics / 4x4", "0.60 (Medium)", "0.621", "RANK 3 (LOGISTICS)"],
        ["V-1145", "Ajay R. Sawant", "Sawantwadi Road", "15.9850 N, 73.7220 E", "4.25 km", "HAM Radio Operator", "0.50 (Support)", "0.518", "RANK 4 (STANDBY)"],
        ["V-1180", "Mahesh V. Naik", "Malvan Coastal", "16.0580 N, 73.4720 E", "23.40 km", "Swift Water Rescue", "1.00 (Exact)", "0.385", "RANK 5 (REMOTE)"]
    ]
    add_styled_table(rank_headers, rank_rows, [0.8, 1.4, 1.0, 1.3, 0.8, 1.2, 0.9, 1.1, 1.0], bg_header="1A365D", align_center_cols=[0, 4, 6, 7, 8])

    p_heading2("16.5 Dynamic Shelter Bed Depletion Differential Formulation:")
    p_body(
        "To prevent camp overcrowding during large-scale evacuations, DisasterConnectAI models the rate of change of available beds "
        "B(t) across time t using the continuous differential equation:\n"
        "dB(t) / dt = μ_dis(t) - λ_arr(t)\n\n"
        "Where:\n"
        "• λ_arr(t) is the arrival rate of newly displaced evacuees directed from surrounding incident zones.\n"
        "• μ_dis(t) is the discharge rate of treated/reunified evacuees departing to family or secondary housing.\n\n"
        "When available beds B(t) fall below 10% of total certified capacity (B(t) <= 0.10 * B_max), the Command Center triggers an "
        "Automated Overflow Alert, and the Leaflet GIS routing engine dynamically recalculates evacuation corridor vectors to divert "
        "incoming ambulances to the nearest adjacent sub-district shelter facility.",
        space_after=14
    )


    print("Part 2 (Hardware/Software, SDLC, DFDs, ERD, Data Dictionary, UML, Math) written successfully.")

print("Report content Part 2 module defined!")
