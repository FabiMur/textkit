from unittest.mock import patch

import pytest

from textkit.transformers import (
    clean_text,
    normalize_text,
    remove_stopwords,
    tokenize_sentences,
    tokenize_words,
)


# Testing for cleaning
class TestCleaning:
    @pytest.mark.parametrize(
        "text, chars_to_remove, expected",
        [
            ("Hello, World!", None, "Hello World"),
            ("This is a test.", [".", " "], "Thisisatest"),
            ("Remove @#$%^&() characters!", None, "Remove  characters"),
            ("No special chars", None, "No special chars"),
            ("", None, ""),
        ],
        ids=[
            "default_characters",
            "custom_characters",
            "all_special_characters",
            "no_characters_to_remove",
            "empty_string",
        ],
    )
    def test_clean_text(self, text: str, chars_to_remove: list[str], expected: str):
        """
        Ensure if the function clean_text removes specified characters from a given text

        :param self: Instance of the test class
        :param text: Text to be cleaned
        :type text: str
        :param chars_to_remove: Characters that should be removed
        :type chars_to_remove: list[str]
        :param expected: Expected result after cleanining
        :type expected: str
        """
        assert clean_text(text, chars_to_remove) == expected


# Testing for normalization
class TestNormalization:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("  Hello World  ", "hello world"),
            ("      ", ""),
            ("lowercase", "lowercase"),
            ("UPPERCASE LETTERS", "uppercase letters"),
            (" first space only", "first space only"),
        ],
        ids=[
            "strip_spaces_lowercase",
            "only_spaces",
            "already_lowercase",
            "all_uppercase",
            "leading_space_only",
        ],
    )
    def test_normalize_text(self, text: str, expected: str):
        """
        Ensure if the function normalize_text removes spaces at the beginning
        and end and converts to lowercase of the given text

        :param self: Instance of the test class
        :param text: Text to be normalized
        :type text: str
        :param expected: Expected result after normalization
        :type expected: str
        """
        assert normalize_text(text) == expected


# Testing for tokenization
class TestTokenization:
    @pytest.mark.parametrize(
        "text, expected_words",
        [
            ("Hello, World! This is a test.", ["Hello", "World", "This", "is", "a", "test"]),
            ("   ", []),
            ("No punctuation here", ["No", "punctuation", "here"]),
            (
                "Multiple...dots!!! And? Questions?",
                ["Multiple", "dots", "And", "Questions"],
            ),
            ("I'm happy! You're amazing.", ["I", "m", "happy", "You", "re", "amazing"]),
        ],
    )
    def test_tokenize_words(self, text: str, expected_words: list[str]):
        """
        Ensure if tokenize_words function splits input text into words

        :param self: Instance of the test class
        :param text: Input text to tokenize into words
        :type text: str
        :param expected_words: Expected tokenized text
        :type expected_words: list[str]
        """
        assert tokenize_words(text) == expected_words

    @pytest.mark.parametrize(
        "text, expected_sentences",
        [
            ("Hello, World! This is a test.", ["Hello, World!", "This is a test."]),
            ("   ", []),
            ("No punctuation here", ["No punctuation here"]),
            ("Multiple...dots!!! And? Questions?", ["Multiple...dots!!!", "And?", "Questions?"]),
            ("I'm happy! You're amazing.", ["I'm happy!", "You're amazing."]),
        ],
    )
    def test_tokenize_sentences(self, text: str, expected_sentences: list[str]):
        """
        Ensure if tokenize_words function splits input text into sentences

        :param self: Instance of the test class
        :param text: Input text to tokenize into sentences
        :type text: str
        :param expected_words: Expected tokenized text
        :type expected_words: list[str]
        """
        assert tokenize_sentences(text) == expected_sentences


class TestStopwords:
    def test_remove_stopwords_all_languages(self):
        """
        Test if test_remove_stopwords correctly removes stopwords from Spanish, English, and French.
        - Simulate the stopword lists for each language.
        - Patch the `_load_stopwords` function to return our simulated lists.
        """
        sample_text = "hello world bonjour mundo hola"

        fake_es = {"mundo", "hola"}
        fake_en = {"hello", "world"}
        fake_fr = {"bonjour"}

        with patch("textkit.transformers.stopwords._load_stopwords") as mock_load:
            mock_load.side_effect = lambda lang: {"es": fake_es, "en": fake_en, "fr": fake_fr}[lang]

            result = remove_stopwords(sample_text)

        assert result == []

    def test_remove_stopwords_keeps_non_stopwords(self):
        """
        Test if test_remove_stopwords correctly keeps non-stopwords while removing stopwords.
        - Simulamos las listas de stopwords para cada idioma con stopwords y no stopwords
        - Parcheamos la función _load_stopwords para que devuelva nuestras listas simuladas
        """
        sample_text = "hello amazing world bonjour beautiful mundo hola"

        fake_es = {"mundo", "hola"}
        fake_en = {"hello", "world"}
        fake_fr = {"bonjour"}

        with patch("textkit.transformers.stopwords._load_stopwords") as mock_load:
            mock_load.side_effect = lambda lang: {"es": fake_es, "en": fake_en, "fr": fake_fr}[lang]

            result = remove_stopwords(sample_text)

        assert result == ["amazing", "beautiful"]
