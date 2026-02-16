import pytest
from src.textkit.analyzers import (
    ExtractAnalyzer,
    LanguageDetector,
    SequenceAnalyzer,
    StatisticsAnalyzer,
)

"""
==========================
Fixtures
==========================
"""


@pytest.fixture
def sample_tokens() -> list[list[str]]:
    return [["hola", "mundo"], ["esta", "es", "una", "prueba", "hola"]]


@pytest.fixture
def sample_lines() -> list[str]:
    return [
        "Hola mundo",
        "Email: usuario@servicio.com",
        "Web oficial: https://test.com",
        "Teléfono: +34 900123123",
        "Fecha: 01/01/2025",
    ]


"""
==========================
Tests para StatisticsAnalyzer
==========================
"""


class TestStatisticsAnalyzer:
    def test_analyze_logic(self, sample_tokens: list[list[str]]) -> None:
        analyzer = StatisticsAnalyzer()
        for tokens in sample_tokens:
            analyzer.analyze(tokens)

        results = analyzer.get_report()
        assert results["total_tokens"] == 7
        assert results["unique_tokens"] == 6
        assert "hola" not in results["rare_words"]
        assert "mundo" in results["rare_words"]

    def test_analyze_empty(self) -> None:
        analyzer = StatisticsAnalyzer()
        results = analyzer.get_report()
        assert results == {}


"""
==========================
Tests para SequenceAnalyzer
==========================
"""


class TestSequenceAnalyzer:
    @pytest.mark.parametrize(
        "n, expected_key", [(1, "top_1_grams"), (2, "top_2_grams"), (5, "top_5_grams")]
    )
    def test_n_gram_ranges(self, sample_tokens: list[list[str]], n: int, expected_key: str) -> None:
        analyzer = SequenceAnalyzer()
        for tokens in sample_tokens:
            analyzer.analyze(tokens, n=n)

        results = analyzer.get_report(n=n)
        assert expected_key in results

    def test_analyze_empty(self) -> None:
        analyzer = SequenceAnalyzer()
        results = analyzer.get_report(n=2)
        assert results == {"top_2_grams": []}

    def test_n_out_of_range(self) -> None:
        analyzer = SequenceAnalyzer()
        with pytest.raises(ValueError, match="entre 1 y 5"):
            analyzer.analyze(["test"], n=10)


"""
==========================
Tests para LanguageDetector
==========================
"""


class TestLanguageDetector:
    def test_detection_spanish(self) -> None:
        detector = LanguageDetector()
        detector.analyze(["estado", "edificio", "pasado"])

        results = detector.get_report()
        assert results["detected_language"] == "es"
        assert results["language_scores"]["es"]["ado"] == 2
        assert results["language_scores"]["es"]["cio"] == 1

    def test_detection_english(self) -> None:
        detector = LanguageDetector()
        detector.analyze(["playing", "action", "running"])

        results = detector.get_report()
        assert results["detected_language"] == "en"
        assert results["language_scores"]["en"]["ing"] == 2

    def test_detection_unknown(self) -> None:
        detector = LanguageDetector()
        detector.analyze(["xyz", "abc", "qwerty"])

        results = detector.get_report()
        assert results["detected_language"] == "unknown"

    def test_analyze_empty(self) -> None:
        detector = LanguageDetector()
        results = detector.get_report()
        assert results["detected_language"] == "unknown"


"""
==========================
Tests para ExtractAnalyzer
==========================
"""


class TestExtractAnalyzer:
    def test_extraction_counts(self, sample_lines: list[str]) -> None:
        analyzer = ExtractAnalyzer()
        for line in sample_lines:
            analyzer.analyze(line)

        results = analyzer.get_report()
        assert results["total_emails"] == 1
        assert results["total_urls"] == 2
        assert results["total_phones"] == 1
        assert results["total_dates"] == 1

    def test_analyze_empty(self) -> None:
        analyzer = ExtractAnalyzer()
        results = analyzer.get_report()
        assert all(count == 0 for count in results.values())
