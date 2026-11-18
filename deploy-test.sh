#!/bin/sh
# Baut die TEST-Version (Branch dev) und stellt sie unter /python-test/ bereit. Berührt NIE die Produktivdaten.
set -e
cd /opt/python-src-test
python3 build.py --test
cp python-trainer.html /opt/python-test/.new.html
mv /opt/python-test/.new.html /opt/python-test/python-trainer.html
# Schriften und Server-Skript im Laufzeitordner aktuell halten (Dienst nur bei geändertem server.py neu starten)
mkdir -p /opt/python-test/fonts && cp fonts/*.woff2 /opt/python-test/fonts/
if ! cmp -s server.py /opt/python-test/server.py; then cp server.py /opt/python-test/server.py; RESTART=1; fi
chown -R pytrainer:pytrainer /opt/python-test/fonts /opt/python-test/server.py /opt/python-test/python-trainer.html
[ -n "$RESTART" ] && systemctl restart python-trainer-test
echo "TEST live: http://192.168.4.44/python-test/"
