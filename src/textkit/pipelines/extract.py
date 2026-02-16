import argparse
import logging
from pathlib import Path

from textkit.extractors import (
    extract_date,
    extract_email,
    extract_phone,
    extract_url,
)
from textkit.reader import Reader

logger = logging.getLogger(__name__)


def extract_pipeline(args: argparse.Namespace):
    logger.info(f"Starting extraction ({args.type}) from: {args.input}")
    text_reader = Reader(args.input)

    with Path(args.output).open("w") as output_file:
        for line in text_reader.read():
            if args.type == "email":
                extracted = extract_email(line)
            elif args.type == "phone":
                extracted = extract_phone(line)
            elif args.type == "date":
                extracted = extract_date(line)
            elif args.type == "url":
                extracted = extract_url(line)
            else:
                raise ValueError(f"Unsupported extraction type: {args.type}")

            for element in extracted:
                output_file.write(element + "\n")

    logger.info(f"Extraction complete. Results saved to: {args.output}")
