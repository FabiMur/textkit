from typing import Iterator
from .base_reader import BaseReader
from pathlib import Path


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
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    yield line
        except Exception as e:
            raise IOError(f"Error reading file {file_path}: {e}")
