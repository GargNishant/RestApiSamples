import pika


class Sender(object):
    """
    Class which is used for Sending Messages to RabbitMq
    Default queue='hello', r_key='hello', host='localhost'
    """
    def __init__(self, queue='hello') -> None:
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._queue = queue
        self._channel.queue_declare(queue=self._queue)

    def publish(self, payload, r_key='hello'):
        self._channel.basic_publish(exchange='', routing_key=str(r_key), body=str(payload))
        print("Message Publish")
        self._connection.close()
