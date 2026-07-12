#!/usr/bin/env python3
"""
Convert .twbx from live Excel connection to extract-only (.hyper) for Tableau Public.
"""
import zipfile, os, re, sys
import pandas as pd
import pantab

TWBX_IN = sys.argv[1] if len(sys.argv) > 1 else "/home/whoami/Projects/RoadToUAS-BigDataScience/Proyek_BigData/Supermarket_Sales_Dashboard_final.twbx"
WORK = "/tmp/twbx-extract-fix"

# Prepare
os.makedirs(WORK, exist_ok=True)
os.chdir(WORK)

# Extract
with zipfile.ZipFile(TWBX_IN) as zf:
    zf.extractall()
    files = zf.namelist()
    twb_file = next(f for f in files if f.endswith('.twb'))
    xlsx_file = next((f for f in files if f.endswith('.xlsx')), None)

print(f"[1/4] Extracted: {twb_file}")

# Read & create .hyper
if xlsx_file:
    df = pd.read_excel(xlsx_file)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    if 'Time' in df.columns:
        df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
else:
    csv_file = next(f for f in files if f.endswith('.csv'))
    df = pd.read_csv(csv_file)

hyper_file = xlsx_file.replace('.xlsx', '.hyper') if xlsx else twb_file.replace('.twb', '.hyper')
os.makedirs(os.path.dirname(hyper_file), exist_ok=True)
pantab.frame_to_hyper(df, hyper_file, table='Extract')
print(f"[2/4] Created: {hyper_file}")

# Patch .twb
with open(twb_file, 'r') as f:
    content = f.read()

# Replace connection block: from <connection class='federated'> to </metadata-records>
start = content.find("<connection class='federated'>")
end = content.find("</metadata-records>", start)
if start < 0 or end < 0:
    print("[FAIL] Could not find connection block")
    sys.exit(1)
end += len("</metadata-records>")

import uuid
conn_id = uuid.uuid4().hex[:26]

new_conn = f"""      <connection class='federated'>
        <named-connections>
          <named-connection caption='Extract' name='extract.{conn_id}'>
            <connection class='extract' filename='{hyper_file}' />
          </named-connection>
        </named-connections>
        <relation connection='extract.{conn_id}' name='Extract' table='[Extract].[Extract]' type='table' />
        <extract>
          <connection class='extract' filename='{hyper_file}' />
          <relation name='Extract' table='[Extract].[Extract]' type='table' />
        </extract>
        <metadata-records>
          <metadata-record class='capability'>
            <remote-name />
            <remote-type>0</remote-type>
            <parent-name>[Extract].[Extract]</parent-name>
            <remote-alias />
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
        </metadata-records>"""

content = content[:start] + new_conn + content[end:]

# Fix object-graph section
obj_start = content.find("<object caption='supermarket_sales'")
obj_end = content.find("</object>", obj_start)
if obj_start >= 0 and obj_end >= 0:
    obj_end += len("</object>")
    new_obj = f"""          <object caption='Extract' id='supermarket!sales_{conn_id}'>
            <properties context='extract'>
              <relation name='Extract' table='[Extract].[Extract]' type='table' />
            </properties>
          </object>"""
    content = content[:obj_start] + new_obj + content[obj_end:]

with open(twb_file, 'w') as f:
    f.write(content)

# Validate
import xml.etree.ElementTree as ET
tree = ET.parse(twb_file)
print(f"[3/4] XML valid: root={tree.getroot().tag}")

# Repack .twbx (exclude .xlsx)
OUT = TWBX_IN  # overwrite
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(twb_file, arcname=twb_file)
    zf.write(hyper_file, arcname=hyper_file)

print(f"[4/4] Written: {OUT}")
print(f"      Size: {os.path.getsize(OUT)} bytes")
print("[OK] .twbx is now extract-only — ready for Tableau Public")
