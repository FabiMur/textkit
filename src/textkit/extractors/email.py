import re

from .patterns import EMAIL_PATTERN


def extract_email(text: str) -> list[str]:
    regex = re.compile(EMAIL_PATTERN, re.VERBOSE)
    return regex.findall(text)
