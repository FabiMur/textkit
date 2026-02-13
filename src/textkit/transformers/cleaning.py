DEFAULT_CHARS_REMOVE = [
    ",",
    ";",
    ":",
    "!",
    "¡",
    "¿",
    "?",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "+",
    "=",
    "|",
    "/",
    "~",
    "^",
    "°",
    "-",
    "_",
]


def clean_text(text: str, chars_to_remove: list[str] | None = None) -> str:
    """
    Clean the text by removing specific characters

    :param text: Text to clean
    :type text: str
    :param clean: List of characters to clean
    :type clean: list[str] | None
    :return: Cleaned text
    :rtype: str
    """
    characters = DEFAULT_CHARS_REMOVE if chars_to_remove is None else chars_to_remove
    cleaned_text = text
    for character in characters:
        cleaned_text = cleaned_text.replace(character, "")
    return cleaned_text
