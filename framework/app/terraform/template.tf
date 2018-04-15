# Configure the Docker provider
variable "container_name" {}

variable "image_name" {}
variable "tags" {}
variable "ansible_dir" {}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "vuln_image" {
  name = "${var.image_name}"
}

# Create a container
resource "docker_container" "vulnerable" {
  image = "${docker_image.vuln_image.latest}"
  name  = "${var.container_name}"

  ports {
    internal = 22
    external = 2222
  }

  provisioner "local-exec" {
    command = "sleep 10; cd ${var.ansible_dir}; ansible-playbook playbook.yml -i hosts --tags ${var.tags}"
  }
}
