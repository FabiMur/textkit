from abc import ABC, abstractmethod
from collections.abc import Iterator


class BaseReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> Iterator[str]:
        pass
