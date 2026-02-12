"""Tests for the analyzers module."""

from src.textkit.analyzers import (
    VolumeAnalyzer,
    PatternAnalyzer,
    LanguageDetector,
)


class TestVolumeAnalyzer:
    def test_volume_basic(self):
        # "hola mundo hola" -> 3 tokens, 2 únicos
        tokens = ["hola", "mundo", "hola"]
        analyzer = VolumeAnalyzer()
        results = analyzer.analyze(tokens)
        
        assert results["total_tokens"] == 3
        assert results["unique_tokens"] == 2
        assert results["lexical_density"] == 0.67  # 2/3
        assert results["avg_token_length"] == 4.33 # (4+5+4)/3

    def test_volume_empty(self):
        tokens = []
        analyzer = VolumeAnalyzer()
        results = analyzer.analyze(tokens)
        assert results == {}

    def test_volume_long_words(self):
        tokens = ["específicamente", "ia"]
        analyzer = VolumeAnalyzer()
        results = analyzer.analyze(tokens)
        # (15 + 2) / 2 = 8.5
        assert results["avg_token_length"] == 8.5


class TestPatternAnalyzer:
    def test_generate_sequences_static(self):
        # Test del método estático directamente
        sequence = ["a", "b", "c", "d"]
        ngrams = PatternAnalyzer.generate_sequences(sequence, 2)
        assert ngrams == [["a", "b"], ["b", "c"], ["c", "d"]]

    def test_pattern_basic(self):
        tokens = ["el", "pepe", "el", "pepe", "el", "juan"]
        analyzer = PatternAnalyzer()
        # n=2 por defecto (bigramas)
        results = analyzer.analyze(tokens, n=2)
        
        # El bigrama ("el", "pepe") aparece 2 veces
        assert results["top_2_grams"][0][0] == ["el", "pepe"]
        # "juan" es la única palabra que aparece una vez (hapax)
        assert "juan" in results["rare_words"]

    def test_pattern_short_sequence(self):
        # Si pides n=3 a una lista de 2, debe dar lista vacía
        tokens = ["hola", "mundo"]
        analyzer = PatternAnalyzer()
        results = analyzer.analyze(tokens, n=3)
        assert results["top_3_grams"] == []


class TestLanguageDetector:
    def test_detect_spanish(self):
        # Tokens con trigramas españoles: "cio" (enunciación), "ado" (pasado)
        tokens = ["enunciación", "pasado", "estado"]
        detector = LanguageDetector()
        results = detector.analyze(tokens)
        
        assert results["detected_language"] == "es"
        assert results["language_scores"]["es"] >= 1

    def test_detect_english(self):
        # Tokens con trigramas ingleses: "the", "ing"
        tokens = ["the", "king", "playing"]
        detector = LanguageDetector()
        results = detector.analyze(tokens)
        
        assert results["detected_language"] == "en"
        assert results["language_scores"]["en"] >= 2

    def test_detect_unknown(self):
        # Texto que no contiene ningún trigrama de los perfiles
        tokens = ["xyz", "www"]
        detector = LanguageDetector()
        results = detector.analyze(tokens)
        
        assert results["detected_language"] == "unknown"