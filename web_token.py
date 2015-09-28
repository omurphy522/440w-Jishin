#!/usr/bin/python

import jwt
key = 'secret'
payload = {'username':'usrnme','authentication':'auth'}
token = jwt.encode(payload, key, 'HS256')

print token




