import re
import string

def clean_text(text: str) -> str:
    """Clean raw input text for NLP tasks."""
    if not isinstance(text, str):
        text = str(text)  # convert non-string input

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove mentions and emails
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"\S+@\S+", "", text)

    # Remove punctuation (keep .,!? optionally)
    text = re.sub(r"[^\w\s.,!?]", "", text)

    # Remove extra whitespace
    text = ' '.join(text.split())

    return text.strip()
