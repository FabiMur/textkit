from pathlib import Path

_RESOURCES_DIR = Path(__file__).resolve().parent / "resources"


def _load_stopwords(lang: str) -> set[str]:
    """
    Load stopwords file for a given language.
    """
    path = _RESOURCES_DIR / f"stopwords_{lang}.txt"
    return {word.strip() for word in path.read_text(encoding="utf-8").splitlines() if word.strip()}


def remove_stopwords(text: str) -> list[str]:
    """
    Remove stopwords (ES, EN, FR) from text.

    :param text: Input text
    :type text: str
    :return: Text without stopwords
    :rtype: str
    """
    es_stopwords = _load_stopwords("es")
    en_stopwords = _load_stopwords("en")
    fr_stopwords = _load_stopwords("fr")

    all_stopwords = es_stopwords | en_stopwords | fr_stopwords

    words = text.split()

    cleaned_words = [word for word in words if word.lower() not in all_stopwords]

    return cleaned_words
