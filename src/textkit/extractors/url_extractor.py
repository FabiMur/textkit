import re

from .base import BaseExtractor
from .patterns import URL_PATTERN


class URLExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        regex = re.compile(URL_PATTERN, re.VERBOSE)
        urls = regex.findall(text)
        return [u.rstrip(".,;:!?)]}\"'") for u in urls]
