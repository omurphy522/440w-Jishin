#!/usr/bin/python
import jwt
import subprocess
import os

entername = raw_input('Enter User Name: ')

def has_kerberos_ticket():
    if subprocess.call(['klist','-s']) == 0:
        print('you\'re authenticated')

    else:
        raw_input('There is no recorded ticket, please enter your password \n')
	authenticate = subprocess.call(['kinit',entername])
	has_kerberos_ticket()

def create_token(usrnam):
	key = 'secret'
	payload = {'username':usrnam ,'authentication':'auth'}
	token = jwt.encode(payload, key, 'HS256') 
	print token
	decode = jwt.decode(token, 'secret', 'HS256')
	print decode	
        #if authenticate == 0:
         #   while(False):
          #     authenticate
           #    if authenticate == 0:
            #       return True
             #      has_kerberos_ticket()
              # else:
               #    print('not authenticated')
                #   return False
has_kerberos_ticket()
create_token(entername)
