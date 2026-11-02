# Notenrechner

Web-App, in der man Fächer und Noten erfasst und den Notenschnitt sieht.
LB Modul 324 von Kaito, Faruk und Laurentiu.

## Lokal starten

```bash
git clone https://github.com/KitoSpammsL2/notenrechner.git
cd notenrechner
python -m venv .venv
```

Umgebung aktivieren, und zwar vor jedem Arbeiten und Committen:

- PowerShell: `.venv\Scripts\Activate.ps1`
- Git Bash: `source .venv/Scripts/activate`
- macOS und Linux: `source .venv/bin/activate`

Danach einmalig einrichten und starten:

```bash
pip install -r requirements-dev.txt
pre-commit install
python main.py
```

Die App läuft unter <http://127.0.0.1:5000>. Lokal braucht sie keine eigene
Datenbank, sie legt selbst eine SQLite-Datei an.

## Tests

```bash
pytest
```

## Arbeitsablauf

Wir arbeiten nach dem GitHub Flow, direkt auf `main` wird nichts gepusht.

1. Issue zuweisen und in GitHub einen Branch dazu erstellen.
2. Lokal mit `git fetch` und `git switch <branch>` auf den Branch wechseln.
3. Zuerst den Test schreiben, dann die Funktion.
4. Committen, die Nachricht nennt das Issue, zum Beispiel `#3 Schnitt berechnen`.
5. Pushen und einen Pull Request erstellen. Jemand anderes macht das Review.
6. Mergen, sobald die CI grün ist.

## Wer arbeitet wo

| Funktion | Dateien |
|---|---|
| Fächer und Noten erfassen | `subjects.py`, `templates/subjects.html`, `tests/test_subjects.py` |
| Schnitt berechnen und anzeigen | `averages.py`, `templates/averages.html`, `tests/test_averages.py` |
| CSV-Export und Oberfläche | `export.py`, `templates/base.html`, `static/style.css`, `tests/test_export.py` |
