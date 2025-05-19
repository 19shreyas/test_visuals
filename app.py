import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample section scores
section_scores = {
    "Section 4": 0.85,
    "Section 5": 0.65,
    "Section 6": 1.0,
    "Section 7": 0.5
}

# Plotly Bar Chart
df_scores = pd.DataFrame(list(section_scores.items()), columns=["Section", "Score"])
bar_fig = px.bar(df_scores, x="Section", y="Score", color="Score", color_continuous_scale="RdYlGn")
st.plotly_chart(bar_fig)

# Radar Chart
radar_fig = go.Figure(data=go.Scatterpolar(
    r=list(section_scores.values()),
    theta=list(section_scores.keys()),
    fill='toself'
))
radar_fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
st.plotly_chart(radar_fig)

# Checklist Evaluation
matched_items = [
    {"Checklist Item ID": "4.1", "Checklist Text": "Lawful purpose must be stated.", "Status": "Explicitly Mentioned", "Justification": "Clearly written in intro."},
    {"Checklist Item ID": "4.2", "Checklist Text": "Consent must be taken before processing.", "Status": "Partially Mentioned", "Justification": "Only mentioned for financial data."},
    {"Checklist Item ID": "4.3", "Checklist Text": "Purpose must not be forbidden by law.", "Status": "Missing", "Justification": "Not mentioned in policy."}
]

df_matched = pd.DataFrame(matched_items)

def highlight_status(val):
    if val == "Explicitly Mentioned":
        return "background-color: #198754; color: white"
    elif val == "Partially Mentioned":
        return "background-color: #FFC107; color: black"
    elif val == "Missing":
        return "background-color: #DC3545; color: white"
    return ""

styled_df = df_matched.style.applymap(highlight_status, subset=["Status"])
st.dataframe(styled_df)
