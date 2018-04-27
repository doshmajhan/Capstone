
import json

try:
    from testutils import BaseTest, create_test_role
    from testutils import api_verify
except Exception:
    import sys
    from os.path import dirname, abspath
    sys.path.append(abspath(dirname(dirname(dirname(abspath(__file__))))))
    from tests.testutils import BaseTest, create_test_role
    from tests.testutils import api_verify

class BasicFunctionalityTest(BaseTest):
    def test_verify_os(self):
        data = api_verify(self.client, {'selected_os': 'Ubuntu 16.04'})
        self.assertEqual(data['error'], False)

    def test_verify_roles(self):
        create_test_role(
            'VSFTPD 2.3.4',
            'vuln-ftp',
            description="Backdoored version of vsftpd 2.3.4 that spawned a reverse shell when\
            ':)' was included in the username.",
            operating_systems=['Ubuntu 16.04'],
            protected_files=['/etc/vsftpd'],
            protected_ports=[20,21],
        )
        data = api_verify(
            self.client,
            {
                'selected_os': 'Ubuntu 16.04',
            })
        self.assertEqual(data['error'], False)
        self.assertIn('VSFTPD 2.3.4', data['additional_roles'])

