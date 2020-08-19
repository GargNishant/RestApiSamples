import pika
import mysql_connect
import ast
from datetime import datetime


class Receiver(object):

    def __init__(self, queue='hello') -> None:
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._queue = queue
        self._channel.queue_declare(queue=self._queue)

    def start_consuming(self):
        self._channel.basic_consume(queue=self._queue, on_message_callback=self.callback, auto_ack=True)
        print("[*] Waiting for Messages. To Exit press CTRL+C")
        self._channel.start_consuming()

    def callback(self, ch, method, prop, body):
        print("[x] Received %r" % body)
        mysql = mysql_connect.MySqlConnect(database='profiles')
        print(type(str(body)))
        json = ast.literal_eval(body.decode('utf-8'))
        device_detail = "device_details"
        session = str(datetime.now())
        result = mysql.execute(query=f"INSERT INTO sample_app_sessions (session, createdAt, deviceDetail, user_id) VALUES "
                                         f"('{session}', '{session}', {device_detail}', {int(json['user_id'])});")
        print(result)
        mysql.close_connection()


if __name__ == '__main__':
    receiver = Receiver()
    receiver.start_consuming()
