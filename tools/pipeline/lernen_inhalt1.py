# ===== Kapitel 1: Ausgabe mit print =====
lesson('l01', 1, 'Dein erstes Programm', 4, [
 ('t', '<p>Ein Programm ist eine Liste von Anweisungen, die der Computer <b>Zeile für Zeile von oben nach unten</b> ausführt. Die wichtigste Anweisung am Anfang heißt <code>print</code> – sie schreibt etwas auf den Bildschirm.</p>'),
 ('c', 'print("Hallo Welt!")'),
 ('t', '<p>Was du ausgeben willst, steht in <b>Klammern</b>. Ein Text braucht <b>Anführungszeichen</b> – am Anfang und am Ende. Die Anführungszeichen selbst werden nicht mit ausgegeben; sie zeigen Python nur, wo der Text anfängt und aufhört.</p>'),
 ('c', 'print("Ich lerne Python")\nprint("Das ist Zeile 2")\nprint("Und das Zeile 3")'),
 ('t', '<p>Jeder <code>print</code>-Befehl beginnt eine neue Zeile. Die Reihenfolge im Programm ist die Reihenfolge in der Ausgabe.</p>'),
 ('t', '<p><b>Kommentare:</b> Alles hinter einem <code>#</code> ignoriert Python. So kannst du dir Notizen in den Code schreiben.</p>'),
 ('c', '# Das hier liest Python nicht\nprint("Das schon")   # und das hier auch nicht'),
 ('tip', '<b>Merke:</b> <code>print("Text")</code> – Text in Anführungszeichen, alles in Klammern. Ändere die Beispiele oben ruhig ab und drücke „Ausführen“: Probieren ist das beste Lernen!'),
], [
 ('Was gibt <code>print("Hallo")</code> aus?', ['"Hallo" (mit Anführungszeichen)', 'Hallo', 'print Hallo'], 1, 'Die Anführungszeichen markieren nur den Text und werden nicht mit ausgegeben.'),
 ('In welcher Reihenfolge führt Python die Zeilen eines Programms aus?', ['von oben nach unten', 'von unten nach oben', 'in zufälliger Reihenfolge'], 0, 'Python arbeitet ein Programm Zeile für Zeile von oben nach unten ab.'),
 ('Was bewirkt ein <code>#</code> in einer Zeile?', ['Der Rest der Zeile wird ausgegeben', 'Der Rest der Zeile ist ein Kommentar und wird ignoriert', 'Das Programm wird beendet'], 1, 'Alles hinter # ist ein Kommentar – nur für Menschen gedacht.'),
], ['a001', 'a002', 'a006', 'a010', 'a011', 'a012'])

lesson('l02', 1, 'Text und Zahlen ausgeben', 4, [
 ('t', '<p>Mit <code>print</code> kannst du auch <b>Zahlen</b> ausgeben. Zahlen schreibst du <b>ohne</b> Anführungszeichen:</p>'),
 ('c', 'print(42)\nprint(3 + 4)\nprint("3 + 4")'),
 ('t', '<p>Schau dir die dritte Zeile an: <code>"3 + 4"</code> steht in Anführungszeichen, ist also nur ein <b>Text</b> – Python rechnet nicht, sondern gibt ihn einfach aus. Ohne Anführungszeichen rechnet Python erst aus (<code>3 + 4</code> wird zu <code>7</code>).</p>'),
 ('t', '<p><b>Mehrere Dinge in einer Zeile:</b> Trenne sie mit einem <b>Komma</b>. Python setzt dazwischen automatisch ein Leerzeichen.</p>'),
 ('c', 'print("Ich bin", 12, "Jahre alt")\nprint("Das Ergebnis ist", 6 * 7)'),
 ('tip', '<b>Merke:</b> Text → Anführungszeichen. Zahlen und Rechnungen → keine Anführungszeichen. Mit Komma verbindest du mehrere Teile in einer Ausgabe.'),
 ('t', '<p>Du kannst einfache (<code>\'</code>) oder doppelte (<code>"</code>) Anführungszeichen benutzen – nur am Anfang und Ende müssen es dieselben sein.</p>'),
 ('c', 'print(\'Das geht auch\')\nprint("Und so: \'Hallo\' in Anführungszeichen")'),
], [
 ('Was gibt <code>print("2 + 3")</code> aus?', ['5', '2 + 3', 'Fehler'], 1, 'In Anführungszeichen ist es ein Text – er wird unverändert ausgegeben.'),
 ('Was gibt <code>print("a", 5)</code> aus?', ['a5', 'a 5', '"a" 5'], 1, 'Das Komma setzt in der Ausgabe ein Leerzeichen zwischen die Teile.'),
 ('Was gibt <code>print(2 * 4)</code> aus?', ['2 * 4', '8', '24'], 1, 'Ohne Anführungszeichen wird gerechnet.'),
], ['a003'])

lesson('l03', 1, 'Zeilenumbruch, sep und end', 5, [
 ('t', '<p>Manchmal willst du den Standard von <code>print</code> verändern. Dafür gibt es <b>Sonderzeichen</b> und <b>Zusatzangaben</b>.</p>'),
 ('t', '<p><b>Zeilenumbruch im Text:</b> Die Zeichenfolge <code>\\n</code> bedeutet „neue Zeile“.</p>'),
 ('c', 'print("Erste Zeile\\nZweite Zeile\\nDritte Zeile")'),
 ('t', '<p><b>sep</b> (englisch „separator“, Trenner) legt fest, was zwischen den Teilen steht – normalerweise ein Leerzeichen:</p>'),
 ('c', 'print("a", "b", "c")\nprint("a", "b", "c", sep="-")\nprint("a", "b", "c", sep="")'),
 ('t', '<p><b>end</b> legt fest, was <i>am Ende</i> der Ausgabe steht – normalerweise ein Zeilenumbruch. Wenn du etwas anderes angibst, geht die nächste Ausgabe in <b>derselben Zeile</b> weiter:</p>'),
 ('c', 'print("Eins", end=" ")\nprint("Zwei", end=" ")\nprint("Drei")\nprint("Vier")'),
 ('warn', '<b>Achtung:</b> <code>sep=</code> und <code>end=</code> stehen immer <b>hinter</b> den Dingen, die ausgegeben werden, und nach einem Komma. Der Wert ist ein Text, also in Anführungszeichen.'),
 ('tip', '<b>Merke:</b> <code>\\n</code> = neue Zeile · <code>sep</code> = Trenner zwischen den Teilen · <code>end</code> = Ende der Ausgabe.'),
], [
 ('Wie viele Zeilen erzeugt <code>print("A\\nB")</code>?', ['1', '2', '3'], 1, '\\n ist ein Zeilenumbruch – es entstehen zwei Zeilen.'),
 ('Was gibt <code>print("x", "y", sep="+")</code> aus?', ['x y', 'x+y', 'xy+'], 1, 'sep ersetzt das Leerzeichen zwischen den Teilen durch +.'),
 ('Was passiert bei <code>print("Hallo", end="")</code> gefolgt von <code>print("Welt")</code>?', ['HalloWelt in einer Zeile', 'Hallo und Welt in zwei Zeilen', 'Fehler'], 0, 'end="" lässt den Zeilenumbruch weg – die nächste Ausgabe schließt direkt an.'),
], ['a004', 'a005', 'a007', 'a013', 'a014'])

lesson('l04', 1, 'Fehlermeldungen lesen', 4, [
 ('t', '<p>Fehler gehören zum Programmieren dazu – auch bei Profis! Wichtig ist, die <b>Fehlermeldung zu lesen</b>: Sie sagt dir, <b>was</b> falsch ist und in <b>welcher Zeile</b>.</p>'),
 ('t', '<p>Probiere es aus – dieses Programm hat einen Fehler (<code>Print</code> mit großem P):</p>'),
 ('c', 'Print("Hallo")', [], 'fehler'),
 ('t', '<p>Python unterscheidet <b>Groß- und Kleinschreibung</b>: <code>print</code> kennt es, <code>Print</code> nicht. Noch ein typischer Fehler – das Anführungszeichen am Ende fehlt:</p>'),
 ('c', 'print("Hallo)', [], 'fehler'),
 ('t', '<p>Die häufigsten Anfängerfehler:</p><ul><li>Groß-/Kleinschreibung falsch (<code>Print</code> statt <code>print</code>)</li><li>Anführungszeichen oder Klammer vergessen</li><li>Tippfehler im Namen</li><li>Doppelpunkt oder Einrückung vergessen (kommt später)</li></ul>'),
 ('tip', '<b>So gehst du vor:</b> 1. Fehlermeldung und Zeilennummer lesen. 2. Genau diese Zeile (und die davor) anschauen. 3. Verbessern und nochmal ausführen. Ein Programm läuft nie auf Anhieb fehlerfrei – das ist normal!'),
], [
 ('Python meldet einen Fehler in Zeile 3. Wo suchst du zuerst?', ['In Zeile 3 (und der Zeile davor)', 'Ganz am Anfang des Programms', 'Gar nicht – das ist ein Computerfehler'], 0, 'Die Zeilennummer zeigt dir, wo Python gestolpert ist. Oft liegt der Fehler dort oder direkt davor.'),
 ('Welcher Befehl ist richtig geschrieben?', ['Print("Hi")', 'print("Hi")', 'PRINT("Hi")'], 1, 'Der Befehl heißt print – komplett klein.'),
], ['a008', 'a009'])

# ===== Kapitel 2: Variablen und Rechnen =====
lesson('l05', 2, 'Variablen: Werte speichern', 5, [
 ('t', '<p>Eine <b>Variable</b> ist wie eine beschriftete Schublade: Du legst einen Wert hinein und holst ihn später über den Namen wieder heraus. Mit <code>=</code> legst du den Wert hinein (<b>Zuweisung</b>).</p>'),
 ('c', 'alter = 12\nname = "Felix"\nprint(name)\nprint(alter)\nprint(name, "ist", alter, "Jahre alt")'),
 ('t', '<p>Der Name steht <b>links</b>, der Wert <b>rechts</b>. Texte brauchen Anführungszeichen, Zahlen nicht. Beim <code>print</code> schreibst du den Variablennamen <b>ohne</b> Anführungszeichen – sonst würde der Name selbst als Text ausgegeben.</p>'),
 ('c', 'farbe = "blau"\nprint(farbe)\nprint("farbe")'),
 ('t', '<p><b>Variablen kann man verändern.</b> Rechts vom <code>=</code> wird zuerst gerechnet, dann wird das Ergebnis in der Variablen gespeichert:</p>'),
 ('c', 'punkte = 10\npunkte = punkte + 5\nprint(punkte)\npunkte = punkte * 2\nprint(punkte)'),
 ('t', '<p><b>Namen:</b> Buchstaben, Ziffern und <code>_</code> sind erlaubt; der Name darf nicht mit einer Ziffer beginnen und keine Leerzeichen enthalten. Wähle sprechende Namen (<code>alter</code> statt <code>a</code>). Groß-/Kleinschreibung zählt: <code>Alter</code> und <code>alter</code> sind verschiedene Variablen.</p>'),
 ('warn', '<b>Achtung:</b> Das Gleichheitszeichen heißt hier „bekommt den Wert“, nicht „ist gleich“. <code>x = x + 1</code> ist in Mathe unmöglich, in Python normal: nimm den alten Wert von x, addiere 1 und speichere es wieder in x.'),
], [
 ('Was gibt <code>x = 4</code> und danach <code>print(x + 1)</code> aus?', ['x + 1', '5', '41'], 1, 'x steht für den Wert 4, also wird 4 + 1 = 5 ausgegeben.'),
 ('Was gibt <code>a = 3</code>, dann <code>a = a * 2</code>, dann <code>print(a)</code> aus?', ['3', '6', '32'], 1, 'Erst wird a * 2 = 6 berechnet, dann in a gespeichert.'),
 ('Welcher Variablenname ist erlaubt?', ['2spieler', 'mein alter', 'mein_alter'], 2, 'Keine Ziffer am Anfang, keine Leerzeichen – der Unterstrich ist erlaubt.'),
], ['a015', 'a016', 'a024', 'a027', 'a029'])

lesson('l06', 2, 'Rechnen mit Python', 6, [
 ('t', '<p>Python ist ein mächtiger Taschenrechner. Die Rechenzeichen:</p><table class="gt"><tr><td><code>+</code></td><td>plus</td><td><code>7 + 2</code> → 9</td></tr><tr><td><code>-</code></td><td>minus</td><td><code>7 - 2</code> → 5</td></tr><tr><td><code>*</code></td><td>mal</td><td><code>7 * 2</code> → 14</td></tr><tr><td><code>/</code></td><td>geteilt (Kommazahl)</td><td><code>7 / 2</code> → 3.5</td></tr><tr><td><code>//</code></td><td>ganzzahlig geteilt</td><td><code>7 // 2</code> → 3</td></tr><tr><td><code>%</code></td><td>Rest der Division</td><td><code>7 % 2</code> → 1</td></tr><tr><td><code>**</code></td><td>Potenz</td><td><code>7 ** 2</code> → 49</td></tr></table>'),
 ('c', 'print(7 + 2, 7 - 2, 7 * 2)\nprint(7 / 2)\nprint(7 // 2)\nprint(7 % 2)\nprint(2 ** 10)'),
 ('t', '<p>Die <b>Division</b> hat zwei Gesichter: <code>/</code> liefert immer eine Kommazahl (mit <b>Punkt</b> geschrieben: <code>3.5</code>). <code>//</code> schneidet den Rest ab, und <code>%</code> liefert genau diesen Rest. Beispiel: Die 5 passt dreimal in die 17 (3 · 5 = 15), übrig bleibt 2. Also ist <code>17 // 5</code> gleich 3 und <code>17 % 5</code> gleich 2.</p>'),
 ('c', 'print(17 // 5)\nprint(17 % 5)\nprint(3 * 5 + 2)'),
 ('t', '<p><b>Punkt vor Strich</b> gilt auch in Python. Mit <b>Klammern</b> bestimmst du die Reihenfolge:</p>'),
 ('c', 'print(2 + 3 * 4)\nprint((2 + 3) * 4)\nprint(10 - 4 - 3)'),
 ('tip', '<b>Der %-Trick:</b> <code>zahl % 2 == 0</code> bedeutet „gerade“, <code>zahl % 10</code> ist die letzte Ziffer. Du wirst den Rest oft brauchen!'),
 ('c', 'laenge = 8\nbreite = 3\nflaeche = laenge * breite\numfang = 2 * (laenge + breite)\nprint("Fläche:", flaeche)\nprint("Umfang:", umfang)'),
], [
 ('Was ist <code>20 // 6</code>?', ['3', '3.33', '2'], 0, 'Ganzzahldivision: 6 passt dreimal in 20.'),
 ('Was ist <code>20 % 6</code>?', ['3', '2', '14'], 1, '20 = 3 · 6 + 2 – der Rest ist 2.'),
 ('Was ist <code>2 + 3 * 4</code>?', ['20', '14', '24'], 1, 'Punkt vor Strich: erst 3 * 4 = 12, dann 2 + 12.'),
 ('Was liefert <code>9 / 2</code>?', ['4', '4.5', '5'], 1, 'Der Schrägstrich / liefert immer eine Kommazahl.'),
], ['a017', 'a018', 'a019', 'a021', 'a022', 'a026', 'a028', 'a030', 'a031'])

lesson('l07', 2, 'Text einsetzen mit f-Strings', 4, [
 ('t', '<p>Oft willst du Variablen in einen Satz einbauen. Mit einem <b>f-String</b> (ein Text mit einem <code>f</code> vor dem ersten Anführungszeichen) setzt Python den Wert von Variablen ein, die du in <b>geschweifte Klammern</b> schreibst:</p>'),
 ('c', 'name = "Sophia"\nalter = 11\nprint(f"{name} ist {alter} Jahre alt.")'),
 ('t', '<p>In den Klammern darf auch eine Rechnung stehen:</p>'),
 ('c', 'a = 6\nb = 7\nprint(f"{a} mal {b} ist {a * b}")'),
 ('t', '<p>Ohne das <code>f</code> würde Python die Klammern einfach als Text ausgeben. Eine Alternative ist das Komma im <code>print</code> – der f-String ist aber übersichtlicher, wenn der Satz länger wird.</p>'),
 ('c', 'x = 5\nprint("x ist {x}")\nprint(f"x ist {x}")\nprint("x ist", x)'),
 ('warn', '<b>Achtung:</b> Mit <code>+</code> kann man Text und Zahl <b>nicht</b> verbinden: <code>"Alter: " + 12</code> gibt einen TypeError. Nimm ein Komma, einen f-String oder wandle die Zahl mit <code>str(12)</code> um (mehr dazu in Kapitel 3).'),
], [
 ('Was gibt <code>x = 3</code> und <code>print(f"Wert: {x}")</code> aus?', ['Wert: {x}', 'Wert: 3', 'Wert: x'], 1, 'Im f-String wird {x} durch den Wert von x ersetzt.'),
 ('Was fehlt, damit <code>print("Hallo {name}")</code> den Namen einsetzt?', ['Ein f vor dem Text', 'Ein Komma', 'Eckige Klammern'], 0, 'Erst das f vor dem Anführungszeichen macht den Text zum f-String.'),
], ['a020', 'a023', 'a025', 'a032'])

# ===== Kapitel 3: Eingabe und Datentypen =====
lesson('l08', 3, 'Eingaben mit input()', 4, [
 ('t', '<p>Bisher kennt dein Programm nur das, was im Code steht. Mit <code>input()</code> kann es etwas von der Person <b>fragen</b>, die es benutzt. Das Programm hält an, wartet auf die Eingabe und speichert sie in einer Variablen.</p>'),
 ('c', 'name = input()\nprint("Hallo", name)', ['Felix']),
 ('t', '<p>In der Aufgaben-App bekommst du die Eingaben vorgegeben (hier „Felix“). In der <b>Spielwiese</b> trägst du sie unter dem Editor ein, eine pro Zeile. Du darfst in die Klammern einen Fragetext schreiben: <code>input("Wie heißt du? ")</code>.</p>'),
 ('c', 'name = input("Wie heißt du? ")\nprint("Schön, dich zu sehen,", name)', ['Sophia']),
 ('t', '<p>Mehrere <code>input()</code>-Aufrufe lesen nacheinander mehrere Eingaben ein – die erste Eingabe gehört zum ersten <code>input</code>, die zweite zum zweiten usw.</p>'),
 ('c', 'vorname = input()\nnachname = input()\nprint(vorname, nachname)', ['Anna', 'Berg']),
 ('warn', '<b>Wichtig:</b> <code>input()</code> liefert <b>immer Text</b> – auch wenn jemand eine Zahl eintippt! Rechnen kann man damit erst nach einer Umwandlung (nächster Abschnitt).'),
], [
 ('Was macht <code>name = input()</code>?', ['Gibt name auf dem Bildschirm aus', 'Wartet auf eine Eingabe und speichert sie in name', 'Löscht die Variable name'], 1, 'input() liest eine Eingabe ein; die Zuweisung speichert sie.'),
 ('Welchen Typ hat das Ergebnis von <code>input()</code>?', ['Immer Text', 'Immer eine ganze Zahl', 'Das hängt von der Eingabe ab'], 0, 'input() gibt immer Text zurück, auch bei „42“.'),
], ['a033', 'a034', 'a039', 'a044', 'a045'])

lesson('l09', 3, 'Datentypen: Text, ganze Zahlen, Kommazahlen', 5, [
 ('t', '<p>Jeder Wert in Python hat einen <b>Typ</b>. Die wichtigsten drei:</p><table class="gt"><tr><td><code>int</code></td><td>ganze Zahl</td><td><code>5</code>, <code>-3</code>, <code>1000</code></td></tr><tr><td><code>float</code></td><td>Kommazahl (mit Punkt!)</td><td><code>5.0</code>, <code>3.14</code></td></tr><tr><td><code>str</code></td><td>Text (englisch „string“)</td><td><code>"5"</code>, <code>"Hallo"</code></td></tr></table>'),
 ('c', 'print(type(5))\nprint(type(5.0))\nprint(type("5"))'),
 ('t', '<p>Der Typ entscheidet, was ein Rechenzeichen tut. Mit Zahlen wird gerechnet – mit Text wird <b>aneinandergehängt</b>:</p>'),
 ('c', 'print(3 + 4)\nprint("3" + "4")\nprint("ha" * 3)'),
 ('t', '<p>Ein <code>"7"</code> in Anführungszeichen ist <b>kein</b> Zahlenwert, sondern ein Text, der zufällig aus einer Ziffer besteht. Das ist der Grund, warum eine eingelesene Zahl (die ja ein Text ist) nicht einfach zum Rechnen taugt.</p>'),
 ('tip', '<b>Merke:</b> Anführungszeichen = Text (<code>str</code>). Mit Punkt = Kommazahl (<code>float</code>). Sonst eine ganze Zahl (<code>int</code>). Mit <code>type(x)</code> kannst du den Typ jederzeit abfragen.'),
], [
 ('Welchen Typ hat <code>"12"</code>?', ['int', 'str', 'float'], 1, 'Wegen der Anführungszeichen ist es ein Text.'),
 ('Was ergibt <code>"3" + "4"</code>?', ['7', '34', 'Fehler'], 1, 'Bei Text bedeutet + aneinanderhängen: "34".'),
 ('Welchen Typ hat <code>2.0</code>?', ['int', 'str', 'float'], 2, 'Ein Punkt macht daraus eine Kommazahl (float).'),
], ['a036'])

lesson('l10', 3, 'Umwandeln mit int(), float(), str() und round()', 5, [
 ('t', '<p>Mit <b>Umwandlungsfunktionen</b> machst du aus einem Typ einen anderen:</p><ul><li><code>int(x)</code> – ganze Zahl</li><li><code>float(x)</code> – Kommazahl</li><li><code>str(x)</code> – Text</li></ul>'),
 ('c', 'print(int("7") + 1)\nprint(float("2.5") * 2)\nprint(str(12) + " Jahre")'),
 ('t', '<p><b>Der Standard-Trick für Eingaben:</b> Zahl einlesen und sofort umwandeln.</p>'),
 ('c', 'zahl = int(input())\nprint(zahl * 2)', ['21']),
 ('c', 'preis = float(input())\nprint(preis * 3)', ['1.5']),
 ('t', '<p><b>round(zahl, stellen)</b> rundet auf eine bestimmte Anzahl Nachkommastellen:</p>'),
 ('c', 'print(round(3.14159, 2))\nprint(round(2.5678, 1))\nprint(round(7.4))'),
 ('warn', '<b>Achtung:</b> <code>int("abc")</code> oder <code>int("3,5")</code> geht nicht – dann gibt es einen <b>ValueError</b>. Kommazahlen schreibt man in Python mit <b>Punkt</b>. Und <code>int(3.9)</code> ergibt <code>3</code> (Nachkommastellen werden abgeschnitten, nicht gerundet).'),
], [
 ('Wie liest du eine ganze Zahl ein?', ['zahl = input()', 'zahl = int(input())', 'zahl = str(input())'], 1, 'input() liefert Text, int() macht daraus eine ganze Zahl.'),
 ('Was gibt <code>round(3.14159, 2)</code> aus?', ['3.1', '3.14', '3.15'], 1, 'Auf zwei Nachkommastellen gerundet: 3.14.'),
 ('Was ergibt <code>int("7") + int("5")</code>?', ['12', '75', 'Fehler'], 0, 'Beide Texte werden in Zahlen umgewandelt und dann addiert.'),
], ['a035', 'a037', 'a038', 'a040', 'a046', 'a047', 'a048', 'a049'])

lesson('l11', 3, 'Typische Fehler mit Eingaben', 4, [
 ('t', '<p>Die zwei häufigsten Fehler bei Eingaben kommen beide vom Thema „<code>input()</code> liefert Text“.</p>'),
 ('t', '<p><b>Fehler 1: TypeError.</b> Text und Zahl lassen sich nicht addieren:</p>'),
 ('c', 'zahl = input()\nprint(zahl + 1)', ['5'], 'fehler'),
 ('t', '<p>Die Lösung: die Eingabe mit <code>int()</code> umwandeln.</p>'),
 ('c', 'zahl = int(input())\nprint(zahl + 1)', ['5']),
 ('t', '<p><b>Fehler 2: Es läuft, aber das Ergebnis ist komisch.</b> Zwei Eingaben werden als Text „addiert“ – also aneinandergehängt:</p>'),
 ('c', 'a = input()\nb = input()\nprint(a + b)', ['3', '4']),
 ('c', 'a = int(input())\nb = int(input())\nprint(a + b)', ['3', '4']),
 ('t', '<p><b>Fehler 3: Syntaxfehler</b> – z. B. das <code>+</code> beim Verbinden von Text vergessen:</p>'),
 ('c', 'name = input()\nprint("Hallo, " + name)', ['Felix']),
 ('tip', '<b>Merke:</b> Rechnest du mit einer Eingabe? Dann <code>int()</code> oder <code>float()</code>! Bei reinem Text brauchst du keine Umwandlung.'),
], [
 ('Du liest <code>a</code> und <code>b</code> mit <code>input()</code> ein und gibst <code>a + b</code> aus. Bei den Eingaben 3 und 4 erscheint …', ['7', '34', 'ein Fehler'], 1, 'Beide sind Text, + hängt sie aneinander.'),
 ('Wie bekommst du bei den Eingaben 3 und 4 das Ergebnis 7?', ['int vor jede Eingabe schreiben: int(input())', 'Ein Leerzeichen einfügen', 'print(a, b) benutzen'], 0, 'Beide Eingaben müssen in Zahlen umgewandelt werden.'),
], ['a041', 'a042', 'a043'])
