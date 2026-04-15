# 🚀 Day 1 — Streamlit Setup & First App

Welcome to **Day 1** of the Streamlit learning journey!
In this step, you’ll set up your environment and build your **first Streamlit app**.

---

## 📌 What You’ll Learn

- Install Streamlit
- Run a Streamlit app
- Basic UI elements:
  - Title, text, markdown
  - User input (text box)
  - Button interaction

---

## ⚙️ Installation

Make sure you have Python installed, then install Streamlit:

```bash
pip install streamlit
```

---

## 📂 Project Structure

```
Day 1 — Setup + First App/
│
└── app.py
```

---

## 🧩 Code Example (`app.py`)

```python
import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Header & Text
st.header("Welcome!")
st.subheader("This is your Day 1 app")
st.text("Learning Streamlit step by step")

# Write
st.write("Hello, this is written using st.write()")

# Markdown
st.markdown("### 📌 This is Markdown text")
st.markdown("**Bold text**, *Italic text*, `code`")

# Variable display
name = "Student"
st.write("Hello,", name)

# User input
user_name = st.text_input("Enter your name:")

if user_name:
    st.success(f"Welcome, {user_name}! 🎉")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🎯 Output

Your app will:

- Display text and headings
- Take user input
- Respond to button clicks

---

## 🧪 Practice Tasks

Try modifying the app:

- Add your name
- Add a favorite quote
- Add another button:

  ```python
  if st.button("Show Message"):
      st.info("Keep learning 🚀")
  ```

---

## 🚀 What’s Next?

Move to **Day 2 — Inputs & Interaction** to build more interactive apps.

---

## 💡 Notes

- Streamlit apps auto-refresh on changes
- No frontend framework needed (pure Python!)

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
