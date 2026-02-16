from collections import Counter
from collections.abc import Sequence
from typing import Any


class SequenceAnalyzer:
    def __init__(self) -> None:
        self.ngram_counts: Counter = Counter()

    def analyze(self, token_list: list[str], n: int = 2) -> None:
        """
        Genera n-gramas de la línea actual y los acumula.

        :param token_list: Lista de palabras.
        :param n: Tamaño de la secuencia (1-5).
        :raises ValueError: Si n está fuera de rango.
        """
        if not (1 <= n <= 5):
            raise ValueError("El valor de n debe estar entre 1 y 5.")

        sequences = self.generate_sequences(token_list, n)
        self.ngram_counts.update(tuple(seq) for seq in sequences)

    def get_report(self, n: int = 2) -> dict:
        """Retorna los 5 n-gramas más frecuentes."""
        return {f"top_{n}_grams": self.ngram_counts.most_common(5)}

    @staticmethod
    def generate_sequences(sequence: Sequence[Any], n: int) -> list:
        """Lógica de ventana deslizante para generar n-gramas."""
        num_windows = len(sequence) - n + 1
        if num_windows <= 0:
            return []
        return [list(sequence[i : i + n]) for i in range(num_windows)]
