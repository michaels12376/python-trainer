#!/usr/bin/env python3
"""Prüft die Erklär-Abschnitte: Beispiele laufen (absichtliche Fehler sind markiert), Quiz-Antworten gültig, jede Aufgabe gehört zu genau einem Abschnitt.
Aufruf:  python3 tools/test_lernen.py"""
import json, os, subprocess, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda f: json.load(open(os.path.join(H, 'daten', f), encoding='utf8'))
L, T, K = J('lernen.json'), J('aufgaben.json'), {k['id'] for k in J('kapitel.json')['kapitel']}
err = []; tids = {t['id']: t for t in T}; zug = {}; n = 0
for l in L:
    if l['kap'] not in K: err.append(f'{l["id"]}: Kapitel')
    if not l['quiz']: err.append(f'{l["id"]}: Quiz fehlt')
    for q in l['quiz']:
        if not 0 <= q['a'] < len(q['o']): err.append(f'{l["id"]}: Quiz-Antwort ungültig: {q["q"][:30]}')
    for i, b in enumerate(l['blocks']):
        if b['t'] == 'c':
            n += 1
            try: p = subprocess.run([sys.executable, '-I', '-c', b['code']], input='\n'.join(b['in']) + '\n', capture_output=True, text=True, timeout=5); rc = p.returncode
            except subprocess.TimeoutExpired: rc = 'timeout'
            if b['err'] and rc == 0: err.append(f'{l["id"]} Beispiel {i}: soll fehlschlagen, läuft aber')
            if not b['err'] and rc != 0: err.append(f'{l["id"]} Beispiel {i}: Fehler ({rc})')
    for t in l['tasks']:
        if t not in tids: err.append(f'{l["id"]}: Aufgabe {t} unbekannt')
        elif tids[t]['kap'] != l['kap']: err.append(f'{l["id"]}: Aufgabe {t} aus anderem Kapitel')
        if t in zug: err.append(f'Aufgabe {t} doppelt zugeordnet ({zug[t]}, {l["id"]})')
        zug[t] = l['id']
for t in tids:
    if t not in zug: err.append(f'Aufgabe {t} gehört zu keinem Abschnitt')
print(f'Abschnitte: {len(L)}, Beispiele: {n}, Quizfragen: {sum(len(l["quiz"]) for l in L)}')
if err: print('\n'.join(err)); print(f'FEHLER ({len(err)})'); sys.exit(1)
print('LERNEN OK')
