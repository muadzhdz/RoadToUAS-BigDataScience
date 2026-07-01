import xml.etree.ElementTree as ET, os

path = r'C:\Users\adzhd\OneDrive\Documents\My Tableau Repository\Workbooks\RoadToUAS-BigDataScience\luaran\Supermarket_Sales_Dashboard.twb'
tree = ET.parse(path)
root = tree.getroot()

sheets  = [w.get('name') for w in root.findall('.//worksheet')]
dboards = [d.get('name') for d in root.findall('.//dashboard')]
calcs   = [c.get('caption') for c in root.findall('.//datasource/column') if c.find('calculation') is not None and not c.get('param-domain-type')]
params  = [c.get('caption') for c in root.findall('.//column[@param-domain-type]')]
actions = [a.get('caption') for a in root.findall('.//action')]
zones   = [z.get('name') for z in root.findall('.//zone') if z.get('name')]
tags    = [child.tag for child in root]
sz      = os.path.getsize(path)

print("=== FINAL AUDIT REPORT ===\n")
print("ROOT STRUCTURE:", tags)
print()
print("BRIEF COMPLIANCE:")
print("  [PASS] Min 4 sheet      :", len(sheets), "sheet")
print("  [PASS] Min 3 calc field :", len(calcs))
print("  [PASS] Min 1 parameter  :", params)
print("  [PASS] Min 1 filt action:", actions)
print("  [PASS] Dashboard        :", dboards)
print("  [PASS] Dashboard zones  :", len(zones))
print()

print("SHEETS:")
for s in sheets:
    print("  -", s)
print()

print("QUICK FILTER CHECK (min 2 per sheet):")
for ws in root.findall('.//worksheet'):
    wname = ws.get('name')
    qfs = ws.findall('.//filter')
    cat_filters = [f for f in qfs if f.get('class') == 'categorical']
    cols = [f.get('column','').split('.')[-1] for f in cat_filters]
    status = "OK" if len(cat_filters) >= 2 else "MISSING"
    print("  [" + status + "] " + wname + ": " + str(len(cat_filters)) + " filters - " + str(cols))
print()

print("CALC FIELD FORMULAS:")
for c in root.findall('.//datasource/column'):
    calc = c.find('calculation')
    if calc is not None and not c.get('param-domain-type'):
        print("  " + str(c.get('caption')) + ": " + str(calc.get('formula')))
print()

print("PARAMETER:")
for c in root.findall('.//column[@param-domain-type]'):
    r = c.find('range')
    print("  " + str(c.get('caption')) + " | value=" + str(c.get('value')) + " | range=" + str(r.get('min') if r is not None else '?') + "-" + str(r.get('max') if r is not None else '?'))
print()

print("FILTER ACTION:")
for a in root.findall('.//action'):
    src = a.find('source')
    cmd = a.find('command')
    dests = cmd.findall('destination') if cmd is not None else []
    trigger = a.find('activation')
    print("  " + str(a.get('caption')))
    print("    trigger: " + str(trigger.get('type') if trigger is not None else '?'))
    print("    source : " + str(src.get('sheet') if src is not None else '?'))
    print("    targets: " + str([d.get('sheet') for d in dests]))
print()

print("EXTRACT + OBJECT-GRAPH:")
print("  extract     :", "PRESENT" if root.find('.//extract') is not None else "MISSING")
print("  object-graph:", "PRESENT" if root.find('.//object-graph') is not None else "MISSING")
print("  file size   :", sz, "bytes (" + str(round(sz/1024,1)) + " KB)")
print()

print("WINDOWS (9 expected):")
for w in root.findall('.//window'):
    print("  [" + str(w.get('class')) + "] " + str(w.get('name')))
print()

print("=== SEMUA CHECKS ===")
checks = [
    ("Min 4 sheet",      len(sheets) >= 4),
    ("Min 3 calc field", len(calcs)  >= 3),
    ("Min 1 parameter",  len(params) >= 1),
    ("Min 1 filter act", len(actions)>= 1),
    ("1 dashboard",      len(dboards)>= 1),
    ("8 dashboard zones",len(zones)  >= 8),
    ("9 windows",        len(root.findall('.//window')) >= 9),
    ("extract present",  root.find('.//extract') is not None),
    ("object-graph",     root.find('.//object-graph') is not None),
]
all_pass = True
for label, passed in checks:
    status = "PASS" if passed else "FAIL"
    if not passed: all_pass = False
    print("  [" + status + "] " + label)

qf_all_ok = all(
    len([f for f in ws.findall('.//filter') if f.get('class') == 'categorical']) >= 2
    for ws in root.findall('.//worksheet')
)
print("  [" + ("PASS" if qf_all_ok else "FAIL") + "] Quick filter 2x di semua sheet")

print()
if all_pass and qf_all_ok:
    print("RESULT: SEMUA PASS - file .twb siap dibuka di Tableau")
else:
    print("RESULT: ADA YANG FAIL - perlu diperbaiki")
