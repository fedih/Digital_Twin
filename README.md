# 🌦 Digital Twin Weather Project  
Real-time weather monitoring using FIWARE, QuantumLeap & Grafana  

![Architecture](https://github.com/user-attachments/assets/2464ea09-affe-4454-bf6c-aa3b4f04f4ba)


 🌟 Features
- 5-min weather updates from OpenWeatherMap API
- NGSI-v2 entities in FIWARE Orion
- Historical storage in CrateDB
- Grafana dashboards with real-time metrics

 🏗 Architecture
```mermaid
graph TD
    A[Python Script] -->|NGSI-v2| B(Orion Context Broker)
    B -->|Subscription| C(QuantumLeap)
    C -->|Time Series| D[CrateDB]
    D -->|SQL Queries| E[Grafana]

🛠 Prerequisites
Windows 11 + WSL 2

Docker Desktop (WSL backend)

OpenWeatherMap API Key
🚀 Quick Start
git clone https://github.com/tonpseudo/digital-twin-weather.git
cd digital-twin-weather

 Set API key in weather-poster.py (Line 8)
nano weather-poster.py

 Launch services
docker-compose build && docker-compose up -d
🌐 Services & Endpoints
Service	URL	Credentials
Orion	http://localhost:1026	-
Mongo Express	http://localhost:8081	admin:pass
CrateDB	http://localhost:4200	-
Grafana	http://localhost:3000	admin:admin

🔄 Data Flow
Python script polls API every 5 mins

Creates WeatherObserved entities in Orion

QuantumLeap stores historical data in CrateDB

Grafana visualizes via SQL queries:

SELECT entity_id, temperature, time_index 
FROM "mtweatherobserved" 
WHERE entity_id = 'WeatherObserved-Paris'
📜 License
MIT Licensed - See LICENSE

