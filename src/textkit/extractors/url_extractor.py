from .base import BaseExtractor
from .patterns import URL_RE


class URLExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        urls = URL_RE.findall(text)
        return [u.rstrip(".,;:!?)]}\"'") for u in urls]
