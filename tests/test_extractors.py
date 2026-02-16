"""Tests for the extractors module."""

from textkit.extractors import (
    extract_date,
    extract_email,
    extract_phone,
    extract_url,
)


class TestDateExtractor:
    def test_extract_dates_base(self):
        text = "La fecha de hoy es 15/09/2024 y mañana será 16/09/2024."
        dates = extract_date(text)
        assert dates == ["15/09/2024", "16/09/2024"]

    def test_extract_dates_no_dates(self):
        text = "No hay fechas en este texto."
        dates = extract_date(text)
        assert dates == []

    def test_extract_dates_different_formats(self):
        text = "Fechas en diferentes formatos: 01.01.2024, 31/12/2024."
        dates = extract_date(text)
        assert dates == ["01.01.2024", "31/12/2024"]


class TestEmailExtractor:
    def test_extract_emails_base(self):
        text = "Contáctanos en contacto@example.com para más información."
        emails = extract_email(text)
        assert emails == ["contacto@example.com"]

    def test_extract_emails_no_emails(self):
        text = "No hay correos electrónicos en este texto."
        emails = extract_email(text)
        assert emails == []

    def test_extract_emails_different_formats(self):
        text = (
            "Correos en diferentes formatos: contacto@example.com, "
            "user.name+tag+sorting@example.com."
        )
        emails = extract_email(text)
        assert emails == ["contacto@example.com", "user.name+tag+sorting@example.com"]


class TestPhoneExtractor:
    def test_extract_phones_base(self):
        text = "Llámanos al +34 123 456 789 o al 123-456-789."
        phones = extract_phone(text)
        assert phones == ["+34 123 456 789", "123-456-789"]

    def test_extract_phones_no_phones(self):
        text = "No hay números de teléfono en este texto."
        phones = extract_phone(text)
        assert phones == []

    def test_extract_phones_different_formats(self):
        text = "Números en diferentes formatos: 234567890, 123 456 789."
        phones = extract_phone(text)
        assert phones == ["234567890", "123 456 789"]


class TestURLExtractor:
    def test_extract_urls_base(self):
        text = "Visita nuestro sitio web en https://www.example.com o http://example.org."
        urls = extract_url(text)
        assert urls == ["https://www.example.com", "http://example.org"]

    def test_extract_urls_no_urls(self):
        text = "No hay URLs en este texto."
        urls = extract_url(text)
        assert urls == []

    def test_extract_urls_different_formats(self):
        text = "URLs en diferentes formatos: www.example.com, example.com/path/to/resource."
        urls = extract_url(text)
        assert urls == ["www.example.com", "example.com/path/to/resource"]
