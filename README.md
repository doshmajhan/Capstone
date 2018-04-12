# Enterprise
# Capstone
Lets graduate


### Requirements:
* Terraform
* Docker (docker-ce)
* Ansible

### Ansible
The `hosts` file contains our configs for logging into our docker container, the ssh port is mapped to `2222` and the credentials are `root:changeme`. Currently it needs to use the IP address of the host machine, so change that under to your IP address under the `[docker]` host.

### Install
After installing the core applications, we need to install the python requirements and initialize terraform

```
cd ~/Capstone
pip install -r requirements.txt
cd terraform
terraform init
```

### Test
`~/Capstone/test.py` contains a simple way to test the install works.
`python test.py -c` to test creation
`python test.py -d` to test deletion 

