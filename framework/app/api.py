"""
This module contains API functionality.
"""

from uuid import uuid4
from flask import Blueprint, request, jsonify
from mongoengine.errors import DoesNotExist, NotUniqueError

from .terraform import create, ANSIBLE_DIR
from .config import SUPPORTED_OPERATING_SYSTEMS
from .model import VulnerableRole
from .utils import get_data, validate_config
from .exceptions import handle_exceptions

API = Blueprint('api', __name__)

@API.route('/api/build', methods=['POST'])
@handle_exceptions
def build():
    """
    Attempt to build the specified machine.

    Example Request Data:
    {
        'name': 'machine-name',
        'selected_os': 'Ubuntu 16.04',
        'selected_roles': ['vuln-ssh'],
    }
    """
    data = get_data(request)

    config = validate_config(data)
    # tags need to be passed like "tag1,tag2" to ansible as a string not list
    config['selected_roles'] = ','.join(role for role in config['selected_roles'])
    print('Building system:\nOS:{}\nRoles:{}'.format(config['selected_os'], config['selected_roles']))
    create(
        {
            'container_name': data.get('name', str(uuid4())),
            'image_name': SUPPORTED_OPERATING_SYSTEMS[config['selected_os']],
            'tags': config['selected_roles'],
            'ansible_dir': ANSIBLE_DIR,
        }
    )

    return jsonify({'error': False})

@API.route('/api/verify', methods=['POST'])
# @handle_exceptions
def verify():
    """
    This method will take a given configuration, and assess it's validity.

    If the configuration is valid, it will return a list of roles that would be valid with
    the current configuration.

    Example Request Data:
    {
        'selected_os': 'Ubuntu 16.04',
        'selected_roles': ['vuln-ssh'],
    }
    """
    data = get_data(request)

    return jsonify({
        'error': False,
        'additional_roles': validate_config(data).get('additional_roles'),
    })

@API.route('/api/os_list', methods=['GET', 'POST'])
@handle_exceptions
def os_list():
    """
    Return a list of supported operating systems.
    """
    return jsonify(
        {
            'error': False,
            'operating_systems': SUPPORTED_OPERATING_SYSTEMS.keys()
        }
    )

@API.route('/api/get_role/<role_title>', methods=['GET', 'POST'])
@handle_exceptions
def get_role(role_title):
    """
    Fetch role information from the database based on the given role name.
    """
    role = VulnerableRole.objects.get(title=role_title) # pylint: disable=no-member
    return jsonify({
        'error': False,
        'role': role.document
    })

@API.route('/api/add_role', methods=['POST'])
@handle_exceptions
def add_role():
    """
    This method allows the user to add a role to the database.

    Example Request Data:
    {
        'title': 'SSH Vuln CVE-2123123213',
        'name': 'vuln-ssh',
        'description': 'A vulnerable ssh configuration.',
        'operating_systems': ['Ubuntu 16.04'],
        'protected_ports': [22],
        'protected_files': ['/etc/ssh'],
    }
    """
    data = get_data(request)

    role = VulnerableRole(
        title=data['title'],
        name=data['name'],
        description=data['description'],
        operating_systems=data['operating_systems'],
        protected_ports=data['protected_ports'],
        protected_files=data['protected_files']
    )
    role.save(force_insert=True)

    return jsonify({'error': False})
