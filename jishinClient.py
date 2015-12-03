__author__ = 'Osei'

import sys
sys.path.append('..')
from soaplib.client import make_service_client
from jishinServer import jishinService
import getpass


username = raw_input('Enter your Username: ')
password = getpass.getpass()

jishinClient = make_service_client('http://localhost:8080/loginUser', jishinService())

token = jishinClient.loginUser(username, password)
print token

