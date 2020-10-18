#!/usr/bin/env python
import json, time
import pika

time.sleep(10)


def produce_messages(channel, message_qty, time_interval):
    a_beautiful_message = json.dumps({
        'title': 'A beautiful message',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    })

    for _ in range(0, message_qty):
        time.sleep(time_interval)
        channel.basic_publish(
            exchange='',
            routing_key='messages',
            body=a_beautiful_message
        )

    print(" [x] Sent %r" % a_beautiful_message)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='wq-rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='messages')

produce_messages(channel, message_qty=100, time_interval=0.2)

connection.close()
