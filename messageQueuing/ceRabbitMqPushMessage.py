# Filename: ceRabbitMqPushMessage.py
# Author: Owen Murphy
# Edited: 11/2/15
# Course: IST 440w
# Instructor: Professor Oakes

class messageQueue:
    def __init__(self):
        pass

    def sendMessage(self, username, results):
        try:
            # import statements
            import pika
             #import logging as LOGGER
            # username is from the user that created the prediction
            # username = raw_input("ENTER USERNAME: ")
            # creates a connection
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
            # LOGGER.info('%s opened a connection')(username)
            channel = connection.channel()
            # LOGGER.info('Channel Opened')
            # creates a durable persistent queue
            channel.queue_declare(queue=username, durable=True)
            # LOGGER.info('%s created a durable queue')(username)
            message = results or "Hello World!"
            if message == "Hello World":
                # LOGGER.error('No Results Sent to' %s)(username)
                connection.close;
            else:
                channel.basic_publish(exchange='',
                                      routing_key=username,
                                      body=message,
                                      properties=pika.BasicProperties(
                                          delivery_mode=2,  # make message persistent
                                      ))  # LOGGER.info('Published message %s')(message)
                print " [x] Sent %s" % (message,)
                connection.close()
                # LOGGER.info('Message Sent to %s')(username)
                # LOGGER.info('Connection Closed')

        except ValueError as e:
            # LOGGER.error(e.message)
            print('No Connection Made message not sent')
        except ImportError as e:
            # LOGGER.error(e.message)
            print('Import Error in ceRabbitMqPushMessage.py')
