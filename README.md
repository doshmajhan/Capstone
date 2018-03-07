# Capstone
Lets graduate

### Docker Image
To build the docker image being used by terraform, in this directory simply run `docker build -t ubuntu_ssh .`

### Ansible
The `inventory.ini` file contains our configs for logging into our docker container, the ssh port is mapped to `2222` and the credentials are `root:changeme`. Currently it needs to use the IP address of the host machine, so change that under to your IP address under the `[docker]` host.

### Terraform
After completing the above steps you should be good to go. Simply run `terraform apply` and it should create and provision your docker container.
