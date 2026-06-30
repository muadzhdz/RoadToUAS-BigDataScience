#!/usr/bin/env python3
"""
Validation Verification Script
Double-checks AI computed metrics against pre-computed values
Run this AFTER AI generates analysis to verify correctness
"""

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "datasets" / "retail" / "supermarket_sales.csv"

def load_data(filepath):
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def validate():
    rows = load_data(DATASET)
    print("=" * 60)
    print(" VALIDATION VERIFICATION - AI Results Check")
    print("=" * 60)
    
    # 1. Basic counts
    print(f"\n[1] Row Count: {len(rows)} (expected: 1000)")
    assert len(rows) == 1000, "Row count mismatch!"
    
    # 2. Missing values
    missing = {}
    for col in rows[0].keys():
        missing[col] = sum(1 for r in rows if not r[col].strip())
    total_missing = sum(missing.values())
    print(f"[2] Missing Values: {total_missing} (expected: 0)")
    assert total_missing == 0, f"Missing values found: {missing}"
    
    # 3. Duplicates
    ids = [r['Invoice ID'] for r in rows]
    print(f"[3] Duplicates: COUNT={len(ids)}, COUNTD={len(set(ids))} (expected: 1000/1000)")
    assert len(ids) == len(set(ids)) == 1000, "Duplicates found!"
    
    # 4. City metrics
    cities = defaultdict(lambda: {'rev': 0, 'tx': 0, 'rating': [], 'qty': 0})
    for r in rows:
        c = r['City']
        cities[c]['rev'] += float(r['Total'])
        cities[c]['tx'] += 1
        cities[c]['rating'].append(float(r['Rating']))
        cities[c]['qty'] += int(r['Quantity'])
    
    expected = {
        'Yangon': {'rev': 106200.37, 'tx': 340, 'rating': 7.03, 'aov': 312.35},
        'Mandalay': {'rev': 106197.67, 'tx': 332, 'rating': 6.82, 'aov': 319.87},
        'Naypyitaw': {'rev': 110568.71, 'tx': 328, 'rating': 7.07, 'aov': 337.10}
    }
    
    print("\n[4] City Metrics:")
    for c, d in sorted(cities.items()):
        avg_r = sum(d['rating'])/len(d['rating'])
        aov = d['rev']/d['tx']
        exp = expected[c]
        print(f"  {c}: Rev=${d['rev']:.2f} (exp ${exp['rev']}), TX={d['tx']}, "
              f"Rating={avg_r:.2f} (exp {exp['rating']}), AOV=${aov:.2f} (exp ${exp['aov']})")
        assert abs(d['rev'] - exp['rev']) < 0.01, f"Revenue mismatch for {c}"
        assert d['tx'] == exp['tx'], f"TX count mismatch for {c}"
        assert abs(avg_r - exp['rating']) < 0.01, f"Rating mismatch for {c}"
        assert abs(aov - exp['aov']) < 0.01, f"AOV mismatch for {c}"
    
    # 5. Product lines
    prods = defaultdict(lambda: {'rev': 0, 'tx': 0, 'rating': []})
    for r in rows:
        p = r['Product line']
        prods[p]['rev'] += float(r['Total'])
        prods[p]['tx'] += 1
        prods[p]['rating'].append(float(r['Rating']))
    
    print("\n[5] Product Lines:")
    for p, d in sorted(prods.items(), key=lambda x: x[1]['rev'], reverse=True):
        avg_r = sum(d['rating'])/len(d['rating'])
        pct = d['rev'] / sum(x['rev'] for x in prods.values()) * 100
        print(f"  {p}: Rev=${d['rev']:.2f} ({pct:.2f}%), Rating={avg_r:.2f}")
    
    # 6. Member vs Normal
    member = {'rev': 0, 'tx': 0, 'rating': []}
    normal = {'rev': 0, 'tx': 0, 'rating': []}
    for r in rows:
        if r['Customer type'] == 'Member':
            member['rev'] += float(r['Total'])
            member['tx'] += 1
            member['rating'].append(float(r['Rating']))
        else:
            normal['rev'] += float(r['Total'])
            normal['tx'] += 1
            normal['rating'].append(float(r['Rating']))
    
    m_aov = member['rev']/member['tx']
    n_aov = normal['rev']/normal['tx']
    m_r = sum(member['rating'])/len(member['rating'])
    n_r = sum(normal['rating'])/len(normal['rating'])
    
    print(f"\n[6] Member vs Normal:")
    print(f"  Member: TX={member['tx']}, Rev=${member['rev']:.2f}, AOV=${m_aov:.2f}, Rating={m_r:.2f}")
    print(f"  Normal: TX={normal['tx']}, Rev=${normal['rev']:.2f}, AOV=${n_aov:.2f}, Rating={n_r:.2f}")
    print(f"  AOV diff: {((m_aov/n_aov)-1)*100:+.1f}%")
    
    # 7. Payment methods
    pays = defaultdict(lambda: {'tx': 0, 'rev': 0, 'rating': []})
    for r in rows:
        p = r['Payment']
        pays[p]['tx'] += 1
        pays[p]['rev'] += float(r['Total'])
        pays[p]['rating'].append(float(r['Rating']))
    
    print("\n[7] Payment Methods:")
    for p, d in sorted(pays.items(), key=lambda x: x[1]['rev'], reverse=True):
        avg_r = sum(d['rating'])/len(d['rating'])
        print(f"  {p}: TX={d['tx']}, Rev=${d['rev']:.2f}, Rating={avg_r:.2f}")
    
    # 8. Hourly
    hourly = defaultdict(lambda: {'tx': 0, 'rev': 0})
    for r in rows:
        h = int(r['Time'].split(':')[0])
        hourly[h]['tx'] += 1
        hourly[h]['rev'] += float(r['Total'])
    
    peak = max(hourly, key=lambda h: hourly[h]['tx'])
    print(f"\n[8] Peak Hour: {peak}:00 = {hourly[peak]['tx']} tx, ${hourly[peak]['rev']:.2f}")
    assert peak == 19, f"Peak hour should be 19, got {peak}"
    
    # 9. Overall
    total_rev = sum(float(r['Total']) for r in rows)
    avg_rating = sum(float(r['Rating']) for r in rows) / len(rows)
    
    print(f"\n[9] Overall: Revenue=${total_rev:.2f}, Avg Rating={avg_rating:.2f}")
    assert abs(total_rev - 322966.75) < 0.01, "Total revenue mismatch"
    assert abs(avg_rating - 6.97) < 0.01, "Avg rating mismatch"
    
    print("\n" + "=" * 60)
    print(" ALL VALIDATIONS PASSED [OK]")
    print("=" * 60)

if __name__ == '__main__':
    validate()
