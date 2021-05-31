from django.shortcuts import render, HttpResponse

# Create your views here.
#MVC = Modelo Vista Controlador -> (metodos)
#MVT = Modelo Template Vista -> (metoros) En djando el template es la vista y la vista el cotrolador

def hola_mundo(request):
    return HttpResponse("Hola mundo con django!!!!")

