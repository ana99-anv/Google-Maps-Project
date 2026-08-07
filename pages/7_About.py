
import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
# Google Maps ETA Optimization using Causal Inference
""")

st.divider()

# ---------------------------------
# Project Objective
# ---------------------------------

st.header("🎯 Project Objective")

st.write("""
Modern logistics systems continuously optimize estimated delivery times (ETAs).
However, simply observing improved delivery performance does not prove that
a new routing algorithm caused the improvement.

This project applies causal inference techniques to estimate the true impact
of a new ETA optimization algorithm while controlling for confounding variables.
""")

st.divider()

# ---------------------------------
# Dataset
# ---------------------------------

st.header("📦 Dataset")

st.write("""
**Dataset**

- Logistics & Supply Chain Operations Dataset

**Records**

- 32,065 shipments

**Features**

- Traffic congestion
- Weather severity
- Route risk
- Warehouse inventory
- Driver behavior
- Fuel consumption
- Shipping costs
- Lead time
- Delay probability
""")

st.divider()

# ---------------------------------
# Methodology
# ---------------------------------

st.header("🧪 Methodology")

st.markdown("""
The project follows a complete causal inference workflow:

1. Data Cleaning & Feature Engineering

2. Treatment Assignment

3. Propensity Score Matching (PSM)

4. Covariate Balance Assessment

5. Average Treatment Effect on the Treated (ATT)

6. Statistical Significance Testing

7. Heterogeneous Treatment Effect (HTE) Analysis

8. Counterfactual Analysis
""")

st.divider()

# ---------------------------------
# Technology
# ---------------------------------

st.header("💻 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.success("""
**Programming**

• Python

• Pandas

• NumPy

• Scikit-learn

• SciPy
""")

with col2:

    st.success("""
**Visualization**

• Plotly

• Streamlit

• Matplotlib
""")

st.divider()

# ---------------------------------
# Business Impact
# ---------------------------------

st.header("📈 Business Impact")

st.write("""
The analysis estimates the causal impact of deploying an improved ETA algorithm.

Key outcomes include:

• Reduced ETA variation

• Improved delivery reliability

• Better customer experience

• More efficient routing decisions

• Evidence-based deployment recommendations
""")

st.divider()

# ---------------------------------
# Skills Demonstrated
# ---------------------------------

st.header("🚀 Skills Demonstrated")

st.markdown("""
- Causal Inference

- Propensity Score Matching

- Statistical Testing

- Counterfactual Reasoning

- Heterogeneous Treatment Effects

- Data Engineering

- Exploratory Data Analysis

- Interactive Dashboard Development

- Business Insight Generation

- Streamlit Deployment
""")

st.divider()

# ---------------------------------
# Footer
# ---------------------------------

st.info("""
This project demonstrates how causal inference can support
data-driven decision making in logistics and route optimization,
moving beyond prediction to estimate the true impact of operational interventions.
""")
