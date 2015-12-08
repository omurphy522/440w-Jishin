# Filename: messageQueueUnitTest.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import sys

sys.path.append('..')
from messageQueuing import ceRabbitMqPushMessage
from messageQueuing import clientRabbitMqPickupMessage
import unittest
from pika.exceptions import *
from Errors import ValidationErrors
import datetime

testQueue = ceRabbitMqPushMessage.messageQueue()
testReceive = clientRabbitMqPickupMessage.messageReceive()
username = "username"
results = 'It Works'
nonexistQueue = 'bob'
date = str(datetime.datetime.now().date() + datetime.timedelta(days=3))
region = 'US'
predicitonType = 'WEEKLY'


class messageQueue_tests(unittest.TestCase):
    def test_message_send_receive_ok(self):
        send = results
        received = results
        sendResponse = testQueue.sendMessage(username, results, date, region, predicitonType)
        receiveResponse = testReceive.getMessage(username)
        self.assertEqual(sendResponse, send)
        count = len(receiveResponse)
        self.assertEqual(count, 1)

    def test_message_send_receive_fail(self):
        self.assertRaises(ValidationErrors.noTagError, testReceive.getMessage, username)

    def test_no_queue(self):
        self.assertRaises(ChannelClosed, testReceive.getMessage, nonexistQueue)


if __name__ == '__main__':
    unittest.main()
