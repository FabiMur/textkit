import argparse
import logging
from pathlib import Path

from textkit.reader import Reader
from textkit.transformers import clean_text, normalize_text, tokenize_sentences, tokenize_words

logger = logging.getLogger(__name__)
sentence_endings = {".", "!", "?"}


def transform_pipeline(args: argparse.Namespace):
    logger.info(f"Starting transformation ({args.operation}) for: {args.input}")
    reader = Reader(args.input)
    buffer = ""

    with Path(args.output).open("w", encoding="utf-8") as writer:
        for line in reader.read():
            chosen_transformation = args.operation

            if chosen_transformation == "clean":
                result = clean_text(line)

            elif chosen_transformation == "normalize":
                result = normalize_text(line)

            elif chosen_transformation == "tokenize_words":
                result = tokenize_words(line)

            elif chosen_transformation == "tokenize_sentences":
                result = tokenize_sentences(line)

                if buffer:
                    if result:
                        result[0] = buffer + " " + result[0]
                    else:
                        result = [buffer]
                buffer = result[-1] if result and result[-1][-1] not in sentence_endings else ""

            if isinstance(result, list):
                for item in result:
                    writer.write(f"{item}\n")
            else:
                writer.write(f"{result}\n")

    logger.info(f"Transformation complete. Results saved to: {args.output}")
