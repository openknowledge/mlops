# Talk: Monitoring von Drift mit Prometheus, Grafana und Evidently

## Abstract

Data2Day
https://www.data2day.de

https://www.data2day.de/veranstaltung-15048-0-monitoring-von-drift-mit-prometheus-grafana-und-evidently.html

Mi: 10:15 - 11:00

Monitoring von Drift mit Prometheus, Grafana und Evidently

Talk: 45 Minuten

Machine-Learning-Modelle erfordern besondere Maßnahmen beim Monitoring. Die Vorhersagekraft des Modells ist dabei
besonders wichtig, aber oft nicht direkt beobachtbar.

In diesem Live-Demo ohne Folien sehen wir uns eine Machine Learning Anwendung an, die mit einem bestimmten Modell in
Produktion gegangen ist. Das Model basiert auf TensorFlow und wir mit einem Flask über Docker serviert. In simulierten
Anfragen detektieren wir einen Drift, der einen Alarm in Grafana auslöst. Diesen interpretieren wir und entscheiden, ob
er kritisch und was die passende Maßnahme ist.


Die Teilnehmenden bekommen einen Eindruck von einem realistischen Setup für das Monitoring von Drift. Es wird erklärt,
warum das so wichtig ist und wie man eine passende Maßnahme ableitet

## Vorbereitung

* Stift einsatzbereit (geladen)
* Notebook vorbereiten:
  * conda activate mlops-workshop-d2d
  * jupyter notebook
  * analysis notebook ansehen
* Installation einmal platt machen: `docker compose down --volumes --rmi all`
* Und wieder hoch fahren dabei alles neu bauen und alle images neu ziehen: `docker compose up --build`

## Ablauf

### Phase 0
1. Ablauf: https://miro.com/app/board/uXjVPWwLbm8=/?share_link_id=448518887103
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
      1. Die Sicherheit der Autos wird immer besser und der Einfluss der individuellen Fahrleistung wird verringert (emergency_breaking, pred) 
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
  1. analysis notebook

### Zusammenfassung