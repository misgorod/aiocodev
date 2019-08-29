import argparse
import logging

import aiohttp.web
import jsonschema
import yaml

from . import constants


def make_app():
    app = aiohttp.web.Application()
    return app


def get_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.load(f)
    try:
        jsonschema.validate(config, constants.CONFIG_SCHEMA)
    except jsonschema.ValidationError as e:
        print("ERROR: Failed to parse config")
        print(f"Message: {e.message}")
    return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config",
        default="/etc/aiocodev/server.yaml",
        help="location of configuration file",
        dest="config_path"
    )
    args = parser.parse_args()
    config = get_config(args.config_path)
    logging.basicConfig(
        level=config["log_level"],
        format="[%(asctime)s] %(levelname)s %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S.%f"
    )
    app = make_app()
    aiohttp.web.run_app(app)
