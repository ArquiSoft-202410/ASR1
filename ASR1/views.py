import json
from django.shortcuts import render
import pika
from .forms import DatosPersonalesForm

def index(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            form_data = {
                'nombre': form.cleaned_data['nombre'],
                'email': form.cleaned_data['email'],
            }
            payload = json.dumps(form_data)
            rabbit_host = '10.128.0.2'
            rabbit_user = 'monitoring_user'
            rabbit_password = 'isis2503'
            exchange = 'ASR1_OTPs'
            topic = 'OTPs'
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange, exchange_type='topic')
            channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
            connection.close()
            return render(request, "ASR1/check.html")
    else:
        form = DatosPersonalesForm()
    return render(request, "ASR1/index.html", {'form': form})