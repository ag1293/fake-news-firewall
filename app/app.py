
from app.model import predict_credibility
import streamlit as st

st.set_page_config(page_title="Fake News Firewall", layout="centered")

st.title("🛡️ Fake News Firewall")
st.write("Check the credibility of a news headline or short article.")

# Text input from user
user_input = st.text_area("Enter a news headline or short article:")

if st.button("Check Credibility"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing..."):
            try:
                result = predict_credibility(user_input)
                st.success(f"Prediction: **{result['label']}**")
                st.metric(label="Trust Score", value=f"{100 - result['confidence']:.2f} / 100")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

st.markdown("---")
st.caption("Built with 💻 Streamlit & NLP")
