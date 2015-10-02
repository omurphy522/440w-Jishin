#!/usr/bin/python
import subprocess
import os

import sys
sys.path.append('..')

import ConstantValues.Constants

class kerberosHandler:

    def has_kerberos_ticket(self, username):
        if subprocess.call(['klist', '-s']) == 0:
            print('you\'re authenticated')
            return True

        else:
            raw_input('There is no recorded ticket, please enter your password \n')
            authenticate = subprocess.call(['kinit', username])
            # since kerberos doesnt return anything we can have it return this value
            return str(ConstantValues.Constants.ConstantValues.AUTHENTICATED.value)
    # has_kerberos_ticket()

# def create_token(usrnam):
# 	key = 'secret'
# 	payload = {'username':usrnam ,'authentication':'auth'}
# 	token = Token.encode(payload, key, 'HS256')
# 	print token
# 	decode = Token.decode(token, 'secret', 'HS256')
# 	print decode
#         #if authenticate == 0:
#          #   while(False):
#           #     authenticate
#            #    if authenticate == 0:
#             #       return True
#              #      has_kerberos_ticket()
#               # else:
#                #    print('not authenticated')
#                 #   return False
# has_kerberos_ticket()
# create_token(entername)