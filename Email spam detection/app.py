import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


@st.cache_data
def load_data():
    df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'text']
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    return df


@st.cache_resource
def train_model(df):
    X = df['text']
    y = df['label']
    cv = CountVectorizer()
    X_vec = cv.fit_transform(X)
    model = MultinomialNB()
    model.fit(X_vec, y)
    return model, cv


df = load_data()
model, cv = train_model(df)


st.title("Spam Message Detector")
st.write("Type a message below and find out if it's spam or not.")

user_input = st.text_area("✉️ Enter your message:", height=150)

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        data = cv.transform([user_input]).toarray()
        prediction = model.predict(data)
        result = "Spam" if prediction[0] else "Ham:Not Spam"
        st.success(f"Prediction: {result}")
