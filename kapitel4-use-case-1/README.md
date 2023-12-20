# Anwendungsfall 1: Variationeller Quantenalgorithmus

Dieser Anwendungsfall zeigt die Modellierung und Ausführung eines variationellen Quantenalgorithmus, des [Quantum Approximate Optimization Algorithm (QAOA)](https://arxiv.org/pdf/1411.4028.pdf), zur Lösung des MaxCut Problems mittels QuantMe.

## Setup

Alle Komponenten des Anwendungsfalls können mittels [Docker-Compose](https://docs.docker.com/compose/) gestartet werden, wobei ein entsprechendes Docker-Compose File [hier](./docker) verfügbar ist:

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

Der Quantum Workflow Modeler ist unter folgender URL verfügbar: [localhost:8080](http://localhost:8080)

TODO