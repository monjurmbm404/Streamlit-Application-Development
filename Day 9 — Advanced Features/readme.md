# 🚀 Day 9 — Advanced Features (Multi-Page, Caching & Performance)

Welcome to **Day 9** of your Streamlit journey!
Today, you’ll learn how to build **scalable, fast, and well-structured apps** using advanced features.

---

## 📌 What You’ll Learn

- Multi-page app structure
- Caching for performance optimization
- Loading indicators & user feedback
- Best practices for scalable apps

---

## 📂 Project Structure

```id="t5k2qp"
Day 9 — Advanced Features/
│
├── app.py
├── data.csv
└── pages/
    ├── 1_📊_Dashboard.py
    ├── 2_📂_Data_View.py
    └── 3_⚙️_Settings.py
```

---

## 🧩 Code Overview

### 🔹 Main App (`app.py`)

```python id="u9m3xs"
import streamlit as st

st.set_page_config(page_title="Advanced App", layout="wide")

st.title("🏠 Home Page")
st.write("Welcome to your advanced Streamlit app!")

st.info("Use the sidebar to navigate between pages")
```

---

### 🔹 Dashboard Page

```python id="k4p8zn"
import streamlit as st
import pandas as pd
import time

st.title("📊 Dashboard")

@st.cache_data
def load_data():
    time.sleep(2)
    return pd.read_csv("data.csv")

with st.spinner("Loading data..."):
    df = load_data()

st.success("Data loaded successfully!")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rows", df.shape[0])
col2.metric("Average Age", int(df["age"].mean()))
col3.metric("Average Salary", int(df["salary"].mean()))

st.line_chart(df["age"])
st.bar_chart(df["salary"])
```

---

### 🔹 Data View Page

```python id="n7r2xm"
import streamlit as st
import pandas as pd

st.title("📂 Data Viewer")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

name_filter = st.text_input("Filter by name")

if name_filter:
    df = df[df["name"].str.contains(name_filter, case=False)]

st.dataframe(df)
```

---

### 🔹 Settings Page

```python id="b3k9qs"
import streamlit as st

st.title("⚙️ Settings")

if "username" not in st.session_state:
    st.session_state.username = ""

name = st.text_input("Enter your name")

if name:
    st.session_state.username = name

st.write("Current user:", st.session_state.username)
```

---

## ▶️ Run the App

```bash id="v2m8xr"
streamlit run app.py
```

Then open:

```id="c9p4zn"
http://localhost:8501
```

---

## 🎯 Project Overview

This advanced app includes:

- 🧭 Multi-page navigation
- ⚡ Cached data loading
- 📊 Dashboard with metrics & charts
- 🔍 Data filtering
- ⚙️ User settings with session state

---

## ⚡ Caching Explained

```python id="f6t2lp"
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

### ✅ Benefits:

- Faster app performance
- Avoid repeated computations
- Efficient data handling

---

## 🚀 Performance Features

- `st.cache_data` → speeds up data loading
- `st.spinner()` → shows loading status
- Efficient filtering → avoids unnecessary processing

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Cache API Calls

```python id="q4n7xs"
@st.cache_data
def fetch_data():
    return requests.get(url).json()
```

---

### 🔹 Add Loading Animation

```python id="m8k3zn"
with st.spinner("Processing..."):
    time.sleep(2)
```

---

### 🔹 Share Data Across Pages

- Use `st.session_state` to share values

---

### 🔹 Add Navigation Instructions

- Improve UX with sidebar guidance

---

## 🚀 What You Learned

- How to build multi-page apps
- How to optimize performance
- How to structure real-world projects
- How to combine multiple advanced features

---

## 💡 Notes

- Use caching for heavy operations
- Keep pages modular and clean
- Optimize before scaling apps

---

## ➡️ Next Step

Move to **Day 10 — Final Project & Deployment** to publish your app online 🌍

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
