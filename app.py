# Filename: app.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

import sys

sys.path.append('..')
import subprocess
import jwt
from Token import web_token
from kerberos import kerberosAuthentication
from messageQueuing import ceRabbitMqPushMessage
from messageQueuing import clientRabbitMqPickupMessage
from ConstantValues.Constants import constantsclass
from apiData.computation import ComputationClass
from apiData import apiParsing
from queries import queryBuilder
from Validators import jishinValidator
from Errors import ValidationErrors
from jishinLogger import LoggingFinal as jishinLogging


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
            jishinLogging.logger.error('Error Logging In: %s' % e)

    def createPrediction(self, token, region, predictionType, date):

        username = jwt.decode(token, 'secret', algorithms='HS256').get('username')
        claims = jwt.decode(token, 'secret', algorithms='HS256').get('claim')
        currentDate = jwt.decode(token, 'secret', algorithms='HS256').get('dateIssued')
        region = region.upper()
        predictionType = predictionType.upper()

        if constantsclass.WEB_SERVICE in claims:

            try:
                validator = jishinValidator.Input_Validator()
                # validates user input before passing it into query builder
                try:

                    validator.validate_date(currentDate, date)
                    validator.validate_region(region)
                    validator.validate_prediction_type(predictionType)

                except ValidationErrors.InputError as ve:
                    jishinLogging.logger.error('Validation Error %s' % ve)
                    for e in validator.errors:
                        jishinLogging.logger.error(e)
                    print ve.msg

                # Retrieve correct collection from db to make computation
                query = queryBuilder.queryBuilder()
                collection = query.retrieveCollection(region, predictionType)
                try:
                    # computation
                    computationHandler = ComputationClass()
                    results = str(computationHandler.computationalCalculations(collection, predictionType, date))
                    # rabbitMq
                    messageQueue = ceRabbitMqPushMessage.messageQueue()
                    messageQueue.sendMessage(username, results, date, region, predictionType)

                except Exception as e:
                    jishinLogging.logger.error('Computation %s' % e)

                return True

            except Exception as e:
                jishinLogging.logger.error('Error Creating Prediction %s' % e)
        else:
            return False

    def receiveResults(self, token):

        username = jwt.decode(token, 'secret', algorithms='HS256').get('username')
        claims = jwt.decode(token, 'secret', algorithms='HS256').get('claim')

        if constantsclass.WEB_SERVICE in claims:

            try:
                messageQueue = ''
                messageQueue = clientRabbitMqPickupMessage.messageReceive()
                results = messageQueue.getMessage(username)
                jishinLogging.logger.info('Results Returned To %s' % username)

                return results

            except Exception as e:
                jishinLogging.logger.error('Error Recieving Results: %s' % e)

        else:
            invalidUser = ['You are not authorized to use this service']
            return invalidUser

    def apiUpdate(self, token):

        username = jwt.decode(token, 'secret', algorithms='HS256').get('username')
        claims = jwt.decode(token, 'secret', algorithms='HS256').get('claim')

        if constantsclass.API_UPDATE in claims:

            try:
                updater = apiParsing.APIParse()
                updater.apiCollectionUpdate()

                return True

            except Exception as e:
                jishinLogging.logger.error('Error Running Update: %s by User: %s' % (e, username))

        else:

            return False
