import argparse
from pathlib import Path

from textkit.reader import Reader
from textkit.transformers import clean_text, normalize_text, tokenize_sentences, tokenize_words


def transform_pipeline(args: argparse.Namespace):
    reader = Reader(args.input)

    with Path(args.output).open("w", encoding="utf-8") as writer:
        for line in reader.read():
            chosen_transformation = args.transformation

            if chosen_transformation == "clean":
                result = clean_text(line)

            elif chosen_transformation == "normalize":
                result = normalize_text(line)

            elif chosen_transformation == "tokenize_words":
                result = tokenize_words(line)

            elif chosen_transformation == "tokenize_sentences":
                result = tokenize_sentences(line)

            if isinstance(result, list):
                for item in result:
                    writer.write(f"{item}\n")
            else:
                writer.write(f"{result}\n")
