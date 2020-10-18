#!/usr/bin/env python
import time
import pika

time.sleep(10)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='wq-rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='messages')

a_beautiful_message = json.dumps({
    'title': 'A beautiful message',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
})
channel.basic_publish(
    exchange='',
    routing_key='messages',
    body=a_beautiful_message
)

print(" [x] Sent %r" % a_beautiful_message)
connection.close()
