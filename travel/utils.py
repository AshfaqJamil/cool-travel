from http import HTTPStatus
import requests
from datetime import datetime
from .models import District, WeatherData

def fetch_weather_data(district):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": district.latitude,
        "longitude": district.longitude,
        "hourly": "temperature_2m",
        "forecast_days": 7
    }
    response = requests.get(url, params=params)
    if response.status_code == HTTPStatus.OK.value:
        weather_data = response.json()
        temperatures = weather_data.get("hourly", {"temperature_2m": []}).get("temperature_2m")
        times = weather_data.get("hourly", {"time": []}).get("time")

        WeatherData.objects.filter(district=district).delete()

        for i in range(0, len(times), 24):
            date = datetime.strptime(times[i], '%Y-%m-%dT%H:%M').date()
            temperature_at_2pm = temperatures[i + 14]
            WeatherData.objects.create(
                district=district,
                date=date,
                temperature_at_2pm=temperature_at_2pm
            )
        return True
    return False