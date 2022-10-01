# Talk: MlOps - concepts, not tools

Talk: 45 Minuten

## Hot Spot MLOps - Experiences in engineering AI-enabled systems

https://www.linkedin.com/events/hotspotmlops-experiencesinengin6950049203809079296/about/

fortiss cordially invites you in cooperation with the Technical University of Munich (TUM) and the Software Engineering Research Lab Sweden (SERL) to our first Hot Spot workshop.

We feature invited talks given by our industry partners and focus on discussing contemporary practices and experienced challenges along the development of AI-enabled software systems and on the topic of MLOps.

YouTube link: https://youtu.be/IoRgfrYJpjc

Preliminary program:
13:00 - 13:15 Welcome by Johannes Kroß (fortiss), Daniel Mendez (BTH & fortiss) and Alexander Pretschner (TUM & fortiss)

13:15 - 14:00 “Operationalizing a responsible approach to AI” by Courtney Bowman (Palantir)

14:00 - 14:45 “MLOps - concepts, not tools” by Oliver Zeigermann (open knowledge GmbH)

15:15 - 16:00 “How much data do we need? Predicting Deep Learning model performance and training data sizes” by Jelena Frtunikj (Argo AI)

16:00 - 16:45 “Contemporary challenges in the engineering of ML-enabled systems - an experience report” by Mustafa K. Isik (Amazon Web Services)

16:45 - 17:00 Closing summary

## Abstract

MlOps - concepts, not tools

Artificial intelligence is no magic and machine learning is just an alternative way of developing software. Thus most of what applies to the traditional way of writing software also is valid for machine learning projects.

This is a challenge since data scientists are often not familiar with basic concepts of software engineering
like refactoring, versioning, continuous integration, and automated testing. On the other hand traditional software developers often lack the
knowledge of the special requirements of a machine learning project.

In this talk I will argue that tools alone can not solve MLOps,
since the awareness of the challenges both for data science and software development as a combination need to be addressed first.
What process should be followed and what tasks need to be performed at each step is the main topic of this talk.

## Vorbereitung

* Nochmal vergägenwärtigen
  * 0: high risk
  * 1: medium risk
  * 2: low risk
* Ablauf ausdrucken
* https://miro.com/app/board/uXjVPU_-X2I=/
  * Übersetzen auf Englisch
* OK Seite auf
* Stift einsatzbereit (geladen)
* Installation einmal platt machen: `docker compose down --volumes --rmi all`
* Und wieder hoch fahren dabei alles neu bauen und alle images neu ziehen: `docker compose up --build`
* Notebooks starten und ausführen
  * http://localhost:8888/notebooks/notebooks/exploration.ipynb
  * http://localhost:8888/notebooks/notebooks/analysis.ipynb
  * Terminal/Bash im Notebook Server aufmachen

## Ablauf

### Phase 0
1. Ablauf: https://miro.com/app/board/uXjVPU_-X2I=/
1. Problemstellung: innovative Kfz-Versicherungsgesellschaft

### Phase I  
1. Exploration durchgehen: http://localhost:8888/notebooks/notebooks/exploration.ipynb
  1. Features
  1. Was wollen wir vorhersagen?

### Phase II  
1. Professionalisierung: Notebook in Libs und Scripte
1. Build: Scripte manuell laufen lassen
  1. `(mlops-workshop-d2d) olli@DESKTOP-BEN73DP:~/mlops-data2day/scripts$ ./train.py -d ../data/reference.csv -m classifier`
  1. `(mlops-workshop-d2d) olli@DESKTOP-BEN73DP:~/mlops-data2day/scripts$ ./validate.py -d ../data/reference.csv -m classifier`
  1. Modell in model Ordner schieben
  1. Diskussion: Modell und Daten sind groß oder Binary, versionieren, aber nicht in Git

### Phase III
1. Betrieb
  1. `http://localhost:8080/ping`
  1. `http://localhost:8000/client.html`
  1. in `app/client.html` Werte anpassen, Power 20, Fallback besprechen
  1. Diskussion
     * Sollten wir unser Modell für jede Anfrage verwenden?
     * Sollten wir alle gültigen Vorhersagen nutzen?
1. Produktion simulieren
    1. wir simulieren 3 Jahre Betrieb mit
    1. `(mlops-workshop-d2d) olli@DESKTOP-BEN73DP:~/mlops-data2day$ ./scripts/example_run_request.py` 
    1. `http://localhost:8085/metrics`
    1. `http://localhost:3000/d/U54hsxv7k/evidently-data-drift-dashboard?orgId=1&refresh=5s`
1. Analyse   
  1. Drift ist offensichtlich, aber gibt es überhaupt ein Problem?
  1. Interpretation
      1. Leute werden immer Älter, das passiert aber langsam (age)
      1. Es wird immer weniger Auto gefahren, Leute steigen um auf die Bahn und öffentliche Verkehrsmittel (miles)
      1. Die Sicherheit der Autos wird immer besser und der Einfluss der individuellen Fahrleistung wird verringert (emergency_braking, pred) 
  1. Optional, wenn noch genug Zeit: Grafana Alarm dazu bauen    
  1. Letztlich bekommen wir GT rein von Daten, die 2 Jahre alt sind
  1. `(mlops-workshop-d2d) olli@DESKTOP-BEN73DP:~/mlops-data2day/scripts$ ./validate.py -d ../data/month-12.csv -m classifier`
  1. Performance des Modells ist stark zurück gegangen
  1. Wir sollten neu trainieren: zurück zu Phase II 
  1. `(mlops-workshop-d2d) olli@DESKTOP-BEN73DP:~/mlops-data2day/scripts$ ./train.py -d ../data/month-12.csv -m classifier`
  1. Neues Modell erfüllt nicht mehr unsere Anforderungen: zurück zu Phase I
     1. http://localhost:8888/notebooks/notebooks/analysis.ipynb
     1. Anforderungen ändern?
     1. Modell tunen?

### Zusammenfassung

Die Detail-Phasen noch einmal durchgehen