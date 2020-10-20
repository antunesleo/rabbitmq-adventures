#!/usr/bin/env python
import json, os, sys, time

import pika


def message_callback(ch, method, properties, body):

    a_beautiful_message = json.loads(body)
    print(" [x] Received %r" % a_beautiful_message)
    time.sleep(5)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    time.sleep(10)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='wq-rabbitmq'))

    channel = connection.channel()
    channel.queue_declare(queue='messages', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='messages', on_message_callback=message_callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
