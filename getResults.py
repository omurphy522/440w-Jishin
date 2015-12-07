__author__ = 'Owen'

import sys

sys.path.append('..')
from soaplib.client import make_service_client
from jishinServer import jishinService
import getpass
from ConstantValues.Constants import constantsclass

username = raw_input('Enter your Username: ')
password = getpass.getpass()
messages = 'no messages'
jishin = make_service_client('http://localhost:8080/loginUser', jishinService())

token = jishin.loginUser(username, password)


if token == constantsclass.INCORRECT_PASSWORD:
    token = jishin.loginUser(username, password)

else:
    while messages:
        messages = jishin.receivePrediction(token)
        if messages:
            for m in messages:
            	print m
        else:
            print 'No Messages In Queue'
  
