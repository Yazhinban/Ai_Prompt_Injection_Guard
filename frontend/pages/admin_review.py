import streamlit as st
from services.api_client import get_admin_reviews, approve_prompt, reject_prompt


def show_admin_review():

    st.title("🛠 Admin Review Panel")

    reviews = get_admin_reviews()

    if not reviews:

        st.success("No prompts waiting for review.")
        return

    for r in reviews:

        prompt_id = r[0]
        prompt = r[1]
        risk_score = r[2]

        st.markdown("---")

        st.write(f"**Prompt ID:** {prompt_id}")
        st.write(f"**Prompt:** {prompt}")
        st.write(f"**Risk Score:** {risk_score}")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(f"Approve {prompt_id}"):

                approve_prompt(prompt_id)

                st.success("Prompt approved")

                st.rerun()

        with col2:

            if st.button(f"Reject {prompt_id}"):

                reject_prompt(prompt_id)

                st.error("Prompt rejected")

                st.rerun()