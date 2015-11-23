# Filename: ceRabbitMqPushMessageFinal.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import sys
sys.path.append('..')
import pika
from logging_owen import handler_logging as jishinLogging
from pika.exceptions import *


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
                # print body
                channel.basic_ack(method_frame.delivery_tag)
                messageList.append(body)
                jishinLogging.logger.info('Message Received For User:  %s' % queue)
                break
            return messageList


        except ValueError as e:
            # handler_logging.logger.error('No Connection Made')
            print('No Connection Made')
        except Exception as e:
            jishinLogging.logger.error('Error in receive Client')
            print ("Error in Receive Client")
        except AMQPError as e:
            jishinLogging.logger.error(e.message)
        except AMQPConnectionError as e:
            jishinLogging.logger.error(e.message)
        except ProtocolSyntaxError as e:
            jishinLogging.logger.error(e.message)
        except UnsupportedAMQPFieldException as e:
            jishinLogging.logger.error(e.message)
