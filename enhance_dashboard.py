#!/usr/bin/env python3
"""
Enhance Supermarket Sales Dashboard - injects interactive dashboard into .twb XML
Usage: python3 enhance_dashboard.py

Tableau 18.1 XSD dashboard content model:
  style?, size?, datasources, datasource-dependencies*, zones, devicelayouts?, simple-id
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


def uid():
    return str(_uuid.uuid4()).upper()


def build_dashboard_xml():
    """Build dashboard section with correct XSD structure."""
    lines = []
    lines.append(f'<dashboard name="Supermarket Sales Dashboard">')
    lines.append('  <style/>')

    # datasources (must include caption to match worksheet references)
    lines.append('  <datasources>')
    lines.append(f'    <datasource caption="supermarket_sales (dataset-blabla)" name="{DS_NAME}"/>')
    lines.append('  </datasources>')

    # datasource-dependencies (all columns used by dashboard + quick filters)
    lines.append(f'  <datasource-dependencies datasource="{DS_NAME}">')
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
        lines.append(f'    <column datatype="string" name="{cname}" role="dimension" type="{typ}"/>')
        lines.append(f'    <column-instance column="{cname}" derivation="{deriv}" name="{iname}" pivot="key" type="{typ}"/>')
    lines.append('  </datasource-dependencies>')

    # zones
    lines.append('  <zones>')
    lines.append('    <zone type-v2="layout-flow" param="vert" name="outer">')

    # ── TITLE ZONE ──
    lines.append('      <zone type-v2="layout-basic" name="title" size-pos="0,0,100000,6000">')
    lines.append('        <zone type="text" name="title_text">')
    title_cdata = (
        '<title>Supermarket Sales Dashboard</title>'
        '<subtitle>📊 Interactive Analytics Supermarket Sales</subtitle>'
        '<p><b>Petunjuk Penggunaan:</b><br/>'
        '1️⃣ <b>Quick Filters</b> — Gunakan dropdown/checkbox di bawah untuk memfilter '
        'berdasarkan <b>City</b>, <b>Product Line</b>, <b>Payment</b>, atau <b>Customer Type</b>. '
        'Semua chart berubah otomatis.<br/>'
        '2️⃣ <b>Klik Chart</b> — Klik baris/garis/dot di chart mana pun untuk cross-filter '
        'semua chart lainnya.<br/>'
        '3️⃣ <b>Reset</b> — Klik <b>X</b> pada filter atau pilih <b>All</b> untuk mereset.</p>'
    )
    lines.append(f'          <text><![CDATA[{title_cdata}]]></text>')
    lines.append('        </zone>')
    lines.append('      </zone>')

    # ── QUICK FILTERS BAR ──
    lines.append('      <zone type-v2="layout-flow" param="horz" name="filter_bar" size-pos="0,6000,100000,7000">')
    lines.append('        <zone type-v2="layout-basic" name="filter_label" size-pos="0,0,10000,7000">')
    lines.append('          <zone type="text" name="flabel">')
    lines.append('            <text><![CDATA[<b>Filters:</b>]]></text>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Each filter must use a source worksheet that HAS the column in its deps
    filters = [
        ("City", "City", "Revenue Trend"),          # all 10 sheets have City
        ("Product line", "Product Line", "Revenue Trend"),  # all 10 have Product line
        ("Payment", "Payment", "Payment Analysis"),  # only Payment Analysis has Payment
        ("Customer type", "Customer Type", "Customer Analysis"),  # only Customer Analysis has Customer type
    ]
    fw = 22500  # each filter width to perfectly fill bar: (100000 - 10000) / 4
    for i, (field, label, src_ws) in enumerate(filters):
        x = 10000 + i * fw
        safe = field.replace(" ", "_")
        lines.append(f'        <zone type-v2="layout-basic" name="qf_{safe}" size-pos="{x},0,{fw},7000">')
        lines.append(f'          <zone type="quick-filter" name="quickfilter_{safe}">')
        lines.append(f'            <filter class="categorical" column="[{DS_NAME}].[none:{field}:nk]"/>')
        lines.append(f'            <worksheet>{src_ws}</worksheet>')
        lines.append('            <filter-options applied-fields="all">')
        lines.append('              <filter-display type="multiple-values-list"/>')
        lines.append('            </filter-options>')
        lines.append('          </zone>')
        lines.append('        </zone>')
    lines.append('      </zone>')

    # ── MAIN CONTENT ──
    lines.append('      <zone type-v2="layout-flow" param="vert" name="main" size-pos="0,13000,100000,80000">')

    # Row 1: Revenue Trend (70%) + Data Quality + Hourly Activity (30%)
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row1" size-pos="0,0,100000,24000">')
    lines.append('          <zone type-v2="layout-basic" name="revenue_trend" size-pos="0,0,70000,24000">')
    lines.append('            <zone type="worksheet">')
    lines.append('              <worksheet>Revenue Trend</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-flow" param="vert" name="kpi_stack" size-pos="70000,0,30000,24000">')
    for name, y, h in [("Data Quality", "0", "11500"), ("Hourly Activity", "12000", "11500")]:
        sn = name.lower().replace(" ", "_")
        lines.append(f'            <zone type-v2="layout-basic" name="{sn}" size-pos="0,{y},30000,{h}">')
        lines.append('              <zone type="worksheet">')
        lines.append(f'                <worksheet>{name}</worksheet>')
        lines.append('              </zone>')
        lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 2: Product Performance | Customer Analysis
    rh2 = 19000
    lines.append(f'        <zone type-v2="layout-flow" param="horz" name="row2" size-pos="0,24000,100000,{rh2}">')
    for name in ("Product Performance", "Customer Analysis"):
        x = "0" if name == "Product Performance" else "50000"
        sn = name.lower().replace(" ", "_")
        lines.append(f'          <zone type-v2="layout-basic" name="{sn}" size-pos="{x},0,50000,{rh2}">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 3: City Comparison | Payment Analysis
    rh3 = 19000
    lines.append(f'        <zone type-v2="layout-flow" param="horz" name="row3" size-pos="0,43000,100000,{rh3}">')
    for name in ("City Comparison", "Payment Analysis"):
        x = "0" if name == "City Comparison" else "50000"
        sn = name.lower().replace(" ", "_")
        lines.append(f'          <zone type-v2="layout-basic" name="{sn}" size-pos="{x},0,50000,{rh3}">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 4: Rating Distribution | Box Plot Total | Box Plot Rating
    rh4 = 18000
    lines.append(f'        <zone type-v2="layout-flow" param="horz" name="row4" size-pos="0,62000,100000,{rh4}">')
    for name, pos in [
        ("Rating Distribution", f"0,0,34000,{rh4}"),
        ("Box Plot Total", f"34000,0,33000,{rh4}"),
        ("Box Plot Rating", f"67000,0,33000,{rh4}"),
    ]:
        sn = name.lower().replace(" ", "_")
        lines.append(f'          <zone type-v2="layout-basic" name="{sn}" size-pos="{pos}">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    lines.append('      </zone>')  # close main
    lines.append('    </zone>')  # close outer
    lines.append('  </zones>')

    dash_uid = uid()
    lines.append(f'  <simple-id uuid="{{{dash_uid}}}"/>')
    lines.append('</dashboard>')
    return '\n'.join(lines)


def build_actions_xml():
    """Build ACTIONS at workbook level with <source-sheet> for each."""
    lines = ['  <actions>']
    for src in SHEETS:
        for tgt in SHEETS:
            if src == tgt:
                continue
            lines.append(f'    <action class="filter" name="Filter from {src} to {tgt}">')
            lines.append('      <action-options source-type="selected" target-type="dashboard"/>')
            lines.append(f'      <source-sheet name="{src}"/>')
            lines.append('      <source-filters/>')
            lines.append('      <target-sheets>')
            lines.append(f'        <sheet name="{tgt}"/>')
            lines.append('      </target-sheets>')
            lines.append('    </action>')
    lines.append('  </actions>')
    return '\n'.join(lines)


def build_window_xml(dash_name):
    win_uid = uid()
    return (
        f'    <window class="dashboard" name="{dash_name}">\n'
        '      <cards>\n'
        '        <edge name="left">\n'
        '          <strip size="160">\n'
        '            <card type="filters"/>\n'
        '          </strip>\n'
        '        </edge>\n'
        '        <edge name="top">\n'
        '          <strip size="2147483647">\n'
        '            <card type="title"/>\n'
        '          </strip>\n'
        '        </edge>\n'
        '      </cards>\n'
        f'      <simple-id uuid="{{{win_uid}}}"/>\n'
        '    </window>'
    )


def main():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    # Extract original from git commit before any dashboard changes
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

    # Write
    with open(twb_path, 'w', encoding='utf-8') as f:
        f.write(twb_text)

    # Repackage twbx
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

    # Copy to project
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

        # Structure
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

        # Quick filters
        qf_count = text.count("quick-filter")
        if qf_count == 4:
            ok.append(f"{qf_count} quick filters")
        else:
            errors.append(f"Quick filters: {qf_count} (expected 4)")

        # Actions
        act_count = text.count("<action ")
        if act_count == 90:
            ok.append(f"{act_count} cross-filter actions")
        else:
            errors.append(f"Actions: {act_count} (expected 90)")

        # source-sheet
        src_sheet_count = text.count("<source-sheet")
        if src_sheet_count == 90:
            ok.append(f"{src_sheet_count} <source-sheet> elements")
        else:
            errors.append(f"<source-sheet>: {src_sheet_count} (expected 90)")

        # Windows
        ws_wins = text.count("class='worksheet'")
        db_wins = text.count('class="dashboard"')
        if ws_wins == 10 and db_wins == 1:
            ok.append(f"{ws_wins} worksheet + {db_wins} dashboard windows")
        else:
            errors.append(f"Windows: ws={ws_wins}, dash={db_wins}")

        # zones (not dashboard-items)
        if "<zones>" in text and "dashboard-items" not in text:
            ok.append("Proper <zones> structure")
        else:
            errors.append("Uses dashboard-items instead of zones")

        # Section order: actions before worksheets before dashboards before windows
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
        for req in ["<style/>", "<datasources>", "<datasource-dependencies", "<zones>", "<simple-id"]:
            if req in dash:
                ok.append(f"Dashboard has {req.split()[0]}")
            else:
                errors.append(f"Dashboard missing {req}")

        # UUID uniqueness
        import re
        uuids = re.findall(r'uuid="\{([^}]+)\}"', text)
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

        print("\n" + "=" * 60)
        print("  COMPREHENSIVE DASHBOARD VERIFICATION")
        print("=" * 60)
        print(f"  File: {final_path}")
        print(f"  Size: {len(text)} bytes, {len(text.splitlines())} lines")
        print()
        for msg in ok:
            print(f"  ✅ {msg}")
        print()
        if errors:
            for msg in errors:
                print(f"  ❌ {msg}")
            return False
        else:
            print("  🎯 ALL CHECKS PASSED — DASHBOARD IS COMPLETE!")
            print("=" * 60)
            return True


if __name__ == "__main__":
    main()
