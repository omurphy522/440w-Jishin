# Filename: jishinRetrieveClient.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

import sys

sys.path.append('..')
from soaplib.client import make_service_client
from jishinServer import jishinService
import getpass
from ConstantValues.Constants import constantsclass

username = raw_input('Enter your Username: ')
password = getpass.getpass()

jishin = make_service_client('http://localhost:8080/loginUser', jishinService())
try:
    token = jishin.loginUser(username, password)

    if token == constantsclass.INCORRECT_PASSWORD:
        token = jishin.loginUser(username, password)

    else:
        # Call API Update Script
        update = jishin.updateApi(token)
        if update:
            print 'Update Successful'
        else:
            print 'Update Unsuccessful'
except Exception as e:
    print e
