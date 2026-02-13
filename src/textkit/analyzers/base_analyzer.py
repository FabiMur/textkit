from collections.abc import Iterable
from typing import Protocol, Any, runtime_checkable

@runtime_checkable
class Analyzer(Protocol):
    def analyze(self, data: Iterable[Any]) -> dict[str, Any]:
        """Consume un iterable de datos y devuelve métricas acumuladas."""
        ...