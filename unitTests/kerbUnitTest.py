__author__ = 'Osei'

from kerberos import kerberosAuthentication
import unitTests

class kerberos_tests(unitTests.TestCase):

    def login_test(self):
        kerb_mock = kerberosAuthentication
        name="name"

        response = kerb_mock.has_kerberos_ticket(name)

        self.assertIsNotNone(response)
