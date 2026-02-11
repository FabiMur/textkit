"""Tests for the extractors module."""

from textkit.extractors import (
    DateExtractor,
    EmailExtractor,
    PhoneExtractor,
    URLExtractor,
)


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


class TestEmailExtractor:
    def test_extract_emails1(self):
        text = "Contáctanos en contacto@example.com para más información."
        extractor = EmailExtractor()
        emails = extractor.extract(text)
        assert emails == ["contacto@example.com"]

    def test_extract_emails2(self):
        text = "No hay correos electrónicos en este texto."
        extractor = EmailExtractor()
        emails = extractor.extract(text)
        assert emails == []

    def test_extract_emails3(self):
        text = "Correos en diferentes formatos: contacto@example.com, user.name+tag+sorting@example.com."
        extractor = EmailExtractor()
        emails = extractor.extract(text)
        assert emails == ["contacto@example.com", "user.name+tag+sorting@example.com"]


class TestPhoneExtractor:
    def test_extract_phones1(self):
        text = "Llámanos al +34 123 456 789 o al 123-456-789."
        extractor = PhoneExtractor()
        phones = extractor.extract(text)
        assert phones == ["+34 123 456 789", "123-456-789"]

    def test_extract_phones2(self):
        text = "No hay números de teléfono en este texto."
        extractor = PhoneExtractor()
        phones = extractor.extract(text)
        assert phones == []


class TestURLExtractor:
    def test_extract_urls1(self):
        text = (
            "Visita nuestro sitio web en https://www.example.com o http://example.org."
        )
        extractor = URLExtractor()
        urls = extractor.extract(text)
        assert urls == ["https://www.example.com", "http://example.org"]

    def test_extract_urls2(self):
        text = "No hay URLs en este texto."
        extractor = URLExtractor()
        urls = extractor.extract(text)
        assert urls == []

    def test_extract_urls3(self):
        text = "URLs en diferentes formatos: www.example.com, example.com/path/to/resource."
        extractor = URLExtractor()
        urls = extractor.extract(text)
        assert urls == ["www.example.com", "example.com/path/to/resource"]
