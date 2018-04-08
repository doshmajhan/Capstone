"""
Configure terraform script to run desired build
"""
import os
from python_terraform import Terraform

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
TF = Terraform(working_dir=WORKING_DIR)
AUTO_APPROVE = {"auto-approve": True}
EXAMPLE_VARS = {
    "container_name" : "calicam",
    "image_name": "thedosh/ubuntu14:latest",
    "tags": "vuln-ssh"
}