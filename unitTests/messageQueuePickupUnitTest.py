__author__ = 'Owen'

from messageQueuing import clientRabbitMqPickupMessage

import unittest

testQueue = clientRabbitMqPickupMessage.getMessage()


class messageQueuePickup_tests(unittest.TestCase):

    def testSendMessage(self):

        username = "username"


        response = testQueue.getMessage(username)

        self.assertEqual(response)
