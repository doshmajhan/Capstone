import argparse
from terraform import api
from terraform import EXAMPLE_VARS
import os

if __name__ == '__main__':
    ansible_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ansible')
    EXAMPLE_VARS['ansible_dir'] = ansible_dir

    parser = argparse.ArgumentParser(description="Test out terraform api")
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-d', action='store_true')    
    args = parser.parse_args()
    
    if args.c:
        print("Creating...")
        api.create(EXAMPLE_VARS)
        print("Created")

    if args.d:
        print("Destroying...")
        api.destroy(EXAMPLE_VARS)
        print("Destroyed")