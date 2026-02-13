from collections.abc import Iterator
from zipfile import Path


class Reader:
    def __init__(self):
        self._supported_formats = ["txt", "html", "md"]

    def read(self, file_path: str):
        """
        Docstring for read

        :param self: Description
        :param file_path: Description
        :type file_path: str
        """
        extension = file_path.split(".")[-1].lower()
        if extension not in self._supported_formats:
            raise ValueError(f"Unsupported file format: {extension}")

        if extension == "txt":
            return self._read_txt(file_path)
        return None

    def _read_txt(self, file_path: str) -> Iterator[str]:
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
                yield from file
        except Exception as e:
            raise OSError(f"Error reading {file_path}: {e}") from e
