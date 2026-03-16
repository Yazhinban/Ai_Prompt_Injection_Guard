import streamlit as st

def show_threat(status,attack_type):

    st.subheader("Threat Analysis")

    if status == "BLOCKED":

        st.error(f"🚨 Attack Detected: {attack_type}")

    else:

        st.success("Prompt is Safe")