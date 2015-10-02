__author__ = 'Osei'

from kerberos import kerberos_authentication
import unittest

class kerberos_tests(unittest.TestCase):

    def login_test(self):
        kerb_mock = kerberos_authentication
        name="name"

        response = kerb_mock.create_token(name)

        self.assertIsNotNone(response)
