from abc import ABC, abstractmethod
from collections.abc import Iterable


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, text: str) -> Iterable[str]:
        raise NotImplementedError("Subclasses must implement this method")
