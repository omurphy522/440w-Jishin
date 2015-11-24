#!/usr/bin/python

import jwt
import sys
sys.path.append('..')
from ConstantValues.Constants import constantsclass
from pymongo import MongoClient

class tokenHandler:

    def create_token(self, username):
        try:
            #Declare client and database being used
            client = MongoClient()
            db = client.eia_data
            collection = db.users
            claims = collection.find({'username': username})
        except Exception as e:
            #jishinLogging.logger.error("Mongo error ", e)
            print('mongo problame')

        if str(constantsclass.AUTHENTICATED)in username:
            key = 'secret'
            payload = claims
            token = jwt.encode(payload, key, 'HS256')
            #jishinLogging.logger.info('Created Token')
            print jwt.decode(token, key, algorithms='HS256')
            return token
        else:
            return False
            #jishinLogging.logger.warning('Token Unable To Be Created')


