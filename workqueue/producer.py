#!/usr/bin/env python
import json, time, uuid
import pika

time.sleep(10)


def produce_messages(channel, message_qty, time_interval):
    for _ in range(0, message_qty):
        a_beautiful_message = json.dumps({
            'id': str(uuid.uuid1()),
            'title': 'A beautiful message',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
        })

        time.sleep(time_interval)
        channel.basic_publish(
            exchange='',
            routing_key='messages',
            body=a_beautiful_message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            ))

        print(" [x] Sent %r" % a_beautiful_message)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='wq-rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='messages', durable=True)

produce_messages(channel, message_qty=100, time_interval=6)

connection.close()
