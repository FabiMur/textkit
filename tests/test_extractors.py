"""Tests for the extractors module."""

from textkit.extractors import DateExtractor


class TestDateExtractor:
    def test_extract_dates1(self):
        text = "La fecha de hoy es 15/09/2024 y mañana será 16/09/2024."
        extractor = DateExtractor()
        dates = extractor.extract(text)
        assert dates == ["15/09/2024", "16/09/2024"]

    def test_extract_dates2(self):
        text = "No hay fechas en este texto."
        extractor = DateExtractor()
        dates = extractor.extract(text)
        assert dates == []

    def test_extract_dates3(self):
        text = "Fechas en diferentes formatos: 01/01/2024, 31/12/2024."
        extractor = DateExtractor()
        dates = extractor.extract(text)
        assert dates == ["01/01/2024", "31/12/2024"]
