import streamlit as st
import pandas as pd

st.set_page_config(page_title="Treatment Simulator", layout="wide")

# Load data
dashboard = pd.read_csv("data/dashboard_data.csv")

st.title("🧪 Treatment Simulator")

st.markdown("""
Explore how delivery performance changes under different operating conditions.
The simulator filters shipments that match your selected scenario and summarizes
their observed outcomes.
""")

st.divider()

# Sidebar filters
st.sidebar.header("Scenario Settings")

traffic = st.sidebar.slider(
    "Traffic Congestion Level",
    int(dashboard["traffic_congestion_level"].min()),
    int(dashboard["traffic_congestion_level"].max()),
    5
)

weather = st.sidebar.slider(
    "Weather Severity",
    float(dashboard["weather_condition_severity"].min()),
    float(dashboard["weather_condition_severity"].max()),
    float(dashboard["weather_condition_severity"].median())
)

risk = st.sidebar.slider(
    "Route Risk Level",
    float(dashboard["route_risk_level"].min()),
    float(dashboard["route_risk_level"].max()),
    float(dashboard["route_risk_level"].median())
)

# Filter similar records
filtered = dashboard[
    (dashboard["traffic_congestion_level"].between(traffic-1, traffic+1)) &
    (dashboard["weather_condition_severity"].between(weather-0.1, weather+0.1)) &
    (dashboard["route_risk_level"].between(risk-1, risk+1))
]

st.subheader("Matching Shipments")

st.write(f"Number of similar shipments: **{len(filtered)}**")

if len(filtered) > 0:

    before = filtered["eta_variation_hours"].mean()
    after = filtered["eta_variation_new"].mean()
    improvement = before - after

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average ETA Before",
        f"{before:.2f} hrs"
    )

    c2.metric(
        "Average ETA After",
        f"{after:.2f} hrs"
    )

    c3.metric(
        "Average Improvement",
        f"{improvement:.2f} hrs"
    )

    st.divider()

    st.subheader("Matching Records")

    st.dataframe(filtered.head(20), use_container_width=True)

else:

    st.warning(
        "No similar shipments were found for this combination of conditions."
    )
