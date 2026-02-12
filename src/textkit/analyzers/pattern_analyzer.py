from collections import Counter

class PatternAnalyzer:
    def analyze(self, tokens: list[str], n: int = 2) -> dict:
        """Analiza patrones y secuencias de palabras."""
        ngrams_list = self.generate_sequences(tokens, n)
        return {
            f"top_{n}_grams": self._get_top_ngrams(ngrams_list, 5),
            "rare_words": self._get_rare_words(tokens)
        }

    @staticmethod
    def generate_sequences(sequence: list | str, n: int) -> list:
        if len(sequence) < n:
            return []
        return [sequence[i : i + n] for i in range(len(sequence) - n + 1)]

    def _get_top_ngrams(self, ngrams: list[tuple], limit: int) -> list[tuple]:
        return Counter(ngrams).most_common(limit)

    def _get_rare_words(self, tokens: list[str]) -> list[str]:
        counts = Counter(tokens)
        return [word for word, count in counts.items() if count == 1][:5]