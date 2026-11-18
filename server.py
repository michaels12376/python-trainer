#!/usr/bin/env python3
"""Kleiner lokaler Server für den Python-Trainer.
Start:  python3 server.py            (Port 8000)   oder   python3 server.py 8080
Dann im Browser (auch iPad im selben WLAN):  http://<IP-des-Rechners>:8000
Fortschritt aller Nutzer wird in python-daten.json neben diesem Skript gespeichert."""
import http.server, json, os, re, shutil, socket, sys, threading, time
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'python-daten.json')
LOCK = threading.Lock()
BACKUPS = os.path.join(HERE, 'backups')
KEEP_DAYS = 30
OK_PATHS = ('/', '/python-trainer.html', '/api/state')
PYO_FILES = ('pyodide.js', 'pyodide.asm.js', 'pyodide.asm.wasm', 'python_stdlib.zip', 'pyodide-lock.json')

def daily_snapshot():
    """Legt pro Tag einmal eine Kopie der Lerndaten an (letzte 30 Tage bleiben erhalten)."""
    try:
        if not os.path.exists(DATA): return
        os.makedirs(BACKUPS, exist_ok=True)
        name = os.path.join(BACKUPS, 'python-daten-' + time.strftime('%Y-%m-%d') + '.json')
        if not os.path.exists(name): shutil.copy2(DATA, name)
        old = sorted(f for f in os.listdir(BACKUPS) if f.startswith('python-daten-'))[:-KEEP_DAYS]
        for f in old: os.remove(os.path.join(BACKUPS, f))
    except Exception: pass
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=HERE, **k)
    def log_message(s, *a): pass
    def end_headers(s):
        pth = s.path.split('?')[0]
        if pth.startswith('/pyodide/'): s.send_header('Cache-Control', 'public, max-age=604800')
        elif not pth.startswith('/api/'): s.send_header('Cache-Control', 'no-cache')  # App-Datei immer auf Aktualität prüfen (sonst zeigen Browser alte Versionen)
        super().end_headers()
    def _json(s, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode()
        s.send_response(code); s.send_header('Content-Type', 'application/json; charset=utf-8')
        s.send_header('Content-Length', str(len(b))); s.send_header('Cache-Control', 'no-store'); s.end_headers(); s.wfile.write(b)
    def do_GET(s):
        if s.path.split('?')[0] == '/api/state':
            with LOCK:
                try: d = json.load(open(DATA, encoding='utf8'))
                except Exception: d = {'v': 1, 'updated': 0, 'users': {}}
            return s._json(200, d)
        if s.path.split('?')[0] == '/api/build':  # Kennung der ausgelieferten App-Version (die App prüft damit, ob sie veraltet ist)
            try: b = re.search(r"const BUILD='(\d+)'", open(os.path.join(HERE, 'python-trainer.html'), encoding='utf8').read()).group(1)
            except Exception: b = ''
            return s._json(200, {'build': b})
        if s.path in ('/', ''): s.path = '/python-trainer.html'
        pp = s.path.split('?')[0]
        if pp.startswith('/pyodide/') and pp[len('/pyodide/'):] in PYO_FILES: return super().do_GET()  # Python (Pyodide) für die Übungen, lokal ausgeliefert
        if pp not in OK_PATHS: return s._json(404, {})  # nur die App selbst ausliefern
        return super().do_GET()
    def do_POST(s):
        if s.path.split('?')[0] != '/api/state': return s._json(404, {})
        n = int(s.headers.get('Content-Length', 0))
        try: d = json.loads(s.rfile.read(n))
        except Exception: return s._json(400, {'error': 'json'})
        if not isinstance(d, dict) or not isinstance(d.get('users'), dict): return s._json(400, {'error': 'format'})
        with LOCK:
            daily_snapshot()
            tmp = DATA + '.tmp'
            json.dump(d, open(tmp, 'w', encoding='utf8'), ensure_ascii=False)
            if os.path.exists(DATA): shutil.copy2(DATA, DATA + '.bak')
            os.replace(tmp, DATA)
        s._json(200, {'ok': True})
if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except Exception: ip = 'localhost'
    print(f'Python-Trainer läuft:  http://localhost:{port}   |   im WLAN: http://{ip}:{port}\nBeenden mit Strg+C')
    http.server.ThreadingHTTPServer(('0.0.0.0', port), H).serve_forever()
