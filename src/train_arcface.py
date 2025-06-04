import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(description="ArcFace training placeholder")
    parser.add_argument("--dataset", type=str, default=None, help="Training dataset")
    return parser.parse_args()


def main(args=None):
    args = get_args() if args is None else args
    logging.basicConfig(level=logging.INFO)
    logging.info("Training ArcFace model on dataset: %s", args.dataset)
    # TODO: Implement ArcFace training
    pass


if __name__ == "__main__":
    main()
