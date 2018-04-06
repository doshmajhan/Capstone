from terraform import api
from terraform import EXAMPLE_VARS
import os

if __name__ == '__main__':
    ansible_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ansible')
    EXAMPLE_VARS['ansible_dir'] = ansible_dir
    
    print("Creating...")
    api.create(EXAMPLE_VARS)
    print("Created")

    print("Destroying...")
    api.destroy(EXAMPLE_VARS)
    print("Destroyed")