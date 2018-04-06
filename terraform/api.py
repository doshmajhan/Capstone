from . import TF, WORKING_DIR, AUTO_APPROVE
from errors import TerraformError

def create(vars):
    return_code, stdout, stderr = TF.apply(refresh=False, var=vars, **AUTO_APPROVE)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))

def destroy(vars):
    return_code, stdout, stderr = TF.destroy(refresh=False, var=vars, force=True)
    if return_code != 0:
        raise TerraformError("Code: {} Stderr: {}".format(return_code, stderr))
