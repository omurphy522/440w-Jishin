#!/usr/bin/python

from bson.json_util import *
import json
import jwt
import sys
sys.path.append('..')
from ConstantValues.Constants import constantsclass
from pymongo import MongoClient
from mikeLogging import LoggingFinal as jishinLogging

class tokenHandler:

    def create_token(self, username, ticket):
        try:
            #Declare client and database being used
            client = MongoClient()
            db = client.eia_data
            collection = db.users
           # databasePayload = collection.find({'username': username}, {'_id': 0, 'claims': 1})
            databasePayload = collection.distinct("claims", {"username": username})
	    print databasePayload
            claim ={'claim': databasePayload}
            print claim
	    
	    # value = json.dumps(claim)
	    # print claim	    
            # print value
            #claimValue = ""
            #for item in databasePayload:
            #    claimValue += item
            #    print claimValue

            #value = dumps(claimValue)
            #print value

	    if ticket:
                secret = 'secret'
                payload = claim
                token = jwt.encode(payload, secret, 'HS256')
                jishinLogging.logger.info('Created Token')
                print dumps( jwt.decode(token, secret, algorithms='HS256'))
                return token

            else:

                jishinLogging.logger.warning('Token Unable To Be Created')
                return False

        except Exception as e:

            jishinLogging.logger.error(e)
            print(e)

