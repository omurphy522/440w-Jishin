__author__ = 'Osei'

import unitTest
import sys
sys.path.append('..')

from token import web_token
from ConstantValues.Constants import constantsclass

tokenHandler = web_token.tokenHandler()

class token_handler_tests(unitTest.TestCase):

    def test_create_token(self):

        user = "username"+constantsclass.AUTHENTICATED

        response = tokenHandler.create_token(user)
        self.assertIsNotNone(response)

    def test_create_token_False(self):

        user = "username"

        response = tokenHandler.create_token(user)
        self.assertFalse(response)