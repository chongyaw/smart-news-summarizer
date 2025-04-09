import secrets

# This library will be used to parse the JSON data returned by the API.
import json

# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library wil be used to fetch the API.
import urllib.request

# pip install newspaper3k
# pip install lxml_html_clean
from newspaper import Article

# GNews API key
apikey = secrets.gnewsapikey

# Use GNews API to search for news articles
def fetch_news(query="AI", max_articles=5):

    query = query.replace(" ", "%20", -1)

    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max={max_articles}&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["articles"]
