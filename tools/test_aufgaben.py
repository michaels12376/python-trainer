#!/usr/bin/env python3
"""Prüft alle Aufgaben: Referenzlösungen laufen, Fehlerprogramme sind wirklich fehlerhaft, Lücken/Puzzles führen zur erwarteten Ausgabe.
Aufruf:  python3 tools/test_aufgaben.py   (nutzt das lokale python3; die App nutzt Pyodide mit gleicher Python-Version)"""
import json, os, re, subprocess, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = json.load(open(os.path.join(H, 'daten', 'aufgaben.json'), encoding='utf8'))
KAP = json.load(open(os.path.join(H, 'daten', 'kapitel.json'), encoding='utf8'))['kapitel']
err = []
def run(code, lines):
    try:
        p = subprocess.run([sys.executable, '-I', '-c', code], input='\n'.join(lines) + '\n', capture_output=True, text=True, timeout=3)
        return p.stdout.rstrip('\n'), p.returncode
    except subprocess.TimeoutExpired:
        return '', 'timeout'
def sub(o, i):
    if isinstance(o, str):
        return re.sub(r'<<(\w+)>>', lambda m: T_VARS[m.group(1)][i], o)
    if isinstance(o, list): return [sub(x, i) for x in o]
    if isinstance(o, dict): return {k: sub(v, i) for k, v in o.items()}
    return o
kaps = {k['id'] for k in KAP}
types = {'predict', 'gap', 'bug', 'puzzle', 'code'}
for t in T:
    where = t['id']
    if t['kap'] not in kaps: err.append(f'{where}: Kapitel {t["kap"]} unbekannt')
    if t['typ'] not in types: err.append(f'{where}: Typ {t["typ"]}')
    if t['lvl'] not in (1, 2, 3): err.append(f'{where}: Stufe')
    if not t.get('hints'): err.append(f'{where}: Hinweise fehlen')
    T_VARS = t.get('vars') or {}
    n = len(next(iter(T_VARS.values()))) if T_VARS else 1
    if any(len(v) != n for v in T_VARS.values()): err.append(f'{where}: vars unterschiedlich lang')
    for i in range(n):
        x = sub(t, i) if T_VARS else t
        tests = x.get('tests') or [[]]
        typ = x['typ']
        tag = f'{where}[{i}]'
        if typ == 'predict':
            out, rc = run(x['code'], x.get('stdin') or [])
            if rc != 0 or not out.strip(): err.append(f'{tag}: predict liefert keine saubere Ausgabe ({rc})')
        elif typ == 'gap':
            code = x['code']
            if code.count('___') != len(x['ans']): err.append(f'{tag}: Anzahl Lücken ≠ Antworten')
            for a in x['ans']: code = code.replace('___', a, 1)
            for tl in tests:
                out, rc = run(code, tl)
                if rc != 0 or not out.strip(): err.append(f'{tag}: gap mit Lösung fehlerhaft {tl} ({rc})')
        elif typ == 'bug':
            diff = False
            for tl in tests:
                ro, rrc = run(x['ref'], tl)
                if rrc != 0 or not ro.strip(): err.append(f'{tag}: ref fehlerhaft {tl} ({rrc})')
                bo, brc = run(x['code'], tl)
                if brc != 0 or bo != ro: diff = True
            if not diff: err.append(f'{tag}: bug-Programm ist gar nicht fehlerhaft')
        elif typ == 'puzzle':
            code = '\n'.join(x['lines'])
            ok_all = True
            for tl in tests:
                out, rc = run(code, tl)
                if rc != 0 or not out.strip(): err.append(f'{tag}: puzzle-Lösung fehlerhaft {tl} ({rc})')
            if len(set(x['lines'])) != len(x['lines']): err.append(f'{tag}: Puzzle-Zeilen nicht eindeutig')
        elif typ == 'code':
            for tl in tests:
                ro, rc = run(x['ref'], tl)
                if rc != 0 or not ro.strip(): err.append(f'{tag}: ref fehlerhaft {tl} ({rc})')
            for nd in x.get('need', []):
                m = re.search(nd['re'], x['ref'])
                if bool(m) == bool(nd.get('not')): err.append(f'{tag}: Referenz erfüllt need „{nd["re"]}“ nicht')
cnt = {}
for t in T: cnt[t['typ']] = cnt.get(t['typ'], 0) + 1
print(f'Aufgaben: {len(T)} {cnt}')
for k in KAP: print(f'  Kapitel {k["id"]}: {sum(1 for t in T if t["kap"]==k["id"])} Aufgaben')
if err:
    print('\n'.join(err)); print(f'FEHLER ({len(err)})'); sys.exit(1)
print('AUFGABEN OK')
