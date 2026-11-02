# Notenrechner

![CI](https://github.com/KitoSpammsL2/notenrechner/actions/workflows/ci.yml/badge.svg)

Web-App, in der man Fächer und Noten erfasst und den Notenschnitt sieht.
LB Modul 324 von Kaito, Faruk und Laurentiu.

## Funktionen

- Fächer und Noten mit Gewichtung erfassen.
- Den gewichteten Notenschnitt pro Fach anzeigen.
- Noten als CSV-Datei herunterladen.
- Bedienung im Browser, auch auf dem Handy.

Die Funktionen werden über die jeweiligen Pull Requests integriert.
Unser [Werkzeugvergleich](docs/werkzeugvergleich.md) erklärt die Begriffe
und warum wir GitHub Issues für dieses Projekt empfehlen.

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
6. Mergen, sobald jemand anderes zugestimmt hat und die CI grün ist.

Bei Pull Requests auf `main` und Pushes auf `main` startet GitHub Actions
die CI mit Python 3.13: Abhängigkeiten installieren, flake8, black und
pytest mit Coverage. Die CI prüft den Code; die Auslieferung nach Azure
benötigt einen eigenen Deployment-Workflow.

## Wer arbeitet wo

| Funktion | Dateien |
|---|---|
| Fächer und Noten erfassen | `subjects.py`, `templates/subjects.html`, `tests/test_subjects.py` |
| Schnitt berechnen und anzeigen | `averages.py`, `templates/averages.html`, `tests/test_averages.py` |
| CSV-Export und Oberfläche | `export.py`, `templates/base.html`, `static/style.css`, `tests/test_export.py` |
