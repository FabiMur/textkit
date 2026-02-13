from collections.abc import Iterator
from zipfile import Path


class Reader:
    def __init__(self, input_file: str):
        self._supported_formats = ["txt", "html", "md"]
        self.input_file = input_file
        self.extension = input_file.split(".")[-1].lower()
        if self.extension not in self._supported_formats:
            raise ValueError(f"Unsupported file format: {self.extension}")
        self.extension = self.extension

    def read(self):
        """
        Docstring for read

        :type self: Reader
        """

        if self.extension == "txt":
            return self._read_txt()
        return ()

    def _read_txt(self) -> Iterator[str]:
        """
        Reads a text file and yields its lines one by one.

        :type self: Reader
        :return: Description
        :rtype: Iterator[str]
        """
        if not self.input_file.endswith(".txt"):
            raise ValueError("File must have a .txt extension")
        if not Path(self.input_file).is_file():
            raise FileNotFoundError(f"File not found: {self.input_file}")

        try:
            with Path(self.input_file).open(encoding="utf-8") as file:
                yield from file
        except Exception as e:
            raise OSError(f"Error reading {self.input_file}: {e}") from e
