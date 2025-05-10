
from dotenv import load_dotenv
import os
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
from model import predict_credibility
import streamlit as st
import requests

st.set_page_config(page_title="Fake News Firewall", layout="centered")

st.title("🛡️ Fake News Firewall")
st.write("Check the credibility of a news headline or short article.")

# Text input from user
user_input = st.text_area("Enter a news headline or short article:")

st.markdown("---")
st.header("📰 Check Live News")

if st.button("Fetch & Analyze Headlines"):
    try:
        url = f"https://newsapi.org/v2/everything?q=AI&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        news_data = response.json()

        # 🔍 Debug output
        st.write("📡 Response:", response.status_code)
        st.json(news_data)

        for article in news_data["articles"][:10]:  # Top 10 articles
            title = article["title"]
            if title:
                result = predict_credibility(title)
                trust_score = 100 - result["confidence"]

                st.markdown(f"**📰 {title}**")
                st.write(f"Prediction: **{result['label']}** | Trust Score: **{trust_score:.2f} / 100**")
                st.markdown("---")
    except Exception as e:
        st.error(f"Failed to fetch news: {e}")

st.markdown("---")
st.caption("Built with 💻 Streamlit & NLP")
