import streamlit as st

def show_response(response):

    st.subheader("AI Response")

    st.markdown(
        f"""
        <div style="
        background:#111827;
        padding:20px;
        border-radius:10px;
        ">
        {response}
        </div>
        """,
        unsafe_allow_html=True
    )