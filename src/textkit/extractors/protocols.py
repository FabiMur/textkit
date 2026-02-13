from typing import Protocol


class BaseExtractor(Protocol):
    def extract(self, text: str) -> list[str]: ...
