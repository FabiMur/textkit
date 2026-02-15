from typing import Any

import pytest
from src.textkit.analyzers import (
    ExtractAnalyzer,
    LanguageDetector,
    SequenceAnalyzer,
    StatisticsAnalyzer,
)


@pytest.fixture
def sample_tokens() -> list[list[str]]:
    return [["hola", "mundo"], ["esta", "es", "una", "prueba", "hola"]]


@pytest.fixture
def sample_lines() -> list[str]:
    return [
        "Hola mundo",
        "Email: usuario@servicio",
        "Web oficial: https://test.com",
        "Teléfono: +34 900123123",
        "Fecha: 01/01/2025",
    ]


class TestStatisticsAnalyzer:
    def test_analyze_logic(self, sample_tokens: list[list[str]]) -> None:
        results = StatisticsAnalyzer().analyze(sample_tokens)
        assert results["total_tokens"] == 7
        assert results["unique_tokens"] == 6
        assert "hola" not in results["rare_words"]
        assert "mundo" in results["rare_words"]

    def test_analyze_empty(self) -> None:
        results = StatisticsAnalyzer().analyze([])
        assert results == {}

    def test_error_invalid_stream(self) -> None:
        bad_data: Any = [123, 456]
        with pytest.raises(TypeError, match="Formato de entrada inválido"):
            StatisticsAnalyzer().analyze(bad_data)


class TestSequenceAnalyzer:
    @pytest.mark.parametrize(
        "n, expected_key", [(1, "top_1_grams"), (2, "top_2_grams"), (5, "top_5_grams")]
    )
    def test_n_gram_ranges(self, sample_tokens: list[list[str]], n: int, expected_key: str) -> None:
        results = SequenceAnalyzer().analyze(sample_tokens, n=n)
        assert expected_key in results

    def test_analyze_empty(self) -> None:
        results = SequenceAnalyzer().analyze([], n=2)
        assert results == {"top_2_grams": []}

    def test_n_out_of_range(self, sample_tokens: list[list[str]]) -> None:
        with pytest.raises(ValueError, match="entre 1 y 5"):
            SequenceAnalyzer().analyze(sample_tokens, n=10)


class TestLanguageDetector:
    @pytest.mark.parametrize(
        "stream, expected_lang",
        [
            ([["enunciación", "estado", "pasado"]], "es"),
            ([["the", "king", "is", "playing"]], "en"),
            ([["xyz", "abc"]], "unknown"),
        ],
    )
    def test_detection(self, stream: list[list[str]], expected_lang: str) -> None:
        results = LanguageDetector().analyze(stream)
        assert results["detected_language"] == expected_lang

    def test_analyze_empty(self) -> None:
        results = LanguageDetector().analyze([])
        assert results["detected_language"] == "unknown"


class TestExtractAnalyzer:
    def test_extraction_counts(self, sample_lines: list[str]) -> None:
        results = ExtractAnalyzer().analyze(sample_lines)
        assert results["total_emails"] == 0
        assert results["total_urls"] == 1
        assert results["total_phones"] == 1
        assert results["total_dates"] == 1

    def test_analyze_empty(self) -> None:
        results = ExtractAnalyzer().analyze([])
        assert all(count == 0 for count in results.values())
