from typing import Protocol, Any, runtime_checkable

class Analyzer(Protocol):
    """
    Define el contrato para cualquier analizador de TextKit.
    Un analizador debe implementar el método 'analyze'.
    """
    def analyze(self, data: Any) -> dict[str, Any]:
        """Recibe datos (tokens o líneas) y devuelve un diccionario de métricas."""
        ...