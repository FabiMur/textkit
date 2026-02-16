import re

from .patterns import EMAIL_PATTERN


def extract_email(text: str) -> list[str]:
    """ "
    Extracts standard email addresses from text.
    Supported format: username@domain.tld

    :param text: Input text to search for email addresses.
    :type text: str
    :return: List of extracted email addresses.
    :rtype: list[str]
    """
    regex = re.compile(EMAIL_PATTERN, re.VERBOSE)
    return regex.findall(text)
