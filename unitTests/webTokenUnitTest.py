__author__ = 'Osei'

import unitTests
import sys
sys.path.append('..')

from token import webToken

tokenHandler = webToken.tokenHandler()

class token_handler_tests(unitTests.TestCase):

    def test_create_token(self):

        user = "username"

        response = tokenHandler.create_token(user)
        self.assertIsNotNone(response)