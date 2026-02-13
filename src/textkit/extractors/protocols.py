from typing import Protocol


class Extractor(Protocol):
    def __call__(self, text: str) -> list[str]: ...
