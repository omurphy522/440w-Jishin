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

            # checks to see if tickets are in the KDC
            if subprocess.call(['klist', '-s']) == 0:

                # checks to see if specified username is active in klist
                list_tick = subprocess.Popen(('klist | grep ' + username), stdout=subprocess.PIPE, shell=True)

                # stores the ouput of list_tick into variable 'out'
                out, err = list_tick.communicate()

                # this basically says if there's no output from klist, there's no ticket and the user must authenticate

                if out == '':
                    user = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
                    userpass = subprocess.Popen(['kinit', username], stdin=user.stdout)
                else:

                    jishinLogging.logger.info(username + ' logged in')

            # if there are no tickets in the kerberos cache...
            else:
                print('no tickets')
                user = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
                userpass = subprocess.Popen(['kinit', username], stdin=user.stdout)

            #	return True
            list_tick = subprocess.Popen(('klist | grep ' + username), stdout=subprocess.PIPE, shell=True)
            out, err = list_tick.communicate()
            if out != '':
                return True
            else:
                return False


except ImportError as e:
    jishinLogging.logger.error("Broken Import Statement Kerberos %s" %e)

except IOError as (errno, strerror):
    jishinLogging.logger.error("IOError Kerberos: %s" %e)

