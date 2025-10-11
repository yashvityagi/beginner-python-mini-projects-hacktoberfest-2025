import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get('cod') != 200:
            print("❌ Error:", data.get('message', 'Unable to fetch data'))
            return

        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        desc = data['weather'][0]['description'].capitalize()
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        print("\n🌦️ Weather Report 🌦️")
        print(f"📍 Location: {city}, {country}")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"🌥️ Condition: {desc}")
        print(f"💧 Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error:", e)
