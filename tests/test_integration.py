# tests/test_cli_integration.py
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def project_root():
    return Path(__file__).parent.parent


def run_textkit(args: list[str], cwd: Path):
    """
    Ejecuta el CLI real (main.py) como lo haría un usuario.
    """
    return subprocess.run(
        [sys.executable, "main.py", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )


def test_help(project_root: Path) -> None:
    """
    Verify that the help command works correctly.
    :param project_root: The project's root directory where main.py is located.
    :type project_root: Path
    """
    p = run_textkit(["--help"], cwd=project_root)
    assert p.returncode == 0
    assert "textkit" in (p.stdout + p.stderr).lower()


def test_extract_email(project_root: Path, tmp_path: Path) -> None:
    """
    Verify that the email extraction command works correctly and writes the expected output.
    :param project_root: The project's root directory where main.py is located.
    :type project_root: Path
    :param tmp_path: A temporary directory provided by pytest to store test files
    :type tmp_path: Path
    """
    in_file = tmp_path / "document.txt"
    in_file.write_text("hola test@example.com foo@bar.org\n", encoding="utf-8")

    out_file = tmp_path / "extracted.txt"
    p = run_textkit(
        ["extract", "--input", str(in_file), "--output", str(out_file), "--type", "email"],
        cwd=project_root,
    )
    assert p.returncode == 0, p.stderr

    out = out_file.read_text(encoding="utf-8").lower()
    assert "test@example.com" in out
    assert "foo@bar.org" in out


def test_analyze_writes_output(project_root: Path, tmp_path: Path) -> None:
    """
    Verify that the analysis command works correctly and writes the expected output.
    :param project_root: The project's root directory where main.py is located.
    :type project_root: Path
    :param tmp_path: A temporary directory provided by pytest to store test files
    :type tmp_path: Path
    """
    in_file = tmp_path / "in.txt"
    out_file = tmp_path / "out.json"
    in_file.write_text("hello world\nhello\n", encoding="utf-8")

    p = run_textkit(
        ["analyze", "--input", str(in_file), "--output", str(out_file), "--ngram_size", "2"],
        cwd=project_root,
    )
    assert p.returncode == 0, p.stderr
    assert out_file.exists()
    assert out_file.read_text(encoding="utf-8").strip() != ""
