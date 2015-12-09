#!/usr/bin/python
try:

    import subprocess
    import os
    import sys
    from jishinLogger import LoggingFinal as jishinLogging

    sys.path.append('..')
    from ConstantValues.Constants import constantsclass


    class kerberosHandler:

        def has_kerberos_ticket(self, username, password):

            subprocess.call(['kdestroy'])       
            user = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
	    userpass = subprocess.Popen(['kinit', username], stdin=user.stdout, stderr=subprocess.STDOUT)
	    storepass, err = userpass.communicate()
            list_tick = subprocess.Popen(('klist | grep ' + username), stdout=subprocess.PIPE, shell=True)
	    out, err = list_tick.communicate()
            if out != '':
		jishinLogging.logger.info('%s Logged In' %username)
                return True
            else:
                subprocess.call(['kdestroy'])
		jishinLogging.logger.warning('Authentication Failed')
                return False


except ImportError as e:
    jishinLogging.logger.error("Broken Import Statement Kerberos %s" % e)

except IOError as (e):
    jishinLogging.logger.error("IOError Kerberos: %s" % e)
