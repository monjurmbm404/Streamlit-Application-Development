# 📂 Day 3 — CSV Data Viewer App

Welcome to **Day 3** of your Streamlit journey!
Today, you’ll build a **powerful data app** that can upload, view, and explore CSV files.

---

## 📌 What You’ll Learn

* Upload files using Streamlit
* Read CSV files using pandas
* Display datasets
* Basic data exploration
* Filtering data

---

## 📂 Project Structure

```id="g8v2kx"
Day 3 — Data Handling/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="w0z4cn"
import streamlit as st
import pandas as pd

st.title("📂 CSV Data Viewer App")

st.write("Upload a CSV file to explore your data")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show raw data
    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Show basic info
    st.subheader("📊 Data Summary")

    st.write("Shape of dataset:", df.shape)
    st.write("Columns:", df.columns.tolist())

    # Select column
    column = st.selectbox("Select a column to explore", df.columns)

    # Show column data
    st.subheader(f"🔍 Data in '{column}'")
    st.write(df[column])

    # Show statistics (if numeric)
    if pd.api.types.is_numeric_dtype(df[column]):
        st.subheader("📈 Statistics")
        st.write(df[column].describe())

    # Filter data
    st.subheader("🔎 Filter Data")

    value = st.text_input("Enter value to filter:")

    if value:
        filtered_df = df[df[column].astype(str).str.contains(value)]
        st.write(filtered_df)

else:
    st.info("Please upload a CSV file to get started.")
```

---

## ▶️ Run the App

```bash id="d9j2ap"
streamlit run app.py
```

Then open:

```id="k4q9zm"
http://localhost:8501
```

---

## 🎯 Project Overview

This app allows users to:

* Upload any CSV file 📂
* View full dataset 📄
* Explore specific columns 🔍
* Filter data dynamically ⚡
* View statistics for numeric data 📊

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Show Top Rows

```python id="n7c2qs"
st.write(df.head())
```

---

### 🔹 Show Bottom Rows

```python id="k2c8yn"
st.write(df.tail())
```

---

### 🔹 Toggle Data Display

```python id="r5d1tp"
if st.checkbox("Show raw data"):
    st.dataframe(df)
```

---

### 🔹 Sort Data

```python id="x8p4va"
sorted_df = df.sort_values(by=column)
st.write(sorted_df)
```

---

## 🚀 What You Learned

* How to handle file uploads
* How to work with real datasets
* How to explore and filter data
* How to build data-driven apps

---

## 💡 Notes

* Ensure your CSV file is properly formatted
* Large files may take time to load
* Use filtering to explore data efficiently

---

## ➡️ Next Step

Move to **Day 4 — Charts & Visualization** to turn your data into interactive graphs 📊

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
