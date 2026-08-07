
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Counterfactual Explorer", layout="wide")

# Load data
df = pd.read_csv("data/counterfactual_results.csv")

st.title("🔮 Counterfactual Explorer")

st.markdown("""
Counterfactual analysis estimates **what would have happened**
if the new ETA optimization algorithm had been applied.
""")

st.divider()

# -----------------------
# Shipment Selector
# -----------------------

shipment = st.selectbox(
    "Select Shipment",
    df.index
)

row = df.loc[shipment]

# -----------------------
# Metrics
# -----------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Original ETA Variation",
    f"{row['eta_variation_hours']:.2f} hrs"
)

c2.metric(
    "Counterfactual ETA",
    f"{row['eta_variation_new']:.2f} hrs"
)

improvement = row["eta_variation_hours"] - row["eta_variation_new"]

c3.metric(
    "Improvement",
    f"{improvement:.2f} hrs"
)

st.divider()

# -----------------------
# Comparison Chart
# -----------------------

chart = pd.DataFrame({
    "Scenario": [
        "Observed",
        "Counterfactual"
    ],
    "ETA Variation": [
        row["eta_variation_hours"],
        row["eta_variation_new"]
    ]
})

fig = px.bar(
    chart,
    x="Scenario",
    y="ETA Variation",
    text_auto=".2f",
    color="Scenario",
    title="Observed vs Counterfactual"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------
# Shipment Details
# -----------------------

st.subheader("Shipment Details")

st.dataframe(
    row.to_frame().T,
    use_container_width=True
)

st.divider()

# -----------------------
# Interpretation
# -----------------------

if improvement > 0:

    st.success(f"""
Applying the new ETA algorithm would reduce
ETA variation by approximately **{improvement:.2f} hours**
for this shipment.
""")

else:

    st.warning("""
This shipment shows little or no improvement
under the simulated intervention.
""")
