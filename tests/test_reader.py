from pathlib import Path

import pytest

from textkit.reader import Reader


@pytest.fixture
def sample_txt_file(tmp_path: Path) -> Path:
    file_path = tmp_path / "sample_document.txt"
    file_content = (
        "Yesterday, all my troubles seemed so far away\n"
        "Now it looks as though they're here to stay\n"
        "Oh, I believe in yesterday"
    )
    file_path.write_text(file_content, encoding="utf-8")
    return file_path


def test_read_txt(sample_txt_file: Path):
    reader = Reader(str(sample_txt_file))
    lines = list(reader._read_txt())

    assert lines == [
        "Yesterday, all my troubles seemed so far away\n",
        "Now it looks as though they're here to stay\n",
        "Oh, I believe in yesterday",
    ]


def test_unsupported_format():
    with pytest.raises(ValueError, match="Unsupported file format: pdf"):
        Reader("document.pdf")


def test_file_not_found():
    """
    If _read_txt function raises a FileNotFoundError when the specified file does not exist.
    """
    with pytest.raises(FileNotFoundError, match=r"File not found: non_existent\.txt"):
        gen = Reader("non_existent.txt")._read_txt()
        next(gen)


def test_wrong_extension_txt(sample_txt_file: Path):
    """
    If _read_text function raises a ValueError when the file does not have a .txt extension.
    :param sample_txt_file: A temporary .txt file created by the fixture.
    :type sample_txt_file: Path
    """
    with pytest.raises(ValueError, match=r"File must have a \.txt extension"):
        gen = Reader(str(sample_txt_file.with_suffix(".md")))._read_txt()
        next(gen)
