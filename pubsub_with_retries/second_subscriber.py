#!/usr/bin/env python
import pika


EXCHANGE_NAME = 'messages'
QUEUE_NAME = 'secondsub.messages'


def open_rabbitmq_connection_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='pwr-rabbitmq'))
    return connection.channel()


def build_rabbitmq_topology(channel):
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')
    queue_declaration = channel.queue_declare(queue=QUEUE_NAME, exclusive=True)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_declaration.method.queue)


def start_subscriber(channel):

    def callback(ch, method, properties, body):
        print("2 subscriber: [x] %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    channel.start_consuming()


channel = open_rabbitmq_connection_channel()
build_rabbitmq_topology(channel)
start_subscriber(channel)
print(' [*] Waiting for logs. To exit press CTRL+C')
