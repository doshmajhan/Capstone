"""
    This module contains any Test Case objects that inherit from unittest.TestCase.
    Additionally, it will contain methods necessary for setup and teardown of those
    test cases.
"""
import sys
import unittest

try:
    from app.model import VulnerableRole
    from app import create_app
except Exception:
    # Configure path to start at app module
    from os.path import abspath, dirname
    sys.path.append(abspath(dirname(dirname(dirname(abspath(__file__))))))
    from app.model import VulnerableRole
    from app import create_app

def create_test_role(
        title,
        name,
        **kwargs):
    """
    Create a test role in the database.
    """
    role = VulnerableRole(
        title=title,
        name=name,
        description=kwargs.get('description'),
        operating_systems=kwargs.get('operating_systems', []),
        protected_ports=kwargs.get('protected_ports', []),
        protected_files=kwargs.get('protected_files', []),
    )
    role.save(force_insert=True)
    return role

def clear_database():
    """
    This function drops all relevant collections in the database.
    """
    VulnerableRole.drop_collection()

def create_test_app():
    """
    This function creates the flask application with test values.
    """
    return create_app(
        TESTING=True,
        MONGODB_SETTINGS=
        {
            'db': 'vulndb_testing',
            'host': 'mongomock://localhost',
            'is_mock': True
        })

class BaseTest(unittest.TestCase):
    """
    This class is meant for unit tests to inherit from.
    It takes care of basics like setup and teardown, as well as a pass test.
    """
    def setUp(self):
        """
        This performs test setup operations.
        """
        self.test_app = create_test_app()
        self.test_app.testing = True
        self.client = self.test_app.test_client()
        clear_database()

    def tearDown(self):
        """
        This clears the database after each test.
        """
        clear_database()

    def test_pass(self):
        """
        This test should always pass.
        """
        pass
