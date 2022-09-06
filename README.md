# ML Ops Data2Day

### Docker

For this workshop you will need [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) running on your machine. *(on mac os and Windows docker-compose is installed with Docker by default)*

#### Run the application, Monitoring Server, Prometheus and Grafana in Docker

To build the application Docker image and start the application container,  as well as Prometheus and Grafana together, run the following command (from the root of this repo):

``` sh
docker-compose up --build
```

*If you see errors it may be because you still have the previous version of the application running and therefore might be using the same port as you are now trying to access with Docker. Or the ports interfere with local installations. A local Grafana installation probably runs on port 3000 as a service.*

You should then be able to access the Prometheus dashboard on `http://localhost:9090` and Grafana on `http://localhost:3000`.

### Local installation for development

Create an `mlops-workshop` conda environment executing:

```
$ conda env create -f environment.yml
```

For Apple with an M1 processor install the the appropriate [Miniconda](https://docs.conda.io/en/latest/miniconda.html) version. You can create the `mlops-workshop` conda environment executing:

```
$ conda env create -f environment-m1.yml
```

and later activate the environment:

```
$ conda activate mlops-workshop-d2d
```

### Monitoring Drift

Monitoring is based on https://github.com/evidentlyai/evidently/tree/main/examples/integrations/grafana_monitoring_service and code is copied from there. Start monitoring as described there.
