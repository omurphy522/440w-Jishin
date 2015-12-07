# Filename: clientRabbitMqPickupMessageFinal.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import sys
sys.path.append('..')
import pika
from jishinLogger import LoggingFinal as jishinLogging
from pika.exceptions import *


class messageQueue:
    def sendMessage(self, username, results, date, region, predicitonType):
        try:
            # Open a connection to RabbitMQ on localhost using all default parameters
            connection = pika.BlockingConnection()

            # Open the channel
            channel = connection.channel()

            # Declare the queue
            channel.queue_declare(queue=username, durable=True, exclusive=False, auto_delete=False)

            # Turn on delivery confirmations
            channel.confirm_delivery()

            # Send a message
            if channel.basic_publish(exchange='',
                                     routing_key=username,
                                     body='Gas will cost approximately '+results+' on '+date+' in '+region+' if using '+predicitonType+' costs.',
                                     properties=pika.BasicProperties(content_type='text/plain',
                                                                     delivery_mode=2),
                                     mandatory=True):
                jishinLogging.logger.info('Message Sent By %s' % username)

                return results
            else:
                jishinLogging.logger.warning('Message Could Not Be Confirmed')
        except Exception as e:
            jishinLogging.logger.error(e.message)
        except AMQPError as e:
            jishinLogging.logger.error(e.message)
        except AMQPConnectionError as e:
            jishinLogging.logger.error(e.message)
        except ProtocolSyntaxError as e:
            jishinLogging.logger.error(e.message)
        except UnsupportedAMQPFieldException as e:
            jishinLogging.logger.error(e.message)
