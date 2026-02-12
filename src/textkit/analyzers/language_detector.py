from .pattern_analyzer import PatternAnalyzer

class LanguageDetector:
    def analyze(self, tokens: list[str]) -> dict:
        """Detecta el idioma comparando el texto con perfiles de trigramas."""
        full_text = "".join(tokens).lower()
        text_trigrams = set(PatternAnalyzer.generate_sequences(full_text, 3))

        profiles = {
            "es": {"cio", "est", "ado"},
            "en": {"the", "ing", "ion"},
            "fr": {"ons", "ais", "eau"}
        }

        scoring = self._get_language_scores(text_trigrams, profiles)
        winner = self._identify_winner(scoring)

        return {
            "detected_language": winner,
            "language_scores": scoring,
        }

    def _get_language_scores(self, text_trigrams: set, profiles: dict) -> dict[str, int]:
        return {lang: len(text_trigrams.intersection(prof)) for lang, prof in profiles.items()}

    def _identify_winner(self, scoring: dict[str, int]) -> str:
        if not scoring or sum(scoring.values()) == 0:
            return "unknown"
        return max(scoring, key=scoring.__getitem__)