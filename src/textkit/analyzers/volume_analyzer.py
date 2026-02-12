class VolumeAnalyzer:
    def analyze(self, tokens: list[str]) -> dict:
        """Calcula métricas de dimensión y densidad léxica."""
        if not tokens:
            return {}

        return {
            "total_tokens": len(tokens),
            "unique_tokens": len(set(tokens)),
            "lexical_density": self._calculate_density(tokens),
            "avg_token_length": self._calculate_avg_length(tokens)
        }

    def _calculate_avg_length(self, tokens: list[str]) -> float:
        return round(sum(len(t) for t in tokens) / len(tokens), 2)

    def _calculate_density(self, tokens: list[str]) -> float:
        return round(len(set(tokens)) / len(tokens), 2)