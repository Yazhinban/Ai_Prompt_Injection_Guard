import streamlit as st

def apply_theme():

    st.markdown(
        """
        <style>

        .stApp {
            background-color:#0b1220;
            color:white;
        }

        h1 {
            color:#22c55e;
            font-weight:700;
        }

        .block-container{
            padding-top:2rem;
        }

        .stButton>button{
            background-color:#22c55e;
            color:white;
            border-radius:8px;
            font-weight:bold;
        }

        .stTextArea textarea{
            background-color:#111827;
            color:white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )