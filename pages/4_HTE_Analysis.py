
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HTE Analysis", layout="wide")

# Load data
traffic = pd.read_csv("data/hte_traffic.csv")
weather = pd.read_csv("data/hte_weather.csv")
risk = pd.read_csv("data/hte_risk.csv")

st.title("👥 Heterogeneous Treatment Effects")

st.markdown("""
Heterogeneous Treatment Effects (HTE) show how the impact of the new ETA
algorithm changes across different operating conditions.
""")

st.divider()

# -------------------------
# Traffic
# -------------------------

st.subheader("🚦 Treatment Effect by Traffic")

fig = px.bar(
    traffic,
    x="traffic_group",
    y="eta_variation_new",
    color="traffic_group",
    text_auto=".2f"
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Higher traffic levels generally benefit more from the optimized ETA algorithm.
""")

st.divider()

# -------------------------
# Weather
# -------------------------

st.subheader("🌦 Treatment Effect by Weather")

fig = px.bar(
    weather,
    x="weather_group",
    y="eta_variation_new",
    color="weather_group",
    text_auto=".2f"
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
The treatment effect varies across weather severity,
suggesting the algorithm adapts differently under adverse conditions.
""")

st.divider()

# -------------------------
# Route Risk
# -------------------------

st.subheader("⚠️ Treatment Effect by Route Risk")

fig = px.bar(
    risk,
    x="risk_group",
    y="eta_variation_new",
    color="risk_group",
    text_auto=".2f"
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Higher-risk routes show different levels of improvement,
which can inform targeted deployment strategies.
""")

st.divider()

# -------------------------
# Summary
# -------------------------

st.subheader("Business Insights")

st.success("""
• Deploy the ETA algorithm first on high-traffic routes.

• Monitor performance separately under severe weather conditions.

• Prioritize high-risk routes if they show larger treatment effects.

• HTE analysis helps identify where the intervention delivers the greatest value.
""")
