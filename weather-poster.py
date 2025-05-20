import requests
import time

# === CONFIGURATION ===
CITY_NAME = "Tunis"  # Modifie si besoin
API_KEY = "VOTRE_CLÉ_API_OPENWEATHERMAP"  # Remplace par ta clé
ORION_URL = "http://localhost:1026/v2/entities"
HEADERS = {
    "Content-Type": "application/json",
    "Fiware-Service": "weather",
    "Fiware-ServicePath": "/"
}

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def send_to_orion(data):
    entity = {
        "id": f"WeatherObserved:{data['id']}",
        "type": "WeatherObserved",
        "temperature": {"value": data["main"]["temp"], "type": "Number"},
        "humidity": {"value": data["main"]["humidity"], "type": "Number"},
        "pressure": {"value": data["main"]["pressure"], "type": "Number"},
        "location": {
            "type": "geo:point",
            "value": f"{data['coord']['lat']},{data['coord']['lon']}"
        }
    }

    res = requests.post(ORION_URL, json=entity, headers=HEADERS)
    print("POST status:", res.status_code)
    if res.status_code >= 400:
        print(res.text)

while True:
    print("Fetching weather data...")
    weather_data = get_weather()
    send_to_orion(weather_data)
    print("Data sent to Orion. Waiting 5 minutes...")
    time.sleep(300)  # Attendre 5 minutes
