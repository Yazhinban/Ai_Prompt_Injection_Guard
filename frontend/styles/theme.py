import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    /* Main spacing */
    .block-container{
        padding-top:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    /* Buttons */
    .stButton>button{
        background-color:#22c55e;
        color:white;
        border-radius:8px;
        border:none;
        font-weight:600;
        padding:8px 16px;
    }

    .stButton>button:hover{
        background-color:#16a34a;
    }

    /* Text area styling */
    .stTextArea textarea{
        border-radius:10px;
        border:1px solid #d1d5db;
        padding:10px;
    }

    /* Sidebar improvements */
    section[data-testid="stSidebar"] {
        border-right:1px solid rgba(0,0,0,0.1);
    }

    </style>
    """, unsafe_allow_html=True)