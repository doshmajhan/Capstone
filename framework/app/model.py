from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField

from .exceptions import InvalidConfiguration

class VulnerableRole(Document):
    """
    Describes a vulnerable role.

    title: The pretty display name of the role.
    name: The name of the ansible role.
    description: The role's description.
    operating_systems: The supported operating systems for the role.
    protected_ports: A list of ports used by the role.
    protected_files: A list of files protected by the role.
    """
    meta = {
        'collection': 'vulns',
        'indexes': [
            {
                'fields': ['name'],
                'unique': True
            }
        ]
    }

    title = StringField(required=True, unique=True, null=False)
    name = StringField(required=True, unique=True, null=False)
    description = StringField()
    operating_systems = ListField(StringField(required=True, null=False), required=True, null=False)
    protected_ports = ListField(IntField(required=True, null=False), required=False, null=False)
    protected_files = ListField(StringField(required=True, null=False), required=False, null=False)

    @property
    def document(self):
        return {
            'title': self.title,
            'name': self.name,
            'description': self.description,
            'operating_systems': self.operating_systems,
            'protected_ports': self.protected_ports,
            'protected_files': self.protected_files
        }

    @staticmethod
    def compatible(role, config):
        """
        Determine if this role is compatible with the current config.
        """
        if any(pport in config['protected_ports'] for pport in role.protected_ports):
            raise InvalidConfiguration('Selected roles are using conflicting ports.')
        if any(pport in config['protected_ports'] for pport in role.protected_ports):
            raise InvalidConfiguration('Selected roles are using conflicting files.')

        if config['selected_os'] not in role.operating_systems:
            raise InvalidConfiguration(
                'Role ({}) is not compatible with the selected os.'.format(role.name))


class RunningMachines(Document):
    """
    Describes a current running vulnerable machine.

    name: The name of the machine
    tags: the tags sent to ansible, aka the roles selected
    operating_systems: Running OS on the machine.
    ip_address: IP of machine
    ports: Listening ports on the machine
    status: the current status of machine (Creating/UP)
    """
    meta = {
        'collection': 'running_machines',
        'indexes': [
            {
                'fields': ['name'],
                'unique': True
            }
        ]
    }

    name = StringField(required=True, unique=True, null=False)
    tags = StringField(required=True, null=False)
    operating_system = StringField(required=True, null=False)
    ip_address = StringField(required=False, null=False)
    ports = ListField(IntField(required=True, null=False), required=False, null=False)
    status = StringField(required=True, null=False)

    @property
    def document(self):
        return {
            'name': self.name,
            'tags': self.tags,
            'operating_system': self.operating_system,
            'ip_address': self.ip_address,
            'ports': self.ports,
            'status': self.status
        }