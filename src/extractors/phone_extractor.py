from .base import BaseExtractor
from .patterns import PHONE_EU_RE


class PhoneExtractor(BaseExtractor):
    def extract(self, text: str) -> list[str]:
        return PHONE_EU_RE.findall(text)
