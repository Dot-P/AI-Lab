import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(description="MAE pretraining placeholder")
    parser.add_argument("--config", type=str, default=None, help="Path to config file")
    return parser.parse_args()


def main(args=None):
    args = get_args() if args is None else args
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting MAE pretraining with config: %s", args.config)
    # TODO: Implement MAE pretraining
    pass


if __name__ == "__main__":
    main()
