# Python 3 Grundlagen

Dies ist ein Überblick über die Grundlagen in Python, einschließlich Variablen, Datentypen, grundlegende Operationen, Bedingungen und Schleifen.

## Variablen

Variablen sind Container, die dazu dienen, Datenwerte zu speichern. Sie werden erstellt, indem man einem Namen einen Wert zuweist. Variablennamen müssen mit einem Buchstaben oder Unterstrich beginnen und können Buchstaben, Zahlen und Unterstriche enthalten. [Weitere Informationen](https://docs.python.org/3/tutorial/introduction.html#variables)

Beispiel für die Zuweisung einer Variable:
```python
variablen_name = 42
```

## Datentypen

Python unterstützt verschiedene Datentypen zur Darstellung unterschiedlicher Arten von Informationen.

### Ganzzahlen (int)

Ganzzahlen werden verwendet, um ganze Zahlen darzustellen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Beispiel:
```python
meine_ganzzahl = 42
```

### Gleitkommazahlen (float)

Gleitkommazahlen werden verwendet, um Zahlen mit Dezimalstellen darzustellen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Beispiel:
```python
meine_gleitkommazahl = 3.14
```

### Zeichenketten (str)

Zeichenketten werden verwendet, um Text darzustellen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

Beispiel:
```python
meine_zeichenkette = "Hallo, Welt"
```

### Listen

Listen sind geordnete Sammlungen von Elementen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Beispiel:
```python
meine_liste = [1, 2, 3]
```
Arbeiten mit Listen:

```python
meine_liste = [1, 2, 3, 4, 5]

# Überprüfen, ob ein Wert in der Liste ist
if 3 in meine_liste:
    print("3 ist in der Liste")

# Die Liste sortieren
meine_liste.sort()
print(meine_liste)
```

### Tupel

Tupel sind geordnete, unveränderliche Sammlungen von Elementen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Beispiel:
```python
mein_tupel = (4, 5, 6)
```

### Wörterbücher (dict)

Wörterbücher speichern Schlüssel-Wert-Paare und ermöglichen es Ihnen, Werte mit eindeutigen Schlüsseln zu verknüpfen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

Beispiel:
```python
mein_wörterbuch = {"name": "Alice", "alter": 30}
```

### Booleans (bool)

Booleans repräsentieren logische Werte, True oder False. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

Beispiel:
```python
mein_bool = True
```

## Grundlegende Operationen

Python unterstützt verschiedene grundlegende Operationen für arithmetische und mathematische Berechnungen.

### Arithmetische Operationen

Python bietet standardmäßige arithmetische Operationen. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Beispiel:
- Addition: `ergebnis = 5 + 3`
- Subtraktion: `ergebnis = 7 - 2`
- Multiplikation: `ergebnis = 4 * 6`
- Division: `ergebnis = 8 / 2`
- Modulus (Rest): `ergebnis = 10 % 3`
- Potenzierung: `ergebnis = 2 ** 4`

### Verwendung der mathematik-Bibliothek

Die mathematik-Bibliothek in Python bietet fortgeschrittenere mathematische Funktionen. [Weitere Informationen](https://docs.python.org/3/library/math.html)

Beispiel:
`import math`
- Quadratwurzel: `ergebnis = math.sqrt(16)`
- Sinusfunktion (erfordert Radianten): `ergebnis = math.sin(math.radians(30))`
- Natürlicher Logarithmus: `ergebnis = math.log(100)`


## Bedingungen

Bedingte Anweisungen werden verwendet, um Entscheidungen basierend auf bestimmten Bedingungen zu treffen. [Weitere Informationen](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

Beispiel:
```python
x = 10
if x > 5:
    print("x ist größer als 5")
elif x == 5:
    print("x ist gleich 5")
else:
    print("x ist kleiner als 5")
```

## Schleifen

Schleifen werden in Python für wiederholte Aufgaben verwendet. [Weitere Informationen](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)

### While-Schleife

Die while-Schleife führt einen Codeblock wiederholt aus, solange eine Bedingung wahr ist. [Weitere Informationen](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

Beispiel:
```python
zähler = 0
while zähler < 5:
    print(zähler)
    zähler += 1
```
### For-Schleife

Die for-Schleife wird verwendet, um über eine Sequenz zu iterieren, wie zum Beispiel eine Liste oder einen Zahlenbereich. [Weitere Informationen](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

Beispiel:
```python
früchte = ["Apfel", "Banane", "Kirsche"]
for frucht in früchte:
    print(frucht)
```

Zusätzlich können Sie die range-Funktion verwenden, um eine Sequenz von Zahlen zu erstellen und darüber zu iterieren. [Weitere Informationen](https://docs.python.org/3/library/stdtypes.html#range)

Beispiel:
```python
for i in range(5):
    print(i)
```
### Abbrechen und Fortsetzen

Python bietet zwei Steueranweisungen innerhalb von Schleifen:

- `break` wird verwendet, um eine Schleife vorzeitig zu verlassen. [Weitere Informationen](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)
- `continue` wird verwendet, um die akt

uelle Iteration zu überspringen und zur nächsten fortzufahren. [Weitere Informationen](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)

Beispiel:
```python
for i in range(10):
    wenn i == 3:
        break  # Verlasse die Schleife, wenn i gleich 3 ist
    wenn i == 7:
        continue  # Überspringe die Iteration, wenn i gleich 7 ist
    print(i)
```

Dies sind die grundlegenden Konzepte von Python 3. Wenn Sie mit der Sprache vertrauter werden, können Sie fortgeschrittenere Themen und Bibliotheken erkunden.
