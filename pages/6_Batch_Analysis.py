
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Batch Analysis", layout="wide")

st.title("📂 Batch Analysis")

st.markdown("""
Upload a logistics dataset to explore shipment characteristics and
download the processed results.
""")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success(f"Loaded {len(df):,} records.")

    st.divider()

    st.subheader("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.divider()

    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include="all"), use_container_width=True)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:

        selected = st.selectbox(
            "Select a numeric feature",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected,
            title=f"Distribution of {selected}"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Processed CSV",
        data=csv,
        file_name="processed_results.csv",
        mime="text/csv"
    )

else:

    st.info("Upload a CSV file to begin analysis.")
