#!/usr/bin/python

import subprocess
import os

def has_kerberos_ticket():
    if subprocess.call(['klist','-s']) == 0:
        print('you\'re authenticated')
    else:
        entername = raw_input('Enter User Name: ')
	print('There is no recorded ticket, please enter your password \n')
	authenticate = subprocess.call(['kinit',entername])
	has_kerberos_ticket()

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

