__author__ = 'Osei'
__author__ = 'Osei'

from soaplib.client import make_service_client
from web_service import HelloService


client = make_service_client('http://localhost:8080/hello', HelloService())
# client2 = make_service_client('http://localhost:8080/performop', HelloService())

username = raw_input('Enter User Name: ')

# ticket = kerberosmethod(username)

# client = tokenclient
# token = tokenmethod(ticket)





# response = client2.performop(5,6,12)
# 'You are now logged in John'
# print response
