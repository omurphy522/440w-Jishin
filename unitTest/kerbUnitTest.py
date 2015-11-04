__author__ = 'Osei'

from kerberos import kerberosAuthentication
import unittest

class kerberos_tests(unittest.TestCase):

    def login_test(self):
        kerb_mock = kerberosAuthentication
        name="name"

        response = kerb_mock.create_token(name)

        self.assertIsNotNone(response)
