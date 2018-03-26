# Configure the Docker provider
variable "container_name" {}

variable "image_name" {}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Create a container
resource "docker_container" "vulnerable" {
  image = "${var.image_name}"
  name  = "${var.container_name}"

  ports {
    internal = 22
    external = 2222
  }

  provisioner "local-exec" {
    command = "sleep 10; cd ansible; ansible-playbook playbook.yml -i hosts"
  }
}
