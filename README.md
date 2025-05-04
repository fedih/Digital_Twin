# Weather-City Digital Twin

[![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/weather-city-twin/ci.yml)](https://github.com/yourusername/weather-city-twin/actions)
[![License](https://img.shields.io/github/license/yourusername/weather-city-twin)](LICENSE)

## 📖 Project Overview

Weather-City Digital Twin is a real-time dashboard application that displays the current and forecasted weather data for any selected city. It polls the [OpenWeatherMap Current Weather Data API](https://openweathermap.org/api) at configurable intervals, stores results in a real-time data store, and pushes live updates to a web frontend via WebSockets.

### Key Features

* **Live Weather Updates**: Current temperature, humidity, wind speed, and conditions refreshed every minute.
* **Forecast Visualization**: 5-day forecast chart with interactive graphs.
* **Real-Time Architecture**: Backend powered by Django, Celery (or Django-beat), Redis (or a time-series DB), and Django Channels.
* **Responsive Frontend**: Dynamic widgets and charts built with React/Vue (or vanilla JS) and Chart.js.
* **Scalable Deployment**: Containerized with Docker, deployable on Kubernetes or Docker Compose.

## 🚀 Quickstart

### Prerequisites

* Python 3.10+ and pip
* Docker & Docker Compose (for containerized setup)
* Redis server (or InfluxDB)
* OpenWeatherMap API key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/weather-city-twin.git
   cd weather-city-twin
   ```

2. **Create a virtual environment & install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**
   Create a `.env` file in the project root:

   ```dotenv
   DEBUG=True
   SECRET_KEY=<your-secret-key>
   OPENWEATHER_API_KEY=<your-openweathermap-api-key>
   REDIS_URL=redis://localhost:6379/0
   ```

4. **Initialize the Database & Redis**

   ```bash
   python manage.py migrate
   # Ensure Redis is running on REDIS_URL
   ```

5. **Start Celery (or Django-beat)**

   ```bash
   # Using Celery
   celery -A weather_city_twin worker -B --loglevel=info

   # OR using django-beat
   python manage.py runserver
   ```

6. **Run the Django Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Dashboard**
   Open your browser at `http://127.0.0.1:8000` and select a city to start viewing live weather data.

## 📐 Architecture

```text
+----------------+        +---------------+       +-------------------+
|                |        |               |       |                   |
| OpenWeatherMap | <----> | Celery Beat   |       | Redis / TS-DB     |
|   API          |        | (Django-beat) |       | (Real-time store) |
+----------------+        +---------------+       +-------------------+
                                   |
                                   v
                          +-------------------+    +---------------+
                          | Django Channels   | -> | WebSocket API |
                          +-------------------+    +---------------+
                                   |
                                   v
                           +-----------------+
                           | Frontend (React |
                           | /Vue /Chart.js) |
                           +-----------------+
```

1. **Poller**: Celery (or Django-beat) worker fetches weather every minute.
2. **Storage**: Raw JSON parsed into Django models and pushed into Redis (or a time-series DB).
3. **WebSockets**: Django Channels broadcasts updates to subscribed clients.
4. **Frontend**: Connects via WebSocket, renders live data and forecast charts.

## 🛠️ Configuration

* **POLL\_INTERVAL**: Interval in seconds for API polling (default: 60).
* **MAX\_HISTORY**: Number of historical entries to retain in Redis.

Set these in `.env` or your deployment environment.

## 🚢 Deployment

### Docker Compose

```bash
# Build and start services
docker-compose up --build -d

# Stop and remove services
docker-compose down
```

### Kubernetes

1. Build Docker images and push to registry.

2. Apply Kubernetes manifests:

   ```bash
   kubectl apply -f k8s/deployment.yml
   kubectl apply -f k8s/service.yml
   ```

3. Configure Ingress and environment secrets.

## ⚙️ Monitoring & Logging

* **Metrics**: Prometheus scraping `/metrics` endpoint.
* **Dashboards**: Grafana pre-configured panels for API latency, poll success rate, WebSocket connections.
* **Logs**: Structured JSON logs sent to stdout, aggregable by EFK/ELK stacks.

## 🏗️ Future Enhancements

1. Multi-city support with topic-based channels
2. Historical playback with time-slider
3. Threshold-based alerts (email, Slack)
4. Geo-visualization with Leaflet/OpenLayers
5. Mobile App or Progressive Web App (PWA)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Open a Pull Request
