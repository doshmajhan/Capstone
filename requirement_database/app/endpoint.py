from flask import Blueprint, request, jsonify
from mongoengine.errors import DoesNotExist, NotUniqueError
from .model import VulnerableRole
API = Blueprint('endpoint', __name__)

@API.route('/deps/<role_name>')
def get_deps(role_name):
    try:
        role = VulnerableRole.objects().get(name=role_name)
        return jsonify({
            'error': False,
            'role': role.document
        })
    except DoesNotExist:
        return jsonify({
            'error': True,
            'description': 'Role does not exist'
        })

@API.route('/add_role', methods=['POST'])
def add_role():
    data = request.get_json()
    if data is None:
        data = request.form
    try:
        role = VulnerableRole(
            name=data['name'],
            operating_systems=data['operating_systems'],
            protected_ports=data['protected_ports'],
            protected_files=data['protected_files']
        )
        role.save(force_insert=True)
        return jsonify(
            'error': False
        )
    except NotUniqueError:
        return jsonify(
            'error': True,
            'description': 'Role already exists in the database',
        )
    except KeyError:
        return jsonify(
            'error': True,
            'description': 'Missing required parameter'
        )
