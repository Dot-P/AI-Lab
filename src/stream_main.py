import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(description="Streaming discovery placeholder")
    parser.add_argument("--input", type=str, default=None, help="Stream input source")
    return parser.parse_args()


def main(args=None):
    args = get_args() if args is None else args
    logging.basicConfig(level=logging.INFO)
    logging.info("Running streaming pipeline on: %s", args.input)
    # TODO: Implement streaming discovery
    pass


if __name__ == "__main__":
    main()
