from .base import BaseExtractor
from .patterns import EMAIL_RE


class EmailExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        return EMAIL_RE.findall(text)
