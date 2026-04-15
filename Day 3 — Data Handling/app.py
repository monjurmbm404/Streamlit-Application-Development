import streamlit as st
import pandas as pd

st.title("📂 CSV Data Viewer App")

st.write("Upload a CSV file to explore your data")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show raw data
    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Show basic info
    st.subheader("📊 Data Summary")

    st.write("Shape of dataset:", df.shape)
    st.write("Columns:", df.columns.tolist())

    # Select column
    column = st.selectbox("Select a column to explore", df.columns)

    # Show column data
    st.subheader(f"🔍 Data in '{column}'")
    st.write(df[column])

    # Show statistics (if numeric)
    if pd.api.types.is_numeric_dtype(df[column]):
        st.subheader("📈 Statistics")
        st.write(df[column].describe())

    # Filter data
    st.subheader("🔎 Filter Data")

    value = st.text_input("Enter value to filter:")

    if value:
        filtered_df = df[df[column].astype(str).str.contains(value)]
        st.write(filtered_df)

else:
    st.info("Please upload a CSV file to get started.")