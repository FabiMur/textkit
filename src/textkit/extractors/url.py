import re

from .patterns import URL_PATTERN


class URLExtractor:
    def extract(self, text: str) -> list[str]:
        regex = re.compile(URL_PATTERN, re.VERBOSE)
        urls = regex.findall(text)
        return [u.rstrip(".,;:!?)]}\"'") for u in urls]
