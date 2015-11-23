import unittest
import sys

sys.path.append('..')
from Token import web_token

tokenTest = web_token.tokenHandler()
name = 'noa5159'

class token_create_token(unittest.TestCase):

    def test_token_case(self):
        username = name
        testClaim = tokenTest.create_token(username)
        self.assertIsNotNone(testClaim)

    def test_claim(self):
        username = name
        testClaim = tokenTest.create_token(username)

if __name__ == '__main__':
    unittest.main()
