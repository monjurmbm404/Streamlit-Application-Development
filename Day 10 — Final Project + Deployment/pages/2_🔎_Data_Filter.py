import streamlit as st
import pandas as pd

st.title("🔎 Data Filter")

df = st.session_state.get("data", None)

if df is not None:
    column = st.selectbox("Select column", df.columns)

    keyword = st.text_input("Filter value")

    if keyword:
        filtered = df[df[column].astype(str).str.contains(keyword)]
    else:
        filtered = df

    st.dataframe(filtered)

    st.download_button(
        "Download Filtered Data",
        filtered.to_csv(index=False),
        "filtered.csv",
        "text/csv"
    )
else:
    st.warning("Please upload data from Dashboard page")