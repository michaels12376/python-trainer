#!/usr/bin/env python3
"""Quelle der Erklär-Abschnitte (Python-Trainer). Erzeugt daten/lernen.json:  python3 tools/pipeline/lernen_quelle.py
Block-Typen: ('t', html) Text · ('c', code, stdin-Liste) ausführbares Beispiel · ('tip', html) Merke-Kasten · ('warn', html) Achtung-Kasten.
quiz = [(Frage, [Antworten], Index der richtigen, Begründung)]; tasks = Aufgaben-IDs, die zu diesem Abschnitt gehören (Nachlesen-Link)."""
import json, os, sys
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L = []
def lesson(id, kap, titel, minuten, blocks, quiz, tasks):
    bl = []
    for b in blocks:
        t = b[0]
        if t == 'c': bl.append({'t': 'c', 'code': b[1], 'in': b[2] if len(b) > 2 else [], 'err': len(b) > 3 and b[3] == 'fehler'})
        else: bl.append({'t': t, 'h': b[1]})
    L.append({'id': id, 'kap': kap, 'titel': titel, 'min': minuten, 'blocks': bl,
              'quiz': [{'q': q[0], 'o': q[1], 'a': q[2], 'why': q[3]} for q in quiz], 'tasks': tasks})
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lernen_inhalt1.py'), encoding='utf8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lernen_inhalt2.py'), encoding='utf8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lernen_inhalt3.py'), encoding='utf8').read())
if __name__ == '__main__':
    ids = [l['id'] for l in L]; assert len(ids) == len(set(ids))
    json.dump(L, open(os.path.join(H, 'daten', 'lernen.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
    print(len(L), 'Erklär-Abschnitte')
