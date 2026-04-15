# 🌐 Day 8 — API Integration (Real-World Apps)

Welcome to **Day 8** of your Streamlit journey!
Today, you’ll learn how to connect your app to **real-world data** using APIs.

---

## 📌 What You’ll Learn

* What an API is
* How to fetch data from APIs
* Use the `requests` library
* Display live data in your app

---

## ⚙️ Installation

Install the required library:

```bash id="m8k2qp"
pip install requests
```

---

## 📂 Project Structure

```id="v4n9xs"
Day 8 — API Integration/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="q7p3zm"
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
```

---

## 🔑 Get Your API Key

1. Visit: https://openweathermap.org/api
2. Create a free account
3. Generate your API key
4. Replace this line in code:

```python
API_KEY = "your_api_key_here"
```

---

## ▶️ Run the App

```bash id="z1k8qr"
streamlit run app.py
```

Then open:

```id="p3m6xy"
http://localhost:8501
```

---

## 🎯 Project Overview

This app allows users to:

* Enter a city name 🏙️
* Fetch live weather data 🌐
* Display temperature, humidity, and conditions 🌦️

👉 This is your first **real-world API-powered app**

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Add Country Code

```python id="c6t2lp"
country = st.text_input("Enter country code (e.g. BD, US)")
```

Update API query:

```python id="n5r8xm"
q={city},{country}
```

---

### 🔹 Show Wind Speed

```python id="b4k7zn"
wind = data["wind"]["speed"]
st.write(f"🌬️ Wind Speed: {wind} m/s")
```

---

### 🔹 Show Weather Icon

```python id="y2p9qs"
icon = data["weather"][0]["icon"]
icon_url = f"http://openweathermap.org/img/wn/{icon}.png"
st.image(icon_url)
```

---

### 🔹 Add Refresh Button

* Allow users to reload data easily

---

## 🚀 What You Learned

* How to connect apps to external APIs
* How to fetch and display live data
* How to handle API responses and errors
* How to build dynamic applications

---

## 💡 Notes

* Always check `response.status_code`
* Handle errors properly
* Keep API keys secure (do not share publicly)

---

## ➡️ Next Step

Move to **Day 9 — Advanced Features** (multi-page apps + caching + performance 🚀)

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
