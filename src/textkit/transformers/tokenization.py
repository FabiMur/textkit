import re


def tokenize_words(text: str) -> list[str]:
    """
    Split the input text into words removing punctuation
    and extra whitespace.

    :param text: Text to tokenize into words
    :type text: str
    :return: Tokenized text
    :rtype: list[str]
    """

    if not text.strip():
        return []
    text_clean = re.sub(r"[^\w\s]", " ", text)
    return [word for word in text_clean.split() if word.strip()]


def tokenize_sentences(text: str):
    """
    Split text into sentences
    Sentences are separated at periods, exclamation or question marks,
    that are followed by a space or the end of the text.

    :param text: Text to tokenize into sentences
    :type text: str
    :return: Tokenized text
    :rtype: list[str]
    """
    if not text.strip():
        return []

    sentences = re.split(r"(?<=[.!?])\s+", text)

    cleaned_sentences = [s.strip() for s in sentences if s.strip()]

    return cleaned_sentences
