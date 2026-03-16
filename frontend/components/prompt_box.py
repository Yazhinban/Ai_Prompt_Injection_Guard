import streamlit as st

def prompt_input():

    st.subheader("Enter Prompt")

    prompt = st.text_area(
        "",
        placeholder="Type a prompt to test AI security...",
        height=150
    )

    col1,col2 = st.columns([1,4])

    send = col1.button("Analyze")

    return prompt, send