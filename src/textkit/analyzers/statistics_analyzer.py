from collections import Counter


class StatisticsAnalyzer:
    def __init__(self) -> None:
        self.word_counts: Counter = Counter()
        self.total_chars: int = 0
        self.total_tokens: int = 0

    def analyze(self, token_list: list[str]) -> None:
        """
        Procesa una lista de tokens y acumula las métricas.

        :param token_list: Lista de palabras de la línea actual.
        :raises TypeError: Si la entrada no es una lista de strings.
        """

        self.total_tokens += len(token_list)
        self.total_chars += sum(len(str(t)) for t in token_list)
        self.word_counts.update(token_list)

    def get_report(self) -> dict:
        """Calcula y retorna los resultados finales del análisis."""
        if self.total_tokens == 0:
            return {}

        return {
            "total_tokens": self.total_tokens,
            "unique_tokens": len(self.word_counts),
            "lexical_density": self._calculate_lexical_density(),
            "avg_token_length": self._calculate_avg_length(),
            "rare_words": self._get_rare_words(limit=5),
        }

    def _calculate_lexical_density(self) -> float:
        """
        Calcula la densidad léxica. Un valor cercano a 1 indica una gran variedad.
        """
        return round(len(self.word_counts) / self.total_tokens, 2)

    def _calculate_avg_length(self) -> float:
        """
        Calcula la longitud media de los tokens.
        """
        return round(self.total_chars / self.total_tokens, 2)

    def _get_rare_words(self, limit: int) -> list[str]:
        """
        Identifica las palabras que aparecen una sola vez.
        """
        return [word for word, count in self.word_counts.items() if count == 1][:limit]
