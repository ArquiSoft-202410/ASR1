import pika
import json
from sys import path
from os import environ
import django
import vonage
from BancoAlpes import settings
from random import randint

path.append('BancoAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'BancoAlpes.settings')
django.setup()

def callback(ch, method, properties, body):
    value = json.loads(body)
    value['codigo'] = randint(100000, 999999)
    print("Received %r" % value)
    #send_sms(value)

def send_sms(value):
    client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
    sms = vonage.Sms(client)
    message = f"OTP: Hola, {value['nombre']}, para validar tu informacion ingresa el siguiente codigo: {value['codigo']}\n\n"
    recipient_number = "573202805733"
    response_data = sms.send_message({
        "from": "Vonage APIs",
        "to": recipient_number,
        "text": message,
    })
    if response_data["messages"][0]["status"] == "0":
        print("Mensaje enviado exitosamente.")
    else:
        print(f"Error al enviar mensaje: {response_data['messages'][0]['error-text']}")

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
channel.exchange_declare(exchange=exchange, exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=topic)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
