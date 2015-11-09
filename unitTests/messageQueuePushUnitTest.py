__author__ = 'Owen'

from messageQueuing import ceRabbitMqPushMessage

import unittest

testQueue = ceRabbitMqPushMessage.messageQueue()

class messageQueue_tests(unittest.TestCase):

    def testSendMessage(self):

        username = "username"
        results = "It Works"
        answer = " [x] Sent %s" % results

        response = testQueue.sendMessage(username, results)

        self.assertEqual(response, answer)
