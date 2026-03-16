import streamlit as st
from components.prompt_box import prompt_input
from components.risk_indicator import show_risk
from components.threat_card import show_threat
from components.response_box import show_response
from services.api_client import analyze_prompt, chat_prompt


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

        # 🚫 BLOCK AI RESPONSE
        if status == "BLOCKED":

            st.warning("⚠️ This prompt was blocked due to security risk.")

        else:

            chat = chat_prompt(prompt)

            show_response(chat["response"])