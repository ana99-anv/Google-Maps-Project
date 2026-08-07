import streamlit as st

st.set_page_config(
    page_title="Google Maps ETA Optimization",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Google Maps ETA Optimization using Causal Inference")

st.markdown(
"""
This dashboard demonstrates how **causal inference** can estimate the true
impact of a new ETA optimization algorithm on shipment delivery times.
"""
)

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Shipments", "32,065")
c2.metric("ATT", "-0.625 hrs")
c3.metric("ETA Gain", "37.5 mins")
c4.metric("P-value", "<0.001")

st.divider()

st.header("Project Overview")

st.write("""
Unlike traditional machine learning models that predict outcomes,
this project estimates **what would have happened** if a new ETA
algorithm had been deployed.

The analysis uses:

- Propensity Score Matching
- Treatment Effect Estimation
- Counterfactual Analysis
- Heterogeneous Treatment Effects
- Statistical Significance Testing
""")

st.divider()

st.success("Select a page from the left sidebar to explore the analysis.")
