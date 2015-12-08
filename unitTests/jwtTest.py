#!/usr/bin/python

import unittest
import sys
import jwt

sys.path.append('..')
from Token import web_token
from pymongo import MongoClient
from ConstantValues.Constants import constantsclass

tokenTest = web_token.tokenHandler()
name = 'noa5159'


class token_create_token(unittest.TestCase):
    def test_token_case(self):
        username = name
        testClaim = tokenTest.create_token(username)
        self.assertIsNotNone(testClaim)

    def test_claim(self):
        username = name
        client = MongoClient()
        db = client.eia_data
        collection = db.users
        claims = collection.find({'username': username})

        for claim in claims:
            if str(constantsclass.AUTHENTICATED) in username:
                testClaim = token_create_token.token_create_token(username)
                self.assertEqual(claim, testClaim)


if __name__ == '__main__':
    unittest.main()
