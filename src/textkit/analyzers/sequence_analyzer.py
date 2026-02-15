from collections import Counter
from collections.abc import Iterable, Sequence
from typing import Any


class SequenceAnalyzer:
    def analyze(self, token_stream: Iterable[list[str]], n: int = 2) -> dict:
        """
        Calcula los n-gramas más comunes de un flujo de tokens.

        :param token_stream: Iterable de listas de palabras.
        :type token_stream: Iterable[list[str]]
        :param n: Tamaño de la secuencia (1 a 5).
        :type n: int
        :return: Diccionario con los 5 n-gramas más frecuentes.
        :rtype: dict[Any, Any]
        :raises ValueError: Si 'n' está fuera del rango permitido.
        """
        if not (1 <= n <= 5):
            raise ValueError("El valor de n debe estar entre 1 y 5.")

        ngram_counts = Counter()

        for token_list in token_stream:
            ngrams = self.generate_sequences(token_list, n)
            ngram_counts.update(tuple(ngram) for ngram in ngrams)

        return {f"top_{n}_grams": ngram_counts.most_common(5)}

    @staticmethod
    def generate_sequences(sequence: Sequence[Any], n: int) -> list:
        """
        Genera una lista de n-gramas a partir de una secuencia dada.
        """
        num_windows = len(sequence) - n + 1
        if num_windows <= 0:
            return []
        return [sequence[i : i + n] for i in range(num_windows)]
