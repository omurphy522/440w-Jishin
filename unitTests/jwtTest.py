import unittest
import sys
sys.path.append('..')
from Token import web_token

tokenTest = web_token.tokenHandler()
name = 'noa5159'
clam = ''
class test_token(unittest.TestCase):

    def tokenCase(self):
        username = name
        claim = clam

        testClaim = tokenTest.create_token(username)
        self.assertEqual(username,claim)



