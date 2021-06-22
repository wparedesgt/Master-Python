from django.http import response
from django.shortcuts import render, HttpResponse , redirect
from miapp.models import Article, Category
from django.db.models import Q


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

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()
    return HttpResponse(f"Articulo Creado: <strong> {articulo.title} </strong> - {articulo.content}")

def save_article(request):
    if request.method == 'GET':

        title = request.GET['title']

        if len(title) <= 5:
            return HttpResponse("<h2>El titulo es muy pequeño!!!</h2>")
            
        content = request.GET['content']
        public = request.GET['public']        

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: <strong> {articulo.title} </strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def create_article(request):

    return render(request, 'create_article.html')


def articulo(request):

    try:
        articulo = Article.objects.get(title="Superman", public = True)
        response = f"Articulo: <br/> {articulo.id}.{articulo.title}"
    except:
        response = "<h1> Articulo no Encontrado </h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    
    articulo.title = "Avengers"
    articulo.content = "Marvel Movies"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo Editado: {articulo.id} - <strong> {articulo.title} </strong> - {articulo.content}")

def articulos(request):
    
    #articulos = Article.objects.order_by('title')
    #articulos = Article.objects.order_by('-title')
    #articulos = Article.objects.order_by('id')[:3]
    #articulos = Article.objects.order_by('id')[3:7]
    #articulos = Article.objects.filter(title="Batman", id=8)
    #articulos = Article.objects.filter(title="Batman")
    #articulos = Article.objects.filter(title__exact='articulo')
    #articulos = Article.objects.filter(title__iexact='articulo')
    #articulos = Article.objects.filter(id__gt = 5) --Mayor que
    #articulos = Article.objects.filter(id__gte = 5) --Mayor o igual que
    #articulos = Article.objects.filter(id__lt = 5) --Menor que
    #articulos = Article.objects.filter(id__lte = 5) --Menor o igual que
    #articulos = Article.objects.filter(id__lte = 5 title__containst = 'articulo') 
    #articulos = Article.objects.filter(title__contains='articulo')
    articulos = Article.objects.all().order_by('-id')
    #articulos = Article.objects.filter(title="Batman").exclude(public = True)
    #articulos = Article.objects.raw("Select * from miapp_article")
    #articulos = Article.objects.filter(
    #    Q(title__contains = "2") | Q(title_contains = "3")
    #)

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')

    

