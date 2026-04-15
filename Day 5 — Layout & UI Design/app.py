import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

# Title
st.title("📊 Professional Dashboard")

# Sidebar
st.sidebar.header("⚙️ Controls")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Data loaded successfully!")

    # Sidebar filters
    columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Select X-axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", columns)

    # Top metrics
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Selected Column", y_axis)

    # Charts section
    st.subheader("📈 Visualizations")

    col4, col5 = st.columns(2)

    with col4:
        st.write("Line Chart")
        st.line_chart(df[[x_axis, y_axis]])

    with col5:
        st.write("Bar Chart")
        st.bar_chart(df[[x_axis, y_axis]])

    # Plotly full-width chart
    st.subheader("🔥 Interactive Chart")

    fig = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(fig, use_container_width=True)

    # Data section
    st.subheader("📄 Dataset Preview")

    st.dataframe(df)

else:
    st.info("👈 Upload a CSV file from the sidebar to begin")