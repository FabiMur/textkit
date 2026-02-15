from collections.abc import Iterable

from src.textkit.extractors.date import extract_date
from src.textkit.extractors.email import extract_email
from src.textkit.extractors.phone import extract_phone
from src.textkit.extractors.url import extract_url


class ExtractAnalyzer:
    def __init__(self):
        """Mapeo de funciones extractoras."""
        self.extractors = {
            "dates": extract_date,
            "emails": extract_email,
            "phones": extract_phone,
            "urls": extract_url,
        }

    def analyze(self, line_stream: Iterable[str]) -> dict:
        """
        Procesa un flujo de líneas y acumula el total de menciones por cada entidad.

        :param line_stream: Iterable que entrega líneas de texto crudo.
        :return: Diccionario con los conteos totales (e.g., {'total_emails': 5}).
        """
        counts = {f"total_{key}": 0 for key in self.extractors}

        for line in line_stream:
            if not line.strip():
                continue

            for key, extractor in self.extractors.items():
                counts[f"total_{key}"] += len(extractor(line))

        return counts
