import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\report_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/admin", tab_title="DisasterConnect AI - Windows Command Center"):
    """
    Renders an authentic Windows 11 / Windows 10 desktop application & browser window frame.
    Explicitly features:
    - Standard Windows window controls on top-right: Minimize (-), Maximize ([ ]), Close (X).
    - Windows Edge/Chrome tab strip on top-left.
    - Windows navigation controls: Back, Forward, Refresh, Address bar with Lock/Shield.
    - Zero macOS/iOS traffic light dots.
    """
    # Outer desktop browser window (Windows frame)
    bg_rect = patches.Rectangle((0.1, 0.1), 15.8, 9.8, fc="#F8FAFC", ec="#64748B", lw=1.5)
    ax.add_patch(bg_rect)

    # 1. Windows Title Bar (Windows 11 / Windows 10 style dark/light header)
    title_bar = patches.Rectangle((0.1, 9.25), 15.8, 0.65, fc="#E2E8F0", ec="#CBD5E1", lw=0.5)
    ax.add_patch(title_bar)

    # Windows browser tab on top-left
    tab = patches.FancyBboxPatch((0.3, 9.25), 4.8, 0.65, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E1", lw=1)
    ax.add_patch(tab)
    # App icon badge
    ax.add_patch(patches.Rectangle((0.45, 9.42), 0.25, 0.28, fc="#800020", ec="none"))
    ax.text(0.57, 9.56, "+", fontsize=9, fontweight='bold', color="#FFFFFF", ha='center', va='center')
    ax.text(0.85, 9.56, tab_title[:40], fontsize=8, fontweight='bold', color="#0F172A", va='center')
    # Close tab 'x'
    ax.text(4.85, 9.56, "x", fontsize=8.5, color="#64748B", ha='center', va='center')

    # New tab '+' button
    ax.text(5.35, 9.56, "+", fontsize=11, color="#64748B", ha='center', va='center')

    # WINDOWS WINDOW CONTROLS ON TOP RIGHT: Minimize (-), Maximize ([ ]), Close (X)
    # Minimize Button
    min_box = patches.Rectangle((14.0, 9.25), 0.6, 0.65, fc="#E2E8F0", ec="none")
    ax.add_patch(min_box)
    ax.plot([14.2, 14.4], [9.55, 9.55], color="#1E293B", lw=1.6)

    # Maximize / Restore Button
    max_box = patches.Rectangle((14.6, 9.25), 0.6, 0.65, fc="#E2E8F0", ec="none")
    ax.add_patch(max_box)
    ax.add_patch(patches.Rectangle((14.78, 9.45), 0.24, 0.22, fill=False, ec="#1E293B", lw=1.2))

    # Close Button (Windows signature red with white X)
    close_box = patches.Rectangle((15.2, 9.25), 0.7, 0.65, fc="#E81123", ec="none")
    ax.add_patch(close_box)
    ax.text(15.55, 9.55, "X", fontsize=9, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # 2. Windows Navigation Bar & Omnibox (Address Bar)
    nav_bar = patches.Rectangle((0.1, 8.6), 15.8, 0.65, fc="#FFFFFF", ec="#E2E8F0", lw=0.5)
    ax.add_patch(nav_bar)

    # Windows Back, Forward, Refresh buttons
    ax.text(0.35, 8.92, "<", fontsize=10, fontweight='bold', color="#64748B", ha='center', va='center')
    ax.text(0.75, 8.92, ">", fontsize=10, fontweight='bold', color="#94A3B8", ha='center', va='center')
    ax.text(1.15, 8.92, "o", fontsize=10, fontweight='bold', color="#64748B", ha='center', va='center')

    # Address / URL Bar with Secure Lock
    url_box = patches.FancyBboxPatch((1.45, 8.68), 13.0, 0.48, boxstyle="round,pad=0.03", fc="#F8FAFC", ec="#CBD5E1", lw=0.8)
    ax.add_patch(url_box)
    ax.text(1.65, 8.92, "[SECURE HTTPS]", fontsize=7, fontweight='bold', color="#166534", va='center')
    clean_url = url if url.startswith("https://") else "https://" + url
    ax.text(2.8, 8.92, clean_url, fontsize=8, color="#334155", va='center', family='monospace')
    ax.text(14.3, 8.92, "Windows Desktop", fontsize=7, color="#64748B", ha='right', va='center')

    # Windows User Profile / More
    ax.add_patch(patches.Circle((14.8, 8.92), 0.16, fc="#800020", ec="none"))
    ax.text(14.8, 8.92, "A", fontsize=7.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')
    ax.text(15.4, 8.92, "...", fontsize=11, fontweight='bold', color="#64748B", ha='center', va='center')

    # 3. Application Top Navigation Header (DisasterConnectAI)
    app_header = patches.Rectangle((0.1, 7.85), 15.8, 0.75, fc="#800020")
    ax.add_patch(app_header)
    ax.text(0.4, 8.22, "DISASTERCONNECT AI", fontsize=11, fontweight='bold', color="#FFFFFF", va='center')
    ax.text(3.4, 8.22, "STATE EMERGENCY OPERATIONS CENTER", fontsize=7, color="#FDE047", va='center')

    # Navigation Tabs
    nav_items = ["Emergency Triage", "GIS Map", "Shelters", "Missing Persons", "Volunteer Dispatch", "AI Assistant", "Admin Command"]
    for i, item in enumerate(nav_items):
        is_sel = (item in tab_title) or (i == 6 and "Command" in tab_title) or (i == 4 and "Volunteer" in tab_title) or (i == 0 and "Intake" in tab_title) or (i == 1 and "GIS" in tab_title)
        x = 6.4 + i * 1.3
        if is_sel:
            sel_patch = patches.FancyBboxPatch((x-0.1, 7.98), 1.2, 0.48, boxstyle="round,pad=0.03", fc="#991B1B", ec="#FDE047", lw=1)
            ax.add_patch(sel_patch)
        ax.text(x + 0.5, 8.22, item, fontsize=7.2, color="#FFFFFF" if not is_sel else "#FEF08A",
                ha='center', va='center', fontweight='bold' if is_sel else 'normal')

    ax.text(15.6, 8.22, "STATUS: ONLINE", fontsize=7.5, fontweight='bold', color="#4ADE80", ha='right', va='center')

# ==============================================================================
# 1. WINDOWS SCREEN: ADMIN COMMAND CENTER & STATEWIDE DISPATCHER
# ==============================================================================
def create_windows_admin_command():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/admin", tab_title="DisasterConnect AI - Windows Command Center")

    # Metrics Summary Cards (KPIs)
    kpis = [
        ("ACTIVE EMERGENCIES", "18", "6 Critical / 12 Moderate", "#FFF5F5", "#E53E3E"),
        ("VOLUNTEERS DEPLOYED", "94", "Sindhudurg & Ratnagiri Units", "#F0FFF4", "#38A169"),
        ("RELIEF CAMPS ACTIVE", "24", "Total Capacity: 4,800 Beds", "#EBF8FF", "#3182CE"),
        ("AI TRIAGE ACCURACY", "99.4%", "Gemini Automated Latency 82ms", "#FAF5FF", "#805AD5"),
    ]
    for i, (title, val, sub, bg, border) in enumerate(kpis):
        x = 0.4 + i * 3.8
        card = patches.FancyBboxPatch((x, 6.7), 3.6, 0.95, boxstyle="round,pad=0.05", fc=bg, ec=border, lw=1.5)
        ax.add_patch(card)
        ax.text(x + 0.2, 7.45, title, fontsize=7.5, fontweight='bold', color=border)
        ax.text(x + 0.2, 7.05, val, fontsize=16, fontweight='bold', color="#1A202C")
        ax.text(x + 0.2, 6.82, sub, fontsize=6.8, color="#718096")

    # Table Header & Controls
    ax.text(0.4, 6.35, "Statewide Real-Time Incident Priority Dispatch Table", fontsize=11, fontweight='bold', color="#1A202C")
    ax.text(15.6, 6.35, "[EXPORT INCIDENT AUDIT CSV]", fontsize=8, fontweight='bold', color="#2B6CB0", ha='right')

    # Table Structure
    table_bg = patches.Rectangle((0.4, 0.4), 15.2, 5.75, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(table_bg)

    # Table Columns
    headers = [("INCIDENT ID", 1.2), ("TYPE & SEVERITY", 3.2), ("DISTRICT / TALUKA", 5.5), ("GPS COORDINATES", 8.0), ("AI TRIAGE ASSESSMENT", 11.2), ("DISPATCH UNIT", 13.8), ("ACTION", 15.1)]
    th_bar = patches.Rectangle((0.4, 5.75), 15.2, 0.4, fc="#EDF2F7")
    ax.add_patch(th_bar)
    for title, x_c in headers:
        ax.text(x_c, 5.95, title, fontsize=7, fontweight='bold', color="#4A5568", ha='center', va='center')

    # Rows
    rows = [
        ("INC-8941", "Flash Flood (L5 CRITICAL)", "Sindhudurg / Kudal", "16.0245 N, 73.6892 E", "High Water Level (5.2m) - 45 Stranded", "SDRF Team 04", "DISPATCHED", "#E53E3E"),
        ("INC-8940", "Landslide (L4 HIGH)", "Sindhudurg / Sawantwadi", "15.9042 N, 73.8198 E", "NH-66 Highway Blockade - Heavy Debris", "PWD & Volunteer Team", "IN-TRANSIT", "#DD6B20"),
        ("INC-8939", "Medical Emergency (L5)", "Sindhudurg / Malvan", "16.0592 N, 73.4682 E", "Oxygen Depletion at Rural Health Post", "Red Cross Paramedic", "EN-ROUTE", "#E53E3E"),
        ("INC-8938", "Building Wall Collapse", "Ratnagiri / Chiplun", "17.5323 N, 73.5182 E", "Residential Structural Breach - 8 Trapped", "Fire Rescue Squad", "ON-SCENE", "#C53030"),
        ("INC-8937", "Power Grid Failure", "Sindhudurg / Kankavli", "16.2731 N, 73.7143 E", "High Tension Transformer Submerged", "MSEDCL Technical Unit", "ASSIGNED", "#3182CE"),
        ("INC-8936", "Drinking Water Shortage", "Sindhudurg / Vengurla", "15.8624 N, 73.6341 E", "Municipal Tanker Contamination", "Volunteer Relief Cell", "RESOLVED", "#38A169"),
        ("INC-8935", "Bridge Scour Warning", "Sindhudurg / Dodamarg", "15.7531 N, 73.9521 E", "Tilari River Pier Scour Detected", "Irrigation Engineers", "MONITORING", "#D69E2E"),
        ("INC-8934", "Cattle Evacuation Need", "Sindhudurg / Devgad", "16.3762 N, 73.3789 E", "60 Livestock Threatened by Rising Creek", "Animal Husbandry Unit", "DISPATCHED", "#3182CE")
    ]

    for idx, (inc_id, inc_type, taluka, coords, triage, unit, action, color) in enumerate(rows):
        y = 5.35 - idx * 0.62
        # alternating row shading
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((0.4, y-0.25), 15.2, 0.58, fc="#F7FAFC", ec="none"))
        ax.plot([0.4, 15.6], [y-0.25, y-0.25], color="#E2E8F0", lw=0.6)

        ax.text(1.2, y, inc_id, fontsize=7.5, fontweight='bold', color="#2B6CB0", ha='center', va='center')
        ax.text(3.2, y, inc_type, fontsize=7.2, fontweight='bold', color=color, ha='center', va='center')
        ax.text(5.5, y, taluka, fontsize=7.2, color="#2D3748", ha='center', va='center')
        ax.text(8.0, y, coords, fontsize=6.8, color="#718096", ha='center', va='center', family='monospace')
        ax.text(11.2, y, triage[:42], fontsize=7, color="#2D3748", ha='center', va='center')
        ax.text(13.8, y, unit, fontsize=7, fontweight='bold', color="#2B6CB0", ha='center', va='center')

        # Action pill button
        pill = patches.FancyBboxPatch((14.65, y-0.18), 0.9, 0.36, boxstyle="round,pad=0.03", fc=color, ec="none")
        ax.add_patch(pill)
        ax.text(15.1, y, action, fontsize=6.2, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_command_center.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 2. WINDOWS SCREEN: REAL-TIME GIS SPATIAL INCIDENT & EVACUATION MAP
# ==============================================================================
def create_windows_gis_map():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/map", tab_title="DisasterConnect AI - GIS Spatial Incident Map")

    # Main layout: Left Layer Control Sidebar (3.4 width), Right Interactive GIS Map (11.8 width)
    # Left Sidebar
    sidebar = patches.Rectangle((0.4, 0.4), 3.4, 7.2, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(sidebar)

    ax.text(0.6, 7.25, "GIS Spatial Layers", fontsize=10, fontweight='bold', color="#1A202C")
    ax.text(0.6, 7.02, "Select active map overlays & telemetry", fontsize=6.8, color="#718096")

    layers = [
        ("[X] Active Flash Floods (L5)", "#E53E3E", True),
        ("[X] Landslide Blockades (L4)", "#DD6B20", True),
        ("[X] Safe Evacuation Shelters", "#38A169", True),
        ("[X] Designated Evacuation Corridors", "#3182CE", True),
        ("[ ] Flood Inundation 100-Yr Model", "#805AD5", False),
        ("[ ] Real-time Weather Radar / IMD", "#D69E2E", False),
        ("[ ] Road Closures & Bridges Down", "#E53E3E", False),
    ]
    for idx, (lbl, col, is_chk) in enumerate(layers):
        y = 6.6 - idx * 0.42
        box = patches.FancyBboxPatch((0.55, y-0.12), 3.1, 0.32, boxstyle="round,pad=0.02",
                                     fc="#F7FAFC" if is_chk else "#FFFFFF", ec=col if is_chk else "#E2E8F0", lw=1)
        ax.add_patch(box)
        ax.text(0.7, y+0.04, lbl, fontsize=7.2, fontweight='bold' if is_chk else 'normal', color=col if is_chk else "#718096", va='center')

    # Selected Incident Details Box in Sidebar
    sel_box = patches.FancyBboxPatch((0.55, 0.6), 3.1, 3.2, boxstyle="round,pad=0.04", fc="#FFF5F5", ec="#E53E3E", lw=1.5)
    ax.add_patch(sel_box)
    ax.text(0.75, 3.55, "SELECTED INCIDENT PIN", fontsize=8, fontweight='bold', color="#E53E3E")
    ax.text(0.75, 3.25, "ID: INC-8941 (CRITICAL L5)", fontsize=8, fontweight='bold', color="#1A202C")
    ax.text(0.75, 3.0, "Type: Flash Flood - Karli River Basin", fontsize=7.2, color="#2D3748")
    ax.text(0.75, 2.75, "Location: Kudal Market Yard Area", fontsize=7.2, color="#2D3748")
    ax.text(0.75, 2.5, "GPS: 16.0245 N, 73.6892 E", fontsize=7, color="#718096", family='monospace')
    ax.text(0.75, 2.25, "Water Ingress: 5.2 Feet (Rising)", fontsize=7.2, color="#E53E3E", fontweight='bold')
    ax.text(0.75, 2.0, "AI Threat: High Risk to Life & Assets", fontsize=7.2, color="#2D3748")
    ax.text(0.75, 1.75, "SDRF Dispatch ETA: 12 Minutes", fontsize=7.2, color="#38A169", fontweight='bold')

    route_btn = patches.FancyBboxPatch((0.75, 0.8), 2.7, 0.45, boxstyle="round,pad=0.03", fc="#800020", ec="none")
    ax.add_patch(route_btn)
    ax.text(2.1, 1.02, "ACTIVATE CORRIDOR ROUTE", fontsize=7.2, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Right: Map Canvas
    map_canvas = patches.Rectangle((4.0, 0.4), 11.6, 7.2, fc="#EBF8FF", ec="#CBD5E0", lw=1)
    ax.add_patch(map_canvas)

    # Stylized Topography & Coastline / River simulation
    river_x = [4.5, 6.0, 8.0, 9.5, 11.5, 13.5, 15.0]
    river_y = [7.0, 6.2, 5.0, 4.2, 3.0, 2.2, 1.5]
    ax.plot(river_x, river_y, color="#63B3ED", lw=8, alpha=0.7)
    ax.text(8.5, 5.3, "KARLI RIVER BASIN (RISING STAGE)", fontsize=7.5, color="#2B6CB0", fontweight='bold', rotation=-22)

    # Secondary Tributaries
    ax.plot([8.0, 9.0, 11.0], [5.0, 6.0, 6.8], color="#90CDF4", lw=4, alpha=0.7)

    # Road Network / Highway
    ax.plot([4.2, 7.0, 10.0, 13.0, 15.4], [1.5, 3.2, 4.8, 6.2, 7.2], color="#A0AEC0", lw=3.5, linestyle="--")
    ax.text(6.0, 2.5, "National Highway 66 (NH-66 Bypass)", fontsize=7.5, color="#4A5568", fontweight='bold', rotation=28)

    # Hazard Blast-Radius (Flood Inundation Zone)
    flood_zone = patches.Circle((9.2, 4.4), 1.6, fc="#FEB2B2", ec="#E53E3E", lw=1.5, alpha=0.45)
    ax.add_patch(flood_zone)

    # Evacuation Corridor Vector
    ax.annotate('', xy=(13.2, 6.5), xytext=(9.2, 4.4),
                arrowprops=dict(facecolor='#38A169', edgecolor='#22543D', width=3, headwidth=10, headlength=10, linestyle='-'))
    ax.text(11.2, 5.8, "SAFE EVACUATION CORRIDOR", fontsize=8, fontweight='bold', color="#22543D", rotation=26)

    # Incident Markers on Map
    incidents = [
        (9.2, 4.4, "INC-8941\nL5 FLOOD", "#E53E3E"),
        (6.5, 6.0, "INC-8940\nL4 LANDSLIDE", "#DD6B20"),
        (13.8, 2.5, "INC-8939\nL5 MEDICAL", "#E53E3E"),
        (5.2, 3.5, "INC-8937\nPOWER GRID", "#3182CE"),
    ]
    for x_m, y_m, label, col in incidents:
        pin_shadow = patches.Circle((x_m, y_m-0.05), 0.28, fc="#000000", alpha=0.2)
        ax.add_patch(pin_shadow)
        pin = patches.Circle((x_m, y_m), 0.25, fc=col, ec="#FFFFFF", lw=1.5)
        ax.add_patch(pin)
        tag = patches.FancyBboxPatch((x_m-0.8, y_m+0.32), 1.6, 0.45, boxstyle="round,pad=0.02", fc="#FFFFFF", ec=col, lw=1)
        ax.add_patch(tag)
        ax.text(x_m, y_m+0.54, label, fontsize=6.2, fontweight='bold', color=col, ha='center', va='center')

    # Safe Shelters on Map
    shelters = [
        (13.2, 6.5, "SHELTER 01: Kudal Central High School\n(350/500 Beds Free)", "#38A169"),
        (7.8, 1.8, "SHELTER 02: Sawantwadi Sports Complex\n(180/300 Beds Free)", "#38A169"),
    ]
    for x_s, y_s, s_name, col in shelters:
        s_pin = patches.RegularPolygon((x_s, y_s), numVertices=4, radius=0.28, fc="#38A169", ec="#FFFFFF", lw=1.5)
        ax.add_patch(s_pin)
        s_tag = patches.FancyBboxPatch((x_s-1.8, y_s+0.35), 3.6, 0.48, boxstyle="round,pad=0.02", fc="#F0FFF4", ec="#38A169", lw=1)
        ax.add_patch(s_tag)
        ax.text(x_s, y_s+0.58, s_name, fontsize=6.2, fontweight='bold', color="#22543D", ha='center', va='center')

    # Map Controls (Top Right of Map)
    map_ctrls = patches.FancyBboxPatch((14.4, 6.2), 0.9, 1.2, boxstyle="round,pad=0.02", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(map_ctrls)
    ax.text(14.85, 7.05, "+", fontsize=14, fontweight='bold', color="#2D3748", ha='center', va='center')
    ax.plot([14.5, 15.2], [6.8, 6.8], color="#E2E8F0", lw=1)
    ax.text(14.85, 6.45, "-", fontsize=16, fontweight='bold', color="#2D3748", ha='center', va='center')

    # Map Scale & Telemetry
    ax.plot([4.4, 5.8], [0.65, 0.65], color="#1A202C", lw=2.5)
    ax.text(5.1, 0.82, "Scale: 5 Kilometers", fontsize=7, color="#1A202C", ha='center')
    ax.text(15.4, 0.65, "GIS Data Grounded: OpenStreetMap & ISRO Bhuvan Tiles | Leaflet.js v1.9.4", fontsize=6.8, color="#718096", ha='right')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_gis_map.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 3. WINDOWS SCREEN: LIVE INCIDENT INTAKE & EMERGENCY SOS GEOLOCATION
# ==============================================================================
def create_windows_incident_intake():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/report", tab_title="DisasterConnect AI - Emergency Incident Intake & SOS")

    # Form Container
    form_bg = patches.Rectangle((1.0, 0.4), 14.0, 7.2, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(form_bg)

    # Form Header
    ax.text(1.5, 7.2, "Citizen Emergency Incident Intake & One-Tap GPS SOS Console", fontsize=12, fontweight='bold', color="#800020")
    ax.text(1.5, 6.9, "Submit life-critical reports directly to State Disaster Management Authority & Local SDRF", fontsize=7.5, color="#718096")

    # Progress Stepper
    steps = [("1. Incident Details", True), ("2. GPS Geolocation", True), ("3. Photo/Video Evidence", True), ("4. Instant Dispatch", False)]
    for i, (st, active) in enumerate(steps):
        x_st = 1.5 + i * 3.3
        bar = patches.Rectangle((x_st, 6.45), 3.0, 0.25, fc="#800020" if active else "#E2E8F0")
        ax.add_patch(bar)
        ax.text(x_st + 1.5, 6.25, st, fontsize=7, fontweight='bold' if active else 'normal',
                color="#800020" if active else "#A0AEC0", ha='center')

    # Left Column: Inputs
    # 1. Disaster Category Dropdown
    ax.text(1.5, 5.85, "Disaster Category *", fontsize=8, fontweight='bold', color="#2D3748")
    cat_box = patches.FancyBboxPatch((1.5, 5.25), 6.2, 0.48, boxstyle="round,pad=0.03", fc="#F8FAFC", ec="#CBD5E1", lw=1)
    ax.add_patch(cat_box)
    ax.text(1.7, 5.48, "Flash Flood / Rising River Surge", fontsize=8, color="#1A202C", va='center')
    ax.text(7.4, 5.48, "v", fontsize=8, color="#718096", ha='center', va='center')

    # 2. Threat Severity Selector
    ax.text(1.5, 4.95, "Threat Severity Level *", fontsize=8, fontweight='bold', color="#2D3748")
    sev_levels = [("L1 Minimal", "#E2E8F0", "#4A5568"), ("L2 Low", "#E2E8F0", "#4A5568"), ("L3 Moderate", "#FEFCBF", "#B7791F"), ("L4 High", "#FEEBC8", "#C05621"), ("L5 CRITICAL", "#FED7D7", "#9B2C2C")]
    for j, (s_txt, s_bg, s_fg) in enumerate(sev_levels):
        x_sev = 1.5 + j * 1.25
        s_pill = patches.FancyBboxPatch((x_sev, 4.45), 1.18, 0.4, boxstyle="round,pad=0.02", fc=s_bg, ec=s_fg, lw=1.2 if j==4 else 0.5)
        ax.add_patch(s_pill)
        ax.text(x_sev + 0.59, 4.65, s_txt, fontsize=6.5, fontweight='bold' if j==4 else 'normal', color=s_fg, ha='center', va='center')

    # 3. Incident Description
    ax.text(1.5, 4.15, "Emergency Description & Immediate Hazards *", fontsize=8, fontweight='bold', color="#2D3748")
    desc_box = patches.FancyBboxPatch((1.5, 2.5), 6.2, 1.5, boxstyle="round,pad=0.03", fc="#F8FAFC", ec="#CBD5E1", lw=1)
    ax.add_patch(desc_box)
    desc_text = (
        "Karli River overflowed near Kudal Bazar Bridge. Approximately 45 people\n"
        "are stranded on the first floor of commercial shops. Floodwater is\n"
        "rapidly rising at 6 inches every 15 minutes. High tension electric cable\n"
        "has submerged nearby. Urgent inflatable rescue boats and SDRF needed."
    )
    ax.text(1.7, 3.8, desc_text, fontsize=7.2, color="#2D3748", va='top', family='sans-serif')

    # 4. People Trapped Count
    ax.text(1.5, 2.2, "Estimated Persons Trapped / In Danger:", fontsize=7.8, fontweight='bold', color="#2D3748")
    count_box = patches.FancyBboxPatch((1.5, 1.65), 6.2, 0.45, boxstyle="round,pad=0.03", fc="#F8FAFC", ec="#CBD5E1", lw=1)
    ax.add_patch(count_box)
    ax.text(1.7, 1.87, "45 Citizens (including 8 senior citizens, 5 infants)", fontsize=8, color="#1A202C", va='center')

    # Right Column: GPS Geolocation & Media Upload
    # GPS Card
    gps_card = patches.FancyBboxPatch((8.3, 3.8), 6.2, 2.3, boxstyle="round,pad=0.04", fc="#F0FFF4", ec="#38A169", lw=1.5)
    ax.add_patch(gps_card)
    ax.text(8.6, 5.85, "AUTOMATIC HIGH-PRECISION GPS LOCK", fontsize=8.5, fontweight='bold', color="#22543D")
    ax.text(8.6, 5.5, "Latitude:   16.0245° N  (+16.024512)", fontsize=8, color="#2D3748", family='monospace')
    ax.text(8.6, 5.2, "Longitude:  73.6892° E  (+73.689218)", fontsize=8, color="#2D3748", family='monospace')
    ax.text(8.6, 4.9, "Jurisdiction: Sindhudurg District / Kudal Taluka", fontsize=7.5, color="#2D3748")
    ax.text(8.6, 4.6, "Accuracy Radius: ± 2.8 Meters (WGS-84 Satellite Fix)", fontsize=7.2, color="#38A169", fontweight='bold')
    ax.text(8.6, 4.25, "[RE-FETCH CURRENT GPS COORDINATES]", fontsize=7, fontweight='bold', color="#2B6CB0")

    # Media Upload Dropzone
    media_card = patches.FancyBboxPatch((8.3, 2.1), 6.2, 1.5, boxstyle="round,pad=0.04", fc="#F8FAFC", ec="#CBD5E1", lw=1, linestyle="--")
    ax.add_patch(media_card)
    ax.text(11.4, 3.15, "DRAG & DROP DISASTER EVIDENCE PHOTOS / VIDEOS", fontsize=7.5, fontweight='bold', color="#4A5568", ha='center')
    ax.text(11.4, 2.85, "Attached: flood_water_kudal_market_01.jpg (2.4 MB) - Verified Geotag", fontsize=7, color="#2B6CB0", ha='center')
    ax.text(11.4, 2.55, "Supported formats: PNG, JPG, MP4, GeoTIFF (Max 50MB)", fontsize=6.8, color="#A0AEC0", ha='center')

    # Bottom Submission Bar
    submit_btn = patches.FancyBboxPatch((8.3, 0.7), 6.2, 0.9, boxstyle="round,pad=0.04", fc="#E53E3E", ec="#9B2C2C", lw=2)
    ax.add_patch(submit_btn)
    ax.text(11.4, 1.25, "BROADCAST LIFE-CRITICAL SOS DISPATCH", fontsize=10, fontweight='bold', color="#FFFFFF", ha='center', va='center')
    ax.text(11.4, 0.92, "Auto-Triaged by Gemini AI & Routed to Sindhudurg SDRF", fontsize=7, color="#FED7D7", ha='center', va='center')

    cancel_btn = patches.FancyBboxPatch((1.5, 0.7), 6.2, 0.9, boxstyle="round,pad=0.04", fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(cancel_btn)
    ax.text(4.6, 1.15, "CLEAR & RETURN TO DASHBOARD", fontsize=8.5, fontweight='bold', color="#4A5568", ha='center', va='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_incident_intake.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 4. WINDOWS SCREEN: RELIEF CAMPS & EVACUATION SHELTERS LIVE CAPACITY REGISTRY
# ==============================================================================
def create_windows_shelters():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/shelters", tab_title="DisasterConnect AI - Relief Camps & Shelters")

    # Header & Filter Toolbar
    ax.text(0.4, 7.25, "Relief Camps & Emergency Evacuation Shelters Live Registry", fontsize=11, fontweight='bold', color="#1A202C")
    ax.text(0.4, 7.02, "Real-time occupancy tracking, bed availability, food rations, and medical supply status", fontsize=7.2, color="#718096")

    # Filter row
    filter_bar = patches.Rectangle((0.4, 6.4), 15.2, 0.48, fc="#EDF2F7", ec="#CBD5E0", lw=0.8)
    ax.add_patch(filter_bar)
    ax.text(0.6, 6.64, "Filter District: [Sindhudurg (All Talukas) v]", fontsize=7.5, color="#2D3748", va='center')
    ax.text(4.2, 6.64, "Camp Status: [Beds Available Only v]", fontsize=7.5, color="#2D3748", va='center')
    ax.text(7.8, 6.64, "Medical Post: [Doctor On-Site v]", fontsize=7.5, color="#2D3748", va='center')
    ax.text(15.4, 6.64, "+ REGISTER NEW RELIEF CAMP", fontsize=7.5, fontweight='bold', color="#800020", ha='right', va='center')

    # 3-Column Desktop Shelter Cards Grid
    shelters = [
        ("Kudal Central High School & Sports Complex", "Kudal Taluka, Sindhudurg", "16.0289 N, 73.6912 E", 500, 315, 185, "Dr. S. Patil (MBBS)", "4 Days Rations", "HIGH PRIORITY", "#38A169"),
        ("Sawantwadi Moti Talav Relief Camp", "Sawantwadi, Sindhudurg", "15.9082 N, 73.8214 E", 350, 170, 180, "Red Cross Station 02", "7 Days Rations", "STABLE", "#38A169"),
        ("Malvan Coastal Community Center", "Malvan Taluka, Sindhudurg", "16.0612 N, 73.4715 E", 250, 240, 10, "First Aid Nurse Unit", "2 Days Rations", "NEAR FULL", "#DD6B20"),
        ("Kankavli Polytechnic Auditorium", "Kankavli, Sindhudurg", "16.2755 N, 73.7168 E", 600, 210, 390, "Civil Hospital Doctors", "10 Days Rations", "OPTIMAL", "#38A169"),
        ("Vengurla Municipal Town Hall", "Vengurla, Sindhudurg", "15.8645 N, 73.6362 E", 200, 195, 5, "Paramedic Volunteers", "1 Day Rations", "OVERFLOW ALERT", "#E53E3E"),
        ("Dodamarg Forest Department Barracks", "Dodamarg, Sindhudurg", "15.7554 N, 73.9542 E", 150, 65, 85, "Mobile Medical Van", "5 Days Rations", "STABLE", "#38A169")
    ]

    for i, (name, taluka, gps, total, occ, free, med, food, status, col) in enumerate(shelters):
        col_idx = i % 3
        row_idx = i // 3
        x = 0.4 + col_idx * 5.15
        y = 3.65 - row_idx * 2.6

        card = patches.FancyBboxPatch((x, y), 4.9, 2.45, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E0", lw=1.2)
        ax.add_patch(card)

        # Status badge
        badge = patches.FancyBboxPatch((x + 3.4, y + 2.05), 1.35, 0.32, boxstyle="round,pad=0.02", fc=col, ec="none")
        ax.add_patch(badge)
        ax.text(x + 4.07, y + 2.21, status, fontsize=6, fontweight='bold', color="#FFFFFF", ha='center', va='center')

        # Shelter Name & Location
        ax.text(x + 0.2, y + 2.2, name[:32], fontsize=8.2, fontweight='bold', color="#1A202C")
        ax.text(x + 0.2, y + 1.95, taluka, fontsize=7.2, color="#4A5568")
        ax.text(x + 0.2, y + 1.75, "GPS: " + gps, fontsize=6.8, color="#718096", family='monospace')

        # Capacity Progress Bar
        pct = occ / total
        bar_bg = patches.Rectangle((x + 0.2, y + 1.35), 4.5, 0.25, fc="#EDF2F7")
        ax.add_patch(bar_bg)
        bar_fill = patches.Rectangle((x + 0.2, y + 1.35), 4.5 * pct, 0.25, fc=col)
        ax.add_patch(bar_fill)

        ax.text(x + 0.2, y + 1.12, f"Occupied: {occ} / {total} Beds ({free} Beds Available)", fontsize=7, fontweight='bold', color="#2D3748")

        # Supply Details
        ax.text(x + 0.2, y + 0.85, f"Medical: {med}", fontsize=6.8, color="#2B6CB0")
        ax.text(x + 0.2, y + 0.62, f"Rations: {food}", fontsize=6.8, color="#2D3748")

        # Action Buttons
        btn1 = patches.FancyBboxPatch((x + 0.2, y + 0.15), 2.1, 0.35, boxstyle="round,pad=0.02", fc="#800020", ec="none")
        ax.add_patch(btn1)
        ax.text(x + 1.25, y + 0.32, "DIRECT EVACUEES HERE", fontsize=6, fontweight='bold', color="#FFFFFF", ha='center', va='center')

        btn2 = patches.FancyBboxPatch((x + 2.5, y + 0.15), 2.2, 0.35, boxstyle="round,pad=0.02", fc="#EDF2F7", ec="#CBD5E0", lw=0.8)
        ax.add_patch(btn2)
        ax.text(x + 3.6, y + 0.32, "UPDATE SUPPLIES / CALL", fontsize=6, fontweight='bold', color="#4A5568", ha='center', va='center')

    # Bottom Status Summary
    ax.text(0.4, 0.65, "Total Statewide Shelter Capacity: 2,050 Beds | Currently Occupied: 1,195 (58.3%) | Total Free: 855 Beds Available",
            fontsize=7.5, fontweight='bold', color="#22543D")

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_shelters.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 5. WINDOWS SCREEN: FAMILY REUNIFICATION & MISSING PERSONS TRACING PORTAL
# ==============================================================================
def create_windows_missing_persons():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/missing-persons", tab_title="DisasterConnect AI - Missing Persons Tracing")

    # Header & Search Bar
    ax.text(0.4, 7.25, "Family Reunification & Missing Persons Tracing Registry", fontsize=11, fontweight='bold', color="#1A202C")
    ax.text(0.4, 7.02, "Centralized database cross-referencing relief camp registries, hospitals, and citizen inquiries", fontsize=7.2, color="#718096")

    # Search Bar
    search_bar = patches.FancyBboxPatch((0.4, 6.35), 10.5, 0.52, boxstyle="round,pad=0.03", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(search_bar)
    ax.text(0.65, 6.61, "Search by Name, Age, Identification Mark, or Last Known Location...", fontsize=7.8, color="#A0AEC0", va='center')

    filter_btn = patches.FancyBboxPatch((11.1, 6.35), 1.8, 0.52, boxstyle="round,pad=0.03", fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(filter_btn)
    ax.text(12.0, 6.61, "Filters (All) v", fontsize=7.5, fontweight='bold', color="#4A5568", ha='center', va='center')

    reg_btn = patches.FancyBboxPatch((13.1, 6.35), 2.5, 0.52, boxstyle="round,pad=0.03", fc="#800020", ec="none")
    ax.add_patch(reg_btn)
    ax.text(14.35, 6.61, "+ REGISTER MISSING PERSON", fontsize=7, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Grid of Missing Persons Cards
    persons = [
        ("Aarav Ramesh Shinde", "Age: 9 Years | Male", "Last seen near Kudal Market during flood surge", "Missing since 14 hrs", "MISSING", "#E53E3E", "Mother: Sunita (98221XXXXX)"),
        ("Parvati Dattatray Rane", "Age: 68 Years | Female", "Admitted to Sawantwadi Sub-District Hospital", "Found Confused at Bus Stand", "HOSPITALIZED", "#DD6B20", "Ward No. 4, Bed 12"),
        ("Ganesh Vitthal Sawant", "Age: 42 Years | Male", "Reunited with family at Kankavli Camp", "Safely Evacuated by SDRF", "REUNITED SAFE", "#38A169", "Verified by District Officer"),
        ("Meera Anand Kadam", "Age: 16 Years | Female", "Separated during Malvan coastal surge evacuation", "Missing since 6 hrs", "MISSING", "#E53E3E", "Father: Anand (94230XXXXX)"),
        ("Suresh Ramchandra Naik", "Age: 54 Years | Male", "Located at Kudal Central High School Camp", "Receiving treatment for cuts", "IN RELIEF CAMP", "#3182CE", "Shelter Room 10B"),
        ("Tanvi Deepak Parab", "Age: 5 Years | Female", "Rescued by Boat Unit in Pinguli Village", "Under Child Welfare Care", "SAFE IN CARE", "#38A169", "Kudal Police Station")
    ]

    for i, (name, age, loc, time_info, status, col, contact) in enumerate(persons):
        col_idx = i % 3
        row_idx = i // 3
        x = 0.4 + col_idx * 5.15
        y = 3.65 - row_idx * 2.55

        card = patches.FancyBboxPatch((x, y), 4.9, 2.4, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E0", lw=1.2)
        ax.add_patch(card)

        # Photo placeholder
        photo_box = patches.FancyBboxPatch((x + 0.2, y + 1.15), 1.0, 1.05, boxstyle="round,pad=0.02", fc="#EDF2F7", ec="#CBD5E0", lw=0.8)
        ax.add_patch(photo_box)
        ax.text(x + 0.7, y + 1.68, "PHOTO", fontsize=7, fontweight='bold', color="#A0AEC0", ha='center', va='center')

        # Status badge
        badge = patches.FancyBboxPatch((x + 3.4, y + 2.0), 1.35, 0.3, boxstyle="round,pad=0.02", fc=col, ec="none")
        ax.add_patch(badge)
        ax.text(x + 4.07, y + 2.15, status, fontsize=5.8, fontweight='bold', color="#FFFFFF", ha='center', va='center')

        # Details
        ax.text(x + 1.35, y + 2.15, name, fontsize=8, fontweight='bold', color="#1A202C")
        ax.text(x + 1.35, y + 1.9, age, fontsize=7, color="#4A5568")
        ax.text(x + 1.35, y + 1.65, time_info, fontsize=6.8, fontweight='bold', color=col)

        # Location description
        ax.text(x + 0.2, y + 0.85, "Details: " + loc[:50], fontsize=6.8, color="#2D3748")
        ax.text(x + 0.2, y + 0.6, "Contact/Record: " + contact, fontsize=6.8, fontweight='bold', color="#2B6CB0")

        # Action Button
        action_btn = patches.FancyBboxPatch((x + 0.2, y + 0.15), 4.5, 0.35, boxstyle="round,pad=0.02", fc="#F7FAFC", ec="#CBD5E0", lw=0.8)
        ax.add_patch(action_btn)
        ax.text(x + 2.45, y + 0.32, "VIEW DOSSIER & SUBMIT SIGHTING INFO", fontsize=6.5, fontweight='bold', color="#800020", ha='center', va='center')

    # Bottom note
    ax.text(0.4, 0.65, "Total Registered Tracing Records: 64 | Reunited Safe: 41 | In Medical Care: 12 | Active Tracing Underway: 11",
            fontsize=7.5, fontweight='bold', color="#2B6CB0")

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_missing_persons.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 6. WINDOWS SCREEN: 24/7 AI EMERGENCY RESPONSE ASSISTANT & TRIAGE CONSOLE
# ==============================================================================
def create_windows_ai_chatbot():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/ai-assistant", tab_title="DisasterConnect AI - AI Emergency Assistant")

    # Dual Pane Layout: Left Sidebar (4.0 width) Quick Prompts & Emergency SOPs, Right Pane (11.2 width) Interactive Triage Chat
    # Left Sidebar
    sidebar = patches.Rectangle((0.4, 0.4), 4.0, 7.2, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(sidebar)

    ax.text(0.6, 7.25, "Emergency SOPs & AI Tools", fontsize=10, fontweight='bold', color="#1A202C")
    ax.text(0.6, 7.02, "Powered by Gemini Multi-Turn Reasoning", fontsize=6.8, color="#718096")

    prompts = [
        "Flash Flood Survival Checklist",
        "Landslide Warning Signs",
        "Find Safe Shelter in Sindhudurg",
        "First Aid: Water Ingestion",
        "Animal & Livestock Rescue",
        "District Emergency Helplines"
    ]
    for idx, pr in enumerate(prompts):
        y = 6.6 - idx * 0.48
        box = patches.FancyBboxPatch((0.55, y-0.12), 3.7, 0.38, boxstyle="round,pad=0.03", fc="#F7FAFC", ec="#CBD5E0", lw=0.8)
        ax.add_patch(box)
        ax.text(0.75, y+0.07, pr, fontsize=7.2, color="#2D3748", va='center')

    # Emergency Contacts Box
    em_box = patches.FancyBboxPatch((0.55, 0.6), 3.7, 2.8, boxstyle="round,pad=0.04", fc="#FFF5F5", ec="#E53E3E", lw=1.2)
    ax.add_patch(em_box)
    ax.text(0.75, 3.15, "OFFICIAL EMERGENCY HELPLINES", fontsize=7.8, fontweight='bold', color="#E53E3E")
    ax.text(0.75, 2.85, "State Disaster Control (SEOC): 1070", fontsize=7.2, color="#1A202C", fontweight='bold')
    ax.text(0.75, 2.6, "District Disaster Cell (DEOC): 1077", fontsize=7.2, color="#1A202C", fontweight='bold')
    ax.text(0.75, 2.35, "Sindhudurg Police Control: 112", fontsize=7.2, color="#1A202C")
    ax.text(0.75, 2.1, "National Disaster Response (NDRF): 1078", fontsize=7.2, color="#1A202C")
    ax.text(0.75, 1.85, "Ambulance / Emergency Medical: 108", fontsize=7.2, color="#1A202C")
    ax.text(0.75, 1.5, "Direct WhatsApp SOS: +91 94230XXXXX", fontsize=7, color="#2B6CB0", fontweight='bold')
    ax.text(0.75, 1.1, "All lines active 24/7 with satellite backup", fontsize=6.5, color="#718096")

    # Right Chat Pane
    chat_pane = patches.Rectangle((4.6, 0.4), 11.0, 7.2, fc="#F8FAFC", ec="#CBD5E0", lw=1)
    ax.add_patch(chat_pane)

    # Chat Messages
    # User message 1
    u1_box = patches.FancyBboxPatch((8.2, 6.4), 7.1, 0.85, boxstyle="round,pad=0.04", fc="#800020", ec="none")
    ax.add_patch(u1_box)
    ax.text(8.4, 6.95, "Citizen (Kudal Bazar Area):", fontsize=7.5, fontweight='bold', color="#FED7D7")
    ax.text(8.4, 6.65, "Water has entered our first floor shop! There are 6 people here.\nWhich evacuation route is safe to reach higher ground?", fontsize=7.2, color="#FFFFFF")

    # AI message 1
    ai1_box = patches.FancyBboxPatch((4.9, 4.4), 10.4, 1.8, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(ai1_box)
    ax.text(5.1, 5.95, "DisasterConnect AI Assistant (Verified Protocol):", fontsize=7.8, fontweight='bold', color="#800020")
    ai_reply = (
        "IMMEDIATE ACTION REQUIRED:\n"
        "1. DO NOT attempt to wade through moving floodwaters on Market Road -- river surge velocity is 2.8 m/s.\n"
        "2. STAY at the highest structural elevation available. Turn OFF your main electricity trip switch immediately.\n"
        "3. Nearest Verified Safe Shelter: Kudal Central High School (1.1 km East on Shivaji Road, fully accessible).\n"
        "4. Your GPS coordinates (16.0245° N, 73.6892° E) have been auto-flagged to SDRF Rescue Boat Unit 04.\n"
        "5. ETA for Inflatable Rescue Craft: 14 Minutes. Keep phone torch / bright cloth visible."
    )
    ax.text(5.1, 5.7, ai_reply, fontsize=7, color="#1A202C", va='top')

    # Action Pills underneath AI message
    p1 = patches.FancyBboxPatch((5.1, 4.5), 3.2, 0.35, boxstyle="round,pad=0.02", fc="#F0FFF4", ec="#38A169", lw=1)
    ax.add_patch(p1)
    ax.text(6.7, 4.67, "OPEN NAVIGATION ROUTE TO SHELTER", fontsize=6.2, fontweight='bold', color="#22543D", ha='center', va='center')

    p2 = patches.FancyBboxPatch((8.5, 4.5), 3.4, 0.35, boxstyle="round,pad=0.02", fc="#FFF5F5", ec="#E53E3E", lw=1)
    ax.add_patch(p2)
    ax.text(10.2, 4.67, "TRANSMIT LIVE RESCUE BEACON TO BOAT 04", fontsize=6.2, fontweight='bold', color="#9B2C2C", ha='center', va='center')

    # User message 2
    u2_box = patches.FancyBboxPatch((8.2, 3.4), 7.1, 0.7, boxstyle="round,pad=0.04", fc="#800020", ec="none")
    ax.add_patch(u2_box)
    ax.text(8.4, 3.85, "Citizen:", fontsize=7.5, fontweight='bold', color="#FED7D7")
    ax.text(8.4, 3.6, "Understood. We are on the rooftop now with torch active. Cell battery 22%.", fontsize=7.2, color="#FFFFFF")

    # AI message 2
    ai2_box = patches.FancyBboxPatch((4.9, 1.95), 10.4, 1.25, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(ai2_box)
    ax.text(5.1, 2.95, "DisasterConnect AI Assistant:", fontsize=7.8, fontweight='bold', color="#800020")
    ai_reply_2 = (
        "Switch phone to Ultra Power Saving Mode now. We have locked your rooftop GPS location.\n"
        "SDRF Rescue Unit Commander Captain Deshmukh has acknowledged your beacon. Unit is 600m away.\n"
        "Stay calm, do not enter the water. Audio siren from the boat will be audible in 3 minutes."
    )
    ax.text(5.1, 2.75, ai_reply_2, fontsize=7, color="#1A202C", va='top')

    # Bottom Input Bar
    input_box = patches.FancyBboxPatch((4.9, 0.6), 8.8, 0.55, boxstyle="round,pad=0.03", fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(input_box)
    ax.text(5.15, 0.88, "Type your emergency question or situation report here...", fontsize=7.5, color="#A0AEC0", va='center')

    send_btn = patches.FancyBboxPatch((13.9, 0.6), 1.4, 0.55, boxstyle="round,pad=0.03", fc="#800020", ec="none")
    ax.add_patch(send_btn)
    ax.text(14.6, 0.88, "SEND", fontsize=8, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_ai_chatbot.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 7. WINDOWS SCREEN: DISTRICT VOLUNTEER ASSIGNMENT & JURISDICTION CONSOLE
# ==============================================================================
def create_windows_volunteer_assignment():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/admin/volunteer-assignment", tab_title="DisasterConnect AI - District Volunteer Assignment")

    # Header & District Selector
    ax.text(0.4, 7.25, "District Volunteer Jurisdictional Assignment & Resource Dispatcher", fontsize=11, fontweight='bold', color="#1A202C")
    ax.text(0.4, 7.02, "Enables District Emergency Officer to assign vetted volunteers to verified disaster incidents by Taluka", fontsize=7.2, color="#718096")

    # District Filter Bar
    dist_bar = patches.Rectangle((0.4, 6.4), 15.2, 0.48, fc="#EDF2F7", ec="#CBD5E0", lw=0.8)
    ax.add_patch(dist_bar)
    ax.text(0.6, 6.64, "Jurisdiction District: [Sindhudurg District v]", fontsize=7.8, fontweight='bold', color="#800020", va='center')
    ax.text(4.8, 6.64, "Filter Taluka: [Kudal Taluka v]", fontsize=7.5, color="#2D3748", va='center')
    ax.text(8.2, 6.64, "Specialization: [All (Swift Water, Paramedic, Food Logistics) v]", fontsize=7.5, color="#2D3748", va='center')
    ax.text(15.4, 6.64, "AUTO-MATCH VOLUNTEERS (AI)", fontsize=7.5, fontweight='bold', color="#2B6CB0", ha='right', va='center')

    # Two-Panel Layout:
    # Left: Unassigned Emergencies in District (7.4 width)
    # Right: Verified Available Volunteers in District (7.4 width)

    # Left Panel
    p_left = patches.Rectangle((0.4, 0.5), 7.4, 5.7, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(p_left)
    th_l = patches.Rectangle((0.4, 5.8), 7.4, 0.4, fc="#FFF5F5")
    ax.add_patch(th_l)
    ax.text(0.6, 6.0, "PENDING INCIDENTS REQUIRING VOLUNTEERS (Kudal)", fontsize=7.5, fontweight='bold', color="#E53E3E", va='center')

    incidents_list = [
        ("INC-8941", "Karli River Flash Flood", "45 Stranded Citizens", "Urgent Boats & Paramedics", "L5 CRITICAL", "#E53E3E"),
        ("INC-8944", "Bazar Road Food Scarcity", "120 Flood Victims Cut Off", "Food & Water Rations", "L3 MODERATE", "#DD6B20"),
        ("INC-8947", "Old Age Home Evacuation", "18 Senior Citizens Stalled", "Wheelchair Ambulance", "L4 HIGH", "#E53E3E"),
        ("INC-8950", "Cattle Shed Submergence", "35 Livestock in Water", "Animal Rescue & Fodder", "L2 LOW", "#3182CE"),
    ]
    for idx, (inc_id, title, desc, needs, prio, col) in enumerate(incidents_list):
        y = 5.2 - idx * 1.25
        card = patches.FancyBboxPatch((0.55, y-0.45), 7.1, 1.15, boxstyle="round,pad=0.03", fc="#FAFAFA", ec=col, lw=1)
        ax.add_patch(card)
        ax.text(0.7, y+0.45, f"{inc_id}: {title}", fontsize=7.8, fontweight='bold', color="#1A202C")
        ax.text(6.8, y+0.45, prio, fontsize=6.5, fontweight='bold', color=col, ha='right')
        ax.text(0.7, y+0.22, f"Impact: {desc}", fontsize=7, color="#4A5568")
        ax.text(0.7, y, f"Required Skill: {needs}", fontsize=7, fontweight='bold', color="#800020")
        ax.text(0.7, y-0.22, "[SELECTED FOR ASSIGNMENT]", fontsize=6.5, fontweight='bold', color="#2B6CB0")

    # Right Panel
    p_right = patches.Rectangle((8.2, 0.5), 7.4, 5.7, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(p_right)
    th_r = patches.Rectangle((8.2, 5.8), 7.4, 0.4, fc="#F0FFF4")
    ax.add_patch(th_r)
    ax.text(8.4, 6.0, "VERIFIED VOLUNTEERS IN KUDAL TALUKA (Ready)", fontsize=7.5, fontweight='bold', color="#22543D", va='center')

    volunteers_list = [
        ("V-1042", "Nitin Suresh Parab", "Swift Water Rescue Certified", "Distance: 1.8 km", "AVAILABLE", "#38A169"),
        ("V-1088", "Dr. Pooja Mahesh Rane", "Paramedic / Trauma Response", "Distance: 2.4 km", "AVAILABLE", "#38A169"),
        ("V-1102", "Sunil D. Kadam", "Food Logistics / 4x4 Vehicle", "Distance: 3.1 km", "AVAILABLE", "#38A169"),
        ("V-1145", "Ajay R. Sawant", "HAM Radio Operator & Drone", "Distance: 4.2 km", "ON STANDBY", "#3182CE"),
    ]
    for idx, (v_id, name, skill, dist, st, col) in enumerate(volunteers_list):
        y = 5.2 - idx * 1.25
        card = patches.FancyBboxPatch((8.35, y-0.45), 7.1, 1.15, boxstyle="round,pad=0.03", fc="#FAFAFA", ec=col, lw=1)
        ax.add_patch(card)
        ax.text(8.5, y+0.45, f"{name} ({v_id})", fontsize=7.8, fontweight='bold', color="#1A202C")
        ax.text(14.6, y+0.45, st, fontsize=6.5, fontweight='bold', color=col, ha='right')
        ax.text(8.5, y+0.22, f"Skillset: {skill}", fontsize=7, color="#2D3748")
        ax.text(8.5, y, f"Proximity to Incident: {dist}", fontsize=7, color="#718096")

        # Assign button
        btn = patches.FancyBboxPatch((12.5, y-0.35), 2.7, 0.38, boxstyle="round,pad=0.02", fc="#800020", ec="none")
        ax.add_patch(btn)
        ax.text(13.85, y-0.16, "ASSIGN TO INC-8941", fontsize=6.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_volunteer_assignment.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

# ==============================================================================
# 8. WINDOWS SCREEN: INCIDENT ANALYTICS, THREAT HEATMAPS & AUDIT TELEMETRY
# ==============================================================================
def create_windows_analytics_telemetry():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    draw_windows_browser_chrome(ax, url="https://disasterconnect.ai/admin/analytics", tab_title="DisasterConnect AI - Threat Analytics & Audit")

    # Header
    ax.text(0.4, 7.25, "Statewide Disaster Threat Analytics, Temporal Heatmaps & System Audit Logs", fontsize=11, fontweight='bold', color="#1A202C")
    ax.text(0.4, 7.02, "Predictive risk assessment, incident resolution velocity, and immutable administrative audit trail", fontsize=7.2, color="#718096")

    # Top Left: Incident Distribution by Category (Bar Chart Box)
    chart1_box = patches.Rectangle((0.4, 3.6), 7.4, 3.2, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(chart1_box)
    ax.text(0.6, 6.55, "INCIDENTS BY DISASTER CATEGORY (Current Event)", fontsize=7.8, fontweight='bold', color="#800020")

    cats = [("Flash Floods", 42, "#E53E3E"), ("Landslides", 26, "#DD6B20"), ("Road Blockades", 16, "#3182CE"), ("Building Breaches", 10, "#805AD5"), ("Medical / Other", 6, "#38A169")]
    for j, (c_name, pct, c_col) in enumerate(cats):
        y_b = 6.05 - j * 0.48
        ax.text(0.6, y_b+0.05, c_name, fontsize=7, color="#2D3748")
        ax.add_patch(patches.Rectangle((2.4, y_b), 4.2, 0.22, fc="#EDF2F7"))
        ax.add_patch(patches.Rectangle((2.4, y_b), 4.2 * (pct / 50.0), 0.22, fc=c_col))
        ax.text(6.8, y_b+0.05, f"{pct}%", fontsize=7, fontweight='bold', color=c_col)

    # Top Right: Hourly Incident Frequency Curve (Simulated Curve)
    chart2_box = patches.Rectangle((8.2, 3.6), 7.4, 3.2, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(chart2_box)
    ax.text(8.4, 6.55, "INCIDENT REPORTING VELOCITY (Last 12 Hours)", fontsize=7.8, fontweight='bold', color="#800020")

    # Axes
    ax.plot([8.8, 15.0], [4.1, 4.1], color="#CBD5E0", lw=1)
    ax.plot([8.8, 8.8], [4.1, 6.2], color="#CBD5E0", lw=1)
    ax.text(8.5, 6.1, "Reports/Hr", fontsize=6.5, color="#718096", rotation=90, va='center')

    # Curve points
    hrs_x = [8.8, 9.4, 10.0, 10.6, 11.2, 11.8, 12.4, 13.0, 13.6, 14.2, 14.8]
    reps_y = [4.3, 4.5, 4.8, 5.6, 6.1, 5.9, 5.4, 5.0, 4.7, 4.4, 4.3]
    ax.plot(hrs_x, reps_y, color="#E53E3E", lw=2.5, marker='o', markersize=4)
    ax.fill_between(hrs_x, reps_y, 4.1, color="#FED7D7", alpha=0.5)

    ax.text(11.2, 6.25, "Peak Inundation (14:00 hrs)", fontsize=6.8, fontweight='bold', color="#E53E3E", ha='center')
    ax.text(8.8, 3.85, "06:00", fontsize=6.5, color="#718096", ha='center')
    ax.text(11.8, 3.85, "12:00", fontsize=6.5, color="#718096", ha='center')
    ax.text(14.8, 3.85, "18:00", fontsize=6.5, color="#718096", ha='center')

    # Bottom: Immutable Administrative Audit Log Table
    audit_box = patches.Rectangle((0.4, 0.4), 15.2, 2.9, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(audit_box)
    ax.text(0.6, 3.05, "SYSTEM AUDIT TRAIL & TELEMETRY LOGS (Real-Time WebSocket Stream)", fontsize=7.8, fontweight='bold', color="#1A202C")
    ax.text(15.4, 3.05, "[EXPORT AUDIT PACK]", fontsize=7, fontweight='bold', color="#2B6CB0", ha='right')

    log_th = patches.Rectangle((0.4, 2.65), 15.2, 0.32, fc="#EDF2F7")
    ax.add_patch(log_th)
    headers = [("TIMESTAMP", 1.4), ("EVENT TYPE", 3.4), ("ACTOR ID & ROLE", 6.0), ("RESOURCE / JURISDICTION", 9.2), ("ACTION DETAILS", 13.0), ("STATUS", 15.1)]
    for h, x_c in headers:
        ax.text(x_c, 2.81, h, fontsize=6.5, fontweight='bold', color="#4A5568", ha='center', va='center')

    audit_rows = [
        ("18:52:14", "DISPATCH_TRIGGERED", "Officer Deshmukh (DEOC)", "INC-8941 / Kudal Taluka", "SDRF Rescue Unit 04 Dispatched with 2 boats", "SUCCESS", "#38A169"),
        ("18:48:02", "AI_TRIAGE_EVAL", "Gemini 2.5 Flash Engine", "INC-8941 / Lat 16.0245, Lon 73.6892", "Calculated Threat Score: 0.982 (CRITICAL L5)", "SUCCESS", "#38A169"),
        ("18:44:30", "SHELTER_UPDATE", "Incharge Patil (Kudal High)", "SHELTER-01 / Capacity Meter", "Bed Count Updated: 315 Occupied, 185 Free", "SUCCESS", "#38A169"),
        ("18:40:15", "VOLUNTEER_ASSIGN", "DEOC Sindhudurg Console", "V-1042 -> INC-8941", "Volunteer Nitin Parab Assigned & SMS Alerted", "SUCCESS", "#38A169"),
    ]
    for idx, (tm, ev, actor, res, details, st, col) in enumerate(audit_rows):
        y_r = 2.4 - idx * 0.45
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((0.4, y_r-0.18), 15.2, 0.42, fc="#F7FAFC", ec="none"))
        ax.plot([0.4, 15.6], [y_r-0.18, y_r-0.18], color="#E2E8F0", lw=0.5)

        ax.text(1.4, y_r, tm, fontsize=6.8, color="#718096", ha='center', va='center', family='monospace')
        ax.text(3.4, y_r, ev, fontsize=6.8, fontweight='bold', color="#2D3748", ha='center', va='center')
        ax.text(6.0, y_r, actor, fontsize=6.8, color="#2B6CB0", ha='center', va='center')
        ax.text(9.2, y_r, res, fontsize=6.8, color="#4A5568", ha='center', va='center')
        ax.text(13.0, y_r, details[:48], fontsize=6.8, color="#1A202C", ha='center', va='center')
        ax.text(15.1, y_r, st, fontsize=6.5, fontweight='bold', color=col, ha='center', va='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "windows_screen_analytics_telemetry.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved:", out_path)

if __name__ == "__main__":
    print("Generating 8 authentic Windows desktop screens...")
    create_windows_admin_command()
    create_windows_gis_map()
    create_windows_incident_intake()
    create_windows_shelters()
    create_windows_missing_persons()
    create_windows_ai_chatbot()
    create_windows_volunteer_assignment()
    create_windows_analytics_telemetry()
    print("All 8 Windows screens generated successfully!")
