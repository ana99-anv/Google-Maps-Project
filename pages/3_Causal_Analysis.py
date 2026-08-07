
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Causal Analysis", layout="wide")

# Load treatment effect metrics
effects = pd.read_csv("data/treatment_effects.csv")

st.title("📈 Causal Analysis")

st.markdown("""
This page summarizes the estimated impact of the new ETA optimization algorithm
using causal inference techniques.
""")

st.divider()

# -------------------------
# Treatment Effect Metrics
# -------------------------

col1, col2, col3, col4 = st.columns(4)

att = effects.loc[effects["Metric"] == "ATT", "Value"].iloc[0]
p = effects.loc[effects["Metric"] == "P-value", "Value"].iloc[0]
t_stat = effects.loc[effects["Metric"] == "T-statistic", "Value"].iloc[0]
ci_lower = effects.loc[effects["Metric"] == "CI Lower", "Value"].iloc[0]
ci_upper = effects.loc[effects["Metric"] == "CI Upper", "Value"].iloc[0]

col1.metric("ATT", f"{att:.3f} hrs")
col2.metric("T-Statistic", f"{t_stat:.2f}")
col3.metric("P-Value", f"{p:.6f}")
col4.metric("95% CI", f"[{ci_lower:.2f}, {ci_upper:.2f}]")

st.divider()

# -------------------------
# Treatment Effect Table
# -------------------------

st.subheader("Treatment Effect Summary")

st.dataframe(effects, use_container_width=True)

st.divider()

# -------------------------
# Interpretation
# -------------------------

st.subheader("Interpretation")

if p < 0.05:
    st.success(
        f"""
The estimated Average Treatment Effect on the Treated (ATT) is **{att:.3f} hours**.

The p-value is **{p:.6f}**, which indicates the observed improvement is
statistically significant at the 5% significance level.

This suggests the new ETA optimization algorithm has a measurable impact on
delivery performance.
"""
    )
else:
    st.warning(
        "The estimated treatment effect is not statistically significant."
    )

st.divider()

# -------------------------
# Confidence Interval
# -------------------------

ci_df = pd.DataFrame({
    "Statistic": ["Lower Bound", "ATT", "Upper Bound"],
    "Value": [ci_lower, att, ci_upper]
})

fig = px.bar(
    ci_df,
    x="Statistic",
    y="Value",
    title="Treatment Effect and 95% Confidence Interval",
    text="Value"
)

st.plotly_chart(fig, use_container_width=True)
