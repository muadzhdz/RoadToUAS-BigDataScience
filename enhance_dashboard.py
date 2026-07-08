#!/usr/bin/env python3
"""
Enhance Supermarket Sales Dashboard - injects interactive dashboard into .twb XML
Usage: python3 enhance_dashboard.py

Corrected XML schema following Tableau 18.1 XSD:
  <dashboard> children: style, size?, datasources, datasource-dependencies*, zones, simple-id
  <actions> at workbook level (not inside dashboard)
  <zones> replaces <dashboard-items>
"""

import os
import shutil
import zipfile
import uuid as _uuid
from xml.sax.saxutils import escape

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

# All column instances used across sheets (needed for datasource-dependencies)
COL_INSTANCES = [
    ("[City]", "None", "[none:City:nk]", "nominal"),
    ("[Customer type]", "None", "[none:Customer type:nk]", "nominal"),
    ("[Date]", "Day-Trunc", "[tdy:Date:qk]", "quantitative"),
    ("[Gender]", "None", "[none:Gender:nk]", "nominal"),
    ("[Hour]", "None", "[none:Hour:nk]", "ordinal"),
    ("[Invoice ID]", "Count", "[cnt:Invoice ID:qk]", "quantitative"),
    ("[Payment]", "None", "[none:Payment:nk]", "nominal"),
    ("[Product line]", "None", "[none:Product line:nk]", "nominal"),
    ("[Quantity]", "Count", "[cnt:Quantity:qk]", "quantitative"),
    ("[Rating]", "None", "[none:Rating:nk]", "ordinal"),
    ("[Rating]", "Sum", "[sum:Rating:qk]", "quantitative"),
    ("[Total]", "Sum", "[sum:Total:qk]", "quantitative"),
]


def uid():
    return str(_uuid.uuid4()).upper()


def build_dashboard_xml():
    """Build dashboard section with correct XSD structure."""
    lines = []
    dash_uid = uid()
    lines.append(f'<dashboard name="Supermarket Sales Dashboard">')

    # style (required)
    lines.append('  <style/>')

    # datasources (required) - reference existing
    lines.append('  <datasources>')
    lines.append(f'    <datasource name="{DS_NAME}"/>')
    lines.append('  </datasources>')

    # datasource-dependencies (required for each column used in zones)
    lines.append(f'  <datasource-dependencies datasource="{DS_NAME}">')
    for col_name, derivation, instance_name, typ in COL_INSTANCES:
        lines.append(f'    <column datatype="string" name="{col_name}" role="dimension" type="{typ}"/>')
        lines.append(f'    <column-instance column="{col_name}" derivation="{derivation}" name="{instance_name}" pivot="key" type="{typ}"/>')
    lines.append('  </datasource-dependencies>')

    # zones (replaces dashboard-items)
    lines.append('  <zones>')

    # Outer vertical flow container
    lines.append('    <zone type-v2="layout-flow" param="vert" name="outer">')

    # --- Title Zone ---
    lines.append('      <zone type-v2="layout-basic" name="title" size-pos="0,0,100000,5000">')
    lines.append('        <zone type="text" name="title_text">')
    title_cdata = ('<title>Supermarket Sales Dashboard</title>'
                   '<subtitle>Interactive Analytics for Strategic Insights</subtitle>'
                   '<p>Click any chart element to cross-filter all visuals. '
                   'Use the filter cards in the left sidebar to refine by City, Product line, etc.</p>')
    lines.append(f'          <text><![CDATA[{title_cdata}]]></text>')
    lines.append('        </zone>')
    lines.append('      </zone>')

    # --- Main Content Area ---
    lines.append('      <zone type-v2="layout-flow" param="vert" name="main" size-pos="0,5000,100000,86000">')

    # Row 1: Revenue Trend (full width) + Data Quality + Hourly Activity
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row1" size-pos="0,0,100000,26000">')
    lines.append('          <zone type-v2="layout-basic" name="revenue_trend" size-pos="0,0,70000,26000">')
    lines.append('            <zone type="worksheet" name="rev_sheet">')
    lines.append('              <worksheet>Revenue Trend</worksheet>')
    lines.append('            </zone>')
    lines.append('          </zone>')
    # Right stacked: Data Quality + Hourly Activity
    lines.append('          <zone type-v2="layout-flow" param="vert" name="kpi_stack" size-pos="70000,0,30000,26000">')
    for name in ("Data Quality", "Hourly Activity"):
        y = "0" if name == "Data Quality" else "13000"
        lines.append(f'            <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="0,{y},30000,12000">')
        lines.append('              <zone type="worksheet">')
        lines.append(f'                <worksheet>{name}</worksheet>')
        lines.append('              </zone>')
        lines.append('            </zone>')
    lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 2: Product Performance | Customer Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row2" size-pos="0,26000,100000,20000">')
    for i, name in enumerate(("Product Performance", "Customer Analysis")):
        x = "0" if name == "Product Performance" else "50000"
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{x},0,50000,20000">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 3: City Comparison | Payment Analysis
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row3" size-pos="0,46000,100000,20000">')
    for i, name in enumerate(("City Comparison", "Payment Analysis")):
        x = "0" if name == "City Comparison" else "50000"
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{x},0,50000,20000">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    # Row 4: Rating Distribution | Box Plot Total | Box Plot Rating
    lines.append('        <zone type-v2="layout-flow" param="horz" name="row4" size-pos="0,66000,100000,20000">')
    thirds = [("Rating Distribution", "0,0,34000,20000"),
              ("Box Plot Total", "34000,0,33000,20000"),
              ("Box Plot Rating", "67000,0,33000,20000")]
    for name, pos in thirds:
        lines.append(f'          <zone type-v2="layout-basic" name="{name.lower().replace(" ","_")}" size-pos="{pos}">')
        lines.append('            <zone type="worksheet">')
        lines.append(f'              <worksheet>{name}</worksheet>')
        lines.append('            </zone>')
        lines.append('          </zone>')
    lines.append('        </zone>')

    lines.append('      </zone>')  # close main
    lines.append('    </zone>')  # close outer
    lines.append('  </zones>')  # close zones

    # simple-id (required)
    lines.append(f'  <simple-id uuid="{{{dash_uid}}}"/>')
    lines.append('</dashboard>')
    return '\n'.join(lines)


def build_window_xml(dash_name):
    """Build dashboard window element."""
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
    """Build cross-filtering actions for workbook level."""
    lines = ['  <actions>']
    for src in SHEETS:
        for tgt in SHEETS:
            if src == tgt:
                continue
            act_uid = uid()
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
    # Start fresh from ORIGINAL twbx
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    # Use original from git (previous commit - before any dashboard injection)
    orig_twbx = os.path.join(os.path.dirname(TMP_DIR), "twbx_work", "SUPER_ORIGINAL.twbx")
    with zipfile.ZipFile(orig_twbx, 'r') as zf:
        zf.extractall(TMP_DIR)

    twb_path = os.path.join(TMP_DIR, TWB_FILENAME)

    with open(twb_path, 'r', encoding='utf-8') as f:
        twb_text = f.read()

    # 1. Inject dashboards section BEFORE <windows>
    dash_xml = build_dashboard_xml()
    dash_section = f"<dashboards>\n{dash_xml}\n</dashboards>"

    windows_start = twb_text.find('<windows')
    if windows_start == -1:
        print("ERROR: Could not find <windows>")
        return False

    twb_text = twb_text[:windows_start] + '  ' + dash_section + '\n  ' + twb_text[windows_start:]

    # 2. Inject dashboard window BEFORE </windows>
    win_xml = build_window_xml("Supermarket Sales Dashboard")
    windows_end = twb_text.find('</windows>')
    if windows_end == -1:
        print("ERROR: Could not find </windows>")
        return False

    twb_text = twb_text[:windows_end] + '\n' + win_xml + '\n' + twb_text[windows_end:]

    # 3. Inject actions at workbook level (before </workbook>)
    actions_xml = build_actions_xml()
    workbook_end = twb_text.find('</workbook>')
    if workbook_end == -1:
        print("ERROR: Could not find </workbook>")
        return False

    twb_text = twb_text[:workbook_end] + '\n' + actions_xml + '\n' + twb_text[workbook_end:]

    # Write modified TWB
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

    # Copy back to project
    final_path = os.path.join(os.getcwd(), TWBX_PATH)
    shutil.copy2(out_path, final_path)

    # Verify XML well-formed
    import xml.etree.ElementTree as ET
    with zipfile.ZipFile(out_path) as z:
        with z.open(TWB_FILENAME) as f:
            raw = f.read()
            try:
                ET.fromstring(raw)
                print(f"✓ Dashboard injected: {final_path}")
                print(f"✓ XML valid: {len(raw)} bytes, {raw.decode().count('<dashboard')} dashboard(s)")
            except ET.ParseError as e:
                print(f"✗ XML error: {e}")
                # Print context around error
                lines = raw.decode().split('\n')
                err_line = int(str(e).split('line ')[1].split(',')[0]) if 'line ' in str(e) else 0
                if err_line:
                    for i in range(max(0, err_line-2), min(len(lines), err_line+2)):
                        print(f"  {i+1}: {lines[i]}")
                return False
    return True


if __name__ == "__main__":
    main()
