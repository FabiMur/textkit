from collections.abc import Iterator
from src.textkit.extractors import (
    DateExtractor,
    EmailExtractor,
    PhoneExtractor,
    URLExtractor,
)

class ExtractAnalyzer:
    def __init__(self):
        """Inicializa los extractores para procesamiento línea a línea."""
        self.extractors = {
            "dates": DateExtractor(),
            "emails": EmailExtractor(),
            "phones": PhoneExtractor(),
            "urls": URLExtractor()
        }

    def analyze(self, lines: Iterator[str]) -> dict:
        """Analiza un flujo de líneas y acumula el recuento de entidades."""
        counts = {f"total_{key}": 0 for key in self.extractors}

        for line in lines:
            if not line.strip():
                continue

            for key, extractor in self.extractors.items():
                matches = extractor.extract(line)
                counts[f"total_{key}"] += len(matches)

        return counts