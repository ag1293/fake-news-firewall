from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from app.data_preprocessing import load_and_prepare_data
import numpy as np

# Load and prepare data
X_train, X_test, y_train, y_test = load_and_prepare_data()

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
clf = LogisticRegression()
clf.fit(X_train_vec, y_train)

def predict_credibility(text: str):
    X_input = vectorizer.transform([text])
    label = clf.predict(X_input)[0]
    confidence = np.max(clf.predict_proba(X_input)) * 100
    return {
        "label": label,
        "confidence": round(confidence, 2)
    }
