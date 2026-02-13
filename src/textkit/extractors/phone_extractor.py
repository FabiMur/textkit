import re

from .base import BaseExtractor
from .patterns import PHONE_EU_PATTERN


class PhoneExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        regex = re.compile(PHONE_EU_PATTERN, re.VERBOSE)
        return regex.findall(text)
