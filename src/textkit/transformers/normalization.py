def normalize_text(text: str) -> str:
    """
    Remove leading and trailing spaces and convert to lowercase.

    :param text: Text to normalize
    :type text: str
    :return: Normalized text
    :rtype: str
    """
    return text.strip().lower()
