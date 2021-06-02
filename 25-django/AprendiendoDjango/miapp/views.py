from django.shortcuts import render, HttpResponse , redirect

# Create your views here.
#MVC = Modelo Vista Controlador -> (metodos)
#MVT = Modelo Template Vista -> (metoros) En djando el template es la vista y la vista el cotrolador

layout = """

<h1>Sitio web Django | William Paredes</h1>

<hr/>

<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
        <a href="/pagina-pruebas">Pagina de Pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>

</ul>
<hr/>
"""

def index(request):

    html = """
            
            <ul>
            """
    year = 2021

    while year <= 2050:

        if year % 2 == 0:                    
            html += f"<li>{str(year)}</li>"
        
        year += 1

    html += "</u>"


    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+
        """
        <h1>Hola mundo con Django!!!</h1>
        <h3>Soy William Paredes</h3>
        """
    )

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', nombre = "William", apellidos = "Paredes")

    return HttpResponse(layout+
        """
        <h1>Pagina de mi web</h1>
        <p>Creado por William Paredes</p>
        """
    )

def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)
    

