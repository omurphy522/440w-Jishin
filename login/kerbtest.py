#!/usr/bin/python
import Token
import subprocess
import os

#entername = raw_input('Enter User Name: ')

class kerberos():
    def has_kerberos_ticket(self, usrnam):
        if subprocess.call(['klist','-s']) == 0:
            print('you\'re authenticated')
 	    key = 'secret'
	    payload = {'username':usrnam, 'authentication':'auth'}
	    token = Token.encode(payload, key, 'HS256')
	    return token

        else:
            print('There is no recorded ticket, please enter your password: ')
	    authenticate = subprocess.call(['kinit',usrnam])
	    has_kerberos_ticket(usrnam)

#    def create_token(self, usrnam):
#	key = 'secret'
#	payload = {'username':usrnam ,'authentication':'auth'}
#	token = Token.encode(payload, key, 'HS256')
#	return token
#	


#decode = Token.decode(token, 'secret', 'HS256')
#	print decode	
        #if authenticate == 0:
         #   while(False):
          #     authenticate
           #    if authenticate == 0:
            #       return True
             #      has_kerberos_ticket()
              # else:
               #    print('not authenticated')
                #   return False
#has_kerberos_ticket()
#create_token(entername)
