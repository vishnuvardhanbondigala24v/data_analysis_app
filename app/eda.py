import streamlit as st
import pandas as pd

def show_basic_info(df):
    st.header("🔍 Exploratory Data Analysis")

    st.subheader("📌 Dataset Overview")
    st.write("Shape of the dataset:")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.subheader("📋 Column Names")
    st.write(df.columns.tolist())

    st.subheader("📊 Data Types")
    st.write(df.dtypes)

    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    st.subheader("🧭 Missing Values")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])

    st.subheader("📌 Sample Data")
    st.dataframe(df.head())
