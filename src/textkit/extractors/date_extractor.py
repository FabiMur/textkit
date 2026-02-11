from .base import BaseExtractor
from .patterns import DATE_EU_RE


class DateExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        return DATE_EU_RE.findall(text)
