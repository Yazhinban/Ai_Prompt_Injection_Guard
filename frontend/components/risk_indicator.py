import streamlit as st

def show_risk(score):

    st.subheader("Risk Score")

    if score < 0.4:
        label = "Low Risk"
        color = "green"

    elif score < 0.7:
        label = "Medium Risk"
        color = "orange"

    else:
        label = "High Risk"
        color = "red"

    st.markdown(
        f"""
        <div style="
            padding:15px;
            border-radius:10px;
            border-left:6px solid {color};
            background-color:rgba(0,0,0,0.05);
            font-size:18px;
        ">
        <b>{label}</b> : {score}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(score)