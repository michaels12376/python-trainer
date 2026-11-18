#!/bin/sh
# Baut den Python-Trainer aus src/ + daten/ und stellt ihn live (Sicherung der alten Version in releases/).
set -e
cd /opt/python-src
python3 build.py
mkdir -p releases
[ -f /opt/python-trainer/python-trainer.html ] && cp /opt/python-trainer/python-trainer.html releases/python-trainer-$(date +%Y%m%d-%H%M%S).html
cp python-trainer.html /opt/python-trainer/.python-trainer.html.new
mv /opt/python-trainer/.python-trainer.html.new /opt/python-trainer/python-trainer.html
echo "live: http://192.168.4.44/python/"
