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