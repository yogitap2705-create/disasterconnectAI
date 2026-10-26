import os

FILE_PATH = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\report_content_part2.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Additional Collections for Section 10
extra_collections = '''
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
'''

# 2. Additional Mathematical Formulations & Worked Numerical Simulations
extra_math = '''
    p_heading2("16.3 Mathematical Simulation Case Study: Karli River Flash Flood (Sindhudurg District):")
    p_body(
        "To illustrate the algorithmic execution of DisasterConnectAI during a live disaster event, consider the following simulated "
        "flash flood scenario in Kudal Taluka. At 14:30 hrs, a citizen reports a sudden river surge near Kudal Bazar Bridge:\\n"
        "• Severity Tier: Level 5 (S_i = 1.0)\\n"
        "• Trapped Citizens: 45 persons trapped on shop rooftops (count = 45 -> T_i = min(1.0, 45/20) = 1.0)\\n"
        "• Immediate Environmental Hazard: Submerged high-tension electrical transformer (H_i = 1.0)\\n"
        "• Vulnerable Citizens: 8 senior citizens and 5 infants present on-site (V_i = 1.0)\\n\\n"
        "Applying the Composite Priority Equation:\\n"
        "P_i = (0.40 * 1.0) + (0.30 * 1.0) + (0.20 * 1.0) + (0.10 * 1.0) = 1.00 (MAXIMUM CRITICAL TIER)\\n\\n"
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
        "B(t) across time t using the continuous differential equation:\\n"
        "dB(t) / dt = μ_dis(t) - λ_arr(t)\\n\\n"
        "Where:\\n"
        "• λ_arr(t) is the arrival rate of newly displaced evacuees directed from surrounding incident zones.\\n"
        "• μ_dis(t) is the discharge rate of treated/reunified evacuees departing to family or secondary housing.\\n\\n"
        "When available beds B(t) fall below 10% of total certified capacity (B(t) <= 0.10 * B_max), the Command Center triggers an "
        "Automated Overflow Alert, and the Leaflet GIS routing engine dynamically recalculates evacuation corridor vectors to divert "
        "incoming ambulances to the nearest adjacent sub-district shelter facility.",
        space_after=14
    )
'''

# Insert extra_collections into Section 10
target_s10_end = '    add_styled_table(al_headers, al_rows, [1.2, 0.9, 0.7, 0.6, 2.2, 1.9], bg_header="1A365D", align_center_cols=[1, 2, 3])'
if target_s10_end in text:
    text = text.replace(target_s10_end, target_s10_end + "\n" + extra_collections)
    print("Injected Collections 10.7 and 10.8 into Section 10!")

# Insert extra_math into Section 16
target_s16_end = '        "and 0.4 for general volunteers, and α=0.50, β=0.35, γ=0.15. This ensures the best-qualified closest responder is selected.",\n        space_after=14\n    )'
if target_s16_end in text:
    text = text.replace(target_s16_end, target_s16_end + "\n" + extra_math)
    print("Injected Mathematical Simulations and Volunteer Ranking Matrix into Section 16!")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Updated {FILE_PATH} successfully! New size: {os.path.getsize(FILE_PATH):,} bytes")
