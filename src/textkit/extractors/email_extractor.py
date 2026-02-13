import re

from .base import BaseExtractor
from .patterns import EMAIL_PATTERN


class EmailExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        regex = re.compile(EMAIL_PATTERN, re.VERBOSE)
        return regex.findall(text)
