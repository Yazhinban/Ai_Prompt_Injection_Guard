import streamlit as st

def show_risk(score):

    st.subheader("Risk Score")

    if score < 0.4:
        st.success(f"Low Risk : {score}")

    elif score < 0.7:
        st.warning(f"Medium Risk : {score}")

    else:
        st.error(f"High Risk : {score}")

    st.progress(score)