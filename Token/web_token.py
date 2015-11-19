#!/usr/bin/python

import jwt
from ConstantValues.Constants import constantsclass

class tokenHandler:

    def create_token(self, username):

        if str(constantsclass.AUTHENTICATED)in username:

            key = 'secret'
            payload = {'username': username, 'authentication': 'auth'}
            token = jwt.encode(payload, key, 'HS256')
            return token

        else:
            return False


