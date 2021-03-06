# Filename: web_token.py
# Author: Owen Murphy
# Course: IST 440w
# Instructor: Professor Oakes


from bson.json_util import *
import jwt
import sys

sys.path.append('..')
from ConstantValues.Constants import constantsclass
from pymongo import MongoClient
from jishinLogger import LoggingFinal as jishinLogging
from datetime import datetime


class tokenHandler:
    def create_token(self, username, ticket):
        try:
            # Declare client and database being used
            client = MongoClient()
            db = client.eia_data
            collection = db.users
            date = str(datetime.now().date())
            databasePayload = collection.distinct("claims", {"username": username})
            claim = {'username': username, 'claim': databasePayload, 'dateIssued': date}

            if ticket:
                secret = 'secret'
                payload = claim
                token = jwt.encode(payload, secret, 'HS256')
                jishinLogging.logger.info('Created Token')
                return token

            else:

                jishinLogging.logger.warning('Token Unable To Be Created')

                return constantsclass.INCORRECT_PASSWORD

        except Exception as e:
            jishinLogging.logger.error(e)
