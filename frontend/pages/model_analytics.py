import streamlit as st
import plotly.express as px

def show_model_analytics():

    st.title("Model Analytics")

    accuracy = 0.91
    precision = 0.88
    recall = 0.87

    st.metric("Accuracy",accuracy)
    st.metric("Precision",precision)
    st.metric("Recall",recall)

    fig = px.bar(
        x=["Accuracy","Precision","Recall"],
        y=[accuracy,precision,recall],
        title="Model Performance"
    )

    st.plotly_chart(fig)