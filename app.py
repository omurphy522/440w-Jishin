__author__ = 'Osei'

import sys
sys.path.append('..')
import jwt
from Token import web_token
from kerberos import kerberosAuthentication
from messageQueuing import ceRabbitMqPushMessageFinal
from messageQueuing import clientRabbitMqPickupMessageFinal
from ConstantValues.Constants import constantsclass
from apiData.computation import ComputationClass
from queries import queryBuilder
from Validators import Menu_Validation
from Errors import ValidationErrors




class Engine:

    def login(self, username, password):

        try:
            # Authenticate and authorize user
            tokenhandler = web_token.tokenHandler()
            kerberoshandler = kerberosAuthentication.kerberosHandler()

            ticket = kerberoshandler.has_kerberos_ticket(username, password)
            token = tokenhandler.create_token(username, ticket)

            return token
        except Exception as e:
            print e

    def createPrediction(self, token, region, predictionType, date):

        username = jwt.decode(token, 'secret', algorithms='HS256').get('username')
        claims = jwt.decode(token, 'secret', algorithms='HS256').get('claim')

        if constantsclass.WEB_SERVICE in claims:

            try:

                # validates user input before passing it into query builder
                try:
                    validator = Menu_Validation.Input_Validator()

                    validator.validate_date(date)
                    validator.validate_region(region)
                    validator.validate_prediction_type(predictionType)

                except ValidationErrors.InputError as ve:
                    print ve.msg

                # Retrieve correct collection from db to make computation
                query = queryBuilder.queryBuilder()
                collection = query.retrieveCollection(region, predictionType)

                # computation
                computationHandler = ComputationClass()
                results = computationHandler.computationalCalculations(collection, predictionType, date)

                # rabbitMq
                messageQueue = ceRabbitMqPushMessageFinal.messageQueue()
                messageQueue.sendMessage(username, results)

                return True

            except Exception as e:
                print e
        else:
            return False


    def reccieveResults(self, token):

        username = jwt.decode(token, 'secret', algorithms='HS256').get('username')
        claims = jwt.decode(token, 'secret', algorithms='HS256').get('claim')

        if constantsclass.WEB_SERVICE in claims:

            try:
               messageQueue  = clientRabbitMqPickupMessageFinal.messageReceive()
               results = messageQueue.getMessage(username)
               return results

            except Exception as e:
                print e
        else:
            invalidUser = ['You are not authorized to use this service']
            return invalidUser


