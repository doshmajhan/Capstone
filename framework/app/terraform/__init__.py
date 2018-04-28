"""
Configure terraform script to run desired build
"""
from os.path import dirname, join, abspath

from python_terraform import Terraform

WORKING_DIR = dirname(abspath(__file__))
ANSIBLE_DIR = join(dirname(abspath(dirname(abspath(__file__)))), 'ansible')
print("BUILD DEBUG: Working in: {}".format(WORKING_DIR))
print("BUILD DEBUG: Ansible in: {}".format(ANSIBLE_DIR))

TF = Terraform(working_dir=WORKING_DIR)
EXAMPLE_VARS = {
    "container_name" : "bodaddy",
    "image_name": "thedosh/ubuntu14",
    "tags": "vuln-ftp", # these tags are for what vuln to install, see ansible/playbook.yml for more tags
    "ansible_dir": ANSIBLE_DIR
}

from .api import create, destroy
from .errors import TerraformError
