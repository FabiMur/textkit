from textkit.cli import create_parser
from textkit.pipelines import analyze_pipeline, extract_pipeline, transform_pipeline


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "extract":
        extract_pipeline(args)
    if args.command == "transform":
        transform_pipeline(args)
    if args.command == "analyze":
        analyze_pipeline(args)


if __name__ == "__main__":
    main()
