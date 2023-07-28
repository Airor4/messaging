import pika
import time


# have to wait for the rabbit mq service to come up and the consumer to start listening
time.sleep(30)
connection = pika.BlockingConnection(pika.ConnectionParameters("my-rabbit"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
