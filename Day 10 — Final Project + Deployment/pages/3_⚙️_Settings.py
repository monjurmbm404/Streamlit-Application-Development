import streamlit as st

st.title("⚙️ Settings")

if "username" not in st.session_state:
    st.session_state.username = ""

name = st.text_input("Enter your name")

if name:
    st.session_state.username = name

st.write("User:", st.session_state.username)

theme = st.selectbox("Theme", ["Light", "Dark"])

st.write("Selected theme:", theme)