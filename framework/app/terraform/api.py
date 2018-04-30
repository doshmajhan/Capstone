from . import TF, WORKING_DIR
from .util import get_ip
from ..exceptions import TerraformError
from ..model import RunningMachines


def create(vars):
    """
    Calls `terraform apply` and passes our vars to to terraform template.
    Once complete the container is provisioned and ready for use.

    :params vars: dictionary of variable values for the terraform template. See __init__.py for example

    :returns: return code of terraform command
    """
    print(vars)
    machine = RunningMachines(
        name=vars['container_name'],
        tags=vars['tags'],
        operating_system=vars['image_name'],
        status="Creating"
    )
    machine.save(force_insert=True)

    return_code, stdout, stderr = TF.apply(refresh=False, var=vars, capture_output=False, skip_plan=True)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))

    machine = RunningMachines.objects.get(name=vars['container_name'])
    machine.status = "UP"
    machine.save()

    print("Done")
    return return_code


def destroy(vars):
    """
    Calls `terraform destroy` and passes vars to terraform template
    pass same vars you passed to create() and it will destroy that container

    :params vars: dictionary of variable values for the terraform template. See __init__.py for example

    :returns: return code of terraform command
    """
    machine = RunningMachines.objects.get(name=vars['container_name'])
    machine.delete()
    return_code, stdout, stderr = TF.destroy(refresh=False, var=vars, force=True, capture_output=False)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))

    return return_code


def get_running_machines():
    """
    Queries terraform API to see our current running machines

    :returns: dictionary of machine info, ip address, container name and OS
    """
    TF.read_state_file()
    resources_dict = TF.tfstate.__dict__['modules'][0]['resources']

    try:
        container_dict = resources_dict['docker_container.vulnerable']['primary']['attributes']
        image_dict = resources_dict['docker_image.vuln_image']['primary']['attributes'] 
    except KeyError:
        return [machine.document for machine in RunningMachines.objects]

    machine = RunningMachines.objects.get(name=container_dict['name'])
    # get list of external ports
    ports = []
    for key in container_dict:
        if "ports" in key and "external" in key:
            ports.append(container_dict[key])

    machine.ports = ports
    machine.ip_address = get_ip()
    machine.save()

    return [machine.document for machine in RunningMachines.objects]