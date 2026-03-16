import streamlit as st
from components.prompt_box import prompt_input
from components.risk_indicator import show_risk
from components.threat_card import show_threat
from components.response_box import show_response

def show_chat():

    st.title("🛡 AI Prompt Injection Guard")

    prompt, send = prompt_input()

    if send and prompt:

        # dummy data for now
        risk_score = 0.82
        status = "BLOCKED"
        attack_type = "PROMPT_INJECTION"

        show_risk(risk_score)

        show_threat(status,attack_type)

        if status == "SAFE":

            show_response("This is an AI response.")