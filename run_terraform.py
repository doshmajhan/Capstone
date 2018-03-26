"""
Configure terraform script to run desired build
"""

from python_terraform import *

WORKING_DIR = "/home/dosh/Capstone"
VARS = {
    "container_name" : "calicam",
    "image_name": "ubuntu_ssh",
}

def run_terraform(vars):
    kwargs = {"auto-approve": True}
    tf = Terraform(working_dir=WORKING_DIR)
    return_code, stdout, stderr = tf.apply(refresh=False, var=vars, **kwargs)
    
    print return_code
    print stdout
    print stderr
    if return_code == 0:
        print "We passed"
    else:
        print "error happened"

if __name__ == '__main__':
    run_terraform(VARS)