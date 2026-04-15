import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

# SESSION STATE
if "data" not in st.session_state:
    st.session_state.data = None

# Upload
uploaded_file = st.file_uploader("Upload CSV", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

if uploaded_file:
    st.session_state.data = load_data(uploaded_file)

df = st.session_state.data

if df is not None:
    st.success("Data loaded!")

    columns = df.columns.tolist()

    x = st.selectbox("X-axis", columns)
    y = st.selectbox("Y-axis", columns)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Selected Y", y)

    fig = px.scatter(df, x=x, y=y)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Upload a CSV file to begin")