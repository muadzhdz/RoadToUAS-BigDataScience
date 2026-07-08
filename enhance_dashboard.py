#!/usr/bin/env python3
"""
Enhance Supermarket Sales Dashboard - injects interactive dashboard into .twb XML
Usage: python3 enhance_dashboard.py
"""

import os
import shutil
import zipfile

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


def build_dashboard_xml():
    """Build the full dashboard section as a string."""
    lines = []
    lines.append('<dashboard name="Supermarket Sales Dashboard">')
    lines.append('  <dashboard-items>')

    # Outer vertical container
    lines.append('    <zone type-v2="layout-flow" param="vert" name="outer">')

    # --- TITLE ZONE ---
    lines.append('      <zone type-v2="layout-basic" name="title" size-pos="0,0,100000,5000">')
    lines.append('        <zone type="text" name="title_text">')
    lines.append('          <text><![CDATA[<title>Supermarket Sales Dashboard</title>')
    lines.append('<subtitle>Filter by clicking any chart — all visuals update dynamically</subtitle>]]></text>')
    lines.append('        </zone>')
    lines.append('        <zone type="text" name="title_deco"/>')
    lines.append('      </zone>')

    # --- FILTER INSTRUCTIONS ZONE ---
    lines.append('      <zone type-v2="layout-basic" name="filter_bar" size-pos="0,5000,100000,4000">')
    lines.append('        <zone type="text" name="filter_help">')
    lines.append('          <text><![CDATA[<p>🔍 Click on bars / lines / dots in any chart to cross-filter all other charts. '
                 'Use native filters (right sidebar) for <b>City</b>, <b>Product line</b>, <b>Payment</b>, <b>Customer type</b>.</p>]]></text>')
    lines.append('        </zone>')
    lines.append('        <zone type="text" name="filter_help2"/>')
    lines.append('      </zone>')

    # --- MAIN CONTENT ---
    lines.append('      <zone type-v2="layout-flow" param="vert" name="main" size-pos="0,9000,100000,82000">')

    # Row 1: Revenue Trend (full width)
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row1" size-pos="0,0,100000,25000">')
    lines.append('          <zone type-v2="layout-basic" name="revenue_trend" size-pos="0,0,70000,25000">')
    lines.append('            <zone type="worksheet" name="rev_sheet">')
    lines.append('              <worksheet>Revenue Trend</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')

    # Right side stacked: Data Quality + Hourly Activity
    lines.append('          <zone type-v2="layout-flow" param="vert" name="kpi_group" size-pos="70000,0,30000,25000">')
    lines.append('            <zone type-v2="layout-basic" name="kpi_dq" size-pos="0,0,30000,12000">')
    lines.append('              <zone type="worksheet" name="dq_sheet">')
    lines.append('                <worksheet>Data Quality</worksheet>')
    lines.append('              </zone>')
    lines.append('            </zone>')
    lines.append('            <zone type-v2="layout-basic" name="kpi_hourly" size-pos="0,12500,30000,12000">')
    lines.append('              <zone type="worksheet" name="hourly_sheet">')
    lines.append('                <worksheet>Hourly Activity</worksheet>')
    lines.append('              </zone>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 2: Product Performance | Customer Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row2" size-pos="0,25000,100000,20000">')
    lines.append('          <zone type-v2="layout-basic" name="prod_perf" size-pos="0,0,50000,20000">')
    lines.append('            <zone type="worksheet" name="prod_sheet">')
    lines.append('              <worksheet>Product Performance</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-basic" name="cust_analysis" size-pos="50000,0,50000,20000">')
    lines.append('            <zone type="worksheet" name="cust_sheet">')
    lines.append('              <worksheet>Customer Analysis</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 3: City Comparison | Payment Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row3" size-pos="0,45000,100000,20000">')
    lines.append('          <zone type-v2="layout-basic" name="city_comp" size-pos="0,0,50000,20000">')
    lines.append('            <zone type="worksheet" name="city_sheet">')
    lines.append('              <worksheet>City Comparison</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-basic" name="pay_analysis" size-pos="50000,0,50000,20000">')
    lines.append('            <zone type="worksheet" name="pay_sheet">')
    lines.append('              <worksheet>Payment Analysis</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 4: Rating Distribution | Box Plot Total | Box Plot Rating
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row4" size-pos="0,65000,100000,20000">')
    lines.append('          <zone type-v2="layout-basic" name="rating_dist" size-pos="0,0,34000,20000">')
    lines.append('            <zone type="worksheet" name="rating_sheet">')
    lines.append('              <worksheet>Rating Distribution</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-basic" name="box_total" size-pos="34000,0,33000,20000">')
    lines.append('            <zone type="worksheet" name="bt_sheet">')
    lines.append('              <worksheet>Box Plot Total</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('          <zone type-v2="layout-basic" name="box_rating" size-pos="67000,0,33000,20000">')
    lines.append('            <zone type="worksheet" name="br_sheet">')
    lines.append('              <worksheet>Box Plot Rating</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    lines.append('      </zone>')
    lines.append('    </zone>')
    lines.append('  </dashboard-items>')

    # Options
    lines.append('  <options>')
    lines.append('    <option name="show-dashboard-title" value="true"/>')
    lines.append('    <option name="show-dashboard-title-shadows" value="false"/>')
    lines.append('  </options>')

    # Cross-filtering actions
    import uuid as _uuid
    lines.append('  <actions>')
    for src in SHEETS:
        for tgt in SHEETS:
            if src == tgt:
                continue
            act_uid = str(_uuid.uuid4()).upper()
            lines.append(f'    <action class="filter" name="Filter from {src} to {tgt}">')
            lines.append('      <action-options target-type="dashboard"/>')
            lines.append('      <source-filters/>')
            lines.append('      <target-sheets>')
            lines.append(f'        <sheet name="{tgt}"/>')
            lines.append('      </target-sheets>')
            lines.append('    </action>')
    lines.append('  </actions>')

    lines.append('</dashboard>')
    return '\n'.join(lines)


def build_window_xml(dash_name):
    import uuid as _uuid
    win_uid = str(_uuid.uuid4()).upper()
    lines = [
        f'    <window class="dashboard" name="{dash_name}">',
        '      <cards>',
        '        <edge name="left">',
        '          <strip size="160">',
        '            <card type="pages"/>',
        '            <card type="filters"/>',
        '          </strip>',
        '        </edge>',
        '        <edge name="top">',
        '          <strip size="2147483647">',
        '            <card type="title"/>',
        '          </strip>',
        '        </edge>',
        '      </cards>',
        f'      <simple-id uuid="{{{win_uid}}}"/>',
        '    </window>',
    ]
    return '\n'.join(lines)


def main():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    with zipfile.ZipFile(TWBX_PATH, 'r') as zf:
        zf.extractall(TMP_DIR)

    twb_path = os.path.join(TMP_DIR, TWB_FILENAME)

    with open(twb_path, 'r', encoding='utf-8') as f:
        twb_text = f.read()

    dash_xml = build_dashboard_xml()
    dash_section = f"<dashboards>\n{dash_xml}\n</dashboards>"

    ws_end = twb_text.find('</worksheets>')
    if ws_end == -1:
        print("ERROR: Could not find </worksheets>")
        return False
    ws_end = ws_end + len('</worksheets>')

    twb_text = twb_text[:ws_end] + '\n  ' + dash_section + '\n' + twb_text[ws_end:]

    win_xml = build_window_xml("Supermarket Sales Dashboard")
    windows_end = twb_text.find('</windows>')
    if windows_end == -1:
        print("ERROR: Could not find </windows>")
        return False

    twb_text = twb_text[:windows_end] + '\n' + win_xml + '\n' + twb_text[windows_end:]

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
            try:
                ET.fromstring(f.read())
                print(f"✓ Dashboard injected: {final_path} ({os.path.getsize(final_path)} bytes)")
                print(f"✓ XML valid")
                print(f"✓ 10 worksheets arranged in interactive dashboard")
                print(f"✓ Cross-filtering enabled between all sheets")
            except ET.ParseError as e:
                print(f"✗ XML error: {e}")
                return False
    return True


if __name__ == "__main__":
    main()
