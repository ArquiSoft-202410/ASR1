import pika
import json
from sys import path
from os import environ
import django

path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()

def callback(ch, method, properties, body):
    print("Received %r" % json.loads(body))

# Configuración de RabbitMQ
rabbit_host = '10.128.0.2'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'ASR1_OTPs'
topic = 'OTPs'

# Conecta a RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbit_host,
        credentials=pika.PlainCredentials(rabbit_user, rabbit_password)
    )
)
channel = connection.channel()

# Asegura que el exchange exista
channel.exchange_declare(exchange=exchange, exchange_type='topic')

# Declara una cola específica para este suscriptor
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# Vincula la cola al exchange con el routing key adecuado
channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=topic)

# Empieza a consumir mensajes de la cola
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
