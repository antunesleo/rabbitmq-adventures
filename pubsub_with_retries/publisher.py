#!/usr/bin/env python
import sys
import time

import pika

time.sleep(30)

EXCHANGE_NAME = 'messages'


def open_rabbitmq_connection_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='pwr-rabbitmq'))
    return connection, connection.channel()


def build_rabbitmq_topology(channel):
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')


def start_publisher(channel):
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=message)
    print(" [x] Sent %r" % message)


connection, channel = open_rabbitmq_connection_channel()
build_rabbitmq_topology(channel)
start_publisher(channel)
connection.close()

time.sleep(15)
