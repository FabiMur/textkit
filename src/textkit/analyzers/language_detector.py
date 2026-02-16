from collections import Counter


class LanguageDetector:
    def __init__(self) -> None:
        self.suffix_counts: Counter = Counter()
        self.profiles = {
            "es": {"cio", "est", "ado", "ito", "ona"},
            "en": {"ing", "ion", "ght", "ish", "thm"},
            "fr": {"ons", "ais", "eau", "eur", "tte"},
        }

    def analyze(self, token_list: list[str]) -> None:
        """Analiza las últimas 3 letras de cada palabra."""
        for word in token_list:
            word_lower = word.lower()
            if len(word_lower) >= 3:
                suffix = word_lower[-3:]
                self.suffix_counts.update([suffix])

    def get_report(self) -> dict:
        """Genera el reporte comparando sufijos con los perfiles."""
        detailed_scoring = {}
        totals = {}

        for lang, profile in self.profiles.items():
            matches = {
                suf: self.suffix_counts[suf] for suf in profile if self.suffix_counts[suf] > 0
            }
            detailed_scoring[lang] = matches
            totals[lang] = sum(matches.values())

        winner = self._identify_winner(totals)

        return {"detected_language": winner, "language_scores": detailed_scoring}

    def _identify_winner(self, totals: dict[str, int]) -> str:
        if not totals or sum(totals.values()) == 0:
            return "unknown"
        return max(totals, key=totals.get)  # type: ignore
