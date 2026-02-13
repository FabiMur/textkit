import re

from .patterns import DATE_EU_PATTERN


def extract_date(text: str) -> list[str]:
    regex = re.compile(DATE_EU_PATTERN, re.VERBOSE)
    return regex.findall(text)
