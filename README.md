# Python-Trainer

Browser-App zum Üben von Python: Aufgaben (Ausgabe vorhersagen, Lückencode, Fehler finden, Zeilen ordnen, selbst programmieren) mit echtem Python im Browser (Pyodide), Fortschritt je Kind, Spickzettel, Spielwiese, Eltern-Bereich. Adressen: `http://192.168.4.44/python/` (Test: `/python-test/`).

Bauen: `python3 build.py` (prüft vorher die Daten). Aufgaben ändern: `tools/pipeline/aufgaben_quelle.py`, dann `python3 tools/pipeline/aufgaben_quelle.py && python3 tools/test_aufgaben.py`.
