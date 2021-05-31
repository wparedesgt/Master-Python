from django.shortcuts import render, HttpResponse

# Create your views here.
#MVC = Modelo Vista Controlador -> Acciones (metodos)
#MVT =Modelo Vista Template (En djando se llama template a la vista y el controlador es la vista) -> (metodos)

def hola_mundo(request):
    return HttpResponse("Hola mundo con Django!!!!")
