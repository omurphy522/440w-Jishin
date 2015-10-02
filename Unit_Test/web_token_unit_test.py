__author__ = 'Osei'

import unittest
import sys
sys.path.append('..')

from Token import web_token

tokenHandler = web_token.tokenHandler()

class token_handler_tests(unittest.TestCase):

    def test_create_token(self):

        user = "username"

        response = tokenHandler.create_token(user)
        self.assertIsNotNone(response)