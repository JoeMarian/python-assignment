from textblob import TextBlob

def summarize_article(content):
    blob = TextBlob(content)
    summary = blob.noun_phrases
    return " ".join(summary[:5])  # Returning first few noun phrases as a summary
