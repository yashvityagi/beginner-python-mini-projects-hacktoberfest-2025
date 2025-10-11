from weather.api import get_weather
from weather.config import API_KEY

def main():
    print("=== 🌍 Simple Weather App ===")
    city = input("Enter city name: ").strip()
    if not city:
        print("⚠️ Please enter a city name.")
        return
    get_weather(city, API_KEY)

if __name__ == "__main__":
    main()
