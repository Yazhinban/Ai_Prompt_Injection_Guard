import streamlit as st


def show_threat(status, attack_type):

    if status == "BLOCKED":

        st.markdown(
            """
            <div style="
                background-color:#2b0000;
                padding:18px;
                border-radius:10px;
                border-left:6px solid red;
                color:white;
                font-size:18px;
                font-weight:600;
            ">
            🚨 PROMPT BLOCKED<br>
            Attack Type: PROMPT INJECTION<br><br>
            The prompt contains instructions that attempt to override AI safety rules.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div style="
                background-color:#0b3d2e;
                padding:18px;
                border-radius:10px;
                border-left:6px solid #00ff9c;
                color:white;
                font-size:18px;
                font-weight:600;
            ">
            ✅ Prompt is Safe
            </div>
            """,
            unsafe_allow_html=True
        )