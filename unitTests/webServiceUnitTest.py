#__author__ = 'Osei'

import unitTests
import sys
sys.path.append('..')


import web_service

soap_service = web_service.SoapService()

class web_service_tests(unitTests.TestCase):

    def test_performOp(self):

        service = soap_service
        num_one = 4
        num_two = 3
        num_three = 2
        expected_result = "18"

        response = web_service.SoapService.performop(service, num_one, num_two, num_three)
        self.assertEqual(response, expected_result)




if __name__=='__main__':
    unitTests.main()
