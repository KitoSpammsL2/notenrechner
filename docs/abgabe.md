# Abgabeübersicht Notenrechner

Stand: 2. November 2026. Grundlage: `M324_Bewertungsraster`, Version 1.0,
mit HZ1 bis HZ5. `offen` kennzeichnet einen fehlenden oder unvollständigen
Nachweis; eine vorhandene Datei allein beweist noch keine persönliche Kompetenz.

## Das Projekt

Der Notenrechner erfasst Fächer und gewichtete Noten, zeigt den Schnitt und
exportiert die Noten als CSV. Die [App auf Azure](https://notenrechner-lb324.azurewebsites.net)
und das [Repository](https://github.com/KitoSpammsL2/notenrechner) sind öffentlich erreichbar.

Kaito setzte die Erfassung von Fächern und Noten sowie Azure und die
Veröffentlichung um ([PR #9](https://github.com/KitoSpammsL2/notenrechner/pull/9),
[PR #11](https://github.com/KitoSpammsL2/notenrechner/pull/11),
[PR #14](https://github.com/KitoSpammsL2/notenrechner/pull/14)).
Faruk setzte die Schnittberechnung um und bearbeitet den PostgreSQL-Test
([PR #10](https://github.com/KitoSpammsL2/notenrechner/pull/10),
[Issue #5](https://github.com/KitoSpammsL2/notenrechner/issues/5)).
Laurentiu übernahm CSV-Export, Oberfläche, Werkzeugvergleich und diese Übersicht
([PR #12](https://github.com/KitoSpammsL2/notenrechner/pull/12),
[PR #13](https://github.com/KitoSpammsL2/notenrechner/pull/13),
[Issue #15](https://github.com/KitoSpammsL2/notenrechner/issues/15)).

## Was ist DevOps

DevOps bedeutet, dass Entwicklung und Betrieb zusammenarbeiten. Dazu gehören
Planung, Programmierung, Tests, Veröffentlichung, Einrichtung der Laufzeitumgebung
und die Prüfung, ob die Anwendung läuft. Wir teilen die Verantwortung dafür,
dass eine Änderung bei den Benutzern funktioniert.

Automatische Prüfungen finden Fehler früh. Ein gemeinsamer Ablauf macht sichtbar,
wer was ändert und warum. Automatische Auslieferung spart wiederholte Handarbeit
und führt dieselben Schritte für jede Version aus. Tests und Reviews senken das
Fehlerrisiko; sie garantieren nicht, dass es keine Fehler mehr gibt.

### Begriffe

- **Anforderung:** Beschreibt, was die App leisten soll. Akzeptanzkriterien sagen,
  woran wir erkennen, dass die Anforderung erfüllt ist.
- **User Story:** Beschreibt den Wunsch aus Sicht einer Person und seinen Nutzen,
  zum Beispiel den Download von Noten als CSV.
- **Issue:** Der Eintrag auf GitHub mit Anforderung, Kriterien, Aufgaben und
  zuständiger Person. Labels ordnen etwa Typ und Bearbeitungsstand ein.
- **Meilenstein:** Bündelt Aufgaben für ein Ziel wie die Version `1.0.0`.
- **Rückverfolgbarkeit:** Wir können von der Anforderung zu Codeänderung, Test,
  Review und Version gehen und auch zurückverfolgen, warum etwas geändert wurde.
- **Branch, Commit und Pull Request:** Ein Branch ist ein eigener Arbeitsstand,
  ein Commit speichert einen Änderungsschritt, ein PR schlägt die Übernahme vor.
- **CI:** Die automatische Prüfung neuer Änderungen. **Deployment** ist die
  Auslieferung in die Laufzeitumgebung. Ein **Tag** benennt einen bestimmten
  Codestand. Ein **Artefakt** ist ein Ergebnis wie ein fertiges Container-Image.

### Entwicklungsumgebung und Versionierung

Eine virtuelle Python-Umgebung trennt unsere Projektpakete von anderen Projekten.
Festgelegte Paketversionen helfen, dieselbe Umgebung einzurichten. Gemeinsame
Formatierungsregeln und Hooks prüfen Änderungen lokal; Container können zusätzlich
eine gemeinsame Laufzeit liefern. Unsere konkrete Anleitung steht im
[README](https://github.com/KitoSpammsL2/notenrechner/blob/main/README.md).

Git speichert unsere Versionen und Branches lokal und auf einem gemeinsamen Server.
Eine andere Möglichkeit zur Codeversionierung ist Subversion mit zentralem Server.
Wir verwenden Git mit GitHub für Zusammenarbeit und Reviews. GitHub Releases bündeln
benannte Versionen; GHCR speichert die zugehörigen Docker-Images mit Versions-Tags.

## Unser Ablauf

Ein echtes Beispiel ist [Issue #7](https://github.com/KitoSpammsL2/notenrechner/issues/7):
Bei jedem Tag sollen zuerst Tests und danach die Azure-Auslieferung laufen.
Kaito entwickelte im Branch `7-deployment`. Die Commits beginnen mit `#7`,
etwa [die erste Implementierung](https://github.com/KitoSpammsL2/notenrechner/commit/b33518374bbde66baa491cdbd5dec483c63883f1).

Vor dem Commit aktivieren wir `.venv`. Die
[Hooks](https://github.com/KitoSpammsL2/notenrechner/blob/main/.pre-commit-config.yaml)
formatieren mit black, prüfen mit flake8 und pytest und verlangen eine Issue-Nummer
in der Commit-Nachricht. Wir pushen den Branch und öffnen einen PR auf `main`.
Die [CI](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/workflows/ci.yml)
installiert Python 3.13 und die Pakete und führt flake8, black und pytest aus.

In [PR #11](https://github.com/KitoSpammsL2/notenrechner/pull/11) verlangte Laurentiu
[eine Korrektur](https://github.com/KitoSpammsL2/notenrechner/pull/11#pullrequestreview-5736139109):
Der Filter `*.*.*` erfasste nicht jeden Tag. Kaito änderte ihn mit
[Commit c8f1c25](https://github.com/KitoSpammsL2/notenrechner/commit/c8f1c250b5a7f19805737df6a2abbf5f97efe4d2)
auf `**`. Nach grüner CI und erfolgreichem Tag-Probelauf gab Laurentiu den PR
[frei](https://github.com/KitoSpammsL2/notenrechner/pull/11#pullrequestreview-5736182346).
Der PR wurde anschliessend gemergt.

Der Tag `0.1.0-rc.1` löste den
[erfolgreichen Deploy-Lauf](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41440684021)
aus: erst Tests, dann Azure-Deployment mit dem gespeicherten Publish-Profile-Secret,
danach HTTP-Prüfung. Der Probelauf fand vor dem Merge statt, damit die Auslieferung
vor der Freigabe geprüft werden konnte. Für reguläre Versionen taggen wir den
gemeinsam integrierten Stand.

[PR #14](https://github.com/KitoSpammsL2/notenrechner/pull/14) ergänzt Release und
Docker-Image. Der Test-Tag `0.1.0-rc.2` führte zu einem
[Release](https://github.com/KitoSpammsL2/notenrechner/releases/tag/0.1.0-rc.2)
und einem [Image im Paketbereich](https://github.com/KitoSpammsL2/notenrechner/pkgs/container/notenrechner).
Im [Workflow-Lauf](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41441490066)
sind Tests, Azure, Release und Docker erfolgreich. Das Image wurde gebaut,
gestartet und vor dem Upload per HTTP geprüft. Der erste Registry-Upload wurde
abgewiesen; der wiederholte Job war erfolgreich. Die Ursache ist noch ungeklärt.
Die Vorabversion ist ein Nachweis des Probelaufs, noch keine endgültige Abgabeversion.

## Nachweise pro Kriterium

### HZ1 Anforderungen verwalten 20 Prozent

| Kriterium | Stufe | Nachweis |
|---|---|---|
| DevOps definieren und Bereiche auflisten (LZ 1.1) | Beginner | [Erklärung und Bereiche](#was-ist-devops) |
| Bedeutung der Prozesse und Werkzeuge erklären (LZ 1.2) | Beginner | [Nutzen im Projekt](#was-ist-devops) |
| Grundbegriffe und ihren Zweck kennen (LZ 1.3) | Beginner | [Begriffe](#begriffe) |
| Anforderungen technisch sinnvoll verwalten (LZ 1.4) | Intermediate | [User-Story-Vorlage](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/ISSUE_TEMPLATE/user-story.md), [Meilenstein 1.0.0](https://github.com/KitoSpammsL2/notenrechner/milestone/1), [Issue #15 mit Person und Labels](https://github.com/KitoSpammsL2/notenrechner/issues/15). [Label bei Meilenstein setzen](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/workflows/add-in-progress-label.yaml) und [neues Label bei Zuweisung entfernen](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/workflows/remove-new-issue-label.yaml). |
| Begriffe nachvollziehbarer Entwicklung kennen (LZ 1.5) | Intermediate | [Begriffe](#begriffe) und [echtes Ablaufbeispiel](#unser-ablauf) |
| Anforderung und Umsetzung verknüpfen (LZ 1.6) | Intermediate | [Issue #7](https://github.com/KitoSpammsL2/notenrechner/issues/7), [Commit mit #7](https://github.com/KitoSpammsL2/notenrechner/commit/c8f1c250b5a7f19805737df6a2abbf5f97efe4d2) und [PR #11 mit Closes #7](https://github.com/KitoSpammsL2/notenrechner/pull/11) |
| Werkzeuge auf Tauglichkeit vergleichen (LZ 1.7) | Advanced | [GitHub Issues, Jira und Azure Boards](https://github.com/KitoSpammsL2/notenrechner/blob/main/docs/werkzeugvergleich.md), umgesetzt in [PR #13](https://github.com/KitoSpammsL2/notenrechner/pull/13) |

### HZ2 Entwicklungsumgebung 10 Prozent

| Kriterium | Stufe | Nachweis |
|---|---|---|
| Möglichkeiten der Einrichtung kennen (LZ 2.1) | Beginner | [Erklärung](#entwicklungsumgebung-und-versionierung), [Projektpakete](https://github.com/KitoSpammsL2/notenrechner/blob/main/requirements-dev.txt), [Umgebungsvariablen ohne Geheimnisse](https://github.com/KitoSpammsL2/notenrechner/blob/main/.env.example) |
| Umgebung nach Anleitung einrichten (LZ 2.2) | Intermediate | [README mit .venv, Installation und Hooks](https://github.com/KitoSpammsL2/notenrechner/blob/main/README.md), [Hook-Konfiguration](https://github.com/KitoSpammsL2/notenrechner/blob/main/.pre-commit-config.yaml) |
| Umgebung selbständig einrichten und erweitern | Advanced | **offen:** Einrichtungsanleitung und [Lint-Konfiguration](https://github.com/KitoSpammsL2/notenrechner/blob/main/.flake8) sind vorhanden; die persönliche selbständige Erweiterung ist damit noch nicht konkret dokumentiert. |

### HZ3 Sourcecode und Artefaktverwaltung 30 Prozent

| Kriterium | Stufe | Nachweis |
|---|---|---|
| Werkzeuge der Versionierung kennen (LZ 3.1) | Beginner | [Git, Subversion, GitHub und Artefaktablage erklärt](#entwicklungsumgebung-und-versionierung) |
| Einen Ablauf für Änderungen beschreiben (LZ 3.2) | Intermediate | [Unser Ablauf](#unser-ablauf) und [README](https://github.com/KitoSpammsL2/notenrechner/blob/main/README.md) |
| Dem Ablauf bei eigenen Änderungen folgen (LZ 3.3) | Intermediate | Laurentius [PR #12](https://github.com/KitoSpammsL2/notenrechner/pull/12) und [PR #13](https://github.com/KitoSpammsL2/notenrechner/pull/13) mit Commits, fremdem Review und Merge; eigenes Review in [PR #11](https://github.com/KitoSpammsL2/notenrechner/pull/11#pullrequestreview-5736182346) |
| Artefakte mit Sourcecodeverwaltung anwenden (LZ 3.4) | Advanced | [Release 0.1.0-rc.2](https://github.com/KitoSpammsL2/notenrechner/releases/tag/0.1.0-rc.2), [GHCR-Paket](https://github.com/KitoSpammsL2/notenrechner/pkgs/container/notenrechner) und [erfolgreicher Build, Containercheck und Upload](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41441490066). **offen:** [Issue #8](https://github.com/KitoSpammsL2/notenrechner/issues/8) ist noch nicht in main integriert. |

### HZ4 Automatisierte Integration 20 Prozent

| Kriterium | Stufe | Nachweis |
|---|---|---|
| Testfall zu einer Anforderung entwickeln (LZ 4.1) | Beginner | [CSV-Kriterien in Issue #4](https://github.com/KitoSpammsL2/notenrechner/issues/4), [Tests inklusive Fachname mit Komma](https://github.com/KitoSpammsL2/notenrechner/blob/main/tests/test_export.py) und [PR #12 mit dokumentiertem roten Test zuerst](https://github.com/KitoSpammsL2/notenrechner/pull/12) |
| Tests automatisch ausführen (LZ 4.2) | Intermediate | [Lokale Hooks](https://github.com/KitoSpammsL2/notenrechner/blob/main/.pre-commit-config.yaml), [CI-Konfiguration](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/workflows/ci.yml) und [erfolgreicher CI-Lauf](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41441296581) |
| Vollständigen automatisierten Integrationstest umsetzen | Advanced | **offen:** [Issue #5](https://github.com/KitoSpammsL2/notenrechner/issues/5) ist noch nicht in main. Dort fehlen PostgreSQL-Service und der Integrationstest über Erfassen, Schnitt und Export. Die vorhandene [Fixture](https://github.com/KitoSpammsL2/notenrechner/blob/main/tests/conftest.py) unterstützt TEST_DATABASE_URL, verwendet ohne diese Variable aber SQLite im Speicher. |

### HZ5 Automatisiertes Deployment 20 Prozent

| Kriterium | Stufe | Nachweis |
|---|---|---|
| Funktion eines automatisierten Deployments erklären | Beginner | [Tag, Tests, Secret, Auslieferung und Antwortprüfung am Beispiel](#unser-ablauf) |
| Automatische Auslieferung einrichten (LZ 5.1) | Intermediate | [Deploy-Workflow](https://github.com/KitoSpammsL2/notenrechner/blob/main/.github/workflows/deploy.yml), [erfolgreicher Tag-Lauf](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41440684021) und [laufende App](https://notenrechner-lb324.azurewebsites.net) |
| Umfassenden Deploymentprozess umsetzen | Advanced | [Azure-Einrichtung als Skript](https://github.com/KitoSpammsL2/notenrechner/blob/main/infra/setup-azure.sh) und [Lauf mit Tests, Azure, Release und Image](https://github.com/KitoSpammsL2/notenrechner/actions/runs/41441490066). **offen:** Das Einrichtungsskript wurde laut [PR #11](https://github.com/KitoSpammsL2/notenrechner/pull/11) nur in Teilen ausgeführt, nicht einmal vollständig am Stück. Die Integration von [PR #14](https://github.com/KitoSpammsL2/notenrechner/pull/14) in main steht noch aus. |

## Noch offen

- **offen:** Persönliche selbständige Erweiterung der Entwicklungsumgebung
  konkret belegen (HZ2 Advanced).
- **offen:** Issue #5 mit PostgreSQL-Service, Integrationstest und grünem Lauf
  in main übernehmen (HZ4 Advanced).
- **offen:** Issue #8 beziehungsweise PR #14 in main übernehmen und diese
  Übersicht aktualisieren (HZ3 und HZ5 Advanced).
- **offen:** Vollständigen Durchlauf des Azure-Einrichtungsskripts belegen
  (HZ5 Advanced). Ein vorhandenes Skript ersetzt diesen Nachweis nicht.
- **offen:** Nach Integration aller Arbeiten die endgültige Version `1.0.0`
  mit Release, Image, grünem Workflow und geprüfter Azure-App nachtragen.
  Derzeit ist `0.1.0-rc.2` die geprüfte Vorabversion.

Die Abgabeform klärt Kaito mit der Lehrperson. Zugangsdaten und `.env` werden
nicht in der Übersicht veröffentlicht.
