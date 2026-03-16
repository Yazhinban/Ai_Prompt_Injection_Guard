import streamlit as st
import pandas as pd
import plotly.express as px
from services.api_client import get_logs, get_stats


def show_dashboard():

    st.title("🛡 Security Dashboard")

    # ---------- GET DATA FROM BACKEND ----------
    stats = get_stats()
    logs = get_logs()

    df = pd.DataFrame(logs)

    # If database empty
    if df.empty:

        st.warning("No prompts analyzed yet.")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Prompts", 0)
        col2.metric("Blocked Attacks", 0)
        col3.metric("Safe Prompts", 0)
        col4.metric("Risk Level", 0)

        return

    # ---------- METRICS ----------
    total_prompts = stats["total_prompts"]
    blocked = stats["blocked_attacks"]
    safe = stats["safe_prompts"]

    avg_risk = round(df["risk_score"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Prompts", total_prompts)
    col2.metric("Blocked Attacks", blocked)
    col3.metric("Safe Prompts", safe)
    col4.metric("Risk Level", avg_risk)

    st.divider()

    # ---------- ATTACK TYPE GRAPH ----------
    st.subheader("Attack Types")

    attack_counts = df["attack_type"].value_counts().reset_index()
    attack_counts.columns = ["attack_type", "count"]

    fig = px.bar(
        attack_counts,
        x="attack_type",
        y="count",
        color="attack_type",
        title="Detected Attack Categories",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- RISK DISTRIBUTION ----------
    st.subheader("Risk Score Distribution")

    fig2 = px.histogram(
        df,
        x="risk_score",
        nbins=10,
        title="Risk Score Spread",
        template="plotly_dark"
    )

    st.plotly_chart(fig2, use_container_width=True)