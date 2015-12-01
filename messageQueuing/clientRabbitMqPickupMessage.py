# Filename: clientRabbitMqPickupMessage.py
# Author: Owen Murphy
# Edited: 11/2/15
# Course: IST 440w
# Instructor: Professor Oakes

class messageReceive:
    def getMessage(self, username):
        # try catch to log errors
        try:
            #import statements
            import pika
            import time
            # well be switched to call username from login
            username = raw_input("ENTER USERNAME: ")
            # generates connection to message server
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host='localhost'))
            channel = connection.channel()
            # generate connection to message queue
            channel.queue_declare(queue=username, durable=True)
            print ' [*] Waiting for messages. To exit press CTRL+C'
            # callback method prints results
            def callback(ch, method, body):
                print " [x] Received %r" % (body,)
                time.sleep( body.count('.') )
                print " [x] Done"
                ch.basic_ack(delivery_tag=method.delivery_tag)

            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(callback,
                                  queue=username)

            channel.start_consuming()
        except ValueError as e:
            # LOGGER.error(e.message)
            print('No Connection Made')
        except ImportError as e:
            # LOGGER.error(e.message)
            print('Import Error in clientRabbitMqPickupMessage.py')
        except Exception as e:
            # LOGGER.error(e.message)
            print('Error in message receive client')
