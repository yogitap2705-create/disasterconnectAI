import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\report_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def draw_browser_chrome(ax, url="https://disasterconnect.ai/admin", tab_title="DisasterConnect AI - Emergency Command"):
    # Outer desktop browser window
    bg_rect = patches.FancyBboxPatch((0.2, 0.2), 15.6, 9.6, boxstyle="round,pad=0.1",
                                    fc="#F4F6F9", ec="#718096", lw=2)
    ax.add_patch(bg_rect)

    # Top title bar
    title_bar = patches.Rectangle((0.2, 9.1), 15.6, 0.7, fc="#E2E8F0")
    ax.add_patch(title_bar)

    # Window control dots (Mac/Windows style)
    ax.add_patch(patches.Circle((0.6, 9.45), 0.12, fc="#E53E3E", ec="none")) # Red
    ax.add_patch(patches.Circle((0.95, 9.45), 0.12, fc="#DD6B20", ec="none")) # Yellow
    ax.add_patch(patches.Circle((1.3, 9.45), 0.12, fc="#38A169", ec="none")) # Green

    # Browser Tab
    tab = patches.FancyBboxPatch((1.8, 9.1), 4.2, 0.65, boxstyle="round,pad=0.05", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(tab)
    ax.text(2.0, 9.42, "[SECURE] " + tab_title, fontsize=8, fontweight='bold', color="#2D3748", va='center')

    # URL / Address Bar
    url_bar = patches.FancyBboxPatch((0.5, 8.45), 15.0, 0.55, boxstyle="round,pad=0.05", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(url_bar)
    clean_url = url if url.startswith("https://") else "https://" + url
    ax.text(0.8, 8.72, clean_url, fontsize=8, color="#4A5568", va='center', family='monospace')
    ax.text(15.2, 8.72, "[LIVE SYSTEM ONLINE]", fontsize=7.5, color="#800020", ha='right', va='center', fontweight='bold')

    # Desktop Application Header / Navbar
    app_nav = patches.Rectangle((0.2, 7.65), 15.6, 0.75, fc="#800020")
    ax.add_patch(app_nav)
    ax.text(0.6, 8.02, "DISASTERCONNECT AI", fontsize=11, fontweight='bold', color="#FFFFFF", va='center')
    ax.text(3.6, 8.02, "EMERGENCY RESPONSE SYSTEM", fontsize=7.5, color="#FBD38D", va='center')

    # Navbar links
    links = ["Incident Triage", "GIS Map", "Shelters", "Directory", "Missing Persons", "SOPs", "Admin Command"]
    for i, link in enumerate(links):
        is_active = (link in tab_title) or (i == 6 and "Command" in tab_title) or (i == 0 and "Intake" in tab_title)
        x_pos = 6.8 + i * 1.25
        if is_active:
            pill = patches.FancyBboxPatch((x_pos-0.1, 7.78), 1.15, 0.48, boxstyle="round,pad=0.05", fc="#9B111E", ec="#FBD38D", lw=1)
            ax.add_patch(pill)
        ax.text(x_pos + 0.48, 8.02, link, fontsize=7.5, color="#FFFFFF" if not is_active else "#FFD700",
                ha='center', va='center', fontweight='bold' if is_active else 'normal')

    # Status indicator
    ax.text(15.4, 8.02, "STATEWIDE HQ", fontsize=7.5, color="#68D391", ha='right', va='center', fontweight='bold')

# 1. Desktop Screen: Admin Command Center
def create_desktop_admin():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/admin", tab_title="Command Center & District Dispatch")

    # Command Header banner
    header_banner = patches.FancyBboxPatch((0.5, 6.7), 15.0, 0.8, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#E2E8F0", lw=1.2)
    ax.add_patch(header_banner)
    ax.text(0.8, 7.22, "Disaster Intelligence Administration & Statewide Dispatch", fontsize=11, fontweight='bold', color="#800020")
    ax.text(0.8, 6.9, "Real-time incident triage, automated district matching, and volunteer resource routing across Maharashtra.", fontsize=8, color="#718096")

    # Key Telemetry Cards
    metrics = [
        ("18", "Active Incidents", "#E53E3E", "#FFF5F5"),
        ("42", "Registered Volunteers", "#2B6CB0", "#EBF8FF"),
        ("36", "Districts Monitored", "#800020", "#FFF5F5"),
        ("100%", "Operational Readiness", "#2F855A", "#F0FFF4")
    ]
    for idx, (val, label, col, bg) in enumerate(metrics):
        card = patches.FancyBboxPatch((0.5 + idx * 3.8, 5.5), 3.6, 1.05, boxstyle="round,pad=0.08", fc=bg, ec=col, lw=1.5)
        ax.add_patch(card)
        ax.text(0.8 + idx * 3.8, 6.18, val, fontsize=16, fontweight='bold', color=col)
        ax.text(0.8 + idx * 3.8, 5.75, label, fontsize=8, color="#4A5568", fontweight='bold')

    # Filter Toolbar
    f_bar = patches.FancyBboxPatch((0.5, 4.6), 15.0, 0.7, boxstyle="round,pad=0.05", fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(f_bar)
    ax.text(0.8, 4.95, "Search: [ Pune / Flash Flood / Dam ]", fontsize=8, color="#4A5568", va='center')
    ax.text(6.0, 4.95, "District Filter: [ All Maharashtra Districts ▼ ]", fontsize=8, color="#800020", fontweight='bold', va='center')
    ax.text(11.2, 4.95, "Priority: [ High Severity (8+) ▼ ]", fontsize=8, color="#C53030", fontweight='bold', va='center')
    ax.text(15.2, 4.95, "Showing: 18 Incidents", fontsize=7.5, color="#718096", ha='right', va='center')

    # Table Header
    th = patches.Rectangle((0.5, 3.9), 15.0, 0.55, fc="#2D3748")
    ax.add_patch(th)
    ax.text(0.8, 4.18, "INCIDENT & AI TRIAGE", fontsize=7.5, fontweight='bold', color="#FFFFFF")
    ax.text(4.2, 4.18, "DISTRICT / GPS LOCATION", fontsize=7.5, fontweight='bold', color="#FFFFFF")
    ax.text(7.6, 4.18, "REPORTED BY", fontsize=7.5, fontweight='bold', color="#FFFFFF")
    ax.text(10.2, 4.18, "ASSIGNED VOLUNTEER & STATUS", fontsize=7.5, fontweight='bold', color="#FFFFFF")
    ax.text(14.0, 4.18, "ACTIONS", fontsize=7.5, fontweight='bold', color="#FFFFFF")

    # Table Rows
    rows_data = [
        ("Flash Flood (Risk: 8.8/10)", "Karve Nagar, Pune (18.4912, 73.8214)", "Rohit Patil", "Rahul Deshmukh [Pune Force]", "Active Mission", "#FFF5F5"),
        ("Chemical Fire (Risk: 9.2/10)", "Ambad MIDC, Nashik (19.9975, 73.7898)", "Dr. Amit Roy", "Sneha Kulkarni [Hazmat]", "Dispatched", "#FFFFFF"),
        ("Storm Surge (Risk: 8.4/10)", "Alibaug Coast, Raigad (18.5158, 72.9984)", "Vijay Kadam", "Auto 1-Click Match Available", "Pending", "#FFF5F5"),
        ("Landslide Warning (7.5/10)", "Varandha Ghat, Satara (17.6805, 73.9803)", "Mahesh Joshi", "Tanvi Mane [First Aid]", "In Progress", "#FFFFFF"),
    ]

    for idx, (inc, loc, rep, vol, stat, row_bg) in enumerate(rows_data):
        y_r = 3.15 - idx * 0.7
        r_rect = patches.Rectangle((0.5, y_r), 15.0, 0.65, fc=row_bg, ec="#E2E8F0", lw=0.8)
        ax.add_patch(r_rect)

        ax.text(0.8, y_r + 0.35, inc, fontsize=7.5, fontweight='bold', color="#800020")
        ax.text(4.2, y_r + 0.35, loc, fontsize=7.2, color="#2D3748")
        ax.text(7.6, y_r + 0.35, rep, fontsize=7.2, color="#4A5568")

        # Volunteer pill
        v_col = "#2B6CB0" if "Auto" not in vol else "#DD6B20"
        ax.text(10.2, y_r + 0.35, vol, fontsize=7.2, fontweight='bold', color=v_col)

        # Status badge
        s_bg = "#C6F6D5" if stat in ["Active Mission", "Dispatched"] else "#FEEBC8"
        s_fg = "#22543D" if stat in ["Active Mission", "Dispatched"] else "#744210"
        b_patch = patches.FancyBboxPatch((13.6, y_r + 0.15), 1.6, 0.35, boxstyle="round,pad=0.05", fc=s_bg, ec="none")
        ax.add_patch(b_patch)
        ax.text(14.4, y_r + 0.32, stat, fontsize=6.8, fontweight='bold', color=s_fg, ha='center')

    path = os.path.join(OUTPUT_DIR, "desktop_screen_command_center.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop command center:", path)

# 2. Desktop Screen: Real-Time GIS Map
def create_desktop_gis():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/map", tab_title="Live GIS Incident Response Map")

    # Map Canvas area
    map_bg = patches.Rectangle((0.5, 0.5), 15.0, 7.0, fc="#E8ECEF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(map_bg)

    # Stylized Map Roads / Rivers
    ax.plot([1.0, 4.0, 7.0, 10.0, 15.0], [2.0, 3.5, 4.2, 3.8, 5.0], color="#90CDF4", lw=7, alpha=0.7) # River
    ax.plot([0.5, 15.5], [4.5, 4.5], color="#CBD5E0", lw=3, linestyle="--") # Highway
    ax.plot([8.0, 8.0], [0.5, 7.5], color="#CBD5E0", lw=3, linestyle="--") # Expressway

    # District Boundaries & Labels
    districts = [
        ("PUNE DISTRICT (High Alert)", 4.5, 3.2),
        ("MUMBAI METROPOLITAN", 2.0, 5.8),
        ("NASHIK INDUSTRIAL ZONE", 7.5, 6.2),
        ("RAIGAD COASTAL BELT", 2.5, 2.0),
        ("SATARA DISTRICT", 6.8, 1.5)
    ]
    for dname, dx, dy in districts:
        ax.text(dx, dy, dname, fontsize=8, fontweight='bold', color="#718096", alpha=0.8)

    # Incident Markers with Perimeters
    incidents = [
        (4.8, 3.6, "PUNE: Flash Flood", "Risk: 8.8/10", "#E53E3E", 1.2),
        (7.8, 5.8, "NASHIK: Chemical Blaze", "Risk: 9.2/10", "#DD6B20", 0.9),
        (2.8, 2.3, "RAIGAD: Storm Surge", "Risk: 8.4/10", "#3182CE", 1.4),
        (11.2, 4.2, "SOLAPUR: Severe Drought", "Risk: 6.2/10", "#D69E2E", 0.8),
    ]

    for ix, iy, ititle, irisk, icol, iradius in incidents:
        # Evacuation perimeter circle
        circle = patches.Circle((ix, iy), iradius, fc=icol, ec=icol, alpha=0.18, lw=1.5, linestyle=":")
        ax.add_patch(circle)
        # Pin icon
        pin = patches.Circle((ix, iy), 0.22, fc=icol, ec="white", lw=2)
        ax.add_patch(pin)
        # Label card
        lbl_box = patches.FancyBboxPatch((ix - 1.1, iy + 0.35), 2.2, 0.75, boxstyle="round,pad=0.05", fc="#FFFFFF", ec=icol, lw=1.2)
        ax.add_patch(lbl_box)
        ax.text(ix, iy + 0.82, ititle, fontsize=6.8, fontweight='bold', color="#1A202C", ha='center')
        ax.text(ix, iy + 0.52, irisk, fontsize=6.2, color=icol, fontweight='bold', ha='center')

    # Floating Map Legend & Control Panel (Desktop UI overlay)
    legend = patches.FancyBboxPatch((0.8, 0.8), 4.4, 2.6, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#A0AEC0", lw=1.2)
    ax.add_patch(legend)
    ax.text(1.1, 3.05, "GIS Situational Layers", fontsize=8.5, fontweight='bold', color="#800020")
    ax.text(1.1, 2.65, "[RED] Critical Hazard Perimeter (> 8.0 Risk)", fontsize=7.2, color="#2D3748")
    ax.text(1.1, 2.30, "[ORANGE] Active Industrial / Fire Incident", fontsize=7.2, color="#2D3748")
    ax.text(1.1, 1.95, "[BLUE] Hydro-Meteorological Storm Surge", fontsize=7.2, color="#2D3748")
    ax.text(1.1, 1.60, "[GREEN] Verified Evacuation Relief Shelter", fontsize=7.2, color="#2D3748")
    ax.text(1.1, 1.20, "GPS Telemetry: WGS-84 Live Satellite Sync", fontsize=6.8, color="#718096", style='italic')

    # Top Right Map Actions
    actions = patches.FancyBboxPatch((10.8, 6.2), 4.4, 1.0, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#A0AEC0", lw=1.2)
    ax.add_patch(actions)
    ax.text(13.0, 6.85, "Filters: [ All Active Incidents ▼ ]", fontsize=7.5, color="#800020", fontweight='bold', ha='center')
    ax.text(13.0, 6.45, "Layer: OpenStreetMap Standard + Radar", fontsize=7.0, color="#4A5568", ha='center')

    path = os.path.join(OUTPUT_DIR, "desktop_screen_gis_map.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop GIS map:", path)

# 3. Desktop Screen: Incident Intake & Instant SOS
def create_desktop_report():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/report", tab_title="Live Incident Intake & GPS Triage")

    # Left Column: Emergency Form
    f_box = patches.FancyBboxPatch((0.6, 0.5), 9.0, 7.0, boxstyle="round,pad=0.1", fc="#FFFFFF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(f_box)

    ax.text(1.0, 7.15, "Emergency Incident Intake Form", fontsize=11, fontweight='bold', color="#800020")
    ax.text(1.0, 6.8, "Submit verified field intelligence to deploy volunteer rescue units and trigger automated AI triage.", fontsize=7.5, color="#718096")

    # SOS Banner inside form
    sos_banner = patches.FancyBboxPatch((1.0, 5.8), 8.2, 0.8, boxstyle="round,pad=0.05", fc="#FFF5F5", ec="#E53E3E", lw=1.5)
    ax.add_patch(sos_banner)
    ax.text(1.2, 6.3, "CRITICAL LIFE-THREATENING EMERGENCY?", fontsize=8, fontweight='bold', color="#9B111E")
    ax.text(1.2, 6.0, "One-tap SOS immediately locks your device GPS coordinates and marks report as Priority 1.", fontsize=7, color="#4A5568")

    sos_btn = patches.FancyBboxPatch((7.0, 5.95), 2.0, 0.5, boxstyle="round,pad=0.05", fc="#E53E3E", ec="none")
    ax.add_patch(sos_btn)
    ax.text(8.0, 6.2, "INSTANT SOS", fontsize=8, fontweight='bold', color="#FFFFFF", ha='center')

    # Fields
    fields = [
        ("Disaster Category", "[ Flood / Flash Flood Surge ▼ ]"),
        ("Jurisdiction District", "[ Pune District (Western Maharashtra) ▼ ]"),
        ("Incident Location / Landmark", "Karve Nagar, near Mula-Mutha river bridge"),
        ("GPS Coordinates (Auto-Detect)", "Latitude: 18.491204, Longitude: 73.821458 (High Accuracy GPS Lock)"),
        ("Hazard Description & Damage", "Water surge entered residential ground floors. 4 families trapped on terrace.")
    ]

    for idx, (f_name, f_val) in enumerate(fields):
        y_f = 5.0 - idx * 0.82
        ax.text(1.0, y_f + 0.35, f_name, fontsize=7.2, fontweight='bold', color="#2D3748")
        inp_rect = patches.FancyBboxPatch((1.0, y_f), 8.2, 0.38, boxstyle="round,pad=0.03", fc="#F7FAFC", ec="#CBD5E0", lw=0.8)
        ax.add_patch(inp_rect)
        ax.text(1.2, y_f + 0.18, f_val, fontsize=7.2, color="#4A5568", va='center')

    # Submit Button
    s_btn = patches.FancyBboxPatch((1.0, 0.75), 8.2, 0.5, boxstyle="round,pad=0.05", fc="#800020", ec="none")
    ax.add_patch(s_btn)
    ax.text(5.1, 1.0, "SUBMIT INCIDENT & DISPATCH RESCUE UNITS", fontsize=8.5, fontweight='bold', color="white", ha='center')

    # Right Column: Automated AI Triage Preview
    ai_box = patches.FancyBboxPatch((10.0, 0.5), 5.4, 7.0, boxstyle="round,pad=0.1", fc="#FFFFFF", ec="#800020", lw=1.8)
    ax.add_patch(ai_box)

    ax.text(10.3, 7.15, "AI Triage & Decision Matrix", fontsize=10.5, fontweight='bold', color="#800020")
    ax.text(10.3, 6.8, "Real-time threat assessment generated by AI Engine", fontsize=7.2, color="#718096")

    # Threat Score Badge
    score_card = patches.FancyBboxPatch((10.3, 5.7), 4.8, 0.9, boxstyle="round,pad=0.05", fc="#FFF5F5", ec="#E53E3E", lw=1.2)
    ax.add_patch(score_card)
    ax.text(10.5, 6.25, "ASSESSED RISK SCORE", fontsize=7, color="#718096", fontweight='bold')
    ax.text(10.5, 5.9, "8.8 / 10", fontsize=15, fontweight='bold', color="#E53E3E")
    ax.text(14.8, 6.1, "SEVERITY: CRITICAL", fontsize=7, fontweight='bold', color="#E53E3E", ha='right')

    # Action Plan
    ax.text(10.3, 5.3, "IMMEDIATE CIVILIAN SURVIVAL PROTOCOL:", fontsize=7.2, fontweight='bold', color="#800020")
    steps = [
        "1. Move immediately to RCC structures above 2nd floor.",
        "2. De-energize building circuit breaker and gas valves.",
        "3. Avoid walking or driving through moving flood water.",
        "4. Signal rescue teams with flashlight or whistle."
    ]
    for s_idx, stp in enumerate(steps):
        ax.text(10.3, 4.85 - s_idx * 0.45, stp, fontsize=6.8, color="#2D3748")

    # Recommended Supplies
    ax.text(10.3, 2.9, "RECOMMENDED EMERGENCY SUPPLIES:", fontsize=7.2, fontweight='bold', color="#800020")
    supplies = ["Water Purification Tablets", "Trauma Medical Kit", "Inflatable Life Raft", "High-Beam Torch"]
    for sp_idx, sup in enumerate(supplies):
        sup_pill = patches.FancyBboxPatch((10.3 + (sp_idx % 2) * 2.5, 2.3 - (sp_idx // 2) * 0.5), 2.3, 0.35,
                                         boxstyle="round,pad=0.03", fc="#EDF2F7", ec="#CBD5E0", lw=0.8)
        ax.add_patch(sup_pill)
        ax.text(10.4 + (sp_idx % 2) * 2.5, 2.48 - (sp_idx // 2) * 0.5, "• " + sup, fontsize=6.2, color="#2D3748")

    path = os.path.join(OUTPUT_DIR, "desktop_screen_incident_intake.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop incident intake:", path)

# 4. Desktop Screen: Relief Shelters Registry
def create_desktop_shelters():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/shelters", tab_title="Relief Camps & Evacuation Shelters")

    # Header
    h_box = patches.FancyBboxPatch((0.5, 6.7), 15.0, 0.8, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#CBD5E0", lw=1.2)
    ax.add_patch(h_box)
    ax.text(0.8, 7.22, "Evacuation Shelters & Relief Camps Live Registry", fontsize=11, fontweight='bold', color="#800020")
    ax.text(0.8, 6.9, "Real-time bed occupancy tracker, emergency rations availability, and verified on-site medical amenities.", fontsize=8, color="#718096")

    # Shelters Grid (Desktop 3-column view)
    shelters_data = [
        ("Balewadi Sports Complex Relief Camp", "Pune District", "340 / 500 Beds", "68% Full", ["Drinking Water", "Meals", "Medical Team", "Generator Backup"], "OPEN"),
        ("Shivajinagar Community Evacuation Hub", "Pune District", "120 / 150 Beds", "80% Full", ["Dry Rations", "Bedding", "Pediatric First Aid"], "OPEN"),
        ("Ambad Municipal High School Camp", "Nashik District", "95 / 200 Beds", "47% Full", ["Medical Ward", "Decontamination Kit", "Blankets"], "OPEN"),
        ("Alibaug Coastal Cyclone Shelter", "Raigad District", "290 / 300 Beds", "96% Full", ["Storm Bunker", "Satellite Radio", "Food Supplies"], "NEAR CAPACITY"),
        ("Kalwa Relief Center", "Thane District", "180 / 250 Beds", "72% Full", ["Cooked Food", "Clean Water", "Ambulance Onsite"], "OPEN"),
        ("Dharavi Multi-Utility Camp", "Mumbai Suburban", "400 / 400 Beds", "100% Full", ["Dry Rations", "Medical Support", "Sanitation"], "FULL - REROUTE")
    ]

    for idx, (s_name, s_dist, s_beds, s_pct, s_amen, s_stat) in enumerate(shelters_data):
        row = idx // 3
        col = idx % 3
        x_s = 0.5 + col * 5.1
        y_s = 4.7 - row * 2.0

        card = patches.FancyBboxPatch((x_s, y_s), 4.8, 1.85, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#E2E8F0", lw=1.5)
        ax.add_patch(card)

        # Status badge
        st_col = "#2F855A" if "OPEN" in s_stat else ("#C53030" if "FULL" in s_stat else "#DD6B20")
        st_bg = "#F0FFF4" if "OPEN" in s_stat else ("#FFF5F5" if "FULL" in s_stat else "#FFFAF0")
        b_p = patches.FancyBboxPatch((x_s + 3.4, y_s + 1.45), 1.25, 0.3, boxstyle="round,pad=0.03", fc=st_bg, ec=st_col, lw=1)
        ax.add_patch(b_p)
        ax.text(x_s + 4.02, y_s + 1.6, s_stat, fontsize=6.2, fontweight='bold', color=st_col, ha='center')

        ax.text(x_s + 0.2, y_s + 1.6, s_name, fontsize=7.5, fontweight='bold', color="#800020")
        ax.text(x_s + 0.2, y_s + 1.35, "[District] " + s_dist, fontsize=7, color="#718096")

        # Occupancy Progress Bar
        pct_val = int(s_pct.replace("% Full", ""))
        ax.text(x_s + 0.2, y_s + 1.05, f"Capacity: {s_beds} ({s_pct})", fontsize=6.8, fontweight='bold', color="#2D3748")
        bar_bg = patches.Rectangle((x_s + 0.2, y_s + 0.8), 4.4, 0.18, fc="#E2E8F0")
        ax.add_patch(bar_bg)
        bar_fg = patches.Rectangle((x_s + 0.2, y_s + 0.8), 4.4 * (pct_val / 100), 0.18, fc=st_col)
        ax.add_patch(bar_fg)

        # Amenities
        amen_text = "Amenities: " + " • ".join(s_amen[:3])
        ax.text(x_s + 0.2, y_s + 0.45, amen_text, fontsize=6.2, color="#4A5568")

        # Button
        btn = patches.FancyBboxPatch((x_s + 0.2, y_s + 0.1), 4.4, 0.28, boxstyle="round,pad=0.02", fc="#800020", ec="none")
        ax.add_patch(btn)
        ax.text(x_s + 2.4, y_s + 0.24, "Get Evacuation Route Directions", fontsize=6.5, fontweight='bold', color="white", ha='center')

    path = os.path.join(OUTPUT_DIR, "desktop_screen_shelters.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop shelters registry:", path)

# 5. Desktop Screen: Missing Persons Tracing
def create_desktop_missing():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/missing-persons", tab_title="Missing Persons & Reunification Registry")

    # Header
    h_box = patches.FancyBboxPatch((0.5, 6.7), 15.0, 0.8, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#CBD5E0", lw=1.2)
    ax.add_patch(h_box)
    ax.text(0.8, 7.22, "Family Reunification & Missing Persons Tracing Registry", fontsize=11, fontweight='bold', color="#800020")
    ax.text(0.8, 6.9, "Search and report displaced family members during flood, cyclone, and industrial disaster emergencies.", fontsize=8, color="#718096")

    # Action bar
    act_bar = patches.FancyBboxPatch((0.5, 5.75), 15.0, 0.75, boxstyle="round,pad=0.05", fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(act_bar)
    ax.text(0.8, 6.12, "Search by Name: [ Rajesh Gaikwad ... ]", fontsize=8, color="#4A5568", va='center')
    ax.text(6.0, 6.12, "District Filter: [ Pune District ▼ ]", fontsize=8, color="#800020", fontweight='bold', va='center')
    ax.text(10.5, 6.12, "Status: [ All Records ▼ ]", fontsize=8, color="#2D3748", va='center')

    btn_new = patches.FancyBboxPatch((13.0, 5.9), 2.3, 0.45, boxstyle="round,pad=0.05", fc="#800020", ec="none")
    ax.add_patch(btn_new)
    ax.text(14.15, 6.12, "+ File Missing Person", fontsize=7.5, fontweight='bold', color="white", ha='center', va='center')

    # Tracing Cards (Desktop 3-column view)
    persons = [
        ("Aarav Suresh Kulkarni", "Age: 9 | Male", "Pune (Karve Nagar)", "Last seen near river park wearing yellow shirt", "MISSING", "#E53E3E"),
        ("Savitri Devendra Patil", "Age: 68 | Female", "Pune (Sinhagad Rd)", "Elderly citizen separated during night flood evacuation", "LOCATED SAFE", "#2F855A"),
        ("Rameshwar Shinde", "Age: 34 | Male", "Nashik (MIDC)", "Factory worker displaced during industrial blaze", "LOCATED SAFE", "#2F855A"),
        ("Ananya Dipak Mane", "Age: 14 | Female", "Raigad (Alibaug)", "Separated from school bus during coastal storm", "MISSING", "#E53E3E"),
        ("Gopal Vithal Gaikwad", "Age: 52 | Male", "Satara (Wai)", "Missing following mudslide near residential settlement", "SEARCH ACTIVE", "#DD6B20"),
        ("Pooja Santosh Jadhav", "Age: 27 | Female", "Thane (Kalwa)", "Sheltered at Kalwa Municipal Relief Center", "LOCATED SAFE", "#2F855A")
    ]

    for idx, (p_name, p_details, p_loc, p_notes, p_stat, p_col) in enumerate(persons):
        row = idx // 3
        col = idx % 3
        x_p = 0.5 + col * 5.1
        y_p = 3.7 - row * 1.9

        card = patches.FancyBboxPatch((x_p, y_p), 4.8, 1.75, boxstyle="round,pad=0.08", fc="#FFFFFF", ec="#E2E8F0", lw=1.5)
        ax.add_patch(card)

        # Status badge
        s_bg = "#FFF5F5" if "MISSING" in p_stat else ("#F0FFF4" if "SAFE" in p_stat else "#FFFAF0")
        b_p = patches.FancyBboxPatch((x_p + 3.2, y_p + 1.35), 1.45, 0.3, boxstyle="round,pad=0.03", fc=s_bg, ec=p_col, lw=1)
        ax.add_patch(b_p)
        ax.text(x_p + 3.92, y_p + 1.5, p_stat, fontsize=6.2, fontweight='bold', color=p_col, ha='center')

        ax.text(x_p + 0.2, y_p + 1.48, p_name, fontsize=7.8, fontweight='bold', color="#1A202C")
        ax.text(x_p + 0.2, y_p + 1.25, p_details + " | " + p_loc, fontsize=6.8, color="#718096")
        ax.text(x_p + 0.2, y_p + 0.95, p_notes, fontsize=6.5, color="#4A5568")

        # Action button
        btn_mark = patches.FancyBboxPatch((x_p + 0.2, y_p + 0.2), 4.4, 0.32, boxstyle="round,pad=0.02",
                                         fc="#EDF2F7" if "SAFE" in p_stat else "#2F855A", ec="#CBD5E0", lw=0.8)
        ax.add_patch(btn_mark)
        btn_txt = "Safety Confirmed [OK]" if "SAFE" in p_stat else "Mark Located Safe (1-Click)"
        btn_fg = "#718096" if "SAFE" in p_stat else "white"
        ax.text(x_p + 2.4, y_p + 0.36, btn_txt, fontsize=6.8, fontweight='bold', color=btn_fg, ha='center')

    path = os.path.join(OUTPUT_DIR, "desktop_screen_missing_persons.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop missing persons:", path)

# 6. Desktop Screen: AI Emergency Chatbot
def create_desktop_chatbot():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_browser_chrome(ax, url="https://disasterconnect.ai/chat", tab_title="24/7 AI Emergency Response Assistant")

    # Main Chat Frame (Desktop 2-column console)
    # Left Column: Emergency Quick Prompts & Helplines
    left_panel = patches.FancyBboxPatch((0.5, 0.5), 4.5, 7.0, boxstyle="round,pad=0.1", fc="#FFFFFF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(left_panel)

    ax.text(0.8, 7.15, "Emergency Knowledge Base", fontsize=9.5, fontweight='bold', color="#800020")
    ax.text(0.8, 6.8, "Instant Disaster SOP Queries", fontsize=7.2, color="#718096")

    prompts = [
        "[SOP] Flash Flood Survival Steps",
        "[SOP] Industrial Fire Evacuation",
        "[FIRST AID] Treatment for Severe Burns",
        "[SUPPLIES] 72-Hour Emergency Kit Checklist",
        "[SEISMIC] Earthquake Drop, Cover, Hold",
        "[COASTAL] Cyclone Storm Surge Safety"
    ]
    for idx, pr in enumerate(prompts):
        y_pr = 6.1 - idx * 0.6
        p_card = patches.FancyBboxPatch((0.8, y_pr), 3.9, 0.45, boxstyle="round,pad=0.03", fc="#F7FAFC", ec="#E2E8F0", lw=1)
        ax.add_patch(p_card)
        ax.text(1.0, y_pr + 0.22, pr, fontsize=7, color="#2D3748", va='center')

    # Helplines Box
    h_card = patches.FancyBboxPatch((0.8, 0.8), 3.9, 1.4, boxstyle="round,pad=0.05", fc="#FFF5F5", ec="#E53E3E", lw=1.2)
    ax.add_patch(h_card)
    ax.text(1.0, 1.95, "NATIONAL EMERGENCY HELPLINES", fontsize=7, fontweight='bold', color="#9B111E")
    ax.text(1.0, 1.65, "• All Emergencies: 112", fontsize=6.8, color="#2D3748")
    ax.text(1.0, 1.40, "• NDRF Disaster Helpline: 1078", fontsize=6.8, color="#2D3748")
    ax.text(1.0, 1.15, "• Ambulance: 108  |  Fire: 101", fontsize=6.8, color="#2D3748")

    # Right Column: Chat Stream Area
    chat_box = patches.FancyBboxPatch((5.3, 0.5), 10.2, 7.0, boxstyle="round,pad=0.1", fc="#FFFFFF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(chat_box)

    # Chat Header
    c_hdr = patches.Rectangle((5.3, 6.75), 10.2, 0.75, fc="#F8F9FA")
    ax.add_patch(c_hdr)
    ax.text(5.6, 7.22, "DisasterConnect AI Virtual Assistant (Gemini 1.5 Flash)", fontsize=9.5, fontweight='bold', color="#800020")
    ax.text(5.6, 6.92, "Active Session | Context: Disaster Risk Reduction & Emergency Medicine", fontsize=7.2, color="#718096")

    # Chat Messages
    # User message
    u_bubble = patches.FancyBboxPatch((8.5, 5.8), 6.6, 0.7, boxstyle="round,pad=0.08", fc="#800020", ec="none")
    ax.add_patch(u_bubble)
    ax.text(8.7, 6.15, "What should I do immediately during a sudden flash flood in a residential area?", fontsize=7.2, color="white")

    # Bot response
    b_bubble = patches.FancyBboxPatch((5.6, 2.3), 9.6, 3.2, boxstyle="round,pad=0.08", fc="#F7FAFC", ec="#E2E8F0", lw=1.2)
    ax.add_patch(b_bubble)
    ax.text(5.9, 5.2, "DisasterConnect AI Assistant:", fontsize=7.5, fontweight='bold', color="#800020")

    ai_advice = [
        "1. IMMEDIATE VERTICAL EVACUATION: Move to reinforced upper floors (2nd floor or above). Avoid basements.",
        "2. UTILITIES ISOLATION: Turn off main electricity circuit breakers and LPG gas cylinders immediately.",
        "3. WATER HAZARD RULE: Never walk, swim, or drive through flood waters. Six inches of water can knock you down.",
        "4. TELECOMMUNICATIONS: Conserve phone battery for life safety emergency calls (Dial 112).",
        "5. SIGNALS: If trapped on terrace, wave a brightly colored cloth or torch to alert rescue teams."
    ]
    for a_idx, adv in enumerate(ai_advice):
        ax.text(5.9, 4.65 - a_idx * 0.5, adv, fontsize=6.8, color="#2D3748")

    # Input Box at bottom
    inp_bg = patches.FancyBboxPatch((5.6, 0.8), 8.2, 0.7, boxstyle="round,pad=0.05", fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(inp_bg)
    ax.text(5.9, 1.15, "Ask emergency guidelines or first aid steps...", fontsize=7.5, color="#A0AEC0", va='center')

    send_btn = patches.FancyBboxPatch((14.0, 0.8), 1.2, 0.7, boxstyle="round,pad=0.05", fc="#800020", ec="none")
    ax.add_patch(send_btn)
    ax.text(14.6, 1.15, "SEND", fontsize=7.5, fontweight='bold', color="white", ha='center', va='center')

    path = os.path.join(OUTPUT_DIR, "desktop_screen_ai_chatbot.png")
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Created desktop AI chatbot:", path)

if __name__ == "__main__":
    create_desktop_admin()
    create_desktop_gis()
    create_desktop_report()
    create_desktop_shelters()
    create_desktop_missing()
    create_desktop_chatbot()
    print("All 6 desktop widescreen screenshots generated successfully!")
