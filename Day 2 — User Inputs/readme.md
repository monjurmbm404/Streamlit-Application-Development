# 🧑 Day 2 — Streamlit Inputs & Mini Project

Welcome to **Day 2** of your Streamlit journey!
Today, you’ll learn how to build **interactive apps** using input widgets and create your first **mini project**.

---

## 📌 What You’ll Learn

* User input widgets:

  * Text input
  * Number input
  * Select box
  * Radio buttons
  * Slider
* Handling user interaction
* Building a simple interactive app

---

## 📂 Project Structure

```id="h9u3w2"
Day 2 — User Inputs/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python id="l3x9k1"
import streamlit as st

st.title("🧑 User Information App")

st.header("Enter Your Details")

# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)

# Selectbox
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

# Radio button
role = st.radio("Select your role:", ["Student", "Developer", "Other"])

# Slider
satisfaction = st.slider("How happy are you today?", 0, 10, 5)

# Button
if st.button("Submit"):
    st.subheader("📊 Your Information")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Role:", role)
    st.write("Happiness Level:", satisfaction)

    # Simple logic
    if age < 18:
        st.warning("You are young, keep learning! 📚")
    else:
        st.success("Great! Keep building awesome projects 🚀")

    if satisfaction > 7:
        st.success("Awesome! You're having a great day 😄")
    else:
        st.info("Hope your day gets even better 🌈")
```

---

## ▶️ Run the App

```bash id="b8k1pq"
streamlit run app.py
```

Then open:

```id="c1s9z4"
http://localhost:8501
```

---

## 🎯 Mini Project

You built a **User Information App** that:

* Takes multiple inputs
* Processes user data
* Displays results dynamically

---

## 🧪 Practice Tasks

Try improving your app:

### 🔹 Add Date Input

```python
st.date_input("Select your birth date")
```

---

### 🔹 Add Favorite Programming Language

```python
st.selectbox("Favorite Language", ["Python", "JavaScript", "C++"])
```

---

### 🔹 Add Conditional Message

* Show a special message if user selects **Developer**

---

### 🔹 Add Reset Button

* Clear inputs or show a reset message

---

## 🚀 What You Learned

* How to collect user input
* How to use multiple widgets together
* How to apply logic based on input

---

## 💡 Notes

* Streamlit reruns the script on every interaction
* Use conditions (`if`) to control behavior
* Keep UI simple and clean

---

## ➡️ Next Step

Move to **Day 3 — CSV Data Viewer App** to work with real datasets 📊

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
