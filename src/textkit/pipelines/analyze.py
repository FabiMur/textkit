import argparse
import json
from pathlib import Path

from src.textkit.analyzers import (
    ExtractAnalyzer,
    LanguageDetector,
    SequenceAnalyzer,
    StatisticsAnalyzer,
)
from src.textkit.reader import Reader
from src.textkit.transformers import clean_text, normalize_text, remove_stopwords, tokenize_words


def analyze_pipeline(args: argparse.Namespace) -> None:
    """Orquesta el análisis y genera un reporte en formato JSON."""
    reader = Reader(args.input)

    n_size = args.ngram_size

    for line in reader.read():
        ExtractAnalyzer().analyze(line)

        processed = normalize_text(clean_text(line))

        tokens = tokenize_words(processed)
        cleaned_tokens = tokenize_words(remove_stopwords(processed))

        if tokens:
            StatisticsAnalyzer().analyze(tokens)
            SequenceAnalyzer().analyze(cleaned_tokens, n=n_size)
            LanguageDetector().analyze(tokens)

    report_data = {
        "metadata": {"source": args.input, "ngram_size": n_size},
        "results": {
            "statistics": StatisticsAnalyzer().get_report(),
            "language_detection": LanguageDetector().get_report(),
            "sequences": SequenceAnalyzer().get_report(n=n_size),
            "entity_counts": ExtractAnalyzer().get_report(),
        },
    }

    _write_json_report(args.output, report_data)


def _write_json_report(output_file: str, data: dict) -> None:
    """Escribe el diccionario de datos en un archivo con formato JSON."""
    output_path = Path(output_file)

    with output_path.open("w", encoding="utf-8") as writer:
        json.dump(data, writer, indent=4, ensure_ascii=False)
