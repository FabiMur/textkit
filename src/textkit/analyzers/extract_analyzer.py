from src.textkit.extractors import extract_date, extract_email, extract_phone, extract_url


class ExtractAnalyzer:
    """Analizador para contar menciones de entidades en texto crudo."""

    def __init__(self) -> None:
        self.counts = {"dates": 0, "emails": 0, "phones": 0, "urls": 0}

    def analyze(self, line: str) -> None:
        """Ejecuta todos los extractores sobre la línea cruda."""
        if not line.strip():
            return

        self.counts["dates"] += len(extract_date(line))
        self.counts["emails"] += len(extract_email(line))
        self.counts["phones"] += len(extract_phone(line))
        self.counts["urls"] += len(extract_url(line))

    def get_report(self) -> dict:
        """Retorna los conteos totales de cada tipo de entidad."""
        return {f"total_{k}": v for k, v in self.counts.items()}
