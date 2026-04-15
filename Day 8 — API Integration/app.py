import streamlit as st
import requests

st.title("🌦️ Weather App (API Integration)")

# Input
city = st.text_input("Enter city name:")

# API Key (get from OpenWeatherMap)
API_KEY = "your_api_key_here"

if st.button("Get Weather"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            st.success(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {temp}°C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁️ Condition: {weather}")

        else:
            st.error("City not found ❌")
    else:
        st.warning("Please enter a city name")