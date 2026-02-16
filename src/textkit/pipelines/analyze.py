import argparse
import json
import logging
from pathlib import Path

from src.textkit.analyzers import (
    ExtractAnalyzer,
    LanguageDetector,
    SequenceAnalyzer,
    StatisticsAnalyzer,
)
from src.textkit.reader import Reader
from src.textkit.transformers import clean_text, normalize_text, remove_stopwords, tokenize_words

logger = logging.getLogger(__name__)


def analyze_pipeline(args: argparse.Namespace) -> None:
    """Pipeline for análisis that generates report in JSON format."""
    logger.info(f"Starting analysis for: {args.input}")

    reader = Reader(args.input)
    n_size = args.ngram_size

    stats_analyzer = StatisticsAnalyzer()
    seq_analyzer = SequenceAnalyzer()
    lang_detector = LanguageDetector()
    ext_analyzer = ExtractAnalyzer()

    for line in reader.read():
        ext_analyzer.analyze(line)

        processed = normalize_text(clean_text(line))
        tokens = tokenize_words(processed)

        cleaned_tokens = remove_stopwords(processed)

        if tokens:
            stats_analyzer.analyze(tokens)
            seq_analyzer.analyze(cleaned_tokens, n=n_size)
            lang_detector.analyze(tokens)

    logger.info("Processing complete. Generating report...")

    report_data = {
        "metadata": {"source": args.input, "ngram_size": n_size},
        "results": {
            "statistics": stats_analyzer.get_report(),
            "language_detection": lang_detector.get_report(),
            "sequences": seq_analyzer.get_report(n=n_size),
            "entity_counts": ext_analyzer.get_report(),
        },
    }

    _write_json_report(args.output, report_data)
    logger.info(f"Report successfully saved to: {args.output}")


def _write_json_report(output_file: str, data: dict) -> None:
    """Writes the data dictionary to a JSON file."""
    output_path = Path(output_file)

    with output_path.open("w", encoding="utf-8") as writer:
        json.dump(data, writer, indent=4, ensure_ascii=False)
