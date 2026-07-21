# 🎨 Day 5 — Layout & Dashboard Design

Welcome to **Day 5** of your Streamlit journey!
Today, you’ll learn how to design **professional dashboards** with clean layouts and better user experience.

---

## 📌 What You’ll Learn

- Use sidebar for controls
- Create layouts with columns
- Display key metrics
- Build structured dashboards
- Improve UI/UX design

---

## 📂 Project Structure

```id="p3n7lx"
Day 5 — Layout & UI Design/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="x7k2qp"
import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Dashboard", layout="wide")

# Title
st.title("📊 Professional Dashboard")

# Sidebar controls
st.sidebar.header("⚙️ Controls")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Data loaded successfully!")

    # Sidebar filters
    columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Select X-axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", columns)

    # Metrics
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Selected Column", y_axis)

    # Charts
    st.subheader("📈 Visualizations")

    col4, col5 = st.columns(2)

    with col4:
        st.write("Line Chart")
        st.line_chart(df[[x_axis, y_axis]])

    with col5:
        st.write("Bar Chart")
        st.bar_chart(df[[x_axis, y_axis]])

    # Interactive chart
    st.subheader("🔥 Interactive Chart")

    fig = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(fig, use_container_width=True)

    # Data preview
    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

else:
    st.info("👈 Upload a CSV file from the sidebar to begin")
```

---

## ▶️ Run the App

```bash id="d2k8zr"
streamlit run app.py
```

Then open:

```id="h4m9qs"
http://localhost:8501
```

---

## 🎯 Project Overview

This dashboard allows users to:

- Upload data from sidebar 📂
- Select columns for analysis 🎛️
- View key metrics 📊
- See charts side-by-side 📈
- Explore data interactively

---

## 🧪 Practice Tasks

Enhance your dashboard with these features:

### 🔹 Add Data Filter

```python id="f9q2xm"
value = st.sidebar.text_input("Filter value")
if value:
    df = df[df[x_axis].astype(str).str.contains(value)]
```

---

### 🔹 Add Chart Type Selector

```python id="z7r1lp"
chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Bar"])

if chart_type == "Line":
    st.line_chart(df[[x_axis, y_axis]])
else:
    st.bar_chart(df[[x_axis, y_axis]])
```

---

### 🔹 Add Expandable Section

```python id="n5w8jc"
with st.expander("Show Full Data"):
    st.dataframe(df)
```

---

### 🔹 Limit Rows Displayed

```python id="k6t3bn"
rows = st.slider("Select rows", 5, len(df), 10)
st.dataframe(df.head(rows))
```

---

## 🚀 What You Learned

- How to structure a dashboard layout
- How to use sidebar for user controls
- How to display metrics and charts cleanly
- How to improve user experience

---

## 💡 Notes

- Use `layout="wide"` for better spacing
- Keep controls in sidebar for clarity
- Avoid clutter — keep UI simple

---

## ➡️ Next Step

Move to **Day 6 — Forms & File Upload** to build structured workflows 🔄

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

