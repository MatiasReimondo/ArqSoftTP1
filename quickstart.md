# Quickstart

## Node

1. `docker-compose up` (agregar -d si no querés que te bloquee la terminal)
1. En el browser entrar a `localhost`. Te va a pedir un login: usuario `admin`, password `admin`
1. Configurar grafana, metiendo a Graphite como data source

![graphite](./images/graphite.png)


1. Importar el dashboard provisto, en el panel a la izquierda tocar el `+`, "Import" y arriba a la derecha "Upload json file". El archivo está en el repo, perf/dashboard.json

![import](./images/import_dashboard.png)

1. Entrar al dashboard. Seleccionar server: `artillery-node` y container: `1c20-tp-1-nginx_1`
1. Correr el script de artiller. En `perf`, correr `npm install` y luego `./run-scenario.sh root node`. Luego de un minuto deberían aparecer resultados en el dashboard:

![dashboard](./images/dashboard.png)

1. Para correr las pruebas en el servidor de python `./run-scenario.sh root gunicorn`. Seleccionar server: `artillery-gunicorn` y container: `1c20-tp-1-nginx_1` para ver datos del server