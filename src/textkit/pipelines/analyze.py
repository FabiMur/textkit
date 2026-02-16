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
from src.textkit.transformers import clean_text, normalize_text, tokenize_words


def analyze_pipeline(args: argparse.Namespace) -> None:
    """Orquesta el análisis y genera un reporte en formato JSON."""
    reader = Reader(args.input)

    stats = StatisticsAnalyzer()
    seq = SequenceAnalyzer()
    lang = LanguageDetector()
    ext = ExtractAnalyzer()

    n_size = args.ngram_size

    for line in reader.read():
        ext.analyze(line)

        processed = normalize_text(clean_text(line))
        tokens = tokenize_words(processed)

        if tokens:
            stats.analyze(tokens)
            seq.analyze(tokens, n=n_size)
            lang.analyze(tokens)

    report_data = {
        "metadata": {"source": args.input, "ngram_size": n_size},
        "results": {
            "statistics": stats.get_report(),
            "language_detection": lang.get_report(),
            "sequences": seq.get_report(n=n_size),
            "entity_counts": ext.get_report(),
        },
    }

    _write_json_report(args.output, report_data)


def _write_json_report(output_file: str, data: dict) -> None:
    """Escribe el diccionario de datos en un archivo con formato JSON."""
    output_path = Path(output_file)

    with output_path.open("w", encoding="utf-8") as writer:
        json.dump(data, writer, indent=4, ensure_ascii=False)
