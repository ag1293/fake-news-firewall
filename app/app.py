import streamlit as st
import requests
from app.model import predict_credibility

st.set_page_config(page_title="Fake News Firewall", layout="centered")

st.title("🛡️ Fake News Firewall")
st.write("Check the credibility of a news headline or short article.")

# Text input from user
user_input = st.text_area("Enter a news headline or short article:")

if st.button("Check Credibility"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Send input to FastAPI backend
        with st.spinner("Analyzing..."):
            try:
                result = predict_credibility(user_input)
                st.success(f"Prediction: **{result['label']}**")
                st.metric(label="Trust Score", value=f"{100 - result['confidence']:.2f} / 100")
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"Prediction: **{result['label']}**")
                    st.metric(label="Trust Score", value=f"{100 - result['confidence']:.2f} / 100")
                else:
                    st.error("Error: Could not get a valid response from backend.")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")

st.markdown("---")
st.caption("Built with 💻 Streamlit & NLP")
