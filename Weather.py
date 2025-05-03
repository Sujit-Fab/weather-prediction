import requests
import pandas as pd

def get_weather_forecast(latitude=23.8103, longitude=90.4125):
    """Fetch weather data for Bangladesh (default: Dhaka)."""
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=rain_sum,temperature_2m_max&timezone=auto"
    response = requests.get(api_url)
    data = response.json()
    
    return pd.DataFrame({
        "Date": data["daily"]["time"],
        "Rainfall (mm)": data["daily"]["rain_sum"],
        "Max Temp (°C)": data["daily"]["temperature_2m_max"]
    })
