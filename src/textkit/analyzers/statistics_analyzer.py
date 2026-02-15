from collections import Counter
from collections.abc import Iterable


class StatisticsAnalyzer:
    def analyze(self, token_stream: Iterable[list[str]]) -> dict:
        """
        Orquesta el cálculo de métricas.

        :param token_stream: Flujo de listas de tokens.
        :type token_stream: Iterable[list[str]]
        :return: Diccionario con los resultados del análisis estadístico.
        :rtype: dict[Any, Any]
        :raises TypeError: Si el flujo de entrada no es procesable.
        """
        word_counts = Counter()
        total_chars = 0
        total_tokens = 0

        try:
            for token_list in token_stream:
                total_tokens += len(token_list)
                total_chars += sum(len(str(t)) for t in token_list)
                word_counts.update(token_list)
        except TypeError as e:
            raise TypeError(f"Formato de entrada inválido: {e}") from e

        if total_tokens == 0:
            return {}

        return {
            "total_tokens": total_tokens,
            "unique_tokens": len(word_counts),
            "lexical_density": self._calculate_lexical_density(len(word_counts), total_tokens),
            "avg_token_length": self._calculate_avg_length(total_chars, total_tokens),
            "rare_words": self._rare_words(word_counts),
        }

    def _calculate_lexical_density(self, unique_count: int, total_count: int) -> float:
        """
        Calcula la densidad léxica. Un valor cercano a 1 indica una gran variedad.
        """
        return round(unique_count / total_count, 2)

    def _calculate_avg_length(self, total_chars: int, total_tokens: int) -> float:
        """
        Calcula la longitud media de los tokens.
        """
        return round(total_chars / total_tokens, 2)

    def _rare_words(self, counts: Counter, limit: int = 5) -> list[str]:
        """
        Identifica las palabras que aparecen una sola vez.
        """
        return [word for word, count in counts.items() if count == 1][:limit]
