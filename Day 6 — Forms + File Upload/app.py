import streamlit as st
import pandas as pd

st.set_page_config(page_title="Form App", layout="wide")

st.title("📂 Data Upload & Analysis App")

# Sidebar upload
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    # FORM starts here
    st.subheader("📝 Filter & Analyze Data")

    with st.form("filter_form"):
        columns = df.columns.tolist()

        selected_column = st.selectbox("Select column", columns)
        keyword = st.text_input("Enter keyword to filter")

        sort_option = st.selectbox("Sort order", ["Ascending", "Descending"])

        submitted = st.form_submit_button("Apply Filter")

    # After form submit
    if submitted:
        filtered_df = df.copy()

        # Filter
        if keyword:
            filtered_df = filtered_df[
                filtered_df[selected_column].astype(str).str.contains(keyword)
            ]

        # Sort
        if sort_option == "Ascending":
            filtered_df = filtered_df.sort_values(by=selected_column)
        else:
            filtered_df = filtered_df.sort_values(by=selected_column, ascending=False)

        st.subheader("🔍 Filtered Results")
        st.dataframe(filtered_df)

        st.write("Rows:", filtered_df.shape[0])

else:
    st.info("👈 Upload a CSV file from the sidebar")