__author__ = 'Osei'

import sys
sys.path.append('..')
from soaplib.client import make_service_client
from jishinServer import jishinService


username = raw_input('Enter your Username: ')

jishinClient = make_service_client('http://localhost:8080/loginUser', jishinService())

token = jishinClient.loginUser(username)
print token

