#!/bin/sh
# Baut die TEST-Version (Branch dev) und stellt sie unter /python-test/ bereit. Berührt NIE die Produktivdaten.
set -e
cd /opt/python-src-test
python3 build.py --test
cp python-trainer.html /opt/python-test/.new.html
mv /opt/python-test/.new.html /opt/python-test/python-trainer.html
echo "TEST live: http://192.168.4.44/python-test/"
