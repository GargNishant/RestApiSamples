import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, prop, body):
    print("[x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
print("[*] Waiting for Messages. To Exit press CTRL+C")
channel.start_consuming()