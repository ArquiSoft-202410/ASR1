from django.shortcuts import render
from .forms import DatosPersonalesForm
from .logic.producer import sendRequest

def index(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            formData = {
                'nombres': form.cleaned_data['nombres'],
                'apellidos': form.cleaned_data['apellidos'],
                'pais': form.cleaned_data['pais'],
                'ciudad': form.cleaned_data['ciudad'],
                'numero': form.cleaned_data['numero'],
                'email': form.cleaned_data['email']
            }
            sendRequest(formData)
            return render(request, "ASR1/check.html")
    else:
        form = DatosPersonalesForm()
    return render(request, "ASR1/index.html", {'form': form})