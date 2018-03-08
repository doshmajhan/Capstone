# Configure the Docker provider
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Create a container
resource "docker_container" "foo" {
  image = "ubuntu_ssh"
  name  = "foo"
  ports {
    internal = 22
    external = 2222
  }

  provisioner "local-exec" {
      command = "sleep 10; cd ansible; ansible-playbook playbook.yml -i hosts"
  }
}

