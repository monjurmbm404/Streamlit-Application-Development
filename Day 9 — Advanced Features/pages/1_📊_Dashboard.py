import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")

st.title("📊 Dashboard")

# CACHED FUNCTION
@st.cache_data
def load_data():
    time.sleep(2)  # simulate heavy load
    return pd.read_csv("data.csv")

# LOADING ANIMATION
with st.spinner("Loading data..."):
    df = load_data()

st.success("Data loaded successfully!")

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Total Rows", df.shape[0])
col2.metric("Average Age", int(df["age"].mean()))
col3.metric("Average Salary", int(df["salary"].mean()))

# CHARTS
col4, col5 = st.columns(2)

with col4:
    st.subheader("📈 Age Distribution")
    st.line_chart(df["age"])

with col5:
    st.subheader("💰 Salary Distribution")
    st.bar_chart(df["salary"])