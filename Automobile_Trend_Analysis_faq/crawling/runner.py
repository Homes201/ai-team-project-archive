"""Rebuild the demo database only when explicitly requested."""

import argparse
import os

from data_to_db import car_data_to_db, faq_data_to_db


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replace", action="store_true", help="Replace existing demo tables")
    args = parser.parse_args()
    if not args.replace:
        parser.error("This command replaces tables; pass --replace explicitly")
    required = ("DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME")
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        parser.error("Missing environment variables: " + ", ".join(missing))
    options = {
        "name": os.environ["DB_USER"], "password": os.environ["DB_PASSWORD"],
        "host": os.environ["DB_HOST"], "port": int(os.environ["DB_PORT"]),
        "db_name": os.environ["DB_NAME"],
    }
    car_data_to_db(**options)
    faq_data_to_db(**options)


if __name__ == "__main__":
    main()
