from mongoengine import connect

try:
    from app.model import VulnerableRole
except Exception:
    # Configure path to start at app module
    import sys
    from os.path import abspath, dirname
    sys.path.append(abspath(dirname(dirname(abspath(__file__)))))
    from app.model import VulnerableRole

SAMPLE_ROLES = [
    {
        'title': 'SSH Vuln CVE-2123123213',
        'name': 'vuln-ssh',
        'description': 'A vulnerable ssh configuration.',
        'operating_systems': ['Ubuntu 16.04', 'CentOS 7.3', 'Fedora 25'],
        'protected_ports': [22],
        'protected_files': ['/etc/ssh'],
    },
    {
        'title': 'VSFTPD 2.3.4 (Backdoor)',
        'name': 'vuln-ftp',
        'description': 'Backdoored version of vsftpd 2.3.4 that spawned a reverse shell when ":)" was included in the username.',
        'operating_systems': ['Ubuntu 16.04'],
        'protected_ports': [20, 21],
        'protected_files': ['/etc/ssh'],
    },
    {
        'title': 'MS08-067 (Net API)',
        'name': 'vuln-ms08-067',
        'operating_systems': ['Windows XP'],
    },
    {
        'title': 'MS17-10 (Eternal Blue)',
        'name': 'vuln-ms17-10',
        'operating_systems': ['Windows XP', 'Windows Server 2012'],
    },
    {
        'title': 'Redis RCE',
        'name': 'vuln-redis',
        'description': 'Gain remote code execution by overriding ssh authorized keys using redis.',
        'operating_systems': ['Ubuntu 16.04', 'CentOS 7.3', 'Fedora 25'],
    },
    {
        'title': 'Wordpress XSS',
        'name': 'vuln-wordpress',
        'description': 'Exploit XSS due to vulnerable wordpress plugin being left enabled.',
        'operating_systems': ['CentOS 7.3'],
    },
]

def add_role(role):
    """
    Create a test role in the database.
    """
    role = VulnerableRole(
        title=role['title'],
        name=role['name'],
        description=role.get('description'),
        operating_systems=role.get('operating_systems', []),
        protected_ports=role.get('protected_ports', []),
        protected_files=role.get('protected_files', []),
    )
    role.save(force_insert=True)
    return role

def main():
    connect('evf_db', host='localhost', port=27017)

    VulnerableRole.drop_collection()
    for role in SAMPLE_ROLES:
        add_role(role)
        print("Added role {}".format(role['title']))

if __name__ == '__main__':
    main()
