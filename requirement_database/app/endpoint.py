from flask import Blueprint, request, jsonify
from mongoengine.errors import DoesNotExist
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
