import re

from .patterns import PHONE_EU_PATTERN


class PhoneExtractor:
    def extract(self, text: str) -> list[str]:
        regex = re.compile(PHONE_EU_PATTERN, re.VERBOSE)
        return regex.findall(text)
