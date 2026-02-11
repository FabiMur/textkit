from abc import ABC, abstractmethod
from typing import Iterator


class BaseReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> Iterator[str]:
        pass
