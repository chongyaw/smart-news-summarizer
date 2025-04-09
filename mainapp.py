# This scripts opens a Streamlit web UI, hence please use the following command:
# streamlit run c:/Users/cy185005/portableapps/PortableGit/bin/smart-news-summarizer/mainapp.py

# Import code from another python script file
from getnewsarticles import fetch_news
from summarize import summarize
from categorize import categorize

# pip install newspaper3k
# pip install lxml_html_clean
from newspaper import Article

# pip install streamlit
import streamlit as st

st.title("Smart News Summarizer")
query = st.text_input("Search topic", "AI")
max_articles = st.number_input("Number of articles to return: ", 1, 3)

if st.button("Fetch and Summarize"):
    articles = fetch_news(query, max_articles)
    for result in articles:
        # Using newspaper3k to scrape an article
        url = result['url']
        article = Article(url)
        article.download()
        article.parse()
        
        st.subheader(article.title)
        st.write(article.url)
        st.write(article.text)
        st.write(f"Tags: {article.tags}")

        listofwords = article.text.split()[:50]

        while listofwords[-1][-1] != ".":
            listofwords.pop(-1)

        partialarticle = " ".join(listofwords)

        st.write(f"**Summary (by OpenAI) **: {summarize(partialarticle)}")
        st.write(f"**Category (by OpenAI) **: {categorize(partialarticle)}")
