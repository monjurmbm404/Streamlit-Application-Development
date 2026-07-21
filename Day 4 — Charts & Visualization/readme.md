# 📊 Day 4 — Charts & Data Visualization

Welcome to **Day 4** of your Streamlit journey!
Today, you’ll transform raw data into **visual insights** using charts and interactive graphs.

---

## 📌 What You’ll Learn

* Create basic charts in Streamlit
* Build interactive visualizations using Plotly
* Select and visualize data columns
* Improve data presentation

---

## 📂 Project Structure

```id="q1n7vc"
Day 4 — Charts & Visualization/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="v9k3tm"
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Visualization App")

st.write("Upload a CSV file and visualize your data")

# Upload file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show dataset
    st.subheader("📄 Dataset")
    st.dataframe(df)

    # Select columns
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    # Basic charts
    st.subheader("📈 Basic Charts")

    st.write("Line Chart")
    st.line_chart(df[[x_axis, y_axis]])

    st.write("Bar Chart")
    st.bar_chart(df[[x_axis, y_axis]])

    # Plotly interactive chart
    st.subheader("🔥 Interactive Chart (Plotly)")

    chart_type = st.selectbox(
        "Select chart type",
        ["Line", "Bar", "Scatter"]
    )

    if chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)

else:
    st.info("Upload a CSV file to start visualizing")
```

---

## ▶️ Run the App

```bash id="u2k8xr"
streamlit run app.py
```

Then open:

```id="p6m4zy"
http://localhost:8501
```

---

## 🎯 Project Overview

This app allows users to:

* Upload a dataset 📂
* Select columns for visualization 🔍
* Generate charts:

  * Line chart 📈
  * Bar chart 📊
  * Scatter plot 🔵
* Explore interactive graphs with zoom & hover

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Add Histogram

```python id="a7d3lp"
fig = px.histogram(df, x=x_axis)
st.plotly_chart(fig)
```

---

### 🔹 Add Color Grouping

```python id="c8x5qm"
color_col = st.selectbox("Color by", columns)
fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col)
st.plotly_chart(fig)
```

---

### 🔹 Limit Rows Displayed

```python id="m4n9zw"
rows = st.slider("Select number of rows", 5, len(df), 10)
st.dataframe(df.head(rows))
```

---

### 🔹 Add Chart Title

```python id="y5t2qa"
fig.update_layout(title="My Custom Chart")
```

---

## 🚀 What You Learned

* How to visualize data using charts
* Difference between static and interactive charts
* How to build user-driven visualizations
* How to improve data storytelling

---

## 💡 Notes

* Choose meaningful columns for better insights
* Use interactive charts for better UX
* Keep visualizations simple and clear

---

## ➡️ Next Step

Move to **Day 5 — Layout & Dashboard Design** to build professional dashboards 🎨

---

# Author

## **Engr. Md Monjur Bakth Mazumder**

🎓 **Secondary School Certificate (SSC) from [Shah Helal High School](https://www.shahhelalhs.edu.bd/)**

🎓 **Diploma in Computer Science and Technology from [Moulvibazar Polytechnic Institute (MPI)](https://mpi.moulvibazar.gov.bd/)**

🎓 **BSc in Computer Science & Engineering (CSE)** _(Ongoing)_ **at [Sylhet International University (SIU)](https://siu.edu.bd/)**

📧 **Email:** monjurmbm404@gmail.com

---

## ⭐ Support the Project

If you found this repository helpful, please consider giving it a **⭐ Star**. It helps others discover the project and motivates future development.

---

## 🌐 Connect with Me

| Platform       | Link                                        |
| -------------- | ------------------------------------------- |
| 💻 GitHub      | https://github.com/monjurmbm404             |
| 💼 LinkedIn    | https://linkedin.com/in/monjurmbm404        |
| 🧩 LeetCode    | https://leetcode.com/u/monjurmbm404         |
| ⚔️ Codeforces  | https://codeforces.com/profile/monjurmbm404 |
| 🍽️ CodeChef    | https://www.codechef.com/users/monjurmbm404 |
| 🏆 VJudge      | https://vjudge.net/user/monjurmbm404        |
| 📘 Facebook    | https://www.facebook.com/monjurmbm404       |
| 🐦 X (Twitter) | https://x.com/monjurmbm404                  |
| ▶️ YouTube     | https://youtube.com/@monjurmbm404           |
| ✍️ Medium      | https://medium.com/@monjurmbm404            |

