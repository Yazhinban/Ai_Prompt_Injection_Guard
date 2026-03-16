import streamlit as st

def show_threat(status, attack_type):

    st.subheader("Threat Analysis")

    if status == "BLOCKED":

        st.markdown(
            f"""
            <div style="
                padding:18px;
                border-radius:10px;
                background-color:#fee2e2;
                border-left:6px solid red;
                font-size:18px;
            ">
            🚨 <b>Attack Detected</b><br>
            Type: {attack_type}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div style="
                padding:18px;
                border-radius:10px;
                background-color:#dcfce7;
                border-left:6px solid green;
                font-size:18px;
            ">
            ✅ Prompt is Safe
            </div>
            """,
            unsafe_allow_html=True
        )