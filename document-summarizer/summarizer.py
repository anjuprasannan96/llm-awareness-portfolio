# summarizer.py

from transformers import pipeline

# Load the summarizer model once (on app load)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk=1000):
    summaries = []
    for i in range(0, len(text), max_chunk):
        chunk = text[i:i+max_chunk]
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(result[0]['summary_text'])
    return " ".join(summaries)
