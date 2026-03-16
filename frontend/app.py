import streamlit as st
from streamlit_option_menu import option_menu
from styles.theme import apply_theme

# Page configuration
st.set_page_config(
    page_title="AI Prompt Injection Guard",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide default Streamlit page navigation
hide_default_nav = """
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
"""
st.markdown(hide_default_nav, unsafe_allow_html=True)

# Apply custom theme
apply_theme()

# Sidebar
with st.sidebar:

    st.markdown("## 🛡 AI Prompt Guard")

    selected = option_menu(
        "Navigation",
        ["Chat", "Dashboard", "Attack Logs", "Model Analytics"],
        icons=["chat-dots", "shield-lock", "database", "bar-chart"],
        menu_icon="shield-lock",
        default_index=0,
    )

# Page routing
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