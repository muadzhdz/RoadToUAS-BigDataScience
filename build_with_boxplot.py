"""
Rebuild Supermarket_Sales_Dashboard.twb with 10 worksheets:
- The original 8 worksheets (with filters, styles)
- 2 new outlier check worksheets: Box Plot Total and Box Plot Rating
- NO <actions> at root level (since Tableau 2026 schema doesn't allow it; to be created in Tableau Desktop)
- NO <shelf-sorts> inside <view> (since Tableau 2026 schema doesn't allow it; sorting is done in Tableau Desktop)
- All 11 windows (10 worksheets + 1 dashboard)
"""
import re, xml.etree.ElementTree as ET

SRC = r'C:\Users\adzhd\OneDrive\Documents\My Tableau Repository\Workbooks\UAS-Kelompok1.twb'
DST = r'C:\Users\adzhd\OneDrive\Documents\My Tableau Repository\Workbooks\RoadToUAS-BigDataScience\luaran\Supermarket_Sales_Dashboard.twb'
DS  = 'federated.02hj2n40cilez216q1kk11tabb4t'

with open(SRC, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# STEP 1: Inject calc fields + parameter
# ============================================================
calc_inject = """      <column caption='Hour' datatype='integer' name='[Hour]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='INT(DATEPART(&apos;hour&apos;, [Time]))' />
      </column>
      <column caption='Day of Week' datatype='string' name='[Day of Week]' role='dimension' type='nominal'>
        <calculation class='tableau' formula='DATENAME(&apos;weekday&apos;, [Date])' />
      </column>
      <column caption='Month' datatype='string' name='[Month]' role='dimension' type='nominal'>
        <calculation class='tableau' formula='DATENAME(&apos;month&apos;, [Date])' />
      </column>
      <column caption='Revenue per Unit' datatype='real' name='[Revenue per Unit]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='[Total] / [Quantity]' />
      </column>
      <column caption='Rating Category' datatype='string' name='[Rating Category]' role='dimension' type='nominal'>
        <calculation class='tableau' formula='IF [Rating] &gt;= 9 THEN &quot;High&quot; ELSEIF [Rating] &gt;= 7 THEN &quot;Medium&quot; ELSE &quot;Low&quot; END' />
      </column>
      <column caption='Transaction Size' datatype='string' name='[Transaction Size]' role='dimension' type='nominal'>
        <calculation class='tableau' formula='IF [Quantity] &gt;= 7 THEN &quot;Large&quot; ELSEIF [Quantity] &gt;= 4 THEN &quot;Medium&quot; ELSE &quot;Small&quot; END' />
      </column>
      <column caption='Week Number' datatype='integer' name='[Week Number]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='DATEPART(&apos;week&apos;, [Date])' />
      </column>
      <column caption='Top N Products' datatype='integer' name='[Parameter 1]' param-domain-type='range' role='measure' type='quantitative' value='6'>
        <range granularity='1' max='6' min='1' />
      </column>
"""
content = content.replace("      <extract count='-1'", calc_inject + "      <extract count='-1'", 1)

# ============================================================
# STEP 2: Helper Functions
# ============================================================
def ci(col, deriv, iname, pivot, typ):
    return f"            <column-instance column='[{col}]' derivation='{deriv}' name='[{iname}]' pivot='{pivot}' type='{typ}' />\n"
def cdef(caption, dtype, cname, role, typ):
    return f"            <column caption='{caption}' datatype='{dtype}' name='[{cname}]' role='{role}' type='{typ}' />\n"

CITY    = cdef('City','string','City','dimension','nominal') + ci('City','None','none:City:nk','key','nominal')
PL      = cdef('Product line','string','Product line','dimension','nominal') + ci('Product line','None','none:Product line:nk','key','nominal')
TOTAL   = cdef('Total','real','Total','measure','quantitative') + ci('Total','Sum','sum:Total:qk','key','quantitative')
INVID   = cdef('Invoice ID','string','Invoice ID','dimension','nominal') + ci('Invoice ID','Count','cnt:Invoice ID:qk','key','quantitative')

QF = f"""          <filter class='categorical' column='[{DS}].[none:City:nk]'>
            <groupfilter function='level-members' level='[none:City:nk]' user:ui-domain='relevant' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[{DS}].[none:Product line:nk]'>
            <groupfilter function='level-members' level='[none:Product line:nk]' user:ui-domain='relevant' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
"""

def make_ws(name, uuid, deps_str, rows, cols, mark, color, labels=True, agg=True):
    label_style = ""
    if labels:
        label_style = """        <style>
          <style-rule element='mark'>
            <format attr='mark-labels-show' value='true' />
            <format attr='mark-labels-cull' value='true' />
          </style-rule>
        </style>"""
    agg_val = 'true' if agg else 'false'
    return f"""    <worksheet name='{name}'>
      <table>
        <view>
          <datasources>
            <datasource caption='supermarket_sales (dataset-blabla)' name='{DS}' />
          </datasources>
          <datasource-dependencies datasource='{DS}'>
{deps_str}          </datasource-dependencies>
{QF}          <aggregation value='{agg_val}' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='{mark}' />
            <encodings>
              <color column='[{DS}].[{color}]' />
            </encodings>
{label_style}
          </pane>
        </panes>
        <rows>[{DS}].[{rows}]</rows>
        <cols>[{DS}].[{cols}]</cols>
      </table>
      <simple-id uuid='{{{uuid}}}' />
    </worksheet>"""

# ============================================================
# STEP 3: Build 10 worksheets
# ============================================================

# --- Sheet 1: Revenue Trend (Line) ---
ws1 = make_ws('Revenue Trend','A1A1A1A1-0001-0001-0001-A1A1A1A1A1A1',
    TOTAL + cdef('Date','date','Date','dimension','ordinal') + ci('Date','Day-Trunc','tdy:Date:qk','key','quantitative') + CITY + PL,
    'sum:Total:qk','tdy:Date:qk','Line','none:City:nk', labels=False)

# --- Sheet 2: Product Performance (Bar) ---
ws2 = make_ws('Product Performance','A2A2A2A2-0002-0002-0002-A2A2A2A2A2A2',
    PL + TOTAL + CITY,
    'none:Product line:nk','sum:Total:qk','Bar','none:City:nk')

# --- Sheet 3: Customer Analysis (Bar) ---
ws3 = make_ws('Customer Analysis','A3A3A3A3-0003-0003-0003-A3A3A3A3A3A3',
    cdef('Customer type','string','Customer type','dimension','nominal') + ci('Customer type','None','none:Customer type:nk','key','nominal') + TOTAL + PL + CITY,
    'sum:Total:qk','none:Customer type:nk','Bar','none:Product line:nk')

# --- Sheet 4: Hourly Activity (Bar) ---
ws4 = make_ws('Hourly Activity','A4A4A4A4-0004-0004-0004-A4A4A4A4A4A4',
    cdef('Hour','integer','Hour','measure','quantitative') + ci('Hour','None','none:Hour:nk','key','nominal') + INVID + CITY + PL,
    'cnt:Invoice ID:qk','none:Hour:nk','Bar','none:City:nk')

# --- Sheet 5: City Comparison (Bar) ---
ws5 = make_ws('City Comparison','A5A5A5A5-0005-0005-0005-A5A5A5A5A5A5',
    CITY + TOTAL + cdef('Rating','real','Rating','measure','quantitative') + ci('Rating','Avg','avg:Rating:qk','key','quantitative') + PL,
    'sum:Total:qk','none:City:nk','Bar','none:City:nk')

# --- Sheet 6: Rating Distribution (Bar) ---
ws6 = make_ws('Rating Distribution','A6A6A6A6-0006-0006-0006-A6A6A6A6A6A6',
    cdef('Rating','real','Rating','measure','quantitative') + ci('Rating','None','none:Rating:nk','key','nominal') + INVID + PL + CITY,
    'cnt:Invoice ID:qk','none:Rating:nk','Bar','none:Product line:nk')

# --- Sheet 7: Payment Analysis (Bar) ---
ws7 = make_ws('Payment Analysis','A7A7A7A7-0007-0007-0007-A7A7A7A7A7A7',
    cdef('Payment','string','Payment','dimension','nominal') + ci('Payment','None','none:Payment:nk','key','nominal') + TOTAL + INVID + CITY + PL,
    'sum:Total:qk','none:Payment:nk','Bar','none:Payment:nk')

# --- Sheet 8: Data Quality (Bar) ---
ws8 = make_ws('Data Quality','A8A8A8A8-0008-0008-0008-A8A8A8A8A8A8',
    CITY + INVID + ci('Invoice ID','CountD','ctd:Invoice ID:qk','key','quantitative') + PL,
    'cnt:Invoice ID:qk','none:City:nk','Bar','none:City:nk')

# --- Sheet 9: Box Plot Total (Box Plot) ---
ws9 = make_ws('Box Plot Total','A9A9A9A9-0009-0009-0009-A9A9A9A9A9A9',
    TOTAL + CITY + PL,
    'none:City:nk','sum:Total:qk','Circle','none:City:nk', labels=False, agg=False)

# --- Sheet 10: Box Plot Rating (Box Plot) ---
ws10 = make_ws('Box Plot Rating','B1B1B1B1-0010-0010-0010-B1B1B1B1B1B1',
    cdef('Rating','real','Rating','measure','quantitative') + ci('Rating','Sum','sum:Rating:qk','key','quantitative') + CITY + PL,
    'none:Product line:nk','sum:Rating:qk','Circle','none:Product line:nk', labels=False, agg=False)

# ============================================================
# STEP 4: Dashboard (8 original zones)
# ============================================================
dashboard_block = f"""  <dashboards>
    <dashboard name='Supermarket Sales Dashboard'>
      <style />
      <size maxheight='900' maxwidth='1200' minheight='900' minwidth='1200' sizing-mode='fixed' />
      <datasources>
        <datasource caption='supermarket_sales (dataset-blabla)' name='{DS}' />
      </datasources>
      <zones>
        <zone h='22776' id='1' w='30480' x='0' y='0'>
          <zone h='22776' id='2' type='layout-flow' w='30480' x='0' y='0'>
            <zone h='2847' id='3' type='layout-flow' w='30480' x='0' y='0'>
              <zone h='2847' id='31' name='Revenue Trend' w='15240' x='0' y='0' />
              <zone h='2847' id='32' name='Product Performance' w='15240' x='15240' y='0' />
            </zone>
            <zone h='2847' id='4' type='layout-flow' w='30480' x='0' y='2847'>
              <zone h='2847' id='41' name='Customer Analysis' w='15240' x='0' y='2847' />
              <zone h='2847' id='42' name='Hourly Activity' w='15240' x='15240' y='2847' />
            </zone>
            <zone h='2847' id='5' type='layout-flow' w='30480' x='0' y='5694'>
              <zone h='2847' id='51' name='City Comparison' w='15240' x='0' y='5694' />
              <zone h='2847' id='52' name='Rating Distribution' w='15240' x='15240' y='5694' />
            </zone>
            <zone h='2847' id='6' type='layout-flow' w='30480' x='0' y='8541'>
              <zone h='2847' id='61' name='Payment Analysis' w='15240' x='0' y='8541' />
              <zone h='2847' id='62' name='Data Quality' w='15240' x='15240' y='8541' />
            </zone>
          </zone>
        </zone>
      </zones>
      <simple-id uuid='{{D0D0D0D0-D001-D001-D001-D0D0D0D0D0D0}}' />
    </dashboard>
  </dashboards>
"""

# ============================================================
# STEP 5: Windows (10 sheets + 1 dashboard = 11 total)
# ============================================================
def make_win(cls, name, uuid):
    return f"""    <window class='{cls}' maximized='true' name='{name}'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{{{uuid}}}' />
    </window>
"""

windows_block  = "  <windows source-height='30'>\n"
windows_block += make_win('worksheet','Revenue Trend',            'F1F1F1F1-0001-0001-0001-F1F1F1F1F1F1')
windows_block += make_win('worksheet','Product Performance',      'F2F2F2F2-0002-0002-0002-F2F2F2F2F2F2')
windows_block += make_win('worksheet','Customer Analysis',        'F3F3F3F3-0003-0003-0003-F3F3F3F3F3F3')
windows_block += make_win('worksheet','Hourly Activity',          'F4F4F4F4-0004-0004-0004-F4F4F4F4F4F4')
windows_block += make_win('worksheet','City Comparison',          'F5F5F5F5-0005-0005-0005-F5F5F5F5F5F5')
windows_block += make_win('worksheet','Rating Distribution',      'F6F6F6F6-0006-0006-0006-F6F6F6F6F6F6')
windows_block += make_win('worksheet','Payment Analysis',         'F7F7F7F7-0007-0007-0007-F7F7F7F7F7F7')
windows_block += make_win('worksheet','Data Quality',             'F8F8F8F8-0008-0008-0008-F8F8F8F8F8F8')
windows_block += make_win('worksheet','Box Plot Total',           'F9F9F9F9-0009-0009-0009-F9F9F9F9F9F9')
windows_block += make_win('worksheet','Box Plot Rating',          'FB1B1B1B-0010-0010-0010-FB1B1B1B1B1B')
windows_block += make_win('dashboard','Supermarket Sales Dashboard','DBDBDBDB-DB01-DB01-DB01-DBDBDBDBDB01')
windows_block += "  </windows>"

# ============================================================
# STEP 6: Rebuild file with XML-compliant order:
# manifest > preferences > datasources > worksheets > dashboards > windows
# (NO <actions> and NO <shelf-sorts> for schema compliance)
# ============================================================
lines = content.splitlines(keepends=True)
idx_ds_end = next(i for i,l in enumerate(lines) if '</datasources>' in l)

# We take everything up to </datasources>
before_worksheets = ''.join(lines[:idx_ds_end+1])

# Combine everything
ws_block = f"  <worksheets>\n{ws1}\n{ws2}\n{ws3}\n{ws4}\n{ws5}\n{ws6}\n{ws7}\n{ws8}\n{ws9}\n{ws10}\n  </worksheets>"
new_content = (before_worksheets.rstrip() + '\n' + 
               ws_block + '\n' + 
               dashboard_block + 
               windows_block + 
               '\n</workbook>')

# Remove old thumbnails if present
new_content = re.sub(r'\s*<thumbnails>.*?</thumbnails>', '', new_content, flags=re.DOTALL)

with open(DST, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("[OK] Workbook successfully written without schema-violating tags!")
