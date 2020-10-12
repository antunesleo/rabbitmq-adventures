#!/usr/bin/env python
import time
import pika

time.sleep(10)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='pra-rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()