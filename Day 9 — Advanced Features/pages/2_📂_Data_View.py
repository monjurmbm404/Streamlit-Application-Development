import streamlit as st
import pandas as pd

st.title("📂 Data Viewer")

# CACHE DATA
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# FILTER
name_filter = st.text_input("Filter by name")

if name_filter:
    df = df[df["name"].str.contains(name_filter, case=False)]

st.dataframe(df)

# DOWNLOAD BUTTON
st.download_button(
    "Download Data",
    df.to_csv(index=False),
    "data.csv",
    "text/csv"
)