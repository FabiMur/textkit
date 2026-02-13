import re

from .patterns import PHONE_EU_PATTERN


def extract_phone(text: str) -> list[str]:
    regex = re.compile(PHONE_EU_PATTERN, re.VERBOSE)
    return regex.findall(text)
