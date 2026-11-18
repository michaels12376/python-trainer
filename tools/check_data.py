#!/usr/bin/env python3
"""Datenprüfung: Struktur, Verweise, Referenz-IDs (ids_baseline.json schützt Lernstände). --update-baseline speichert den aktuellen Stand."""
import json, os, re, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda f: json.load(open(os.path.join(H, 'daten', f), encoding='utf8'))
err = []
kap = {k['id'] for k in J('kapitel.json')['kapitel']}
T = J('aufgaben.json'); ids = [t['id'] for t in T]
if len(ids) != len(set(ids)): err.append('Aufgaben-IDs doppelt')
for t in T:
    w = t['id']
    if t['kap'] not in kap: err.append(f'{w}: Kapitel unbekannt')
    if t['typ'] not in ('predict', 'gap', 'bug', 'puzzle', 'code'): err.append(f'{w}: Typ')
    if t['lvl'] not in (1, 2, 3): err.append(f'{w}: Stufe')
    if not t.get('hints'): err.append(f'{w}: Hinweise fehlen')
    for f in {'predict': ['code'], 'gap': ['code', 'ans'], 'bug': ['text', 'code', 'ref'], 'puzzle': ['text', 'lines'], 'code': ['text', 'ref']}.get(t['typ'], []):
        if not t.get(f): err.append(f'{w}: Feld {f} fehlt')
    if t['typ'] == 'gap' and t['code'].count('___') != len(t.get('ans', [])): err.append(f'{w}: Lücken ≠ Antworten')
    used = set(re.findall(r'<<(\w+)>>', json.dumps(t, ensure_ascii=False)))
    if used - set((t.get('vars') or {}).keys()): err.append(f'{w}: Parameter ohne vars: {used - set((t.get("vars") or {}).keys())}')
    v = (t.get('vars') or {}).values()
    if v and len({len(x) for x in v}) != 1: err.append(f'{w}: vars unterschiedlich lang')
for k in kap:
    if not any(t['kap'] == k for t in T): err.append(f'Kapitel {k} ohne Aufgaben')
sp = J('spick.json')
for s in sp:
    if s['kap'] not in kap: err.append(f'Spickzettel {s["id"]}: Kapitel unbekannt')
cur = {'tasks': ids}
bp = os.path.join(H, 'daten', 'ids_baseline.json')
if '--update-baseline' in sys.argv:
    json.dump(cur, open(bp, 'w', encoding='utf8'), ensure_ascii=False); print('Referenz gespeichert:', {k: len(v) for k, v in cur.items()})
elif os.path.exists(bp):
    for k, v in json.load(open(bp, encoding='utf8')).items():
        miss = [i for i in v if i not in cur.get(k, [])]
        if miss: err.append(f'{k}: IDs fehlen gegenüber der Referenz (Lernstände!): {miss[:5]}')
print(f'Daten: {len(ids)} Aufgaben, {len(kap)} Kapitel, {len(sp)} Spickzettel')
if err: print('\n'.join('FEHLER ' + e for e in err)); print(f'Datenprüfung: {len(err)} Fehler'); sys.exit(1)
print('Datenprüfung: 0 Fehler')
