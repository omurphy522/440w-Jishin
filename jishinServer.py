__author__ = 'Osei'


import sys
sys.path.append('..')
import app as confidenceEngine
import web
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

urls = ("/loginUser", "jishinService",
        "/createPrediction", "jishinService",
        "/receivePrediction", "jishinService")
render = web.template.Template("$def with (var)\n$:var")

class SoapService(SimpleWSGISoapApp):
    """Class for webservice """

    @soapmethod(soap_types.String, _returns=soap_types.String)
    def loginUser(self, username):

        try:

            # Create instance of confidence engine class
            engine = confidenceEngine.Engine()

            # Authenticate and Authorize user
            token = engine.login(username)

            return token

        except Exception as e:
            print e

    @soapmethod(soap_types.String, soap_types.String, soap_types.String, soap_types.String, _returns=soap_types.Boolean)
    def createPrediction(self, token, region, predictionType, date):

        try:

            engine = confidenceEngine.Engine()

            # Calls prediction method based on values passed on
            prediction = engine.createPrediction(token, region, predictionType, date )

            return prediction

        except Exception as e:
            print e

    @soapmethod(soap_types.String, _return=soap_types.Array)
    def receivePrediction(self, token):

        try:

            engine = confidenceEngine.Engine()
            
            # Calls queue to get results
            results = engine.reccieveResults(token)
            return results

        except Exception as e:
            print e


class jishinService(SoapService):
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

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()