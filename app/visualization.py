import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_charts(df):
    st.header("📊 Data Visualizations")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Histogram
    st.subheader("📈 Histogram")
    col = st.selectbox("Select a numeric column for histogram", numeric_cols)
    if col:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

    # Boxplot
    st.subheader("📦 Boxplot")
    col = st.selectbox("Select a numeric column for boxplot", numeric_cols, key="boxplot")
    if col:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        st.pyplot(fig)

    # Scatter Plot
    st.subheader("🔘 Scatter Plot")
    x_col = st.selectbox("X-axis", numeric_cols, key="scatter_x")
    y_col = st.selectbox("Y-axis", numeric_cols, key="scatter_y")
    if x_col and y_col:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("🌡️ Correlation Heatmap")
    if len(numeric_cols) >= 2:
        fig, ax = plt.subplots()
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
