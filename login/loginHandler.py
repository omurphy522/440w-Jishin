# import kerbtest
#
# kerb = kerbtest.kerberos()
# usrnam = raw_input("Please Enter Username: ")
#
# token = kerb.has_kerberos_ticket(usrnam)
#
# print token

from Token import web_token
from kerberos import kerberos_authentication
# test purposes only
from ConstantValues.Constants import constantsclass

def loginMethod(self, username):

    # Create instances of tokenHandler and kerberosHandler to access class methods
    tokenHandler = web_token.tokenHandler()
    kerberosHandler = kerberos_authentication.kerberosHandler()

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



