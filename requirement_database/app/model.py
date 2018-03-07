from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField

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
