# Anwendungsfall 2: Quantum Humanities

Dieser Anwendungsfall zeigt die Modellierung und Ausführung eines Quanten-Workflows zur Orchestrierung folgender Bearbeitungsschritte im Bereich der Quantum Humanities:

1. Klassische Vorverarbeitung von Kostümdaten

2. Berechnung von Clustern mittels des k-Means Algorithmus auf einem Quantencomputer

3. Trainieren eines Classifiers auf einem Quantencomputer

4. Klassische Evaluation des trainierten Classifiers

## Setup

Alle Komponenten des Anwendungsfalls können mittels [Docker-Compose](https://docs.docker.com/compose/) gestartet werden, wobei ein entsprechendes Docker-Compose File [hier](./docker/docker-compose.yml) verfügbar ist:

1. Zunächst muss die IP-Adresse der Maschine, auf der die Docker Engine läuft, in das [.env](./docker/.env) eingetragen werden:
  * ``PUBLIC_HOSTNAME``: Die IP-Adresse muss öffentlich zugänglich sein und es darf *nicht* ``localhost`` verwendet werden.

2. Ausführen des Docker-Compose Files:
```
cd docker
docker-compose pull
docker-compose up
```
3. Nach einigen Minuten sind alle Komponenten verfügbar.

## Modellieren und Ausführen des Anwendungsfalls

Der Quantum Workflow Modeler ist unter folgender URL verfügbar: [http://localhost:8080](http://localhost:8080)

Anschließend wird der folgende Bildschirm angezeigt:

![Übersicht über den Modeler](./docs/modeler-overview.jpg)

Der Workflow für diesen Anwendungsfall ist [hier](./workflow/quantum-humanities-workflow.bpmn) verfügbar und kann mittels ``Open`` oben links im Modeler geöffnet werden:

![Übersicht über den Workflow](./docs/workflow-overview.jpg)

TODO