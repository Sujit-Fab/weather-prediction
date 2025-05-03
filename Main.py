import streamlit as st
from weather import get_weather_forecast  # Import from weather.py

st.title("My Analytics Tool")
weather_df = get_weather_forecast()  # Fetch weather data
st.line_chart(weather_df.set_index("Date"))
