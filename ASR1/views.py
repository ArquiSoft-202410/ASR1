from django.shortcuts import render
from .forms import DatosPersonalesForm
from .logic.producer import sendRequest

def index(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            formData = {
                'nombre': form.cleaned_data['nombre'],
                'email': form.cleaned_data['email'],
                'numero': form.cleaned_data['numero']
            }
            sendRequest(formData)
            return render(request, "ASR1/check.html")
    else:
        form = DatosPersonalesForm()
    return render(request, "ASR1/index.html", {'form': form})