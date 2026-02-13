import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TextKit: A toolkit for text processing.")

    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("--input", help="Path to the input text file.", type=str)
    analyze_parser.add_argument(
        "--output", help="Path to the output file.", default="output.txt", type=str
    )

    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("--input", help="Path to the input text file.", type=str)
    extract_parser.add_argument(
        "--output", help="Path to the output file.", default="extracted.txt", type=str
    )
    extract_parser.add_argument(
        "--type",
        help="Type of data to extract (email, phone, date).",
        choices=["email", "phone", "date", "url"],
        required=True,
    )

    transform_parser = subparsers.add_parser("transform")
    transform_parser.add_argument("--input", help="Path to the input text file.", type=str)
    transform_parser.add_argument(
        "--output", help="Path to the output file.", default="transformed.txt", type=str
    )
    # TODO: Define transformation operations and their arguments

    return parser
