from dotenv import load_dotenv
import os
import requests
import streamlit as st
from model import predict_credibility

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# App UI
st.set_page_config(page_title="Fake News Firewall", layout="centered")

st.title("🛡️ Fake News Firewall")
st.write("Check the credibility of a news headline or short article.")

# 🧠 Manual Input
user_input = st.text_area("Enter a news headline or short article:")

if st.button("Check Credibility"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = predict_credibility(user_input)
        st.success(f"Prediction: **{result['label']}**")
        st.metric("Trust Score", f"{100 - result['confidence']:.2f} / 100")

st.markdown("---")

# 🌐 Live News Analysis
st.header("📰 Check Live News")

# Optional: Let user choose topic
keyword = st.text_input("🔍 Enter a keyword to fetch live news about:", value="India")

if st.button("Fetch & Analyze Headlines"):
    try:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={keyword}&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
        )
        response = requests.get(url)
        news_data = response.json()

        for article in news_data["articles"][:10]:
            title = article["title"]
            if title:
                result = predict_credibility(title)
                trust_score = 100 - result["confidence"]

                st.markdown(f"**📰 {title}**")
                st.write(f"Prediction: **{result['label']}**")
                st.metric("Trust Score", f"{trust_score:.2f} / 100")
                st.markdown("---")
    except Exception as e:
        st.error(f"Failed to fetch news: {e}")

st.markdown("---")
st.caption("Built with 💻 Streamlit & NLP")
