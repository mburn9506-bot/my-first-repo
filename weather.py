import requests
import yaml

# Load YAML configuration
def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def get_weather(city_name):
    config = load_config()

    base_url = config["api"]["base_url"]
    api_key = config["api"]["api_key"]
    units = config["api"].get("units", "metric")

    params = {
        "q": city_name,
        "appid": api_key,
        "units": units
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]

        print(f"🌍 City: {data['name']}")
        print(f"🌡️ Temperature: {main['temp']}°C")
        print(f"☁️ Weather: {weather['description'].capitalize()}")
        print(f"💨 Humidity: {main['humidity']}%")
    else:
        print("❌ Error fetching weather data:", response.status_code)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
# run the app "python3 weather.py" in terminal
