__author__ = 'Osei'

import sys

sys.path.append('..')
from soaplib.client import make_service_client
from jishinServer import jishinService
import getpass
from ConstantValues.Constants import constantsclass

username = raw_input('Enter your Username: ')
password = getpass.getpass()
messages = ''
jishin = make_service_client('http://localhost:8080/loginUser', jishinService())

token = jishin.loginUser(username, password)
print token

if token == constantsclass.INCORRECT_PASSWORD:
    token = jishin.loginUser(username, password)

else:
    region = raw_input('Enter the region would you like to predict for: ')
    predictionType = raw_input('Enter the  type of prediction would you like to make: ')
    date = raw_input('Enter the date: ')

    prediction = jishin.createPrediction(token, region, predictionType, date)
    if prediction:
        messages = jishin.receivePrediction(token)

        for m in messages:
            print m
    else:
        print 'Forbidden'
