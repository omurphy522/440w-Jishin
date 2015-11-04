import sys
import pika
#import logging


class rabbitmq():
    def send_results(self, usrnam, results):
        username = raw_input("ENTER USERNAME: ")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
  
        channel.queue_declare(queue=username, durable=True)

        message = ' '.join(sys.argv[1:]) or "Hello World!"
        channel.basic_publish(exchange='',
                      routing_key=username,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
        return: " [x] Sent %r" % (message,)
        connection.close()
