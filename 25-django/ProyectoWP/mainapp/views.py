from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import Register_Form

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Sobre Mi'
    })

def register_page(request):

    register_form = Register_Form()

    if request.method == 'POST':
        register_form = Register_Form(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')

            return redirect('/inicio')




    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })


