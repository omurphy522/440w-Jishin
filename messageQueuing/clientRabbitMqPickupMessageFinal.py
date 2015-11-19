# Filename: ceRabbitMqPushMessageFinal.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import pika
from logging_owen import handler_logging


class messageReceive:

    def getMessage(self, username):

        # try catch to log errors
        try:
            connection = pika.BlockingConnection()
            channel = connection.channel()
            queue = username
            messageList = []
            # For method gets all messages from the queue and prints them one at a time
            while True:
                method_frame, header_frame, body = channel.basic_get(queue=queue)
                print body
                channel.basic_ack(method_frame.delivery_tag)
                messageList.append(body)
                # handler_logging.logger.info('message received %s' % body)
                break
            return messageList
        except ValueError as e:
            # handler_logging.logger.error('No Connection Made')
            print('No Connection Made')
        except Exception as e:
            # handler_logging.logger.error('Error in receive Client')
            print ("Error in Receive Client")