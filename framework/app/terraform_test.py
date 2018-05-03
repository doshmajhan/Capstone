import argparse
from terraform import api
from terraform import EXAMPLE_VARS
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test out terraform api")
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-d', action='store_true')
    parser.add_argument('-s', action='store_true')
    args = parser.parse_args()

    if args.c:
        print("Creating...")
        api.create(EXAMPLE_VARS)
        print("Created")

    if args.d:
        print("Destroying...")
        api.destroy(EXAMPLE_VARS)
        print("Destroyed")

    if args.s:
        info = api.get_running_machines()
        print(info)