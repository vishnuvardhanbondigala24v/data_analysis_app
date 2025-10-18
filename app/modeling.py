import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, classification_report
import pandas as pd

def run_models(df):
    st.header("🧠 Machine Learning Models")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) < 2:
        st.warning("Need at least two numeric columns for modeling.")
        return

    model_type = st.selectbox("Choose a model type", ["Linear Regression", "K-Means Clustering"])

    if model_type == "Linear Regression":
        st.subheader("📈 Linear Regression")
        x_col = st.selectbox("Select feature (X)", numeric_cols, key="lr_x")
        y_col = st.selectbox("Select target (Y)", numeric_cols, key="lr_y")

        if x_col and y_col:
            X = df[[x_col]]
            y = df[y_col]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            st.write(f"Model Coefficient: {model.coef_[0]:.4f}")
            st.write(f"Intercept: {model.intercept_:.4f}")
            st.write(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

    elif model_type == "K-Means Clustering":
        st.subheader("🔗 K-Means Clustering")
        selected_cols = st.multiselect("Select numeric columns for clustering", numeric_cols)

        if selected_cols:
            X = df[selected_cols]
            k = st.slider("Select number of clusters (k)", 2, 10, 3)
            model = KMeans(n_clusters=k, random_state=42)
            df['Cluster'] = model.fit_predict(X)
            st.write("Cluster labels added to dataset:")
            st.dataframe(df[['Cluster'] + selected_cols])
