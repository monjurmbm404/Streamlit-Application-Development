import streamlit as st

st.title("⚙️ Settings")

# SESSION STATE
if "username" not in st.session_state:
    st.session_state.username = ""

name = st.text_input("Enter your name")

if name:
    st.session_state.username = name

st.write("Current user:", st.session_state.username)

# THEME SIMULATION
theme = st.selectbox("Select theme", ["Light", "Dark"])

st.write("Selected theme:", theme)