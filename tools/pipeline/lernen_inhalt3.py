# ===== Kapitel 7: Funktionen =====
lesson('l24', 7, 'Eigene Funktionen: def und Aufruf', 5, [
 ('t', '<p>Eine <b>Funktion</b> ist ein benannter Programmteil, den du immer wieder benutzen kannst – wie ein Rezept, das du nur einmal aufschreibst und dann beliebig oft kochst. Du kennst schon eingebaute Funktionen: <code>print</code>, <code>len</code>, <code>input</code>. Jetzt baust du eigene.</p>'),
 ('c', 'def hallo():\n    print("Hallo!")\n    print("Schön, dich zu sehen.")\n\nhallo()\nhallo()'),
 ('t', '<p><code>def</code> („define“, festlegen) <b>legt die Funktion nur fest</b> – ausgeführt wird sie erst, wenn du sie <b>aufrufst</b>: <code>hallo()</code>. Du kannst sie beliebig oft aufrufen.</p><p>Aufbau: <code>def name():</code> – mit Doppelpunkt – und darunter der <b>eingerückte</b> Funktionskörper.</p>'),
 ('c', 'def zeige_rahmen():\n    print("**********")\n\nzeige_rahmen()\nprint("Mitte")\nzeige_rahmen()'),
 ('warn', '<b>Reihenfolge:</b> Die Funktion muss <b>vor</b> dem Aufruf definiert sein. Und vergiss nicht die Klammern beim Aufruf: <code>hallo</code> ohne <code>()</code> ruft nichts auf.'),
 ('tip', '<b>Warum Funktionen?</b> Du schreibst etwas nur einmal, vermeidest Wiederholungen und kannst Programme in kleine, verständliche Teile zerlegen.'),
], [
 ('Wann wird der Code in einer Funktion ausgeführt?', ['Sobald die def-Zeile steht', 'Wenn die Funktion aufgerufen wird', 'Nie'], 1, 'def legt sie nur fest, der Aufruf führt sie aus.'),
 ('Was steht hinter dem Kopf einer Funktion <code>def hallo()</code>?', ['Ein Doppelpunkt', 'Ein Semikolon', 'Nichts'], 0, 'Wie bei if und for: Doppelpunkt und dann eingerückt.'),
 ('Wie ruft man <code>hallo</code> auf?', ['hallo', 'hallo()', 'def hallo()'], 1, 'Mit Klammern.'),
], ['a106', 'a112', 'a115', 'a120'])

lesson('l25', 7, 'Parameter: Funktionen etwas mitgeben', 5, [
 ('t', '<p>Eine Funktion wird flexibler, wenn du ihr beim Aufruf etwas <b>mitgibst</b>. Das schreibst du in die Klammern – als <b>Parameter</b>:</p>'),
 ('c', 'def gruss(name):\n    print("Hallo", name)\n\ngruss("Felix")\ngruss("Sophia")'),
 ('t', '<p>Der Parameter <code>name</code> ist eine Variable, die nur in der Funktion lebt; beim Aufruf bekommt sie den Wert in den Klammern (das <b>Argument</b>). Du kannst auch <b>mehrere</b> Parameter angeben – beim Aufruf in der gleichen Reihenfolge:</p>'),
 ('c', 'def vorstellen(name, alter):\n    print(name, "ist", alter, "Jahre alt")\n\nvorstellen("Felix", 13)\nvorstellen("Sophia", 11)'),
 ('t', '<p><b>Standardwerte:</b> Einem Parameter kannst du einen Wert „für den Notfall“ geben. Lässt man ihn beim Aufruf weg, gilt der Standardwert:</p>'),
 ('c', 'def potenz(basis, exponent=2):\n    print(basis ** exponent)\n\npotenz(5)\npotenz(2, 10)'),
 ('warn', '<b>TypeError:</b> Ruft man eine Funktion mit der falschen Anzahl Argumente auf (<code>vorstellen("Felix")</code> bei zwei Parametern), meldet Python einen Fehler: Es fehlt ein Argument.'),
], [
 ('Was ist <code>name</code> in <code>def gruss(name):</code>?', ['Ein Parameter', 'Eine Liste', 'Ein Text'], 0, 'Parameter stehen in der Klammer der def-Zeile.'),
 ('Was passiert bei <code>def f(a, b):</code> und dem Aufruf <code>f(1)</code>?', ['Ein Fehler (Argument fehlt)', 'b wird 0', 'Es funktioniert normal'], 0, 'Ohne Standardwert müssen alle Parameter angegeben werden.'),
 ('Was gibt <code>def potenz(b, e=2)</code> bei <code>potenz(3)</code> zurück/aus?', ['3 hoch 2 = 9', '3 hoch 3', 'Fehler'], 0, 'e hat den Standardwert 2.'),
], ['a107', 'a110', 'a114', 'a117', 'a118', 'a122'])

lesson('l26', 7, 'return: Ergebnisse zurückgeben', 6, [
 ('t', '<p>Funktionen können nicht nur etwas ausgeben, sondern auch ein <b>Ergebnis zurückliefern</b>. Das macht <code>return</code>. Das Ergebnis kannst du speichern oder weiterverwenden:</p>'),
 ('c', 'def quadrat(x):\n    return x * x\n\nprint(quadrat(5))\nergebnis = quadrat(4) + quadrat(3)\nprint(ergebnis)'),
 ('t', '<p><b>print oder return?</b> <code>print</code> <i>zeigt</i> etwas auf dem Bildschirm an – danach ist es weg. <code>return</code> <i>gibt</i> den Wert an die Stelle, wo die Funktion aufgerufen wurde – dort kannst du damit weiterrechnen.</p>'),
 ('c', 'def f_print(x):\n    print(x + 1)\n\ndef f_return(x):\n    return x + 1\n\na = f_print(5)\nb = f_return(5)\nprint("a ist", a)\nprint("b ist", b)'),
 ('t', '<p>Eine Funktion ohne <code>return</code> liefert den Wert <code>None</code> („nichts“) zurück – damit kann man nicht rechnen (<code>None + 1</code> ist ein <code>TypeError</code>).</p>'),
 ('t', '<p><b>return beendet die Funktion sofort.</b> Das nutzt man oft mit <code>if</code>:</p>'),
 ('c', 'def groesser(a, b):\n    if a > b:\n        return a\n    return b\n\nprint(groesser(3, 9))\nprint(groesser(10, 4))'),
 ('t', '<p>Auch Wahrheitswerte kann man zurückgeben – praktisch für Fragen:</p>'),
 ('c', 'def ist_gerade(zahl):\n    return zahl % 2 == 0\n\nprint(ist_gerade(4))\nprint(ist_gerade(7))'),
 ('tip', '<b>Faustregel:</b> Soll die Funktion nur etwas anzeigen → <code>print</code>. Soll sie ein Ergebnis liefern, mit dem man weiterarbeitet → <code>return</code>.'),
], [
 ('Was liefert eine Funktion ohne <code>return</code> zurück?', ['0', 'None', 'Einen Fehler'], 1, 'Der Wert None – „nichts“.'),
 ('Wann sollte eine Funktion <code>return</code> benutzen?', ['Wenn sie nur etwas anzeigt', 'Wenn man mit dem Ergebnis weiterrechnen will', 'Nie'], 1, 'return gibt den Wert zurück, print zeigt ihn nur an.'),
 ('Was passiert nach einem <code>return</code> in der Funktion?', ['Sie läuft weiter', 'Sie wird sofort beendet', 'Das Programm stoppt'], 1, 'return beendet die Funktion und gibt den Wert zurück.'),
], ['a108', 'a109', 'a113', 'a116', 'a121', 'a123'])

lesson('l27', 7, 'Lokale Variablen und Funktionen planen', 5, [
 ('t', '<p>Variablen, die du <b>in</b> einer Funktion anlegst (und die Parameter), sind <b>lokal</b>: Sie leben nur, solange die Funktion läuft. Außerhalb kennt Python sie nicht.</p>'),
 ('c', 'x = 10\n\ndef f():\n    x = 5          # ein neues, lokales x\n    return x\n\nprint(f())\nprint(x)'),
 ('t', '<p>Das x in der Funktion und das x draußen sind <b>zwei verschiedene Variablen</b>. Das ist gut so: Du kannst in jeder Funktion beliebige Namen benutzen, ohne dass sich Funktionen gegenseitig stören.</p>'),
 ('c', 'def addiere(a, b):\n    summe = a + b\n    return summe\n\nprint(addiere(3, 4))\nprint(summe)', [], 'fehler'),
 ('t', '<p>Die letzte Zeile gibt einen <b>NameError</b>: <code>summe</code> gibt es nur in der Funktion. Willst du ein Ergebnis nach draußen holen, benutze <code>return</code>.</p>'),
 ('t', '<p><b>Funktionen planen – so gehst du vor:</b></p><ol><li>Was soll reinkommen (Parameter)? Was soll rauskommen (<code>return</code>)?</li><li>Beispiele von Hand durchrechnen: <code>fakultaet(4)</code> ist 4 · 3 · 2 · 1 = 24.</li><li>Funktion schreiben und mit mehreren Aufrufen <b>testen</b> – auch mit Sonderfällen wie 0 oder 1.</li></ol>'),
 ('c', 'def fakultaet(n):\n    ergebnis = 1\n    for i in range(1, n + 1):\n        ergebnis = ergebnis * i\n    return ergebnis\n\nprint(fakultaet(4))\nprint(fakultaet(5))\nprint(fakultaet(0))'),
], [
 ('Was passiert bei <code>print(summe)</code> außerhalb der Funktion, wenn <code>summe</code> nur in der Funktion angelegt wurde?', ['Es wird der Wert ausgegeben', 'NameError', 'Es wird 0 ausgegeben'], 1, 'Lokale Variablen kennt man nur in der Funktion.'),
 ('Wie holst du ein Ergebnis aus einer Funktion heraus?', ['Mit return', 'Mit global print', 'Gar nicht'], 0, 'return gibt den Wert zurück.'),
], ['a111', 'a119', 'a124', 'a125'])

# ===== Kapitel 8: Texte bearbeiten =====
lesson('l28', 8, 'Texte sind Folgen von Zeichen', 5, [
 ('t', '<p>Ein Text (<code>str</code>) besteht aus einzelnen <b>Zeichen</b> – und funktioniert ganz ähnlich wie eine Liste: Du kannst die Länge abfragen, einzelne Zeichen über den <b>Index</b> holen (ab 0!) und mit <code>for</code> jedes Zeichen durchgehen.</p>'),
 ('c', 'wort = "Python"\nprint(len(wort))\nprint(wort[0])\nprint(wort[3])\nprint(wort[-1])'),
 ('c', 'for buchstabe in "Hallo":\n    print(buchstabe)'),
 ('t', '<p>Auch Leerzeichen und Satzzeichen sind Zeichen – <code>len("Hallo Welt")</code> ist 10.</p><p>Damit lässt sich viel anfangen: Zeichen zählen, Wörter umdrehen, Buchstaben suchen.</p>'),
 ('c', 'wort = "Zebra"\numgekehrt = ""\nfor b in wort:\n    umgekehrt = b + umgekehrt\nprint(umgekehrt)'),
 ('t', '<p>Mit <code>in</code> prüfst du, ob ein Zeichen (oder Teiltext) enthalten ist:</p>'),
 ('c', 'print("a" in "Banane")\nprint("x" in "Banane")\nprint("nan" in "Banane")'),
 ('warn', '<b>Index-Falle:</b> Das letzte Zeichen hat den Index <code>len(wort) - 1</code>, nicht <code>len(wort)</code>. Kürzer und sicherer: <code>wort[-1]</code>.'),
], [
 ('Was ist <code>"Katze"[1]</code>?', ['K', 'a', 't'], 1, 'Index 1 ist das zweite Zeichen.'),
 ('Was ist <code>len("Hi du")</code>?', ['4', '5', '2'], 1, 'Auch das Leerzeichen zählt als Zeichen.'),
 ('Wie holst du den letzten Buchstaben von <code>wort</code>?', ['wort[len(wort)]', 'wort[-1]', 'wort[last]'], 1, 'Der Index -1 ist das letzte Zeichen.'),
], ['a126', 'a127', 'a134', 'a137', 'a138'])

lesson('l29', 8, 'Ausschnitte im Text – und Texte lassen sich nicht ändern', 5, [
 ('t', '<p>Wie bei Listen holst du mit <code>text[a:b]</code> einen <b>Ausschnitt</b>: ab Index <code>a</code> bis <b>vor</b> Index <code>b</code>.</p>'),
 ('c', 'wort = "Programmieren"\nprint(wort[0:4])\nprint(wort[4:])\nprint(wort[:3])\nprint(wort[-3:])'),
 ('t', '<p>Rückwärts: <code>text[::-1]</code> dreht einen Text um.</p>'),
 ('c', 'print("Python"[::-1])'),
 ('warn', '<b>Texte sind unveränderlich!</b> Du kannst ein einzelnes Zeichen nicht überschreiben – <code>wort[0] = "J"</code> gibt einen <b>TypeError</b>. Stattdessen baust du einen <b>neuen Text</b> zusammen:'),
 ('c', 'wort = "Hallo"\nwort = "J" + wort[1:]\nprint(wort)'),
 ('t', '<p>Texte lassen sich mit <code>+</code> verketten und mit einer Zahl vervielfachen:</p>'),
 ('c', 'print("Ha" + "llo")\nprint("ha" * 3)\nprint("-" * 20)'),
], [
 ('Was ist <code>"Schule"[1:4]</code>?', ['chu', 'chul', 'Sch'], 0, 'Index 1, 2 und 3: c, h, u.'),
 ('Wie änderst du das erste Zeichen von <code>"Hallo"</code> in ein J?', ['wort[0] = "J"', 'wort = "J" + wort[1:]', 'wort.change("J")'], 1, 'Text lässt sich nicht ändern – man baut einen neuen.'),
 ('Was ergibt <code>"ab" * 3</code>?', ['ababab', 'ab3', 'Fehler'], 0, 'Text mal Zahl wiederholt den Text.'),
], ['a129', 'a135', 'a141'])

lesson('l30', 8, 'Textmethoden: upper, lower, count, replace', 5, [
 ('t', '<p>Texte haben viele nützliche <b>Methoden</b> (Funktionen, die man mit Punkt hinter den Text schreibt). Die wichtigsten:</p>'),
 ('c', 'text = "Hallo Welt"\nprint(text.upper())\nprint(text.lower())\nprint(len(text))'),
 ('c', 'print("Mississippi".count("s"))\nprint("Banane".replace("a", "o"))\nprint("  Hallo  ".strip())'),
 ('t', '<table class="gt"><tr><td><code>text.upper()</code></td><td>alles groß</td></tr><tr><td><code>text.lower()</code></td><td>alles klein</td></tr><tr><td><code>text.count("a")</code></td><td>wie oft kommt "a" vor?</td></tr><tr><td><code>text.replace("a", "o")</code></td><td>ersetzt jedes a durch o</td></tr><tr><td><code>text.strip()</code></td><td>entfernt Leerzeichen am Rand</td></tr></table>'),
 ('t', '<p><b>Groß-/Kleinschreibung vergleichen:</b> <code>"JA" == "ja"</code> ist falsch. Wandle vorher mit <code>lower()</code> um – dann ist es egal, wie der Benutzer tippt:</p>'),
 ('c', 'eingabe = "JA"\nif eingabe.lower() == "ja":\n    print("ok")\nelse:\n    print("nein")'),
 ('warn', 'Methoden <b>verändern den Text nicht</b>, sondern liefern einen neuen. <code>text.upper()</code> allein ändert nichts – speichere das Ergebnis: <code>text = text.upper()</code> oder gib es direkt mit <code>print</code> aus.'),
], [
 ('Was gibt <code>"Hallo".upper()</code> zurück?', ['hallo', 'HALLO', 'Hallo'], 1, 'upper macht alles groß.'),
 ('Was liefert <code>"banane".count("n")</code>?', ['1', '2', '3'], 1, 'Zwei n: ba-n-a-n-e.'),
 ('Warum ist <code>text.lower()</code> beim Vergleichen nützlich?', ['Damit Groß-/Kleinschreibung egal ist', 'Damit der Text kürzer wird', 'Damit der Text sortiert wird'], 0, 'Beide Seiten in Kleinbuchstaben – dann stimmt der Vergleich unabhängig von der Schreibweise.'),
], ['a128', 'a130', 'a132', 'a133', 'a136', 'a140', 'a142'])

lesson('l31', 8, 'split, join und Muster mit Texten', 6, [
 ('t', '<p><code>split()</code> zerlegt einen Text in eine <b>Liste von Wörtern</b> (getrennt an Leerzeichen). <code>"-".join(liste)</code> macht den umgekehrten Weg.</p>'),
 ('c', 'satz = "ich lerne python gern"\nwoerter = satz.split()\nprint(woerter)\nprint(len(woerter))\nprint(woerter[2])\nprint("-".join(woerter))'),
 ('t', '<p>So zählst du <b>Wörter</b>: <code>len(satz.split())</code>.</p><p><b>Vokale zählen</b> verbindet vieles aus diesem Kapitel: eine Schleife über die Zeichen, ein <code>if</code> mit <code>in</code> und ein Zähler.</p>'),
 ('c', 'satz = input().lower()\nanzahl = 0\nfor b in satz:\n    if b in "aeiou":\n        anzahl += 1\nprint(anzahl)', ['Hallo Welt']),
 ('t', '<p>Ein <b>Palindrom</b> liest sich vorwärts und rückwärts gleich („Anna“, „Otto“). Prüfen: Text kleinschreiben und mit dem umgedrehten vergleichen.</p>'),
 ('c', 'wort = "Anna".lower()\nif wort == wort[::-1]:\n    print("Palindrom")\nelse:\n    print("kein Palindrom")'),
 ('tip', '<b>Merke:</b> Texte durchlaufen (for), Zeichen prüfen (in), zählen (Zähler), umdrehen ([::-1]), zerlegen (split), zusammenfügen (join). Mit diesen Bausteinen löst du die meisten Textaufgaben.'),
], [
 ('Was liefert <code>"a b c".split()</code>?', ['["a", "b", "c"]', '"abc"', '3'], 0, 'split zerlegt an Leerzeichen in eine Liste.'),
 ('Wie zählst du die Wörter in <code>satz</code>?', ['len(satz)', 'len(satz.split())', 'satz.count()'], 1, 'Zerlegen und dann die Anzahl der Elemente zählen.'),
 ('Wie prüfst du, ob <code>w</code> ein Palindrom ist?', ['w == w[::-1]', 'w == w[0]', 'w in w'], 0, 'Der umgedrehte Text muss dem Original gleichen.'),
], ['a131', 'a139', 'a143', 'a144'])

# ===== Kapitel 9: Dictionaries =====
lesson('l32', 9, 'Dictionaries: Schlüssel und Werte', 5, [
 ('t', '<p>Ein <b>Dictionary</b> (Wörterbuch) speichert <b>Paare</b>: zu einem <b>Schlüssel</b> gehört ein <b>Wert</b> – wie in einem Telefonbuch (Name → Nummer) oder Vokabelheft (Wort → Übersetzung). Es steht in <b>geschweiften Klammern</b>, die Paare haben die Form <code>schlüssel: wert</code>.</p>'),
 ('c', 'alter = {"Felix": 13, "Sophia": 11}\nprint(alter)\nprint(alter["Felix"])\nprint(alter["Sophia"])'),
 ('t', '<p>In Listen suchst du über die Nummer (Index), im Dictionary über den <b>Schlüssel</b>. Das ist praktisch, wenn die Nummer keine Bedeutung hat – oder wenn du „nachschlagen“ willst.</p>'),
 ('c', 'englisch = {"Hund": "dog", "Katze": "cat", "Haus": "house"}\nprint(englisch["Katze"])'),
 ('tip', '<b>Merke:</b> <code>{ }</code> mit <code>schlüssel: wert</code> · Wert holen: <code>d[schlüssel]</code> · Ein leeres Dictionary ist <code>{}</code>. Schlüssel sind eindeutig – jeder Schlüssel kommt nur einmal vor.'),
 ('t', '<p>Als Schlüssel nimmt man meist Texte oder Zahlen; als Werte ist (fast) alles erlaubt – auch Listen:</p>'),
 ('c', 'noten = {"Mathe": [2, 1, 3], "Latein": [1, 2]}\nprint(noten["Mathe"])\nprint(noten["Latein"][0])'),
], [
 ('Wie holst du den Wert zum Schlüssel <code>"Felix"</code> aus dem Dictionary <code>d</code>?', ['d(Felix)', 'd["Felix"]', 'd.Felix'], 1, 'Mit dem Schlüssel in eckigen Klammern.'),
 ('Welche Klammern benutzt man für ein Dictionary?', ['Geschweifte { }', 'Eckige [ ]', 'Runde ( )'], 0, 'Dictionaries stehen in geschweiften Klammern.'),
], ['a145', 'a151', 'a158'])

lesson('l33', 9, 'Einträge ändern, ergänzen und prüfen', 5, [
 ('t', '<p>Einen <b>neuen Eintrag</b> legst du an, indem du einem neuen Schlüssel einen Wert zuweist. Gibt es den Schlüssel schon, wird sein Wert <b>überschrieben</b>.</p>'),
 ('c', 'd = {"a": 1}\nd["b"] = 2        # neu\nd["a"] = 10       # überschrieben\nprint(d)'),
 ('t', '<p>Mit <code>in</code> prüfst du, ob ein <b>Schlüssel</b> vorhanden ist; <code>len</code> zählt die Einträge:</p>'),
 ('c', 'preise = {"Apfel": 2, "Birne": 3}\nprint("Apfel" in preise)\nprint("Kiwi" in preise)\nprint(len(preise))'),
 ('warn', '<b>KeyError:</b> Greifst du auf einen Schlüssel zu, den es nicht gibt, bricht Python mit einem KeyError ab. Auch Groß-/Kleinschreibung zählt: <code>d["felix"]</code> ist nicht <code>d["Felix"]</code>.'),
 ('c', 'alter = {"Felix": 13}\nprint(alter["felix"])', [], 'fehler'),
 ('t', '<p>Vorher prüfen verhindert den Fehler:</p>'),
 ('c', 'alter = {"Felix": 13}\nname = "felix"\nif name in alter:\n    print(alter[name])\nelse:\n    print("unbekannt")'),
], [
 ('Was passiert bei <code>d["x"] = 5</code>, wenn es den Schlüssel <code>"x"</code> schon gibt?', ['Fehler', 'Der alte Wert wird überschrieben', 'Es entsteht ein zweiter Eintrag'], 1, 'Jeder Schlüssel kommt nur einmal vor – der Wert wird ersetzt.'),
 ('Wie prüfst du, ob der Schlüssel <code>"a"</code> in <code>d</code> ist?', ['"a" in d', 'd.has("a")', 'd == "a"'], 0, 'Mit dem Operator in.'),
 ('Was löst <code>d["fehlt"]</code> aus, wenn es den Schlüssel nicht gibt?', ['None', 'Einen KeyError', 'Eine leere Zeile'], 1, 'Ein nicht vorhandener Schlüssel ist ein KeyError.'),
], ['a146', 'a147', 'a152', 'a154', 'a155'])

lesson('l34', 9, 'get, Schleifen und items', 5, [
 ('t', '<p><b>get</b> holt einen Wert – und liefert einen Ersatzwert (statt eines Fehlers), wenn der Schlüssel fehlt:</p>'),
 ('c', 'd = {"rot": 1, "gelb": 2}\nprint(d.get("rot"))\nprint(d.get("blau", 0))\nprint(d.get("blau"))'),
 ('t', '<p>Ohne Ersatzwert gibt <code>get</code> <code>None</code> zurück. Perfekt für ein <b>Telefonbuch</b> mit „unbekannt“:</p>'),
 ('c', 'nummern = {"Felix": "123", "Sophia": "456"}\nname = input()\nprint(nummern.get(name, "unbekannt"))', ['Anna']),
 ('t', '<p><b>Schleife über ein Dictionary:</b> Eine <code>for</code>-Schleife läuft über die <b>Schlüssel</b>:</p>'),
 ('c', 'noten = {"Mathe": 2, "Latein": 1}\nfor fach in noten:\n    print(fach, noten[fach])'),
 ('t', '<p>Mit <code>.items()</code> bekommst du <b>Schlüssel und Wert gleichzeitig</b>:</p>'),
 ('c', 'noten = {"Mathe": 2, "Latein": 1}\nfor fach, note in noten.items():\n    print(fach, "->", note)'),
 ('tip', '<b>Merke:</b> <code>d.get(k, ersatz)</code> = sicher nachschlagen · <code>for k in d</code> = alle Schlüssel · <code>for k, v in d.items()</code> = Schlüssel und Wert.'),
], [
 ('Was liefert <code>{"a": 1}.get("b", 0)</code>?', ['0', 'None', 'Einen Fehler'], 0, 'Den Ersatzwert, weil „b“ fehlt.'),
 ('Worüber läuft <code>for x in d</code>?', ['Über die Werte', 'Über die Schlüssel', 'Über Schlüssel und Werte'], 1, 'Standardmäßig über die Schlüssel.'),
 ('Welche Methode liefert Schlüssel und Wert zusammen?', ['d.items()', 'd.pairs()', 'd.all()'], 0, 'items() gibt Paare aus Schlüssel und Wert.'),
], ['a148', 'a149', 'a153', 'a157', 'a159', 'a160'])

lesson('l35', 9, 'Dictionary als Zähler', 5, [
 ('t', '<p>Ein sehr häufiges Muster: <b>zählen, wie oft etwas vorkommt</b> – etwa jeden Buchstaben in einem Wort. Das Dictionary merkt sich für jedes Zeichen den Zählerstand.</p>'),
 ('c', 'zaehler = {}\nfor b in "hallo":\n    if b in zaehler:\n        zaehler[b] += 1\n    else:\n        zaehler[b] = 1\nprint(zaehler)'),
 ('t', '<p>So funktioniert es: Kommt ein Buchstabe <b>zum ersten Mal</b> vor, gibt es noch keinen Schlüssel – wir legen ihn mit dem Wert 1 an. Kommt er wieder vor, erhöhen wir den Zähler.</p>'),
 ('warn', '<b>KeyError!</b> Ohne die Prüfung <code>if b in zaehler</code> würde <code>zaehler[b] += 1</code> beim ersten Vorkommen abstürzen – denn der Schlüssel existiert noch nicht.'),
 ('t', '<p>Danach kannst du die Zähler schön ausgeben:</p>'),
 ('c', 'zaehler = {"h": 1, "a": 1, "l": 2, "o": 1}\nfor b in zaehler:\n    print(b + ": " + str(zaehler[b]))'),
 ('tip', '<b>Merke:</b> „<b>if schlüssel in d</b>: erhöhen – <b>else</b>: mit 1 anlegen“. Mit <code>d.get(k, 0) + 1</code> geht es auch in einer Zeile: <code>d[k] = d.get(k, 0) + 1</code>.'),
 ('c', 'z = {}\nfor b in "banane":\n    z[b] = z.get(b, 0) + 1\nprint(z)'),
], [
 ('Warum braucht der Zähler die Prüfung <code>if b in zaehler</code>?', ['Damit es schneller läuft', 'Damit beim ersten Vorkommen kein KeyError entsteht', 'Weil Python es verlangt, auch wenn es nichts bringt'], 1, 'Der Schlüssel existiert beim ersten Mal noch nicht.'),
 ('Was steht in <code>z</code> nach <code>z = {}</code> und zweimal <code>z["a"] = z.get("a", 0) + 1</code>?', ['{"a": 1}', '{"a": 2}', '{}'], 1, 'Erst 0 + 1, dann 1 + 1.'),
], ['a150', 'a156', 'a161', 'a162'])

# ===== Kapitel 10: Mini-Projekte =====
lesson('l36', 10, 'Wie plant man ein Programm?', 5, [
 ('t', '<p>Aus vielen kleinen Bausteinen wird ein richtiges Programm. Aber wo fängst du an? So geht es Schritt für Schritt:</p><ol><li><b>Verstehen:</b> Was soll das Programm tun? Was kommt rein (Eingabe), was soll raus? Rechne ein Beispiel von Hand.</li><li><b>Zerlegen:</b> Welche Schritte sind nötig? (Einlesen → rechnen/prüfen → ausgeben)</li><li><b>Klein anfangen:</b> Schreibe den ersten Schritt, teste ihn mit „Ausprobieren“, dann den nächsten.</li><li><b>Prüfen:</b> Funktioniert es auch bei 0, 1, sehr großen Zahlen, leeren Eingaben?</li></ol>'),
 ('t', '<p><b>Beispiel Zahlenraten (Auswertung):</b> Die Geheimzahl ist 42. Das Programm liest einen Tipp ein und sagt, ob er zu klein, zu groß oder richtig ist.</p><p>Planung: einlesen → drei Fälle unterscheiden (kleiner, größer, gleich) → passenden Text ausgeben. Drei Fälle? Das sind <code>if</code>, <code>elif</code>, <code>else</code>:</p>'),
 ('c', 'tipp = int(input())\nif tipp < 42:\n    print("zu klein")\nelif tipp > 42:\n    print("zu groß")\nelse:\n    print("richtig")', ['10']),
 ('t', '<p><b>Beispiel Taschenrechner:</b> Zwei Zahlen und ein Rechenzeichen einlesen und das Ergebnis ausgeben. Das Rechenzeichen ist ein <b>Text</b> – vergleiche es mit <code>==</code>:</p>'),
 ('c', 'a = int(input())\nb = int(input())\nz = input()\nif z == "+":\n    print(a + b)\nelif z == "-":\n    print(a - b)\nelif z == "*":\n    print(a * b)\nelse:\n    print(a / b)', ['6', '3', '*']),
 ('tip', '<b>Tipp:</b> Teste dein Programm immer mit mehreren Eingaben – auch mit den „Randfällen“ (kleinste, größte, gleiche Werte). Die Aufgaben prüfen genau das!'),
], [
 ('Was ist der erste Schritt bei einer neuen Programmieraufgabe?', ['Sofort alles tippen', 'Verstehen, was rein- und rauskommt – am besten mit einem Beispiel von Hand', 'Eine Funktion mit dem Namen programm anlegen'], 1, 'Erst verstehen und ein Beispiel durchrechnen, dann programmieren.'),
 ('Warum sollte man mit mehreren Eingaben testen?', ['Weil Python sonst abstürzt', 'Damit Sonder- und Randfälle auffallen', 'Das ist unnötig'], 1, 'Viele Fehler zeigen sich nur bei besonderen Werten.'),
], ['a163', 'a164', 'a165', 'a166'])

lesson('l37', 10, 'Bewährte Muster', 5, [
 ('t', '<p>Viele Programme bestehen aus denselben <b>Mustern</b>, die du jetzt alle kennst. Hier die wichtigsten im Überblick:</p><p><b>Zähler:</b> zählt, wie oft etwas passiert.</p>'),
 ('c', 'anzahl = 0\nfor i in range(1, 51):\n    if i % 7 == 0:\n        anzahl += 1\nprint(anzahl)'),
 ('t', '<p><b>Merker (Flag):</b> eine Variable mit <code>True</code>/<code>False</code>, die sich merkt, ob etwas aufgetreten ist – z. B. beim Primzahltest: Hat die Zahl einen Teiler gefunden?</p>'),
 ('c', 'n = 13\nprim = True\nfor t in range(2, n):\n    if n % t == 0:\n        prim = False\nif prim:\n    print("Primzahl")\nelse:\n    print("keine Primzahl")'),
 ('t', '<p><b>Zwei Werte weiterschieben:</b> bei der Fibonacci-Folge ist jede Zahl die Summe der beiden davor:</p>'),
 ('c', 'a = 1\nb = 1\nfor i in range(8):\n    print(a, end=" ")\n    a, b = b, a + b\nprint()'),
 ('t', '<p><b>Mehrere Bedingungen:</b> FizzBuzz prüft zuerst den Fall „durch beide teilbar“:</p>'),
 ('c', 'for i in range(1, 16):\n    if i % 15 == 0:\n        print("FizzBuzz")\n    elif i % 3 == 0:\n        print("Fizz")\n    elif i % 5 == 0:\n        print("Buzz")\n    else:\n        print(i)'),
 ('tip', '<b>Quersumme, Zeichen zählen, Passwort prüfen …</b> – meist hilft: Text als Zeichenfolge durchlaufen (<code>for b in text:</code>) und einen Zähler/Merker nutzen.'),
], [
 ('Wofür braucht man einen „Merker“ (Flag)?', ['Um sich zu merken, ob etwas aufgetreten ist', 'Um Variablen zu löschen', 'Um die Schleife zu beschleunigen'], 0, 'Er wird auf True/False gesetzt, wenn ein Ereignis vorkommt.'),
 ('Warum steht bei FizzBuzz der Fall „durch 15 teilbar“ zuerst?', ['Weil 15 die größte Zahl ist', 'Weil sonst schon der Fall „durch 3“ greift und die Kette endet', 'Das ist beliebig'], 1, 'Bei elif-Ketten gewinnt der erste passende Zweig – der allgemeinste Fall muss vorne stehen.'),
], ['a167', 'a168', 'a169', 'a170', 'a171', 'a173'])

lesson('l38', 10, 'Fehler suchen und Programme überdenken', 5, [
 ('t', '<p>Auch geübte Programmierer machen Fehler – wichtig ist, sie systematisch zu finden („Debugging“). Es gibt zwei Sorten:</p><ul><li><b>Fehlermeldung:</b> Python bricht ab und sagt dir Zeile und Fehlerart (<code>SyntaxError</code>, <code>NameError</code>, <code>TypeError</code>, <code>IndexError</code>, <code>KeyError</code> …).</li><li><b>Falsches Ergebnis ohne Fehlermeldung:</b> Das Programm läuft, tut aber nicht, was du willst. Hier musst du selbst nachdenken.</li></ul>'),
 ('t', '<p><b>Trick 1: Zwischenwerte ausgeben.</b> Baue <code>print</code> ein, um zu sehen, was in den Variablen steht:</p>'),
 ('c', 'n = 5\nergebnis = 0\nfor i in range(1, n + 1):\n    ergebnis = ergebnis * i\n    print("i =", i, "ergebnis =", ergebnis)\nprint(ergebnis)'),
 ('t', '<p>Man sieht sofort: <code>ergebnis</code> bleibt immer 0 – weil das Produkt mit <b>0</b> startet. Es muss mit <b>1</b> beginnen.</p>'),
 ('t', '<p><b>Trick 2: Beispiel von Hand durchrechnen</b> und mit der Ausgabe vergleichen. <b>Trick 3: Verdächtige Stellen prüfen</b> – häufige Fehlerquellen sind:</p><ul><li>falscher Startwert (0 statt 1)</li><li>„Eins daneben“ bei <code>range</code> (Ende nicht erreicht)</li><li><code>=</code> statt <code>==</code></li><li>falsche Einrückung (gehört die Zeile in die Schleife?)</li><li>Eingaben nicht umgewandelt (<code>int()</code>)</li></ul>'),
 ('c', 'zahl = 5\nwhile zahl > 0:\n    print(zahl)\n    zahl = zahl - 1\nprint("Fertig")'),
 ('tip', '<b>Merke:</b> Bleibe ruhig, lies die Fehlermeldung, grenze die Fehlerstelle ein (mit <code>print</code>), ändere <b>eine</b> Sache und teste erneut. So wirst du schnell sicher.'),
], [
 ('Was hilft, wenn ein Programm ohne Fehlermeldung ein falsches Ergebnis liefert?', ['Zwischenwerte mit print ausgeben und ein Beispiel von Hand durchrechnen', 'Das Programm neu starten', 'Alles löschen und neu schreiben'], 0, 'So findest du heraus, wo die Werte vom Erwarteten abweichen.'),
 ('Womit startet man ein Produkt in einer Schleife?', ['0', '1', 'None'], 1, 'Mit 0 wäre das Ergebnis immer 0.'),
], ['a172', 'a174', 'a175', 'a176'])
