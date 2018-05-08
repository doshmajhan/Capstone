# Extensive Vulnerability Framework

### Table of Contents
[Requirements](#requirements)<br>
[Layout](#layout)<br>
[Front End](#front-end)<br>
[API](#api)<br>
[Docker](#docker)<br>
[Ansible](#ansible)<br>
[Terraform](#terraform)<br>
[Install](#install)<br>
[Test](#test)<br>
[Run](#run)<br>



### Requirements
* Terraform
* Docker (docker-ce)
* Ansible
* Python2.7
* MongoDB


### Layout
Front end has our user interface, they select a OS first, we then return a list of valid vulnerabilities we have stored in MongoDB for that OS. After they choose a vulnerability, they submit the configuration. The selected options get sent to our API which will call terraform to create the machine. 

### Front End
Our frontend is served by the API itself however it would be quite simple to decouple it from the api as all data is collected using AJAX requests (Asyncronous Javascript and XML).  The HTML files are found in the framework/app/templates/ directory while all the static content is found in the framework/app/static directory.  We are serving the html as a jinja template which can be explored in the framework/app/ui.py file.  Flask automatically searches for the templates and static folders so there is no need to change this structure or explicitly tell the render_template function where the files live.  All of the AJAX requests are found in the static/js/framework.js file.  The other two files in this directory are for the html/css and do not need to be changed unless you want to tinker with the views that they create.  Going forward we would recommend using a more robust frontend framework such as Vuejs, React, or Angular however this is not the most pressing issue to resolve.  


### API
write stuff here


### Docker
All of our machines are built from docker images. Each image is a based install of the OS, andis stored in [https://hub.docker.com/u/thedosh](https://). In the main folder of our repo you can find our `Dockerfile` which shows how the image is created. The base image of the OS, like Ubuntu 14 for example, is pulled down. We then install and SSH server, make sure it is running, changing the authentication to allow root login with password, and then change the root password to `changme` so that Ansible can log in and provision it.

### Terraform
In `framework/app/terraform/template.tf` is the specifics of how terraform is configured. We use Docker containers to create our machines. Under the provisioner section you can see the ansible command that we run. The essential portion of it is the `tags` variable. When the user selects a vulnerability from our user interface, that associated tag for that vulnerability is retrieved from MongoDB. That tag is then passed to the Ansible command we run in the terraform provisioning, so we only run roles that are matched with that tag. That tag represents a role within ansible that installs that vulnerability.


### Ansible
The `hosts` file contains our configs for logging into our docker container, the ssh port is mapped to `2222` and the credentials are `root:changeme`. Currently it needs to use the IP address of the host machine, so change that under to your IP address under the `[docker]` host.

Each vulnerability is a role within our ansible directory. It goes through all the steps needed to configure a vulnerability for that system. It is then added to the main `playbook.yml` and tagged accordingly so it can be ran indiviually. 

### Install
After installing the core applications, we need to install the python requirements and initialize terraform

```
cd ~/Capstone
pip install -r requirements.txt
cd framework/app/terraform
terraform init
```

### Test
`~/Capstone/framework/app/terraform_test.py` contains a simple way to test the install works.
`python terraform_test.py -c` to test creation
`python terraform_test.py -d` to test deletion 


### Run
After installing all the requirements, ensure that MongoDB is started, make sure terraform has been initiated. Then run `python framework/app/run.py` to start the application, the user interface is located at [http://localhost:5000](http://).
