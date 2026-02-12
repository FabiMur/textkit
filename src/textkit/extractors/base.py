from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, text: str) -> list[str]:
        raise NotImplementedError("Subclasses must implement this method")
