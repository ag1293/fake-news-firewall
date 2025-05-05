import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load and prepare data
def load_and_prepare_data():
    df_fake = pd.read_csv("data/Fake.csv")
    df_true = pd.read_csv("data/True.csv")

    df_fake['label'] = 'Fake'
    df_true['label'] = 'Real'

    df = pd.concat([df_fake, df_true])
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df['content'] = df['title'] + " " + df['text']
    X = df['content']
    y = df['label']

    return train_test_split(X, y, test_size=0.2, random_state=42)

# Prepare the data
X_train, X_test, y_train, y_test = load_and_prepare_data()

# Train the model
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
clf = LogisticRegression()
clf.fit(X_train_vec, y_train)

# Optional: Save the model (comment this out on Railway if no write permission)
# joblib.dump(clf, "model/fake_news_model.pkl")
# joblib.dump(vectorizer, "model/vectorizer.pkl")

# Prediction function
def predict_credibility(text: str):
    X_input = vectorizer.transform([text])
    label = clf.predict(X_input)[0]
    confidence = np.max(clf.predict_proba(X_input)) * 100
    return {
        "label": label,
        "confidence": round(confidence, 2)
    }
