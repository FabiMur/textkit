import re

from .patterns import PHONE_EU_PATTERN

""""
Extracts phone numbers with country code and exactly 9 digits from text.
Supported format: [+][country code][number]

:param text: Input text to search for phone numbers.
:type text: str
:return: List of extracted phone numbers.
:rtype: list[str]
"""


def extract_phone(text: str) -> list[str]:
    regex = re.compile(PHONE_EU_PATTERN, re.VERBOSE)
    return regex.findall(text)
