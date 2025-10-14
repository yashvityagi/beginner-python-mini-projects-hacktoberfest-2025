# Simple Weather App (OpenWeatherMap API)

---

## Features
- Fetches real-time weather data for any city
- Displays:
  - Temperature in Celsius
  - Weather condition (clear, cloudy, rain, etc.)
  - Humidity
  - Wind speed
- Simple command-line interface

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YourGitHubUsername/beginner-python-mini-projects-hacktoberfest-2025.git
```

### 2. Navigate to the project folder
```bash
cd beginner-python-mini-projects-hacktoberfest-2025/src/DinethShakya23-create-a-weather-app-using-openweathermap-api
```

### 3. (Optional) Create and activate a virtual environment
```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```
### 4. Install dependencies
```bash
pip install requests
# Or, if using requirements.txt:
pip install -r requirements.txt
```

### 5. Add your OpenWeatherMap API key

- Open "weather_app.py" and replace "API_KEY" with your own key (obtained from https://openweathermap.org).

### 6. Run the script
```bash
python weather_app.py
```