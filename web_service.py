__author__ = 'Osei'
import web
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

urls = ("/hello", "HelloService",
        "/hello.wsdl", "HelloService",
        "/performop", "HelloService")
render = web.template.Template("$def with (var)\n$:var")



class SoapService(SimpleWSGISoapApp):
    """Class for webservice """

    #__tns__ = 'http://test.com'

    @soapmethod(soap_types.String, _returns=soap_types.String)
    def hello(self,message):
        """ Method for webservice"""
        return "You are now logged in "+message

    @soapmethod(soap_types.Integer, soap_types.Integer, soap_types.Integer, _returns=soap_types.String)
    def performop(self, x, y, z):

        # x = bunch[0]
        # y = bunch[1]
        # z = bunch[2]
        # total = 0
        # total = (y*(x + z))
        return str(y*(x + z))






class HelloService(SoapService):
    """Class for web.py """
    def start_response(self,status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)


    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))


    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()