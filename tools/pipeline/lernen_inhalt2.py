# ===== Kapitel 4: Bedingungen =====
lesson('l12', 4, 'Vergleiche und Wahrheitswerte', 4, [
 ('t', '<p>Bisher hat dein Programm immer alle Zeilen ausgeführt. Mit <b>Bedingungen</b> entscheidet es selbst, was es tut. Dazu braucht es Fragen, auf die es mit „ja“ (<code>True</code>) oder „nein“ (<code>False</code>) antworten kann – <b>Vergleiche</b>:</p><table class="gt"><tr><td><code>==</code></td><td>gleich</td></tr><tr><td><code>!=</code></td><td>ungleich</td></tr><tr><td><code>&lt;</code> &nbsp; <code>&gt;</code></td><td>kleiner, größer</td></tr><tr><td><code>&lt;=</code> &nbsp; <code>&gt;=</code></td><td>kleiner/gleich, größer/gleich</td></tr></table>'),
 ('c', 'print(5 > 3)\nprint(5 == 6)\nprint(5 != 6)\nprint(4 <= 4)\nprint("a" == "a")'),
 ('t', '<p>Das Ergebnis eines Vergleichs ist ein <b>Wahrheitswert</b>: <code>True</code> (wahr) oder <code>False</code> (falsch).</p>'),
 ('warn', '<b>Der häufigste Fehler:</b> Ein <b>einzelnes</b> <code>=</code> speichert einen Wert in einer Variablen (<code>x = 5</code>). Zum <b>Vergleichen</b> brauchst du <b>zwei</b> Gleichheitszeichen: <code>x == 5</code>.'),
 ('c', 'x = 5\nprint(x == 5)\nprint(x == 6)\nprint(x > 10)'),
 ('t', '<p>Auch Texte kann man vergleichen – aber Groß-/Kleinschreibung zählt: <code>"Ja" == "ja"</code> ist <code>False</code>.</p>'),
], [
 ('Welches Zeichen prüft, ob zwei Werte gleich sind?', ['=', '==', '!='], 1, 'Zwei Gleichheitszeichen vergleichen; eins weist einen Wert zu.'),
 ('Was ergibt <code>7 != 7</code>?', ['True', 'False', 'Fehler'], 1, '!= bedeutet „ungleich“ – 7 ist aber gleich 7.'),
 ('Was ergibt <code>"Ja" == "ja"</code>?', ['True', 'False', 'Fehler'], 1, 'Groß- und Kleinschreibung zählen, die Texte sind verschieden.'),
], ['a051', 'a055', 'a059'])

lesson('l13', 4, 'if und else', 5, [
 ('t', '<p>Mit <code>if</code> („falls“) führst du Code nur aus, <b>wenn eine Bedingung stimmt</b>. Mit <code>else</code> („sonst“) legst du fest, was passiert, wenn sie nicht stimmt.</p>'),
 ('c', 'zahl = 12\nif zahl > 10:\n    print("groß")\nelse:\n    print("klein")'),
 ('t', '<p>Zwei Dinge sind entscheidend:</p><ol><li>Hinter der Bedingung (und hinter <code>else</code>) steht ein <b>Doppelpunkt</b>.</li><li>Was zum <code>if</code> oder <code>else</code> gehört, wird <b>eingerückt</b> (4 Leerzeichen, die Tab-Taste macht das). Die Einrückung ist in Python kein Schmuck – sie zeigt, was zusammengehört!</li></ol>'),
 ('c', 'zahl = 3\nif zahl > 10:\n    print("groß")\n    print("das ist auch im if-Block")\nprint("das läuft immer")'),
 ('t', '<p>Probiere <code>zahl = 3</code> und <code>zahl = 30</code> aus: Die zwei eingerückten Zeilen laufen nur bei 30, die letzte Zeile (nicht eingerückt) läuft immer.</p>'),
 ('t', '<p>Mit Eingaben wird es spannend – das Programm reagiert auf den Benutzer:</p>'),
 ('c', 'alter = int(input())\nif alter >= 18:\n    print("volljährig")\nelse:\n    print("minderjährig")', ['15']),
 ('warn', '<b>Typische Fehler:</b> Doppelpunkt vergessen · Einrückung vergessen · <code>=</code> statt <code>==</code> · ein <code>else</code>, das nicht auf der gleichen Höhe wie das <code>if</code> steht. Ein <code>print</code> <b>ohne</b> <code>else</code> läuft immer – nutze <code>else</code>, wenn nur eines von beiden passieren soll.'),
], [
 ('Welche Zeilen gehören zum if-Block?', ['Alle Zeilen darunter', 'Die direkt darunter, die eingerückt sind', 'Nur die erste Zeile darunter'], 1, 'Die Einrückung bestimmt, was zum Block gehört.'),
 ('Was steht hinter <code>if zahl > 3</code>?', ['Ein Semikolon', 'Ein Doppelpunkt', 'Nichts'], 1, 'Jede if-Zeile endet mit einem Doppelpunkt.'),
 ('Wann läuft der else-Zweig?', ['Immer', 'Wenn die if-Bedingung nicht stimmt', 'Wenn die Bedingung stimmt'], 1, 'else bedeutet „sonst“.'),
], ['a050', 'a056', 'a058', 'a060', 'a062'])

lesson('l14', 4, 'Mehrere Fälle mit elif', 4, [
 ('t', '<p>Manchmal gibt es mehr als zwei Möglichkeiten. Dann hängst du an das <code>if</code> beliebig viele <code>elif</code> („sonst falls“) an – und zum Schluss ein <code>else</code> für alles andere.</p>'),
 ('c', 'note = 2\nif note == 1:\n    print("sehr gut")\nelif note == 2:\n    print("gut")\nelif note == 3:\n    print("befriedigend")\nelse:\n    print("das üben wir noch")'),
 ('t', '<p><b>Wichtig:</b> Python prüft die Bedingungen <b>von oben nach unten</b> und führt nur den <b>ersten</b> passenden Zweig aus. Die restlichen werden übersprungen. Deshalb kommt es auf die <b>Reihenfolge</b> an:</p>'),
 ('c', 'alter = 14\nif alter < 12:\n    print("Kind")\nelif alter < 18:\n    print("Jugendlicher")\nelse:\n    print("Erwachsener")'),
 ('tip', '<b>Merke:</b> Immer von „klein nach groß“ (oder „streng nach eng“) prüfen. Beim Alter 14 ist <code>alter &lt; 18</code> auch wahr – aber der Zweig <code>alter &lt; 12</code> kam zuerst und war falsch, also landet 14 im zweiten Zweig.'),
 ('warn', 'Mehrere einzelne <code>if</code> (ohne <code>elif</code>) werden alle geprüft und können mehrfach ausgeführt werden. Mit <code>elif</code> wird höchstens ein Zweig genommen.'),
], [
 ('Bei <code>note = 1</code> und einer Kette if note == 1 / elif note <= 3 / else – welche Zweige laufen?', ['Nur der erste', 'Der erste und der zweite', 'Alle'], 0, 'Der erste passende Zweig wird ausgeführt, danach ist die Kette beendet.'),
 ('Wofür steht <code>elif</code>?', ['„sonst falls“ – eine weitere Bedingung', 'Das Ende des Programms', 'Eine Wiederholung'], 0, 'elif = else + if.'),
], ['a052', 'a063'])

lesson('l15', 4, 'and, or, not und der Rest-Trick', 5, [
 ('t', '<p>Mit <code>and</code>, <code>or</code> und <code>not</code> verknüpfst du Bedingungen:</p><ul><li><code>a and b</code> – <b>beide</b> müssen stimmen</li><li><code>a or b</code> – <b>mindestens eine</b> muss stimmen</li><li><code>not a</code> – das <b>Gegenteil</b></li></ul>'),
 ('c', 'zahl = 7\nprint(zahl > 5 and zahl < 10)\nprint(zahl < 5 or zahl > 20)\nprint(not zahl == 7)'),
 ('c', 'alter = 15\nif alter >= 12 and alter < 18:\n    print("Jugendlicher")\nelse:\n    print("kein Jugendlicher")'),
 ('t', '<p><b>Der Rest-Trick:</b> Mit <code>%</code> findest du heraus, ob eine Zahl durch eine andere teilbar ist: Bleibt Rest 0, geht es auf.</p>'),
 ('c', 'zahl = 14\nif zahl % 2 == 0:\n    print("gerade")\nelse:\n    print("ungerade")\nprint(zahl % 7 == 0)'),
 ('tip', '<b>Gerade:</b> <code>zahl % 2 == 0</code> · <b>durch 5 teilbar:</b> <code>zahl % 5 == 0</code> · <b>durch 3 und 5 teilbar:</b> <code>zahl % 3 == 0 and zahl % 5 == 0</code>.'),
 ('warn', 'Schreibe beide Seiten ganz aus: <code>zahl &gt; 5 and zahl &lt; 10</code> – nicht <code>zahl &gt; 5 and &lt; 10</code>. Bei zusammengesetzten Bedingungen helfen <b>Klammern</b>: <code>(a and b) or c</code>.'),
], [
 ('Wann ist <code>a and b</code> wahr?', ['Wenn mindestens eine wahr ist', 'Wenn beide wahr sind', 'Wenn keine wahr ist'], 1, 'and verlangt, dass beide Teile stimmen.'),
 ('Wie prüfst du, ob <code>x</code> gerade ist?', ['x / 2 == 0', 'x % 2 == 0', 'x // 2 == 0'], 1, 'Gerade Zahlen lassen beim Teilen durch 2 den Rest 0.'),
 ('Was ist <code>not (3 > 5)</code>?', ['True', 'False', 'Fehler'], 0, '3 > 5 ist False, not macht daraus True.'),
], ['a053', 'a054', 'a057', 'a061', 'a064', 'a065'])

# ===== Kapitel 5: Schleifen =====
lesson('l16', 5, 'for und range: Wiederholen', 5, [
 ('t', '<p>Willst du etwas mehrmals tun, schreibst du es nicht mehrmals auf – du benutzt eine <b>Schleife</b>. Die <code>for</code>-Schleife zählt mit:</p>'),
 ('c', 'for i in range(5):\n    print("Hallo", i)'),
 ('t', '<p>So liest du das: „Für jedes <code>i</code> aus <code>range(5)</code> mach Folgendes …“ Die Variable <code>i</code> bekommt nacheinander die Werte <code>0, 1, 2, 3, 4</code>. Wichtig: <code>range(5)</code> beginnt bei <b>0</b> und hört <b>vor</b> 5 auf – es sind also 5 Durchläufe.</p>'),
 ('t', '<p>Wieder gilt: Doppelpunkt hinter dem Schleifenkopf, und der <b>Schleifenkörper ist eingerückt</b>. Alles Eingerückte wird bei jedem Durchlauf wiederholt, die nicht eingerückte Zeile danach nur einmal:</p>'),
 ('c', 'for i in range(3):\n    print("Wiederholt!")\nprint("Fertig")'),
 ('t', '<p><b>Von 1 bis n:</b> Gib Start und Ende an: <code>range(1, 6)</code> liefert 1, 2, 3, 4, 5 – das Ende (6) gehört <b>nicht</b> mehr dazu.</p>'),
 ('c', 'for i in range(1, 6):\n    print(i)'),
 ('warn', '<b>Typischer Fehler:</b> „Von 1 bis 5“ heißt <code>range(1, 6)</code>, nicht <code>range(1, 5)</code>. Das Ende von range wird nie erreicht. Und: Vergisst du die Einrückung, meldet Python einen <b>IndentationError</b>.'),
], [
 ('Wie viele Durchläufe hat <code>for i in range(4)</code>?', ['3', '4', '5'], 1, 'i läuft von 0 bis 3 – das sind vier Werte.'),
 ('Welche Zahlen liefert <code>range(1, 4)</code>?', ['1, 2, 3', '1, 2, 3, 4', '0, 1, 2, 3'], 0, 'Start 1, das Ende 4 wird nicht mehr erreicht.'),
 ('Wie gibst du die Zahlen 1 bis 10 aus?', ['range(1, 10)', 'range(1, 11)', 'range(10)'], 1, 'Das Ende 11 wird nicht erreicht – also kommt 10 gerade noch dazu.'),
], ['a066', 'a067', 'a072', 'a075', 'a079', 'a080', 'a081'])

lesson('l17', 5, 'range mit Schrittweite', 3, [
 ('t', '<p><code>range</code> kann bis zu drei Angaben haben: <code>range(start, ende, schritt)</code>. Der Schritt sagt, um wie viel jedes Mal weitergezählt wird.</p>'),
 ('c', 'for i in range(0, 10, 2):\n    print(i)'),
 ('t', '<p>Mit einem <b>negativen Schritt</b> zählst du rückwärts – dann muss der Start größer sein als das Ende:</p>'),
 ('c', 'for i in range(10, 0, -3):\n    print(i)'),
 ('tip', '<b>Merke:</b> <code>range(10)</code> = 0 bis 9 · <code>range(2, 7)</code> = 2 bis 6 · <code>range(1, 10, 3)</code> = 1, 4, 7 · <code>range(5, 0, -1)</code> = 5, 4, 3, 2, 1. Das Ende wird <b>nie</b> erreicht.'),
 ('warn', 'Bei <b>Summen bis n</b> musst du auf den Endwert achten: Soll n mitgezählt werden, schreibe <code>range(1, n + 1)</code>.'),
 ('c', 'n = 5\nsumme = 0\nfor i in range(1, n + 1):\n    summe = summe + i\nprint(summe)'),
], [
 ('Welche Zahlen liefert <code>range(2, 10, 3)</code>?', ['2, 5, 8', '2, 5, 8, 11', '3, 6, 9'], 0, 'Start 2, immer +3, kleiner als 10 bleiben: 2, 5, 8.'),
 ('Wie zählst du von 5 auf 1 herunter?', ['range(5, 1)', 'range(5, 0, -1)', 'range(1, 5, -1)'], 1, 'Mit Schritt -1 und Ende 0 (das nicht mehr erreicht wird).'),
], ['a070', 'a077'])

lesson('l18', 5, 'while: Wiederholen, solange …', 5, [
 ('t', '<p>Die <code>while</code>-Schleife wiederholt, <b>solange eine Bedingung stimmt</b>. Du nutzt sie, wenn du vorher nicht weißt, wie oft etwas passiert.</p>'),
 ('c', 'zahl = 3\nwhile zahl > 0:\n    print(zahl)\n    zahl = zahl - 1\nprint("Start!")'),
 ('t', '<p>So läuft das ab: Python prüft die Bedingung (<code>zahl &gt; 0</code>). Stimmt sie, läuft der eingerückte Block, danach wird <b>wieder geprüft</b> – bis die Bedingung nicht mehr stimmt.</p>'),
 ('warn', '<b>Endlosschleife!</b> Verändert sich in der Schleife nichts, das die Bedingung irgendwann falsch macht, läuft sie ewig. Lass deshalb in jeder while-Schleife die Variable aus der Bedingung <b>verändern</b> (<code>zahl = zahl - 1</code>). Die App bricht Endlosschleifen nach 5 Sekunden ab – aber lieber gar nicht erst bauen!'),
 ('t', '<p>Ein Klassiker: so lange fragen, bis die Antwort stimmt.</p>'),
 ('c', 'geheim = 7\ntipp = 0\nwhile tipp != geheim:\n    tipp = int(input())\nprint("Gefunden!")', ['3', '9', '7']),
 ('t', '<p><b>for oder while?</b> <code>for</code>, wenn du die Anzahl der Durchläufe kennst (oder eine Liste durchgehst) – <code>while</code>, wenn „bis etwas passiert“.</p>'),
], [
 ('Was passiert bei <code>while True:</code> ohne Veränderung im Block?', ['Die Schleife läuft nie', 'Die Schleife läuft endlos', 'Die Schleife läuft einmal'], 1, 'True bleibt immer wahr – die Schleife endet nie.'),
 ('Wie oft läuft die Schleife: <code>zahl = 3</code>, <code>while zahl > 0:</code>, <code>zahl = zahl - 1</code>?', ['2-mal', '3-mal', '4-mal'], 1, 'zahl wird 3, 2, 1 – dann ist 0 > 0 falsch.'),
], ['a068', 'a073', 'a076', 'a078'])

lesson('l19', 5, 'Schleifen-Muster: Summe, Zähler, Filter', 6, [
 ('t', '<p>Mit Schleifen löst du viele typische Aufgaben. Dafür gibt es drei Grundmuster.</p><p><b>1. Summe bilden:</b> Starte mit 0 und addiere in jeder Runde etwas dazu.</p>'),
 ('c', 'summe = 0\nfor i in range(1, 6):\n    summe = summe + i\nprint(summe)'),
 ('t', '<p>Kürzer schreibt man <code>summe += i</code> („addiere i zu summe“). Für ein <b>Produkt</b> startest du mit 1.</p><p><b>2. Zählen:</b> Ein Zähler beginnt bei 0 und wird nur erhöht, wenn eine Bedingung stimmt (Schleife + <code>if</code>).</p>'),
 ('c', 'anzahl = 0\nfor i in range(1, 21):\n    if i % 3 == 0:\n        anzahl += 1\nprint(anzahl)'),
 ('t', '<p><b>3. Filtern/Ausgeben:</b> Nur das ausgeben, was zu einer Bedingung passt.</p>'),
 ('c', 'for i in range(1, 11):\n    if i % 2 == 0:\n        print(i, "ist gerade")'),
 ('t', '<p>Das <b>Teiler</b>-Muster: Probiere alle Zahlen von 1 bis n durch und gib die aus, bei denen <code>n % i == 0</code> gilt.</p>'),
 ('c', 'n = 12\nfor i in range(1, n + 1):\n    if n % i == 0:\n        print(i)'),
 ('tip', '<b>Merke:</b> Variable <b>vor</b> der Schleife anlegen (0 oder 1), in der Schleife verändern, <b>nach</b> der Schleife ausgeben. Steht das <code>print</code> in der Schleife, kommt es bei jedem Durchlauf.'),
 ('c', 'for i in range(1, 4):\n    print("*" * i)'),
], [
 ('Womit startest du eine Summe, womit ein Produkt?', ['Summe 1, Produkt 0', 'Summe 0, Produkt 1', 'Beide mit 0'], 1, 'Zum Addieren ist 0 neutral, zum Multiplizieren 1.'),
 ('Wohin gehört <code>print(summe)</code>, wenn nur das Endergebnis erscheinen soll?', ['In die Schleife', 'Hinter die Schleife (nicht eingerückt)', 'Vor die Schleife'], 1, 'Nach der Schleife ausgeben – dann kommt es nur einmal.'),
 ('Wie zählst du, wie viele Zahlen von 1 bis 20 gerade sind?', ['Zähler + if i % 2 == 0 in der Schleife', 'Nur print(20 / 2)', 'Eine while-Schleife ohne Bedingung'], 0, 'Ein Zähler, der nur bei passenden Zahlen erhöht wird.'),
], ['a069', 'a071', 'a074', 'a082', 'a083', 'a084', 'a085'])

# ===== Kapitel 6: Listen =====
lesson('l20', 6, 'Listen anlegen und Index', 5, [
 ('t', '<p>Eine <b>Liste</b> speichert viele Werte unter einem Namen – wie ein Regal mit nummerierten Fächern. Eine Liste steht in <b>eckigen Klammern</b>, die Elemente sind durch Kommas getrennt:</p>'),
 ('c', 'zahlen = [10, 20, 30, 40]\nnamen = ["Felix", "Sophia", "Anna"]\nprint(zahlen)\nprint(namen)'),
 ('t', '<p>Jedes Element hat einen <b>Index</b> (eine Nummer). Wichtig: Der Index zählt <b>ab 0</b>! Das erste Element hat den Index 0, das zweite den Index 1 usw.</p>'),
 ('c', 'tiere = ["Hund", "Katze", "Maus"]\nprint(tiere[0])\nprint(tiere[1])\nprint(tiere[2])\nprint(len(tiere))'),
 ('t', '<p><code>len(liste)</code> verrät, wie viele Elemente drin sind. Das letzte Element hat deshalb den Index <code>len(liste) - 1</code> – oder du schreibst kurz <code>liste[-1]</code>.</p>'),
 ('c', 'tiere = ["Hund", "Katze", "Maus"]\nprint(tiere[-1])\nprint(tiere[-2])'),
 ('warn', '<b>IndexError:</b> Einen Index, den es nicht gibt, kennt Python nicht. Bei 3 Elementen sind 0, 1 und 2 erlaubt – <code>liste[3]</code> ist ein Fehler.'),
 ('tip', '<b>Merke:</b> Index ab 0 · <code>-1</code> = letztes Element · <code>len()</code> = Anzahl · Eine leere Liste ist <code>[]</code>.'),
], [
 ('Welchen Index hat das erste Element einer Liste?', ['0', '1', '-1'], 0, 'Python zählt ab 0.'),
 ('Was gibt <code>[5, 8, 13][1]</code> aus?', ['5', '8', '13'], 1, 'Index 1 ist das zweite Element.'),
 ('Wie greifst du auf das letzte Element zu?', ['liste[len(liste)]', 'liste[-1]', 'liste[last]'], 1, 'Der Index -1 bedeutet „von hinten das erste“.'),
], ['a086', 'a087', 'a095', 'a100'])

lesson('l21', 6, 'Listen verändern', 5, [
 ('t', '<p>Listen kann man ändern – anders als Texte. Die wichtigsten Befehle (die „Methoden“ schreibt man mit Punkt hinter den Listennamen):</p>'),
 ('c', 'liste = [1, 2, 3]\nliste.append(4)        # hinten anhängen\nprint(liste)\nliste[0] = 99          # ein Element ändern\nprint(liste)\nliste.remove(2)        # einen Wert entfernen\nprint(liste)'),
 ('t', '<p><code>append</code> hängt <b>ein</b> Element hinten an. So baust du eine Liste schrittweise auf: erst eine <b>leere Liste</b> anlegen, dann in einer Schleife füllen.</p>'),
 ('c', 'quadrate = []\nfor i in range(1, 6):\n    quadrate.append(i * i)\nprint(quadrate)'),
 ('c', 'z = [5, 2, 9, 1]\nz.sort()                # sortiert die Liste\nprint(z)\nprint(len(z), sum(z), max(z), min(z))'),
 ('warn', 'Listen haben <code>append</code>, nicht <code>add</code>! Und <code>append</code> verändert die Liste selbst – es gibt keinen Rückgabewert (<code>x = liste.append(3)</code> macht x zu <code>None</code>).'),
 ('t', '<p>Mit <code>in</code> prüfst du, ob etwas in der Liste steckt:</p>'),
 ('c', 'farben = ["rot", "gelb"]\nprint("rot" in farben)\nprint("blau" in farben)'),
], [
 ('Wie hängst du <code>5</code> an die Liste <code>z</code> an?', ['z.add(5)', 'z.append(5)', 'z + 5'], 1, 'Die Methode heißt append.'),
 ('Womit startest du, um eine Liste in einer Schleife zu füllen?', ['liste = 0', 'liste = []', 'liste = ""'], 1, 'Mit einer leeren Liste.'),
 ('Was liefert <code>len([4, 8, 15])</code>?', ['2', '3', '15'], 1, 'Die Liste hat drei Elemente.'),
], ['a088', 'a092', 'a096', 'a098', 'a101', 'a102'])

lesson('l22', 6, 'Listen durchlaufen und Ausschnitte', 5, [
 ('t', '<p>Mit <code>for</code> kannst du direkt <b>über die Elemente</b> einer Liste laufen – ganz ohne Index:</p>'),
 ('c', 'namen = ["Felix", "Sophia", "Anna"]\nfor name in namen:\n    print("Hallo", name)'),
 ('t', '<p>Die Variable (<code>name</code>) nimmt nacheinander jedes Element an. Damit lassen sich die Schleifenmuster aus Kapitel 5 leicht auf Listen anwenden, z. B. eine Summe:</p>'),
 ('c', 'zahlen = [3, 5, 7]\nsumme = 0\nfor z in zahlen:\n    summe += z\nprint(summe)'),
 ('t', '<p><b>Ausschnitte (Slicing):</b> Mit <code>liste[a:b]</code> holst du die Elemente ab Index <code>a</code> bis <b>vor</b> Index <code>b</code>. Lässt du eine Angabe weg, geht der Ausschnitt bis zum Anfang bzw. Ende.</p>'),
 ('c', 'z = [10, 20, 30, 40, 50]\nprint(z[1:3])\nprint(z[:2])\nprint(z[3:])\nprint(z[-2:])'),
 ('tip', '<b>Merke:</b> Das Ende beim Slicing wird – wie bei <code>range</code> – <b>nicht</b> mitgenommen. <code>z[1:3]</code> sind die Elemente mit Index 1 und 2.'),
 ('t', '<p>Das größte Element findest du auch von Hand mit einer Schleife: Merke dir den bisher größten Wert und ersetze ihn, wenn du einen größeren siehst.</p>'),
 ('c', 'zahlen = [4, 9, 2, 7]\ngroesste = zahlen[0]\nfor z in zahlen:\n    if z > groesste:\n        groesste = z\nprint(groesste)'),
], [
 ('Was liefert <code>[10, 20, 30, 40][1:3]</code>?', ['[10, 20]', '[20, 30]', '[20, 30, 40]'], 1, 'Index 1 und 2 – die 3 ist nicht mehr dabei.'),
 ('Was ist <code>x</code> in jeder Runde von <code>for x in liste:</code>?', ['Der Index', 'Das jeweilige Element', 'Die Länge'], 1, 'x nimmt nacheinander jedes Element an.'),
], ['a089', 'a090', 'a094', 'a097'])

lesson('l23', 6, 'Listen-Muster: Summe, Größte, Zählen, Filtern', 5, [
 ('t', '<p>Python hat eingebaute Hilfen für Listen von Zahlen:</p>'),
 ('c', 'z = [3, 8, 5, 12]\nprint(sum(z))\nprint(max(z))\nprint(min(z))\nprint(sum(z) / len(z))'),
 ('t', '<p>Der <b>Durchschnitt</b> ist die Summe geteilt durch die Anzahl: <code>sum(z) / len(z)</code>.</p><p><b>Zählen:</b> <code>liste.count(x)</code> zählt, wie oft x vorkommt.</p>'),
 ('c', 'z = [2, 5, 2, 7, 2]\nprint(z.count(2))\nprint(z.count(9))'),
 ('t', '<p><b>Filtern:</b> Schleife und <code>if</code> – gib nur die Elemente aus, die passen.</p>'),
 ('c', 'z = [3, 8, 5, 12, 7, 20]\nfor x in z:\n    if x % 2 == 0:\n        print(x)'),
 ('t', '<p><b>Die zweitgrößte Zahl:</b> Sortiere die Liste – dann steht die größte hinten, die zweitgrößte davor.</p>'),
 ('c', 'z = [4, 9, 2, 7]\nz.sort()\nprint(z)\nprint(z[-2])'),
 ('tip', '<b>Merke:</b> <code>sum</code>, <code>max</code>, <code>min</code>, <code>len</code>, <code>count</code>, <code>sort</code> – damit sparst du dir oft die Schleife. Brauchst du eine Bedingung (z. B. nur gerade Zahlen), bleibt es bei Schleife + <code>if</code>.'),
], [
 ('Wie berechnest du den Durchschnitt der Liste <code>z</code>?', ['sum(z) * len(z)', 'sum(z) / len(z)', 'max(z) / min(z)'], 1, 'Summe durch Anzahl.'),
 ('Welche Zahl steht nach <code>z.sort()</code> bei <code>[4, 9, 2, 7]</code> an letzter Stelle?', ['2', '9', '7'], 1, 'Sortiert wird aufsteigend – die größte Zahl steht hinten.'),
], ['a091', 'a093', 'a099', 'a103', 'a104', 'a105'])
