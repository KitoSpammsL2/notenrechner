# Werkzeuge zur Anforderungsverwaltung

Stand der Dokumentation und Preise: **2. November 2026**.
Verglichen werden GitHub Issues, Jira Cloud und Azure DevOps Services mit
Azure Boards. Unser Team besteht aus drei Personen und hat einen Tag Zeit.

## Begriffe und Fundstellen

Die Begriffe sind nicht überall genau gleich. Bei Jira verwenden wir die
englische Cloud-Oberfläche; aktuelle Dokumentation nennt Vorgänge auch
„work items“ und Projekte „spaces“. Bei Azure Boards beziehen wir uns auf
den Agile-Prozess. Andere Prozesse haben andere Vorgangstypen.

| Unser Begriff | GitHub Issues | Jira Cloud | Azure Boards (Agile) |
|---|---|---|---|
| Acceptance criteria | Als Abschnitt „Acceptance Criteria“ im Beschreibungstext des Issues, wie in unseren Issues. Eigene Eingaben lassen sich über [Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) vorgeben. | Unsere einfache Abbildung: Abschnitt „Acceptance Criteria“ im Feld **Description** der Story. Die [Beschreibung](https://support.atlassian.com/jira-software-cloud/docs/update-a-work-items-details/) erlaubt Text und Tabellen; diese Überschrift ist unsere Konvention, kein hier vorausgesetztes Standardfeld. | Feld **Acceptance Criteria** im geöffneten User-Story-Formular; dort stehen die Bedingungen für den Abschluss. [Agile-Prozess](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process-workflow?view=azure-devops) |
| Assignee | **Assignees**, rechts im geöffneten Issue. [Zuweisung](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users) | **Assignee**, in den Kontextfeldern rechts beziehungsweise unterhalb der Beschreibung. [Feldaufbau](https://support.atlassian.com/jira-software-cloud/docs/update-a-work-items-details/) | **Assigned To**, im Work-Item-Formular. [Work Items](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops) |
| Issue | **Issue**, im Repository unter **Issues**. [Issues erstellen](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) | **Work item**, früher oft **Issue**, zum Beispiel vom Typ Story oder Task; über Board oder Liste öffnen. [Listenansicht](https://support.atlassian.com/jira-software-cloud/docs/what-is-the-list-view/) | **Work item**, für unsere Anforderungen vom Typ **User Story**, unter **Boards → Work Items** oder im Backlog. „Issue“ ist im Agile-Prozess ein eigener Typ und nicht einfach ein Synonym für jede Anforderung. [Typen](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops) |
| Label | **Labels**, rechts im Issue; Verwaltung unter **Issues → Labels**. [Labels und Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work) | **Labels**, in den Kontextfeldern des Work Items. [Labels verwenden](https://support.atlassian.com/jira/kb/how-to-create-and-use-labels-in-jira-cloud/) | **Tags**, im geöffneten Work Item. [Tags und weitere Felder](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops) |
| Milestone | **Milestone**, Auswahl rechts im Issue; Übersicht unter **Issues → Milestones**, mit Termin und Fortschritt. [Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) | Für ein Release wie `1.0.0`: **Version**, zugeordnet über **Fix versions**, verwaltet unter **Releases** im Softwareprojekt. Das ist eine zweckbezogene Entsprechung. [Versionen](https://support.atlassian.com/jira-software-cloud/docs/what-is-a-version/) | Für zeitliche Planung: **Iteration Path** am Work Item; Termine unter **Project settings → Project configuration → Iterations**. Eine Iteration kann ein Release oder einen Sprint abbilden; sie ist kein identisches Milestone-Feld. [Iterationen](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops) |

## Vergleich für unser Team

Kosten beziehen sich auf die Aufgabenverwaltung für drei Personen, ohne
kostenpflichtige Erweiterungen, zusätzliches Hosting oder Mehrverbrauch.
Die Einschätzung zum Einrichtungsaufwand ist unsere Bewertung für das
bestehende GitHub-Projekt, keine gemessene Herstellerangabe.

| Kriterium | GitHub Issues | Jira Cloud | Azure DevOps Services |
|---|---|---|---|
| Kosten für drei Personen | GitHub Free: 0 USD für den kostenlosen Plan mit Issues. [Preise](https://github.com/pricing) | Free: 0 USD, bis zehn Personen. [Preise](https://www.atlassian.com/en/software/jira/pricing) | Die ersten fünf Basic-Benutzer sind kostenlos, einschliesslich Azure Boards. [Preise](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) |
| Einrichtungsaufwand | Für uns gering: Repository, Issues, Meilenstein und CI sind bereits vorhanden. | Für uns höher: zusätzliches Projekt beziehungsweise Space einrichten und den GitHub-Code anbinden. [Entwicklungsinformationen](https://support.atlassian.com/jira-software-cloud/docs/view-development-information-for-an-issue/) | Für uns höher: Organisation und Projekt mit Prozess einrichten; für GitHub-Verknüpfungen eine Verbindung konfigurieren. [Voraussetzungen](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops) |
| Verknüpfung mit Code | Issue und PR im selben Repository; `Closes #4` verknüpft den PR und schliesst das Issue beim Merge in den Standardbranch. [Verknüpfung](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) | Nach Anbindung eines Entwicklungstools zeigt das Work Item unter **Development** zum Beispiel Branches, Commits und PRs. [Development](https://support.atlassian.com/jira-software-cloud/docs/view-development-information-for-an-issue/) | Nach GitHub-Anbindung verknüpft zum Beispiel `AB#123` in einer Commit-Nachricht oder PR-Beschreibung das Work Item. [GitHub-Verknüpfung](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops) |
| Automatisierung | GitHub Actions führt Workflows bei Ereignissen wie PRs aus; für Tests und Auslieferung verwendbar. [Actions](https://docs.github.com/en/actions/get-started/understand-github-actions) | Atlassian Automation automatisiert Abläufe; Nutzung ist tarifabhängig begrenzt. Code-Tests benötigen eine angebundene CI. [Automation](https://support.atlassian.com/cloud-automation/docs/jira-cloud-automation/) | Azure Pipelines automatisiert Build, Tests und Auslieferung; Kontingente und Zugänge separat beachten. [Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) |

## Unsere Empfehlung

Wir empfehlen **GitHub Issues** für dieses Projekt. Laurentiu hat vor der
Empfehlung als eigenen Grund genannt: „Code und Aufgaben an einem Ort“.
Das passt zu unserem vorhandenen Repository, den Issues mit prüfbaren
Akzeptanzkriterien, der Zuordnung zu Personen und dem Meilenstein `1.0.0`.

Mit drei Personen und einem Tag Zeit bringt ein Werkzeugwechsel aus unserer
Sicht wenig Nutzen. Wir können jede Anforderung über Issue, Branch, Commit
und Pull Request nachvollziehen und die vorhandene CI weiterverwenden.
Jira und Azure Boards bieten ebenfalls Aufgabenverwaltung und
Code-Verknüpfungen; für uns würde die zusätzliche Einrichtung Zeit kosten.
Alle drei haben einen kostenlosen Einstieg für unsere Teamgrösse, daher
entscheiden hier vor allem der vorhandene Ablauf und die kurze Frist.

Unser Ablauf: Akzeptanzkriterien im Issue festhalten, Person und Meilenstein
setzen, im eigenen Branch zuerst Tests schreiben, dann implementieren und
einen PR mit `Closes #...` öffnen. Merge erst nach fremder Freigabe und grüner
CI. Die vorhandene `ci.yml` prüft Formatierung, Lint und Tests; eine automatische
Auslieferung muss in einem eigenen Deployment-Workflow eingerichtet sein.
