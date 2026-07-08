#!/usr/bin/env python3
"""
Enhance Supermarket Sales Dashboard - injects interactive dashboard into .twb XML
Usage: python3 enhance_dashboard.py

Tableau 18.1 XSD dashboard content model:
  style?, size?, datasources, datasource-dependencies*, zones, devicelayouts?, simple-id
"""

import os
import shutil
import zipfile
import uuid as _uuid

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

    # datasources
    lines.append('  <datasources>')
    lines.append(f'    <datasource name="{DS_NAME}"/>')
    lines.append('  </datasources>')

    # datasource-dependencies
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

    # ── TITLE ZONE ──────────────────────────────────
    lines.append('      <zone type-v2="layout-basic" name="title" size-pos="0,0,100000,6000">')
    lines.append('        <zone type="text" name="title_text">')
    title_cdata = (
        '<title>Supermarket Sales Dashboard</title>'
        '<subtitle>📊 Interactive Analytics Supermarket Sales</subtitle>'
        '<p><b>Petunjuk Penggunaan:</b><br/>'
        '1️⃣ <b>Quick Filters</b> — Gunakan dropdown/checkbox di bawah ini untuk memfilter '
        'berdasarkan <b>City</b>, <b>Product Line</b>, <b>Payment</b>, atau <b>Customer Type</b>. '
        'Semua chart akan berubah otomatis.<br/>'
        '2️⃣ <b>Klik Chart</b> — Klik bar/line/dot di chart mana pun untuk cross-filter '
        'semua chart lainnya.<br/>'
        '3️⃣ <b>Reset Filter</b> — Klik icon <b>X</b> pada filter atau pilih <b>All</b> '
        'untuk mereset.</p>'
    )
    lines.append(f'          <text><![CDATA[{title_cdata}]]></text>')
    lines.append('        </zone>')
    lines.append('      </zone>')

    # ── QUICK FILTERS BAR ──────────────────────────
    lines.append('      <zone type-v2="layout-flow" param="horz" name="filter_bar" size-pos="0,6000,100000,7000">')
    # Label
    lines.append('        <zone type-v2="layout-basic" name="filter_label" size-pos="0,0,10000,7000">')
    lines.append('          <zone type="text" name="flabel">')
    lines.append('            <text><![CDATA[<b>Filters:</b>]]></text>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    filters = [
        ("City", "City"),
        ("Product line", "Product Line"),
        ("Payment", "Payment"),
        ("Customer type", "Customer Type"),
    ]
    for i, (field, label) in enumerate(filters):
        x = 10000 + i * 22000
        lines.append(f'        <zone type-v2="layout-basic" name="qf_{field}" size-pos="{x},0,22000,7000">')
        lines.append(f'          <zone type="quick-filter" name="quickfilter_{field}">')
        lines.append(f'            <filter class="categorical" column="[{DS_NAME}].[none:{field}:nk]"/>')
        lines.append('            <worksheet>Revenue Trend</worksheet>')
        lines.append('          </zone>')
        lines.append('        </zone>')

    lines.append('      </zone>')

    # ── MAIN CONTENT ──────────────────────────────
    lines.append('      <zone type-v2="layout-flow" param="vert" name="main" size-pos="0,13000,100000,80000">')

    # Row 1: Revenue Trend (full width) + Data Quality + Hourly Activity
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row1" size-pos="0,0,100000,25000">')
    lines.append('          <zone type-v2="layout-basic" name="revenue_trend" size-pos="0,0,70000,25000">')
    lines.append('            <zone type="worksheet">')
    lines.append('              <worksheet>Revenue Trend</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-flow" param="vert" name="kpi_stack" size-pos="70000,0,30000,25000">')
    for name, y in [("Data Quality", "0"), ("Hourly Activity", "12500")]:
        lines.append(f'            <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="0,{y},30000,12000">')
        lines.append('              <zone type="worksheet">')
        lines.append(f'                <worksheet>{name}</worksheet>')
        lines.append('              </zone>')
        lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 2: Product Performance | Customer Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row2" size-pos="0,25000,100000,20000">')
    for name in ("Product Performance", "Customer Analysis"):
        x = "0" if name == "Product Performance" else "50000"
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{x},0,50000,20000">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 3: City Comparison | Payment Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row3" size-pos="0,45000,100000,20000">')
    for name in ("City Comparison", "Payment Analysis"):
        x = "0" if name == "City Comparison" else "50000"
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{x},0,50000,20000">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 4: Rating Distribution | Box Plot Total | Box Plot Rating
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row4" size-pos="0,65000,100000,18000">')
    thirds = [
        ("Rating Distribution", "0,0,34000,18000"),
        ("Box Plot Total", "34000,0,33000,18000"),
        ("Box Plot Rating", "67000,0,33000,18000"),
    ]
    for name, pos in thirds:
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{pos}">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    lines.append('      </zone>')
    lines.append('    </zone>')
    lines.append('  </zones>')

    dash_uid = uid()
    lines.append(f'  <simple-id uuid="{{{dash_uid}}}"/>')
    lines.append('</dashboard>')
    return '\n'.join(lines)


def build_window_xml(dash_name):
    win_uid = uid()
    return (
        f'    <window class="dashboard" name="{dash_name}">\n'
        '      <cards>\n'
        '        <edge name="left">\n'
        '          <strip size="160">\n'
        '            <card type="pages"/>\n'
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


def build_actions_xml():
    lines = ['  <actions>']
    for src in SHEETS:
        for tgt in SHEETS:
            if src == tgt:
                continue
            lines.append(f'    <action class="filter" name="Filter {src} to {tgt}">')
            lines.append('      <action-options target-type="dashboard"/>')
            lines.append('      <source-filters/>')
            lines.append('      <target-sheets>')
            lines.append(f'        <sheet name="{tgt}"/>')
            lines.append('      </target-sheets>')
            lines.append('    </action>')
    lines.append('  </actions>')
    return '\n'.join(lines)


def main():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    # Extract original from git HEAD~1
    import subprocess
    orig_path = os.path.join(TMP_DIR, "original.twbx")
    subprocess.run(
        ["git", "show", "HEAD~2:Proyek_BigData/Supermarket_Sales_Dashboard.twbx"],
        stdout=open(orig_path, "wb"), stderr=subprocess.DEVNULL
    )

    with zipfile.ZipFile(orig_path, 'r') as zf:
        zf.extractall(TMP_DIR)

    twb_path = os.path.join(TMP_DIR, TWB_FILENAME)

    with open(twb_path, 'r', encoding='utf-8') as f:
        twb_text = f.read()

    # 1. Inject <dashboards> before <windows>
    dash_xml = build_dashboard_xml()
    dash_section = f"<dashboards>\n{dash_xml}\n</dashboards>"
    windows_start = twb_text.find('<windows')
    twb_text = twb_text[:windows_start] + '  ' + dash_section + '\n  ' + twb_text[windows_start:]

    # 2. Inject dashboard window before </windows>
    win_xml = build_window_xml("Supermarket Sales Dashboard")
    windows_end = twb_text.find('</windows>')
    twb_text = twb_text[:windows_end] + '\n' + win_xml + '\n' + twb_text[windows_end:]

    # 3. Inject actions before </workbook>
    actions_xml = build_actions_xml()
    workbook_end = twb_text.find('</workbook>')
    twb_text = twb_text[:workbook_end] + '\n' + actions_xml + '\n' + twb_text[workbook_end:]

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

    # Verify
    import xml.etree.ElementTree as ET
    with zipfile.ZipFile(out_path) as z:
        with z.open(TWB_FILENAME) as f:
            raw = f.read()
            text = raw.decode()
            try:
                ET.fromstring(text)
                print(f"✓ Dashboard injected: {final_path}")
                print(f"✓ XML valid: {len(raw)} bytes")
                # Report key features
                features = {
                    "dashboard": text.count("<dashboard ") == 1,
                    "quick-filters": "quick-filter" in text,
                    "cross-actions": text.count("<action ") == 90,
                    "all-sheets": all(s in text for s in SHEETS),
                    "instructions": "Petunjuk Penggunaan" in text,
                    "zones-not-items": "<zones>" in text and "dashboard-items" not in text,
                    "worksheet-windows": text.count("class='worksheet'") == 10,
                    "dashboard-window": "class=\"dashboard\"" in text,
                }
                for k, v in features.items():
                    print(f"  {'✓' if v else '✗'} {k}")
                if all(features.values()):
                    print("✅ PERFECT! Dashboard ready for use.")
            except ET.ParseError as e:
                print(f"✗ XML error: {e}")
                return False
    return True


if __name__ == "__main__":
    main()
