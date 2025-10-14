import requests

API_KEY = "Place your OpenWeatherMap API key here"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    try:
        # Build request URL
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found. Please check the name and try again.")
            return

        # Extract relevant data
        city = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display data
        print(f"\n🌤️  Weather in {city}")
        print(f"🌡️  Temperature: {temperature}°C")
        print(f"☁️  Condition: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️  Wind Speed: {wind_speed} m/s")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("=== Simple Weather App ===")
    city = input("Enter a city name: ").strip()
    get_weather(city)
