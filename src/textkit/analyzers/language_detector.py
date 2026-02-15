from collections.abc import Iterable

from .sequence_analyzer import SequenceAnalyzer


class LanguageDetector:
    def analyze(self, token_stream: Iterable[list[str]]) -> dict:
        """
        Analiza el flujo de tokens para determinar el idioma.

        :param token_stream: Iterable de listas de palabras.
        :return: Resultados de detección y puntuaciones por idioma.
        """
        all_trigrams = set()

        for token_list in token_stream:
            text_line = "".join(token_list).lower()
            line_trigrams = SequenceAnalyzer.generate_sequences(text_line, 3)
            all_trigrams.update(line_trigrams)

        profiles = {
            "es": {"cio", "est", "ado"},
            "en": {"the", "ing", "ion"},
            "fr": {"ons", "ais", "eau"},
        }

        scoring = {
            language: len(all_trigrams.intersection(profile))
            for language, profile in profiles.items()
        }
        winner = self._identify_winner(scoring)

        return {
            "detected_language": winner,
            "language_scores": scoring,
        }

    def _identify_winner(self, scoring: dict[str, int]) -> str:
        """Determina el idioma con mayor puntuación de coincidencia."""
        if not scoring or sum(scoring.values()) == 0:
            return "unknown"
        return max(scoring, key=scoring.__getitem__)
