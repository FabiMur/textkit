from collections.abc import Iterator
from pathlib import Path

from .base_reader import BaseReader


class TxtReader(BaseReader):
    def read(self, file_path: str) -> Iterator[str]:
        """
        Reads a text file and yields its lines one by one.

        :param self: Description
        :param file_path: Description
        :type file_path: str
        :return: Description
        :rtype: Iterator[str]
        """
        if not file_path.endswith(".txt"):
            raise ValueError("File must have a .txt extension")
        if not Path(file_path).is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with Path(file_path).open(encoding="utf-8") as file:
                for line in file:
                    yield from line
        except Exception as e:
            raise OSError(f"Error reading {file_path}: {e}") from e
