import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Visualization App")

st.write("Upload a CSV file and visualize your data")

# Upload file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show data
    st.subheader("📄 Dataset")
    st.dataframe(df)

    # Select columns
    columns = df.columns.tolist()

    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    # Basic charts
    st.subheader("📈 Basic Charts")

    st.write("Line Chart")
    st.line_chart(df[[x_axis, y_axis]])

    st.write("Bar Chart")
    st.bar_chart(df[[x_axis, y_axis]])

    # Plotly chart
    st.subheader("🔥 Interactive Chart (Plotly)")

    chart_type = st.selectbox(
        "Select chart type",
        ["Line", "Bar", "Scatter"]
    )

    if chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)

else:
    st.info("Upload a CSV file to start visualizing")