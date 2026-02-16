import re

from .patterns import URL_PATTERN


def extract_url(text: str) -> list[str]:
    """ "
    Extracts URLs from text.
    Supported format: [scheme://][www.]domain.tld[/path]

    :param text: Input text to search for URLs.
    :type text: str
    :return: List of extracted URLs.
    :rtype: list[str]
    """
    regex = re.compile(URL_PATTERN, re.VERBOSE)
    urls = regex.findall(text)
    return [u.rstrip(".,;:!?)]}\"'") for u in urls]
