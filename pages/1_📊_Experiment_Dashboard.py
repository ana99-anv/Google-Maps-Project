
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
dashboard = pd.read_csv("data/dashboard_data.csv")
effects = pd.read_csv("data/treatment_effects.csv")

st.title("📊 Experiment Dashboard")
st.markdown("### Overview of the causal inference experiment")

# KPI cards
col1, col2, col3, col4 = st.columns(4)

att = effects.loc[effects["Metric"] == "ATT", "Value"].iloc[0]
p = effects.loc[effects["Metric"] == "P-value", "Value"].iloc[0]

col1.metric("Shipments", f"{len(dashboard):,}")
col2.metric("Treatment", int(dashboard["treatment"].sum()))
col3.metric("ATT", f"{att:.3f} hrs")
col4.metric("P-value", f"{p:.5f}")

st.divider()

# Treatment distribution
fig = px.histogram(
    dashboard,
    x="treatment",
    color="treatment",
    title="Treatment vs Control"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Preview data
st.subheader("Dataset Preview")
st.dataframe(dashboard.head())
