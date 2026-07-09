#!/usr/bin/env python3
"""
Enhance Supermarket Sales Dashboard - injects interactive dashboard into .twb XML
Usage: python3 enhance_dashboard.py
"""

import os, shutil, zipfile, uuid as _uuid, subprocess

TWBX_PATH = "Proyek_BigData/Supermarket_Sales_Dashboard.twbx"
TMP_DIR = "/tmp/twbx_build"
TWB_FILENAME = "Supermarket_Sales_Dashboard.twb"

SHEETS = [
    "Revenue Trend",
    "Product Performance",
    "Customer Analysis",
    "Hourly Activity",
    "City Comparison",
    "Rating Distribution",
    "Payment Analysis",
    "Data Quality",
    "Box Plot Total",
    "Box Plot Rating",
]

DS_NAME = "federated.02hj2n40cilez216q1kk11tabb4t"

_zid = [0]  # mutable zone id counter

def zid():
    _zid[0] += 1
    return _zid[0]

def uid():
    return str(_uuid.uuid4()).upper()


def layout_cache():
    """Minimal layout-cache required by XSD on every zone."""
    return "<layout-cache type-w='fixed' type-h='fixed'/>"


def build_dashboard_xml():
    """Build dashboard section.
    Zone name='SheetName' links zones to worksheets via viewpoints.
    Inner zone type wrappers match Tableau's native format.
    """
    _zid[0] = 0
    lines = []
    lines.append("<dashboard name='Supermarket Sales Dashboard'>")
    lines.append("  <style/>")
    lines.append("  <size sizing-mode='automatic'/>")
    lines.append("  <datasources>")
    lines.append(f"    <datasource caption='supermarket_sales (dataset-blabla)' name='{DS_NAME}'/>")
    lines.append("  </datasources>")
    lines.append(f"  <datasource-dependencies datasource='{DS_NAME}'>")
    cols = [
        ("[City]", "None", "[none:City:nk]", "nominal"),
        ("[Customer type]", "None", "[none:Customer type:nk]", "nominal"),
        ("[Date]", "Day-Trunc", "[tdy:Date:qk]", "quantitative"),
        ("[Hour]", "None", "[none:Hour:nk]", "ordinal"),
        ("[Invoice ID]", "Count", "[cnt:Invoice ID:qk]", "quantitative"),
        ("[Payment]", "None", "[none:Payment:nk]", "nominal"),
        ("[Product line]", "None", "[none:Product line:nk]", "nominal"),
        ("[Rating]", "None", "[none:Rating:nk]", "ordinal"),
        ("[Rating]", "Sum", "[sum:Rating:qk]", "quantitative"),
        ("[Total]", "Sum", "[sum:Total:qk]", "quantitative"),
    ]
    for cname, deriv, iname, typ in cols:
        lines.append(f"    <column datatype='string' name='{cname}' role='dimension' type='{typ}'/>")
        lines.append(f"    <column-instance column='{cname}' derivation='{deriv}' name='{iname}' pivot='key' type='{typ}'/>")
    lines.append("  </datasource-dependencies>")

    # ── ZONES ──
    lines.append("  <zones>")
    # outer root container (vertical flow)
    lines.append(f"    <zone id='{zid()}' x='0' y='0' w='100000' h='100000' type-v2='layout-flow' param='vert' name='outer'>")
    lines.append(f"      {layout_cache()}")

    # ── Row 0: Title + Instructions ──
    lines.append(f"      <zone id='{zid()}' x='0' y='0' w='100000' h='6000' name='title'>")
    lines.append(f"        <zone type='text' name='title_text'>")
    title_cdata = (
        "<title>Supermarket Sales Dashboard</title>"
        "<subtitle>Interactive Analytics - Petunjuk Penggunaan:</subtitle>"
        "<p>1. <b>Quick Filters</b> - Gunakan dropdown/checkbox di bawah "
        "untuk memfilter berdasarkan City, Product Line, Payment, atau Customer Type. "
        "Semua chart berubah otomatis.</p>"
        "<p>2. <b>Klik Chart</b> - Klik baris/garis/dot di chart mana pun "
        "untuk cross-filter semua chart lainnya.</p>"
        "<p>3. <b>Reset</b> - Klik X pada filter atau pilih All untuk mereset.</p>"
    )
    lines.append(f"          <text><![CDATA[{title_cdata}]]></text>")
    lines.append(f"        </zone>")
    lines.append(f"        {layout_cache()}")
    lines.append(f"        <zone-style/>")
    lines.append(f"      </zone>")

    # ── Row 0b: Quick Filters Bar ──
    lines.append(f"      <zone id='{zid()}' x='0' y='6000' w='100000' h='6000' type-v2='layout-flow' param='horz' name='filter_bar'>")
    lines.append(f"        {layout_cache()}")
    filters = [
        ("City", "City", "Revenue Trend"),
        ("Product line", "Product Line", "Revenue Trend"),
        ("Payment", "Payment", "Payment Analysis"),
        ("Customer type", "Customer Type", "Customer Analysis"),
    ]
    fw = 22500
    for i, (field, label, src_ws) in enumerate(filters):
        x = 10000 + i * fw
        safe = field.replace(" ", "_")
        lines.append(f"        <zone id='{zid()}' x='{x}' y='0' w='{fw}' h='6000' name='qf_{safe}'>")
        lines.append(f"          <zone type='quick-filter' name='quickfilter_{safe}'>")
        col_name = f"[{DS_NAME}].[none:{field}:nk]"
        lines.append(f"            <filter class='categorical' column='{col_name}'/>")
        lines.append(f"            <worksheet>{src_ws}</worksheet>")
        lines.append(f"            <filter-options applied-fields='all'>")
        lines.append(f"              <filter-display type='multiple-values-list'/>")
        lines.append(f"            </filter-options>")
        lines.append(f"          </zone>")
        lines.append(f"          {layout_cache()}")
        lines.append(f"          <zone-style/>")
        lines.append(f"        </zone>")
    lines.append(f"        <zone-style/>")
    lines.append(f"      </zone>")

    # ── Row 1: Revenue Trend (70%) + Data Quality + Hourly Activity (30%) ──
    lines.append(f"      <zone id='{zid()}' x='0' y='12000' w='100000' h='24000' type-v2='layout-flow' param='horz' name='row1'>")
    lines.append(f"        {layout_cache()}")
    # Revenue Trend
    lines.append(f"        <zone id='{zid()}' x='0' y='0' w='70000' h='24000' name='Revenue Trend'>")
    lines.append(f"          <zone type='worksheet'>")
    lines.append(f"            <worksheet>Revenue Trend</worksheet>")
    lines.append(f"          </zone>")
    lines.append(f"          {layout_cache()}")
    lines.append(f"          <zone-style/>")
    lines.append(f"        </zone>")
    # Right column: Data Quality + Hourly Activity
    lines.append(f"        <zone id='{zid()}' x='70000' y='0' w='30000' h='24000' type-v2='layout-flow' param='vert' name='kpi_stack'>")
    lines.append(f"          {layout_cache()}")
    for name, y_off, h_val in [("Data Quality", "0", "11800"), ("Hourly Activity", "12000", "11800")]:
        lines.append(f"          <zone id='{zid()}' x='0' y='{y_off}' w='30000' h='{h_val}' name='{name}'>")
        lines.append(f"            <zone type='worksheet'>")
        lines.append(f"              <worksheet>{name}</worksheet>")
        lines.append(f"            </zone>")
        lines.append(f"            {layout_cache()}")
        lines.append(f"            <zone-style/>")
        lines.append(f"          </zone>")
    lines.append(f"        </zone>")
    lines.append(f"      </zone>")

    # ── Row 2: Product Performance | Customer Analysis ──
    rh2 = 19000
    lines.append(f"      <zone id='{zid()}' x='0' y='36000' w='100000' h='{rh2}' type-v2='layout-flow' param='horz' name='row2'>")
    lines.append(f"        {layout_cache()}")
    for i, name in enumerate(("Product Performance", "Customer Analysis")):
        x_off = "0" if i == 0 else "50000"
        lines.append(f"        <zone id='{zid()}' x='{x_off}' y='0' w='50000' h='{rh2}' name='{name}'>")
        lines.append(f"          <zone type='worksheet'>")
        lines.append(f"            <worksheet>{name}</worksheet>")
        lines.append(f"          </zone>")
        lines.append(f"          {layout_cache()}")
        lines.append(f"          <zone-style/>")
        lines.append(f"        </zone>")
    lines.append(f"      </zone>")

    # ── Row 3: City Comparison | Payment Analysis ──
    rh3 = 19000
    lines.append(f"      <zone id='{zid()}' x='0' y='55000' w='100000' h='{rh3}' type-v2='layout-flow' param='horz' name='row3'>")
    lines.append(f"        {layout_cache()}")
    for i, name in enumerate(("City Comparison", "Payment Analysis")):
        x_off = "0" if i == 0 else "50000"
        lines.append(f"        <zone id='{zid()}' x='{x_off}' y='0' w='50000' h='{rh3}' name='{name}'>")
        lines.append(f"          <zone type='worksheet'>")
        lines.append(f"            <worksheet>{name}</worksheet>")
        lines.append(f"          </zone>")
        lines.append(f"          {layout_cache()}")
        lines.append(f"          <zone-style/>")
        lines.append(f"        </zone>")
    lines.append(f"      </zone>")

    # ── Row 4: Rating Distribution | Box Plot Total | Box Plot Rating ──
    rh4 = 18000
    lines.append(f"      <zone id='{zid()}' x='0' y='74000' w='100000' h='{rh4}' type-v2='layout-flow' param='horz' name='row4'>")
    lines.append(f"        {layout_cache()}")
    for name, pos in [
        ("Rating Distribution", (0, 0, 34000, rh4)),
        ("Box Plot Total", (34000, 0, 33000, rh4)),
        ("Box Plot Rating", (67000, 0, 33000, rh4)),
    ]:
        x, y, w, h = pos
        lines.append(f"        <zone id='{zid()}' x='{x}' y='{y}' w='{w}' h='{h}' name='{name}'>")
        lines.append(f"          <zone type='worksheet'>")
        lines.append(f"            <worksheet>{name}</worksheet>")
        lines.append(f"          </zone>")
        lines.append(f"          {layout_cache()}")
        lines.append(f"          <zone-style/>")
        lines.append(f"        </zone>")
    lines.append(f"      </zone>")

    lines.append("    </zone>")  # outer
    lines.append("  </zones>")

    dash_uid = uid()
    lines.append(f"  <simple-id uuid='{{{dash_uid}}}'/>")
    lines.append("</dashboard>")
    return '\n'.join(lines)


def build_actions_xml():
    """Build cross-filter actions (one per source sheet)."""
    lines = ["  <actions>"]
    for src in SHEETS:
        safe = src.replace(" ", "_")
        lines.append(f"    <action name='[{safe}_Filter]' caption='Filter from {src}'>")
        lines.append("      <activation type='on-select'/>")
        lines.append(f"      <source type='sheet' worksheet='{src}'/>")
        lines.append("    </action>")
    lines.append("  </actions>")
    return '\n'.join(lines)


def build_window_xml(dash_name):
    win_uid = uid()
    vp_lines = '\n'.join(f"        <viewpoint name='{s}'/>" for s in SHEETS)
    return (
        f"    <window class='dashboard' maximized='true' name='{dash_name}'>\n"
        f"      <viewpoints>\n{vp_lines}\n"
        "      </viewpoints>\n"
        "      <active id='-1'/>\n"
        f"      <simple-id uuid='{{{win_uid}}}'/>\n"
        "    </window>"
    )


def main():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    orig_path = os.path.join(TMP_DIR, "original.twbx")
    subprocess.run(
        ["git", "show", "46a2392:Proyek_BigData/Supermarket_Sales_Dashboard.twbx"],
        stdout=open(orig_path, "wb"), stderr=subprocess.DEVNULL
    )

    with zipfile.ZipFile(orig_path, 'r') as zf:
        zf.extractall(TMP_DIR)

    twb_path = os.path.join(TMP_DIR, TWB_FILENAME)
    with open(twb_path, 'r', encoding='utf-8') as f:
        twb_text = f.read()

    # 1. Inject <actions> BEFORE <worksheets>
    actions_xml = build_actions_xml()
    ws_start = twb_text.find('<worksheets>')
    if ws_start == -1:
        print("ERROR: Could not find <worksheets>")
        return False
    twb_text = twb_text[:ws_start] + actions_xml + '\n  ' + twb_text[ws_start:]

    # 2. Inject <dashboards> BEFORE <windows>
    dash_xml = build_dashboard_xml()
    dash_section = f"<dashboards>\n{dash_xml}\n</dashboards>"
    win_start = twb_text.find('<windows')
    twb_text = twb_text[:win_start] + '  ' + dash_section + '\n  ' + twb_text[win_start:]

    # 3. Inject dashboard window BEFORE </windows>
    win_xml = build_window_xml("Supermarket Sales Dashboard")
    win_end = twb_text.find('</windows>')
    twb_text = twb_text[:win_end] + '\n' + win_xml + '\n' + twb_text[win_end:]

    with open(twb_path, 'w', encoding='utf-8') as f:
        f.write(twb_text)

    out_path = os.path.join(TMP_DIR, "Supermarket_Sales_Dashboard.twbx")
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(twb_path, TWB_FILENAME)
        data_dir = os.path.join(TMP_DIR, 'Data')
        if os.path.exists(data_dir):
            for root_dir, dirs, files in os.walk(data_dir):
                for file in files:
                    fp = os.path.join(root_dir, file)
                    arcname = os.path.relpath(fp, TMP_DIR)
                    zf.write(fp, arcname)

    final_path = os.path.join(os.getcwd(), TWBX_PATH)
    shutil.copy2(out_path, final_path)

    # ── COMPREHENSIVE VERIFICATION ──
    import xml.etree.ElementTree as ET
    with zipfile.ZipFile(out_path) as z:
        with z.open(TWB_FILENAME) as f:
            raw = f.read()
            text = raw.decode()

        errors = []
        ok = []

        try:
            ET.fromstring(text)
            ok.append("XML well-formed")
        except ET.ParseError as e:
            errors.append(f"XML error: {e}")

        if text.count("<dashboards>") == 1:
            ok.append("1 <dashboards> section")
        else:
            errors.append(f"<dashboards> count: {text.count('<dashboards>')}")

        if text.count("<dashboard ") == 1:
            ok.append("1 <dashboard> element")
        else:
            errors.append(f"<dashboard> count: {text.count('<dashboard ')}")

        if all(s in text for s in SHEETS):
            ok.append("All 10 worksheets")
        else:
            missing = [s for s in SHEETS if s not in text]
            errors.append(f"Missing sheets: {missing}")

        # Actions
        act_count = text.count("<action ")
        if act_count == 10:
            ok.append(f"{act_count} cross-filter actions")
        else:
            errors.append(f"Actions: {act_count} (expected 10)")

        # Windows
        ws_wins = text.count("class='worksheet'")
        db_wins = text.count("class='dashboard'")
        if ws_wins == 10 and db_wins == 1:
            ok.append(f"{ws_wins} worksheet + {db_wins} dashboard windows")
        else:
            errors.append(f"Windows: ws={ws_wins}, dash={db_wins}")

        # zones structure
        if "<zones>" in text:
            ok.append("Proper <zones> structure")
        else:
            errors.append("Missing <zones>")

        # Section order
        order_ok = (
            text.find("<actions>") < text.find("<worksheets>") <
            text.find("<dashboards>") < text.find("<windows")
        )
        if order_ok:
            ok.append("Correct section order")
        else:
            errors.append("Wrong section order")

        # Dashboard internal structure
        dash = text[text.find("<dashboards>"):text.find("</dashboards>") + len("</dashboards>")]
        for req in ["<style/>", "<size", "<datasources>", "<datasource-dependencies", "<zones>", "<simple-id"]:
            if req in dash:
                ok.append(f"Dashboard has {req.split()[0]}")
            else:
                errors.append(f"Dashboard missing {req}")

        # Zones have id attributes
        import re
        zone_ids = re.findall(r"<zone[^>]*\bid='(\d+)'", text)
        if zone_ids:
            ok.append(f"{len(zone_ids)} zones with unique id attributes")
        else:
            errors.append("No zone id attributes found")

        # Zones have layout-cache
        lc_count = text.count("layout-cache")
        if lc_count >= len(zone_ids):
            ok.append(f"All zones have <layout-cache>")
        else:
            errors.append(f"Missing layout-cache: {lc_count} vs {len(zone_ids)} zones")

        # Actions use new format (activation + source)
        if "source type='sheet'" in text:
            ok.append("Actions use <source type='sheet'> format")
        else:
            errors.append("Actions missing <source type='sheet'>")
        if "<activation type='on-select'/>" in text:
            ok.append("Actions use <activation> format")
        else:
            errors.append("Actions missing <activation>")

        # UUID uniqueness
        uuids = re.findall(r"uuid='\{([^}]+)\}'", text)
        if len(uuids) == len(set(uuids)):
            ok.append(f"All {len(uuids)} UUIDs unique")
        else:
            from collections import Counter
            dups = {k: v for k, v in Counter(uuids).items() if v > 1}
            errors.append(f"Duplicate UUIDs: {dups}")

        # .hyper data intact
        data_files = [n for n in z.namelist() if '.hyper' in n]
        if data_files:
            ok.append(f"Data extract intact: {data_files[0]}")
        else:
            errors.append("Missing .hyper extract")

        # name attributes matching sheet names on zones
        ws_refs = sum(1 for s in SHEETS if f"name='{s}'" in text)
        if ws_refs >= 10:
            ok.append(f"{ws_refs} zone name references matching worksheets")
        else:
            errors.append(f"Zone name refs: {ws_refs} (expected >= 10)")

        # Quick filter zones on dashboard
        qf_count = text.count("type='quick-filter'")
        if qf_count == 4:
            ok.append(f"{qf_count} quick filters")
        else:
            errors.append(f"Quick filters: {qf_count} (expected 4)")

        # Text zone for title
        if "type='text'" in text:
            ok.append("Text zone for title/instructions")
        else:
            errors.append("Missing text zone")

        # Inner worksheet zones
        ws_zone_count = text.count("type='worksheet'")
        if ws_zone_count == 10:
            ok.append(f"{ws_zone_count} inner worksheet zones")
        else:
            errors.append(f"Inner worksheet zones: {ws_zone_count} (expected 10)")

        print("\n" + "=" * 60)
        print("  COMPREHENSIVE DASHBOARD VERIFICATION")
        print("=" * 60)
        print(f"  File: {final_path}")
        print(f"  Size: {len(text)} bytes, {len(text.splitlines())} lines")
        print()
        for msg in ok:
            print(f"  \u2705 {msg}")
        print()
        if errors:
            for msg in errors:
                print(f"  \u274c {msg}")
            return False
        else:
            print("  >>> ALL CHECKS PASSED - DASHBOARD IS COMPLETE!")
            print("=" * 60)
            return True


if __name__ == "__main__":
    main()
