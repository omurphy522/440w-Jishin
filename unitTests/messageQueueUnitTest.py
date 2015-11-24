# Filename: messageQueueUnitTest.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

from messageQueuing import ceRabbitMqPushMessageFinal
from messageQueuing import clientRabbitMqPickupMessageFinal
import unittest

testQueue = ceRabbitMqPushMessageFinal.messageQueue()
testReceive = clientRabbitMqPickupMessageFinal.messageReceive()
username = "username"
results = 'It Works'
nonexistQueue = 'bob'

class messageQueue_tests(unittest.TestCase):

    def test_message_send_receive_ok(self):
        send = results
        received = results
        sendResponse = testQueue.sendMessage(username, results)
        receiveResponse = testReceive.getMessage(username)
        self.assertEqual(sendResponse, send)
        count = len(receiveResponse)
        self.assertEqual(count, 1)

    def test_message_send_receive_fail(self):
        self.assertRaises(Exception, testReceive.getMessage(username))

    def test_no_queue(self):
        self.assertRaises(Exception, testReceive.getMessage(nonexistQueue))


if __name__=='__main__':
    unittest.main()