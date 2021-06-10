from django.shortcuts import render, HttpResponse , redirect
from miapp.models import Article, Category

# Create your views here.
#MVC = Modelo Vista Controlador -> (metodos)
#MVT = Modelo Template Vista -> (metoros) En djando el template es la vista y la vista el cotrolador

layout = """


"""

def index(request):
    """
    html =
            <h1>Inicio</h1>
            <p>Años hasta el 2050:</p>
            <ul>
            
    year = 2021

    while year <= 2050:

        if year % 2 == 0:                    
            html += f"<li>{str(year)}</li>"
        
        year += 1

    html += "</u>"
    """
    
    year = 2021
    hasta = range(year, 2051)

    nombre = 'William Paredes'
    lenguajes = ['JavaScript', 'Python', 'R', 'PHP']


    return render(request, 'index.html',{
        'title':'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')
    

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', nombre = "William", apellidos = "Paredes")

    return render(request, 'pagina.html',{
        'texto': 'Este es mi texto',
        'lista':['uno','dos','tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request):
    articulo = Article(
        title = 'Primer Articulo',
        content = 'Contenido del Articulo',
        public = True
    )

    articulo.save()
    return HttpResponse("Articulo Creado")


    

