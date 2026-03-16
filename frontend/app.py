import streamlit as st
from streamlit_option_menu import option_menu
from styles.theme import apply_theme

st.set_page_config(
    page_title="AI Prompt Injection Guard",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_default_nav = """
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
"""
st.markdown(hide_default_nav, unsafe_allow_html=True)

apply_theme()

with st.sidebar:

    st.markdown("## 🛡 AI Prompt Guard")

    selected = option_menu(
        "Navigation",
        [
            "Chat",
            "Dashboard",
            "Attack Logs",
            "Model Analytics",
            "Admin Review"
        ],
        icons=[
            "chat-dots",
            "shield-lock",
            "database",
            "bar-chart",
            "person-lock"
        ],
        menu_icon="shield-lock",
        default_index=0,
    )

if selected == "Chat":
    from pages.chat import show_chat
    show_chat()

elif selected == "Dashboard":
    from pages.dashboard import show_dashboard
    show_dashboard()

elif selected == "Attack Logs":
    from pages.attack_logs import show_logs
    show_logs()

elif selected == "Model Analytics":
    from pages.model_analytics import show_model_analytics
    show_model_analytics()

elif selected == "Admin Review":
    from pages.admin_review import show_admin_review
    show_admin_review()