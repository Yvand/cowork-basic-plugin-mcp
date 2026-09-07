"""Echo text supplied on the command line."""

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Echo text back to the caller.")
    parser.add_argument("text", help="Text to echo")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(args.text)


if __name__ == "__main__":
    main()