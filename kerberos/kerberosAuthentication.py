#!/usr/bin/python
try:

	import subprocess
	import os
	import sys
	sys.path.append('..')
	import constantValues.constants

	class kerberosHandler:

		def has_kerberos_ticket(self, username):

			#checks to see if tickets are in the KDC
			if subprocess.call(['klist','-s']) == 0:

			#checks to see if specified username is active in klist
				list_tick = subprocess.Popen(('klist | grep ' + username), stdout=subprocess.PIPE, shell = True)

			#stores the ouput of list_tick into variable 'out'
				out, err = list_tick.communicate()

			#this basically says if there's no output from klist, there's no ticket and the user must authenticate

				if out == '':
					subprocess.call(['kinit', username])
				else:

					print('you\'re all good to go')

			#if there are no tickets in the kerberos cache...
			else:
				print('no users currently have tickets')
				username = raw_input('enter username: ')
				subprocess.call(['kinit',username])


			return str(constantValues.constants.constantsclass.AUTHENTICATED)

except ImportError as e:
	print("Broken Impot Statement")
except IOError as (errno,strerror):
	print("IOError")
