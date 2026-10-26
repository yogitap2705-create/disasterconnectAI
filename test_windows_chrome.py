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
    bg_rect = patches.Rectangle((0.1, 0.1), 15.8, 9.8, fc="#F4F6F9", ec="#718096", lw=1.5)
    ax.add_patch(bg_rect)

    # 1. Windows Title Bar (Windows 11 / Windows 10 style dark/light header)
    title_bar = patches.Rectangle((0.1, 9.25), 15.8, 0.65, fc="#E8EDF2", ec="#CBD5E1", lw=0.5)
    ax.add_patch(title_bar)

    # Windows browser tab on top-left
    tab = patches.FancyBboxPatch((0.3, 9.25), 4.6, 0.65, boxstyle="round,pad=0.04", fc="#FFFFFF", ec="#CBD5E1", lw=1)
    ax.add_patch(tab)
    # Shield icon / app icon
    ax.add_patch(patches.Rectangle((0.45, 9.45), 0.22, 0.25, fc="#800020", ec="none"))
    ax.text(0.75, 9.57, tab_title[:38], fontsize=8, fontweight='bold', color="#1E293B", va='center')
    # Close tab 'x'
    ax.text(4.65, 9.57, "x", fontsize=8, color="#64748B", ha='center', va='center')

    # New tab '+' button
    ax.text(5.15, 9.57, "+", fontsize=11, color="#64748B", ha='center', va='center')

    # WINDOWS WINDOW CONTROLS ON TOP RIGHT: Minimize (-), Maximize ([ ]), Close (X)
    # Minimize Button
    min_box = patches.Rectangle((14.0, 9.25), 0.6, 0.65, fc="#E8EDF2", ec="none")
    ax.add_patch(min_box)
    ax.plot([14.2, 14.4], [9.55, 9.55], color="#1E293B", lw=1.5)

    # Maximize / Restore Button
    max_box = patches.Rectangle((14.6, 9.25), 0.6, 0.65, fc="#E8EDF2", ec="none")
    ax.add_patch(max_box)
    ax.add_patch(patches.Rectangle((14.78, 9.47), 0.24, 0.22, fill=False, ec="#1E293B", lw=1.2))

    # Close Button (Windows signature red on hover or dark with white X)
    close_box = patches.Rectangle((15.2, 9.25), 0.7, 0.65, fc="#E81123", ec="none")
    ax.add_patch(close_box)
    ax.text(15.55, 9.57, "X", fontsize=9, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # 2. Windows Navigation Bar & Omnibox (Address Bar)
    nav_bar = patches.Rectangle((0.1, 8.6), 15.8, 0.65, fc="#FFFFFF", ec="#E2E8F0", lw=0.5)
    ax.add_patch(nav_bar)

    # Windows Back, Forward, Refresh buttons
    ax.text(0.35, 8.92, "<", fontsize=10, fontweight='bold', color="#64748B", ha='center', va='center')
    ax.text(0.75, 8.92, ">", fontsize=10, fontweight='bold', color="#94A3B8", ha='center', va='center')
    ax.text(1.15, 8.92, "o", fontsize=10, fontweight='bold', color="#64748B", ha='center', va='center')

    # Address / URL Bar with Lock icon
    url_box = patches.FancyBboxPatch((1.45, 8.68), 13.0, 0.48, boxstyle="round,pad=0.03", fc="#F1F5F9", ec="#CBD5E1", lw=0.8)
    ax.add_patch(url_box)
    ax.text(1.65, 8.92, "[SECURE HTTPS]", fontsize=7, fontweight='bold', color="#166534", va='center')
    clean_url = url if url.startswith("https://") else "https://" + url
    ax.text(2.8, 8.92, clean_url, fontsize=8, color="#334155", va='center', family='monospace')
    ax.text(14.3, 8.92, "Windows 11 Desktop", fontsize=7, color="#64748B", ha='right', va='center')

    # Windows User Profile / Extensions
    ax.add_patch(patches.Circle((14.8, 8.92), 0.16, fc="#800020", ec="none"))
    ax.text(14.8, 8.92, "A", fontsize=7.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')
    ax.text(15.4, 8.92, "...", fontsize=11, fontweight='bold', color="#64748B", ha='center', va='center')

    # 3. Application Top Navigation Header (DisasterConnectAI)
    app_header = patches.Rectangle((0.1, 7.85), 15.8, 0.75, fc="#800020")
    ax.add_patch(app_header)
    ax.text(0.4, 8.22, "DISASTERCONNECT AI", fontsize=11, fontweight='bold', color="#FFFFFF", va='center')
    ax.text(3.4, 8.22, "STATE EMERGENCY OPERATIONS CENTER (SEOC)", fontsize=7, color="#FDE047", va='center')

    # Navigation Tabs
    nav_items = ["Emergency Triage", "GIS Map", "Shelters", "Missing Persons", "Volunteer Dispatch", "AI Assistant", "Admin Command"]
    for i, item in enumerate(nav_items):
        is_sel = (item in tab_title) or (i == 6 and "Command" in tab_title) or (i == 4 and "Volunteer" in tab_title) or (i == 0 and "Intake" in tab_title)
        x = 6.4 + i * 1.3
        if is_sel:
            sel_patch = patches.FancyBboxPatch((x-0.1, 7.98), 1.2, 0.48, boxstyle="round,pad=0.03", fc="#991B1B", ec="#FDE047", lw=1)
            ax.add_patch(sel_patch)
        ax.text(x + 0.5, 8.22, item, fontsize=7.2, color="#FFFFFF" if not is_sel else "#FEF08A",
                ha='center', va='center', fontweight='bold' if is_sel else 'normal')

    ax.text(15.6, 8.22, "STATUS: ONLINE", fontsize=7.5, fontweight='bold', color="#4ADE80", ha='right', va='center')

print("Windows Chrome frame helper defined!")
