import streamlit as st
from app import upload, eda, visualization, modeling, report

st.set_page_config(page_title="Data Analysis App", layout="wide")

st.title("📊 User-Driven Data Analysis App")

uploaded_file = upload.upload_data()

if uploaded_file is not None:
    df = upload.load_data(uploaded_file)
    st.success("File uploaded successfully!")

    eda.show_basic_info(df)
    visualization.show_charts(df)
    modeling.run_models(df)
    report.generate_summary(df)
