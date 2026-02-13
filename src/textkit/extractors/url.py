import re

from .patterns import URL_PATTERN


def extract_url(text: str) -> list[str]:
    regex = re.compile(URL_PATTERN, re.VERBOSE)
    urls = regex.findall(text)
    return [u.rstrip(".,;:!?)]}\"'") for u in urls]
