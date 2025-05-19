# Digital Twin Weather Project

Ce projet met en place une architecture « Digital Twin » pour collecter, stocker et visualiser les données météorologiques d’une ville en temps réel, à l’aide de FIWARE (Orion Context Broker), MongoDB, QuantumLeap, CrateDB et Grafana, le tout orchestré via Docker Compose. Un script Python interroge l’API OpenWeatherMap toutes les 5 minutes et pousse les observations dans Orion. QuantumLeap relaie ensuite ces données vers CrateDB, et Grafana affiche des dashboards dynamiques.

---
flowchart LR
    subgraph Data_Sources
        A[OpenWeatherMap API]
    end

    subgraph Docker_Env
        direction TB
        B[weather-poster<br>(Python)] -->|POST NGSI-v2| C[Orion<br>Context Broker]
        C -->|Subscription| D[QuantumLeap]
        D -->|Time-series Ingest| E[CrateDB]
        F[Grafana] -->|Query SQL| E
    end

    subgraph User
        U(Utilisateur) -->|Web UI| F
    end

    A -->|HTTP Request| B

## 🗂 Structure du dépôt

digital-twin-weather/
├── Dockerfile.weather # Dockerfile pour le conteneur du script Python
├── docker-compose.yml # Définition des services FIWARE, bases et Grafana
├── weather-poster.py # Script Python qui récupère et poste la météo
└── README.md # Ce fichier


---

## 🚀 Prérequis

- Windows 11 avec WSL 2 activé  
- Docker Desktop (intégration WSL)  
- Compte et clé API sur [OpenWeatherMap](https://openweathermap.org/api)  
- (Optionnel) VS Code + extension Remote – WSL  

---

## ⚙️ Installation & démarrage

1. **Clone ce dépôt**  
   ```bash
   git clone https://github.com/tonpseudo/digital-twin-weather.git
   cd digital-twin-weather
2. Configure ta clé API

  Ouvre weather-poster.py

  Remplace API_KEY = "VOTRE_CLÉ_API_OPENWEATHERMAP" par ta clé

3. Lance les conteneurs
   docker-compose build
   docker-compose up -d

4. Vérifie les services

  Orion Context Broker : http://localhost:1026/version
  
  Mongo Express : http://localhost:8081
  
  CrateDB : http://localhost:4200
  
  Grafana : http://localhost:3000
📡 Workflow
Le script weather-poster.py :

Interroge l’API OpenWeatherMap toutes les 5 minutes.

Génère une entité NGSI-v2 WeatherObserved.

Poste dans Orion via l’endpoint /v2/entities?options=upsert.

Subscription Orion → QuantumLeap

Orion notifie QuantumLeap sur les entités WeatherObserved.

QuantumLeap insère ces observations dans CrateDB (index
weatherobserved).

Dashboard Grafana

Data source CrateDB connectée.

Panels « Temperature », « Humidity », « Pressure » en séries temporelles.

🎨 Personnalisation
Modifier la ville : Change CITY_NAME dans weather-poster.py ou via variable d’environnement dans docker-compose.yml.

Intervalle : Ajuste time.sleep(300) dans le script pour modifier la fréquence.

Dashboard : Duplique/édite les panels Grafana pour ajouter d’autres métriques (vent, précipitations, etc.).

📜 Licence
Ce projet est distribué sous la licence MIT. Voir LICENSE pour plus de détails.
