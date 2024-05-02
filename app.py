import streamlit as st
from newspaper import Article
import joblib

# Load text classification model
model = joblib.load("news-classification-model.pkl")
news_labels = {'0': 'Technical', '1': 'Business', '2': 'Sport', '3': 'Entertainment', '4': 'Politics'}

st.title("News Category Classification")


st.subheader("You can input news text and get the predicted category.")

if st.button("About"):
    st.success("Hello! I am Sourikta from CSDA,DUK. This is a text classification tool.")

status = st.radio("Select option: ", ('Enter a URL', 'Enter a Paragraph'))

# Text classification part



if status == 'Enter a URL':
    url_input = st.text_input("Enter the URL:")
    if st.button("Predict Category"):
        article = Article(url_input)
        article.download()
        article.parse()
        user_input = article.text
        predicted_label = model.predict([user_input])[0]
        predicted_news_label = news_labels[str(predicted_label)]
        st.info(f"Predicted News Category: {predicted_news_label}")

else:
    paragraph_input = st.text_area("Enter the Paragraph:")
    if st.button("Predict Category"):
        user_input = paragraph_input
        predicted_label = model.predict([user_input])[0]
        predicted_news_label = news_labels[str(predicted_label)]
        st.info(f"Predicted News Category: {predicted_news_label}")
