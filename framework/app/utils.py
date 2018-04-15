"""
This module contains utility functions for the application.
"""
from .model import VulnerableRole
from .exceptions import BadRequest, InvalidConfiguration

def get_data(request):
    """
    Retrieve the data from a request.
    """
    data = request.get_json()
    if data is None:
        data = request.form
    if data is None:
        raise BadRequest("Could not get JSON data.")
    return data

def validate_config(data):
    """
    Determine if a configuration is valid.
    """
    config = {
        'selected_os': data['selected_os'],
        'protected_ports': [],
        'protected_files': [],
        'additional_roles': [],
    }

    for role_name in data['selected_roles']:
        role = VulnerableRole.objects.get(name=role_name) # pylint: disable=no-member

        # Verify OS, File, and Port compatibility
        VulnerableRole.compatible(role, config)

        # Update the ports and files in use
        config['protected_ports'] += role.protected_ports
        config['protected_files'] += role.protected_files

    for role in VulnerableRole.objects(name__nin=data['selected_roles']): # pylint: disable=no-member
        try:
            VulnerableRole.compatible(role, config)
            config['additional_roles'].append(role.name)
        except InvalidConfiguration:
            pass

    return config
