# Filename: clientRabbitMqPickupMessageFinal.py
# Author: Owen Murphy
# Edited: 11/18/15
# Course: IST 440w
# Instructor: Professor Oakes

import pika

class messageQueue:

    def sendMessage(self, username, results):
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
                                     body=results,
                                     properties=pika.BasicProperties(content_type='text/plain',
                                                                     delivery_mode=2),
                                     mandatory=True):
                # print('Message publish was confirmed')
                return results
            else:
                # Logger.error
                print('Message could not be confirmed')
        except ValueError as e:
            # LOGGER.error(e.message)
            print('No connection made message not sent')