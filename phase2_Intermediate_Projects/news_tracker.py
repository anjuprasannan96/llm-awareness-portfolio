import feedparser
from utils.llama3_utils import query_llama3

GOOGLE_NEWS_RSS = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def fetch_google_news():
    """Fetch latest headlines from Google News RSS."""
    feed = feedparser.parse(GOOGLE_NEWS_RSS)
    headlines = [entry.title for entry in feed.entries[:10]]
    return headlines

def summarize_headlines_with_llama3(headlines):
    """Summarize headlines using LLaMA3."""
    prompt = f"""
Summarize the following news headlines into key trending topics:
{headlines}
"""
    return query_llama3(prompt)
