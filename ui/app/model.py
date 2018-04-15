from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField

from .exceptions import InvalidConfiguration

class VulnerableRole(Document):

    meta = {
        'collection': 'vulns',
        'indexes': [
            {
                'fields': ['name'],
                'unique': True
            }
        ]
    }

    name = StringField(required=True, unique=True, null=False)
    operating_systems = ListField(StringField(required=True, null=False), required=True, null=False)
    protected_ports = ListField(IntField(required=True, null=False), required=True, null=False)
    protected_files = ListField(StringField(required=True, null=False), required=True, null=False)

    @property
    def document(self):
        return {
            'name': self.name,
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
