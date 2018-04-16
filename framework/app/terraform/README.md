### Terraform wrapper

Import into your code with `from terraform import api`. 

Start the creation process with `api.create(VARS)`

Example vars can be found in terraform/__init__.py.

```
EXAMPLE_VARS = {
    "container_name" : "calicam",  // The name the container will have
    "image_name": "thedosh/ubuntu14:latest", // The image location, our images will be in thedosh/ repo
    "tags": "vuln-ssh" // The tags for the roles to be run on the image, look at ansbile/playbook.yml for reference
}
```

To remove the created image, run `api.destroy(VARS)` with the same vars you created with.

