# 🔄 Day 6 — Forms & File Upload

Welcome to **Day 6** of your Streamlit journey!
Today, you’ll learn how to build **structured workflows** using forms and handle file uploads like real-world applications.

---

## 📌 What You’ll Learn

- Use `st.form()` for grouped inputs
- Handle file uploads with `st.file_uploader()`
- Control execution with submit buttons
- Build clean and structured user workflows

---

## 📂 Project Structure

```id="r6k2qp"
Day 6 — Forms + File Upload/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="m9t4zn"
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Form App", layout="wide")

st.title("📂 Data Upload & Analysis App")

# Sidebar upload
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    # Form section
    st.subheader("📝 Filter & Analyze Data")

    with st.form("filter_form"):
        columns = df.columns.tolist()

        selected_column = st.selectbox("Select column", columns)
        keyword = st.text_input("Enter keyword to filter")

        sort_option = st.selectbox("Sort order", ["Ascending", "Descending"])

        submitted = st.form_submit_button("Apply Filter")

    # After submit
    if submitted:
        filtered_df = df.copy()

        # Filter data
        if keyword:
            filtered_df = filtered_df[
                filtered_df[selected_column].astype(str).str.contains(keyword)
            ]

        # Sort data
        if sort_option == "Ascending":
            filtered_df = filtered_df.sort_values(by=selected_column)
        else:
            filtered_df = filtered_df.sort_values(by=selected_column, ascending=False)

        st.subheader("🔍 Filtered Results")
        st.dataframe(filtered_df)

        st.write("Rows:", filtered_df.shape[0])

else:
    st.info("👈 Upload a CSV file from the sidebar")
```

---

## ▶️ Run the App

```bash id="v3k9pt"
streamlit run app.py
```

Then open:

```id="h8m2qs"
http://localhost:8501
```

---

## 🎯 Project Overview

This app allows users to:

- Upload a CSV file 📂
- Fill a form with filters 📝
- Submit inputs 🔘
- View filtered and sorted results 📊

👉 This mimics **real-world app workflows (input → submit → result)**

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Add Date Input

```python id="q4t7lp"
st.date_input("Select a date")
```

---

### 🔹 Add Numeric Filter

```python id="n2w6xr"
min_value = st.number_input("Minimum value", value=0)
filtered_df = filtered_df[filtered_df[selected_column] >= min_value]
```

---

### 🔹 Add Download Button

```python id="z8p1qm"
st.download_button(
    "Download CSV",
    filtered_df.to_csv(index=False),
    "filtered_data.csv",
    "text/csv"
)
```

---

### 🔹 Add Toggle for Raw Data

```python id="y5c3kn"
if st.checkbox("Show original data"):
    st.dataframe(df)
```

---

## 🚀 What You Learned

- How to group inputs using forms
- How to control execution flow
- How to process user-submitted data
- How to build structured workflows

---

## 💡 Notes

- Forms prevent unnecessary reruns
- Use submit buttons for better UX
- Keep workflows simple and guided

---

## ➡️ Next Step

Move to **Day 7 — Session State** to build apps that remember users 🔁

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
