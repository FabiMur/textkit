import re

from .base import BaseExtractor
from .patterns import DATE_EU_PATTERN


class DateExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        regex = re.compile(DATE_EU_PATTERN, re.VERBOSE)
        return regex.findall(text)
