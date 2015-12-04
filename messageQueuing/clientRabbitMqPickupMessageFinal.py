# Filename: ceRabbitMqPushMessageFinal.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import sys

sys.path.append('..')
import pika
from mikeLogging import LoggingFinal as jishinLogging
from pika.exceptions import *
from Errors import ValidationErrors, InputErrors


class messageReceive:
    def getMessage(self, username):

        # try catch to log errors
        try:

            connection = pika.BlockingConnection()
            channel = connection.channel()
            queue = username
            # messageList returns a list of all received messages in current queue
            messageList = []

            # For method gets all messages from the queue and prints them one at a time
            while True:

                method_frame, header_frame, body = channel.basic_get(queue=queue)
                # print method_frame, header_frame, body
                if method_frame:
                    channel.basic_ack(method_frame.delivery_tag)
                    messageList.append(body)
                    jishinLogging.logger.info('Message Received For User:  %s' % queue)
                    break
                else:
                    raise ValidationErrors.noTagError(method_frame, InputErrors.InputErrors.NO_TAG_ERROR)
	    print messageList
            return messageList



        except AMQPConnectionError as e:
            jishinLogging.logger.error('AMPQ Connection Error %s' % e.message)
        except ProtocolSyntaxError as e:
            jishinLogging.logger.error('Protocol Syntax Error %s' % e.message)
        except UnsupportedAMQPFieldException as e:
            jishinLogging.logger.error('Unsupported AMPQ Exception %s' % e.message)
