from collections.abc import Iterable
from typing import Any, Protocol


class Analyzer(Protocol):
    def analyze(self, data: Iterable[Any]) -> dict[str, Any]:
        """Recibe un iterable de datos y devuelve métricas de análisis."""
        ...
