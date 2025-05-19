Digital Twin Météo

Ce projet implémente un Digital Twin pour un système météorologique, inspiré de l'architecture « Airplane Cabin Digital Twin ». Il permet de simuler, collecter, stocker et visualiser en temps réel des données météo (température, humidité, pression, etc.).

1. Architecture Générale
   flowchart LR
  subgraph Data Pipeline
    A[Simulateur de Capteurs] -->|NGSIv2 données réelles| B[Orion Context Broker]
    B -->|Persistance| C[(MongoDB)]
    C --> D[API d'Inspection (Express)]
  end

  subgraph Conversion
    D -->|NGSIv2 to TS| E[QuantumLeap]
  end

  subgraph Time-Series & Visualisation
    E -->|stockage timeseries| F[(CrateDB)]
    F -->|live visualization| G[Grafana]
  end

2. Prérequis

Docker & Docker Compose

Node.js & npm

Python 3.8+

MongoDB (inclus via Docker)

CrateDB (inclus via Docker)

Grafana (inclus via Docker)

PostgreSQL (optionnel si besoin de retentions avancées)


3. Installation
   1. Cloner le dépôt:
      git clone https://github.com/votre-repo/digital-twin-meteo.git
      cd digital-twin-meteo
   2. Configurer les variables d'environnement

      Copier le fichier .env.example en .env

      Adapter les paramètres :
      ORION_HOST=orion
   ORION_PORT=1026
   MONGO_HOST=mongo
   MONGO_PORT=27017
   CRATEDB_HOST=cratedb
   CRATEDB_PORT=4200
   QUANTUMLEAP_HOST=quantumleap
   QUANTUMLEAP_PORT=8668
   GRAFANA_PORT=3000
3. Démarrer les services avec Docker Compose:
   docker-compose up -d
4. Modules principaux

Simulateur de Capteurs (Python)

Génère des mesures simulées (température, humidité, pression)

Envoie des entités NGSIv2 vers Orion à intervalles réguliers

Orion Context Broker

Reçoit et stocke le contexte des capteurs

Permet l’interrogation et la subscription aux mises à jour

MongoDB

Persistance historique des données de contexte

API d’Inspection (Node.js / Express)

Point d’accès pour interroger et valider les données stockées

QuantumLeap

Convertit les entités NGSIv2 en série temporelle

Envoie les séries vers CrateDB

CrateDB

Stockage des données temps réel et historique en séries temporelles

Grafana

Dashboards dynamiques pour visualiser l’évolution des mesures

5. Lancement et Tests

Vérifier les logs:

docker-compose logs -f

Simuler des données:

cd simulator
python3 simulate_meteo.py

Accéder à Grafana:

URL : http://localhost:3000

Login par défaut : admin / admin

Importer le dashboard dash_meteo.json

6. Développement et extensions

Ajouter de nouveaux capteurs : Modifier simulate_meteo.py et le modèle NGSIv2

Alertes et subscriptions : Configurer des subscriptions dans Orion

Stockage longue durée : Archiver MongoDB ou CrateDB

Scalabilité : Orchestrer via Kubernetes
