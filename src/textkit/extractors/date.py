import re

from .patterns import DATE_EU_PATTERN


def extract_date(text: str) -> list[str]:
    """ "
    Extracts European date formats from text.
    Supported formats: DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY

    :param text: Input text to search for dates.
    :type text: str
    :return: List of extracted date strings.
    :rtype: list[str]
    """
    regex = re.compile(DATE_EU_PATTERN, re.VERBOSE)
    return regex.findall(text)
