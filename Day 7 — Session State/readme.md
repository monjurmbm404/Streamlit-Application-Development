# 🔁 Day 7 — Session State (Persistent Apps)

Welcome to **Day 7** of your Streamlit journey!
Today, you’ll learn how to build apps that **remember user actions** using session state.

---

## 📌 What You’ll Learn

- What `st.session_state` is
- Store and persist data across interactions
- Build multi-step applications
- Avoid data reset on every user action

---

## 📂 Project Structure

```id="k8v2xm"
Day 7 — Session State/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="w4n7zt"
import streamlit as st

st.set_page_config(page_title="Session State App", layout="centered")

st.title("📝 To-Do List App (Session State)")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input
new_task = st.text_input("Enter a new task:")

# Add task
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")

# Display tasks
st.subheader("📌 Your Tasks")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"{i+1}. {task}")

        with col2:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks yet. Add one!")

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []
    st.warning("All tasks cleared!")
```

---

## ▶️ Run the App

```bash id="n3k9qp"
streamlit run app.py
```

Then open:

```id="z7m1xs"
http://localhost:8501
```

---

## 🎯 Project Overview

This app allows users to:

- Add tasks ➕
- Delete tasks ❌
- Store tasks during session 🔁

👉 Without session state, all data resets on every interaction
👉 With session state, your app behaves like a **real application**

---

## 🧪 Practice Tasks

Enhance your app with these features:

### 🔹 Mark Task as Done

```python id="b6t2lp"
done = st.checkbox("Done", key=f"done_{i}")
```

---

### 🔹 Show Total Tasks

```python id="p5n8xr"
st.write("Total Tasks:", len(st.session_state.tasks))
```

---

### 🔹 Store User Name

```python id="q2m4zn"
if "name" not in st.session_state:
    st.session_state.name = ""

name = st.text_input("Enter your name")

if name:
    st.session_state.name = name

st.write("Hello,", st.session_state.name)
```

---

### 🔹 Multi-Step App

- Step 1: Input data
- Step 2: Show results using session state

---

## 🚀 What You Learned

- How to persist data in Streamlit
- How to manage app state
- How to build interactive and dynamic apps
- How to create multi-step workflows

---

## 💡 Notes

- Always initialize session state before use
- Use unique keys for buttons and inputs
- Use `st.experimental_rerun()` carefully

---

## ➡️ Next Step

Move to **Day 8 — API Integration** to connect your app with real-world data 🌐

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

