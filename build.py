#!/usr/bin/env python3
"""Baut python-trainer.html aus src/ + daten/ (alles inline, eine Datei).  Aufruf:  python3 build.py"""
import json, os, subprocess, sys, time
H = os.path.dirname(os.path.abspath(__file__))
S = lambda *p: os.path.join(H, *p)
if '--skip-check' not in sys.argv:
    if subprocess.call([sys.executable, S('tools', 'check_data.py')]) != 0:
        sys.exit('Abbruch: Datenprüfung meldet Fehler (siehe oben).')
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
J = lambda f: json.load(open(S('daten', f), encoding='utf8'))
VERSION = open(S('VERSION'), encoding='utf8').read().strip()
data = "const BUILD='" + time.strftime('%Y%m%d%H%M%S') + "';\nconst APP_VERSION='" + VERSION + "';\nconst KAPITEL=%s;\nconst TASKS=%s;\nconst SPICK=%s;\n" % (dump(J('kapitel.json')['kapitel']), dump(J('aufgaben.json')), dump(J('spick.json')))
rd = lambda f: open(S('src', f), encoding='utf8').read().replace('</script>', '<\\/script>')
out = (open(S('src', 'index.tpl.html'), encoding='utf8').read().replace('/*CSS*/', rd('style.css')).replace('/*DATA*/', data.replace('</script>', '<\\/script>'))
       .replace('/*RUN*/', rd('run.js')).replace('/*CORE*/', rd('core.js')).replace('/*MAIN*/', rd('main.js')))
if '--test' in sys.argv:  # TEST-Version: eigener Speicherschlüssel (gleiche Adresse/Origin wie Produktiv!), Banner, Titel
    out = out.replace("const LS_KEY='python-trainer-v1';", "const LS_KEY='python-trainer-TEST-v1';").replace('<title>Python-Trainer</title>', '<title>TEST Python-Trainer</title>')
    out = out.replace('<div id="app"></div>', '<div style="background:#b3261e;color:#fff;text-align:center;padding:4px;font-size:13px;margin:0 -16px">TESTVERSION – eigene Daten, nicht die der Kinder</div><div id="app"></div>')
open(S('python-trainer.html'), 'w', encoding='utf8').write(out)
print('python-trainer.html', len(out) // 1024, 'KB')
