import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Header & Text
st.header("Welcome!")
st.subheader("This is your Day 1 app")
st.text("Learning Streamlit step by step")

# Write (can display almost anything)
st.write("Hello, this is written using st.write()")

# Markdown
st.markdown("### 📌 This is Markdown text")
st.markdown("**Bold text**, *Italic text*, `code`")

# Simple variable display
name = "Student"
st.write("Hello,", name)

# Basic user input
user_name = st.text_input("Enter your name:")

if user_name:
    st.success(f"Welcome, {user_name}! 🎉")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")