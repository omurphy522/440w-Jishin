# import kerbtest
#
# kerb = kerbtest.kerberos()
# usrnam = raw_input("Please Enter Username: ")
#
# token = kerb.has_kerberos_ticket(usrnam)
#
# print token

from token import tokenWeb
from kerberos import kerberosAuthentication
# test purposes only
from constantValues.constants import constantsclass

def loginMethod(self, username):

    # Create instances of tokenHandler and kerberosHandler to access class methods
    tokenHandler = tokenWeb.tokenHandler()
    kerberosHandler = kerberosAuthentication.kerberosHandler()

    # Get username from user

    # Check if user has a kerberos ticket, returns a value
    # ticket = kerberosHandler.has_kerberos_ticket(username)
    # ticket = ticket.lower()

    # Add ticket to username
    # username = ticket+username

    # Test purposes
    username = username+constantsclass.AUTHENTICATED

    # generate token for user using new username value
    token = tokenHandler.create_token(username)

    print token
    return token



