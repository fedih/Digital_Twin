🌦 Digital Twin Weather Project
A real-time weather monitoring system using FIWARE, QuantumLeap, and Grafana. Collect, store, and visualize city weather data with Docker-powered architecture.

Architecture Diagram

📋 Table of Contents
Project Overview

Architecture

Prerequisites

Quick Start

Services & Endpoints

Data Workflow

Customization Guide

Troubleshooting

License

🌍 Project Overview
Implements a digital twin pattern to:

Collect weather data from OpenWeatherMap API (5-min intervals)

Store in FIWARE Orion Context Broker

Persist historical data in CrateDB via QuantumLeap

Visualize through Grafana dashboards

🏗 Architecture
Diagram
Code









🛠 Prerequisites
System Requirements

Windows 11 with WSL 2 enabled

Docker Desktop (WSL integration)

API Keys

OpenWeatherMap API Key (Free tier sufficient)

Recommended Tools

VS Code with Remote - WSL extension

Postman for API testing

🚀 Quick Start
1. Clone Repository
bash
git clone https://github.com/tonpseudo/digital-twin-weather.git
cd digital-twin-weather
2. Configure API Key
python
# weather-poster.py (Line 8)
API_KEY = "your_api_key_here"  # Get from OpenWeatherMap
3. Build & Launch Services
bash
docker-compose build  # Build custom Python container
docker-compose up -d  # Start all services in background
4. Verify Deployment
bash
docker-compose ps  # Check container statuses
🌐 Services & Endpoints
Service	URL	Purpose	Credentials
Orion Context Broker	http://localhost:1026	NGSI entity management	-
MongoDB	mongodb://localhost:27017	Orion storage	-
Mongo Express	http://localhost:8081	MongoDB Web UI	admin:pass
QuantumLeap	http://localhost:8668	Historical data bridge	-
CrateDB	http://localhost:4200	Time series storage	-
Grafana	http://localhost:3000	Visualization	admin:admin
🔄 Data Workflow
Data Collection
Python script executes every 5 minutes:

python
while True:
    get_weather_data()
    time.sleep(300)  # 300 seconds = 5 minutes
Entity Creation
Sample NGSI-v2 entity structure:

json
{
  "id": "WeatherObserved-Paris",
  "type": "WeatherObserved",
  "temperature": {"value": 22.3, "type": "Float"},
  "humidity": {"value": 68, "type": "Integer"},
  "pressure": {"value": 1016, "type": "Integer"}
}
Data Persistence
QuantumLeap automatically creates CrateDB table:

sql
CREATE TABLE "mtweatherobserved" (
  "entity_id" TEXT,
  "temperature" FLOAT,
  "humidity" INTEGER,
  "pressure" INTEGER,
  "time_index" TIMESTAMP
);
🛠 Customization Guide
Change Monitored City
Option 1: Edit script directly

python
# weather-poster.py (Line 9)
CITY_NAME = "London"
Option 2: Use environment variable (recommended)

yaml
# docker-compose.yml
services:
  weather-poster:
    environment:
      - CITY_NAME=Berlin
Modify Data Collection Interval
python
# Adjust sleep duration (seconds)
time.sleep(600)  # 10-minute intervals
Grafana Dashboard Enhancements
Add new panels for wind speed:

sql
SELECT entity_id, wind_speed, time_index 
FROM "mtweatherobserved"
ORDER BY time_index DESC
Create precipitation alerts using threshold checks

🚨 Troubleshooting
Common Issues	Solutions
Orion not receiving data	Check Docker logs: docker-compose logs orion
Missing data in CrateDB	Verify QuantumLeap health: curl http://localhost:8668/v2/version
Grafana connection issues	Confirm CrateDB credentials in Data Sources config
API key errors	Validate key at https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}
📜 License
MIT Licensed - See LICENSE for full details.

Maintainer: Your Name | Version: 1.1.0
FIWARE Badge
