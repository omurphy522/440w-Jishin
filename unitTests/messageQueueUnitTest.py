__author__ = 'Owen'

from messageQueuing import ceRabbitMqPushMessage
from messageQueuing import clientRabbitMqPickupMessage

import unittest

testQueue = ceRabbitMqPushMessage.messageQueue()
testReceive = clientRabbitMqPickupMessage.messageReceive()

class messageQueue_tests(unittest.TestCase):

    def testMessage(self):

        username = "username"
        results = "It Works"
        answer = " [x] Sent %s" % results
        received = " [x] Received %r" % results
        sendResponse = testQueue.sendMessage(username, results)
        receiveResponse = testReceive.getMessage(username)

        self.assertEqual(sendResponse, answer)
        self.assertEqual(receiveResponse, received)

