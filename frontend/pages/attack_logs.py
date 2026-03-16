import streamlit as st
import pandas as pd
from services.api_client import get_logs, delete_log


def show_logs():

    st.title("Attack Logs")

    logs = get_logs()

    if not logs:
        st.info("No logs found yet.")
        return

    df = pd.DataFrame(logs)

    for index, row in df.iterrows():

        col1, col2, col3, col4, col5 = st.columns([4,1,1,1,1])

        col1.write(row["prompt"])
        col2.write(row["risk_score"])
        col3.write(row["attack_type"])
        col4.write(row["status"])

        if col5.button("Delete", key=row["id"]):

            delete_log(row["id"])

            st.success("Log deleted")

            st.rerun()