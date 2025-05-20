# 🌦 Digital Twin Weather Project  
Real-time weather monitoring using **FIWARE**, **QuantumLeap**, and **Grafana**

---

🌟 Features
- 🌍 Real-time weather updates every 5 minutes from **OpenWeatherMap API**
- 📡 **NGSI-v2** WeatherObserved entities managed by **FIWARE Orion Context Broker**
- 🧠 Historical data storage in **CrateDB** via **QuantumLeap**
- 📊 Custom dashboards in **Grafana** for visualizing metrics

---

🏗 Architecture

![Architecture](https://github.com/user-attachments/assets/2464ea09-affe-4454-bf6c-aa3b4f04f4ba)

---

🛠 Prerequisites
- 🖥 Windows 11 with **WSL 2**
- 🐳 **Docker Desktop** (WSL backend enabled)
- 🔑 **OpenWeatherMap API Key**

---

🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fedih/digital-twin-weather.git
   cd digital-twin-weather
