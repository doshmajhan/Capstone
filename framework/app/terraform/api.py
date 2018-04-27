from . import TF, WORKING_DIR
from errors import TerraformError

def create(vars):
    """
    Calls `terraform apply` and passes our vars to to terraform template.
    Once complete the container is provisioned and ready for use.

    :params vars: dictionary of variable values for the terraform template. See __init__.py for example

    :returns:
    """
    print("Create")
    print(vars)
    return_code, stdout, stderr = TF.apply(refresh=False, var=vars, capture_output=False, skip_plan=True)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))

    print("Done")
    return return_code

def destroy(vars):
    """
    Calls `terraform destroy` and passes vars to terraform template
    pass same vars you passed to create() and it will destroy that container

    :params vars: dictionary of variable values for the terraform template. See __init__.py for example

    :returns:
    """
    return_code, stdout, stderr = TF.destroy(refresh=False, var=vars, force=True, capture_output=False)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))

    return return_code