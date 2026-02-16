from .sequence_analyzer import SequenceAnalyzer


class LanguageDetector:
    def __init__(self) -> None:
        self.all_trigrams: set[str] = set()
        self.profiles = {
            "es": {"cio", "est", "ado"},
            "en": {"the", "ing", "ion"},
            "fr": {"ons", "ais", "eau"},
        }

    def analyze(self, token_list: list[str]) -> None:
        """Extrae trigramas de la línea y los añade al estado global."""
        text_line = "".join(token_list).lower()

        trigrams = SequenceAnalyzer.generate_sequences(text_line, 3)
        self.all_trigrams.update("".join(tg) for tg in trigrams)

    def get_report(self) -> dict:
        """Compara trigramas acumulados con perfiles lingüísticos."""
        scoring = {
            lang: len(self.all_trigrams.intersection(profile))
            for lang, profile in self.profiles.items()
        }

        winner = self._identify_winner(scoring)
        return {"detected_language": winner, "language_scores": scoring}

    def _identify_winner(self, scoring: dict[str, int]) -> str:
        if not scoring or sum(scoring.values()) == 0:
            return "unknown"
        return max(scoring, key=scoring.get)  # type: ignore
