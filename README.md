# MobSF_LootScanner
Dieses Python-Skript dient dazu, die durch die dynamischen Analyse von MobSF erzeugten .txt-Dateien nach bestimmten Keywords zu durchsuchen.

# Aufbau
Die von MobSF erzeugten Dateien werden vom Nutzer im Ordner "Testdateien" abgelegt.
Die vom Skript erzeugten Ergebnisse liegen nach Abschluss im Ordner "Ergebnisse".
Für jede zu durchsuchende Datei wird eine entsprechende Ergebnisdatei angelegt. Diese Dateien haben die Bezeichnung "Ergebnis__" + "den Dateinamen der zu testenden Datei".txt
Innerhalb der Ergebnisdateien werden die Ergebnisse nach den einzelnen Keywords sortiert, wobei die Keywords als Überschrift gesetzt werden.


# (Funktionen der) Keywords-Liste:
In der Liste werden alle Wörter / Sätze eingetragen, nach denen gesucht werden soll.
Sollen bestimmte Wörter nicht gesucht werden, können diese mit # markiert werden.
Will man nur einen kleinen Teilbereich der Wörter zur Suche einsetzen, so empfielt es sich, diese oben vor die Liste zu kopieren und danach ein //end zu setzen.
Damit wird die Suche abgebrochen.
Beide Techniken sollen verhindern, dass Wörter aus der Liste gelöscht werden müssen und damit eventuell in Vergessenheit geraten. Auch das komplizierte Anlegen von mehreren
Keyword-Dateien wird so verhindert.

