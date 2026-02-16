import stopwordsiso as stopwords


def remove_stopwords(text: str) -> str:
    """
    Clean the text by removing specific characters

    :param text: Text to clean
    :type text: str
    :param stopwords_to_remove: List of stopwords to remove
    :type stopwords_to_remove: list[str] | None
    :return: Cleaned text
    :rtype: str
    """
    es_stopwords = stopwords.stopwords("es")
    en_stopwords = stopwords.stopwords("en")
    fr_stopwords = stopwords.stopwords("fr")

    all_stopwords = set(es_stopwords) | set(en_stopwords) | set(fr_stopwords)

    words = text.split()

    cleaned_words = [word for word in words if word.lower() not in all_stopwords]

    return " ".join(cleaned_words)
