import streamlit as st
import pandas as pd

def generate_summary(df):
    st.header("📝 Report Summary")

    st.subheader("📌 Key Dataset Info")
    st.write(f"- Rows: {df.shape[0]}")
    st.write(f"- Columns: {df.shape[1]}")
    st.write(f"- Missing Values: {df.isnull().sum().sum()}")

    st.subheader("📊 Top Numeric Columns")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in numeric_cols[:3]:  # Show top 3
        st.write(f"**{col}** → Mean: {df[col].mean():.2f}, Std: {df[col].std():.2f}")

    st.subheader("🧠 Modeling Insights")
    if 'Cluster' in df.columns:
        st.write(f"- K-Means Clustering applied: {df['Cluster'].nunique()} clusters detected.")
    else:
        st.write("- No clustering applied yet.")

    st.subheader("📌 Final Thoughts")
    st.markdown("""
    - Use the visualizations to spot trends and outliers.
    - Consider applying more models for deeper insights.
    - Export results or share findings with your team.
    """)

    # Optional: Add download button for processed data
    st.download_button("Download Processed Data", df.to_csv(index=False), file_name="processed_data.csv", mime="text/csv")
