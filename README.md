# MobSF_LootScanner

[Deutsch](#deutsch) | [English](#english)

---

## Deutsch

Dieses Python-Skript dient dazu, die durch die dynamische Analyse von MobSF erzeugten `.txt`-Dateien nach bestimmten Keywords zu durchsuchen.

### Aufbau
Die von MobSF erzeugten Dateien werden vom Nutzer im Ordner `Testdateien` abgelegt.
Die vom Skript erzeugten Ergebnisse liegen nach Abschluss im Ordner `Ergebnisse` (wird bei Bedarf automatisch angelegt).
Für jede zu durchsuchende Datei wird eine entsprechende Ergebnisdatei angelegt. Diese Dateien haben die Bezeichnung `Ergebnis__` + Dateiname der zu testenden Datei.
Innerhalb der Ergebnisdateien werden die Ergebnisse nach den einzelnen Keywords sortiert, wobei die Keywords als Überschrift gesetzt werden. Die Suche ist case-insensitive.

### Nutzung
```
python3 main.py
```
Standardmäßig werden `./Testdateien/` durchsucht, Ergebnisse landen in `./Ergebnisse/`, Keywords kommen aus `./Keywords`.

Pfade lassen sich per Argument überschreiben:
```
python3 main.py --input /pfad/zu/dateien --output /pfad/zu/ergebnissen --keywords /pfad/zu/keywords.txt
```

### (Funktionen der) Keywords-Liste
In der Datei werden alle Wörter / Sätze eingetragen, nach denen gesucht werden soll.
Sollen bestimmte Wörter nicht gesucht werden, können diese mit `#` markiert werden.
Will man nur einen kleinen Teilbereich der Wörter zur Suche einsetzen, so empfiehlt es sich, diese oben vor die Liste zu kopieren und danach ein `//end` zu setzen.
Damit wird die Suche abgebrochen.
Beide Techniken sollen verhindern, dass Wörter aus der Liste gelöscht werden müssen und damit eventuell in Vergessenheit geraten. Auch das komplizierte Anlegen von mehreren Keyword-Dateien wird so verhindert.

### Voraussetzungen
Keine externen Abhängigkeiten (nur Python-Standardbibliothek)

---

## English

This Python script searches the `.txt` files produced by MobSF's dynamic analysis for specific keywords.

### Structure
MobSF-generated files are placed by the user into the `Testdateien` (test files) folder.
Results are written into the `Ergebnisse` (results) folder after completion (created automatically if missing).
For each analyzed file, a corresponding result file is created, named `Ergebnis__` + the original filename.
Within each result file, matches are grouped by keyword, with the keyword as a heading. The search is case-insensitive.

### Usage
```
python3 main.py
```
By default, `./Testdateien/` is searched, results go to `./Ergebnisse/`, and keywords come from `./Keywords`.

Paths can be overridden via arguments:
```
python3 main.py --input /path/to/files --output /path/to/results --keywords /path/to/keywords.txt
```

### Keyword list behavior
The file contains all words/phrases to search for.
Words to exclude from the search can be marked with `#`.
To use only a small subset of the list, copy those words above the rest and add a `//end` marker — the search stops there.
Both techniques avoid having to delete words from the list (and risk forgetting them), and avoid maintaining multiple separate keyword files.

### Requirements
No external dependencies (Python standard library only)
