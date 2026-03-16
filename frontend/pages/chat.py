import streamlit as st
from components.prompt_box import prompt_input
from components.risk_indicator import show_risk
from components.threat_card import show_threat
from components.response_box import show_response
from services.api_client import analyze_prompt


def show_chat():

    st.title("🛡 AI Prompt Injection Guard")

    prompt, send = prompt_input()

    if send and prompt:

        result = analyze_prompt(prompt)

        risk_score = result["risk_score"]
        attack_type = result["attack_type"]
        status = result["status"]

        show_risk(risk_score)

        show_threat(status, attack_type)

        # BLOCKED
        if status == "BLOCKED":

            st.warning("⚠️ Prompt blocked due to security risk.")

        # UNDER REVIEW
        elif status == "UNDER_REVIEW":

            st.info("🛑 Prompt sent for admin review.")

        # SAFE
        elif status == "SAFE":

            show_response(result["response"])