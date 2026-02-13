import re


def tokenize_words(text: str) -> list[str]:
    """Split text into words"""
    if not text.strip():
        return []
    text_clean = re.sub(r"[^\w\s]", " ", text)
    return [word for word in text_clean.split() if word.strip()]


def tokenize_sentences(text: str) -> list[str]:
    """Split text into sentences"""
    if not text.strip():
        return []
    sentences = re.split(r"[.!?]+", text)
    cleaned_sentences = []
    for sentence in sentences:
        sentence_clean = re.sub(r"[^\w\s]", " ", sentence)
        sentence_clean = " ".join(sentence_clean.split())
        if sentence_clean:
            cleaned_sentences.append(sentence_clean)
    return cleaned_sentences
