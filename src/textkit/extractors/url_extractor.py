from .base import BaseExtractor
from .patterns import URL_RE


class URLExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        return URL_RE.findall(text)
