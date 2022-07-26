import imp
from multiprocessing import context
from django.shortcuts import render
from familiares.models import Familiares

def create_familiares (request):
    nuevo_familiar= Familiares.objects.create(nombre='Cintia',apellido='Melendez',hobbie='Salir a correr y pasear el perro',edad=36)
    context={
        'nuevo_familiar':nuevo_familiar
    }
    return render(request,'nuevo_familiar.html',context=context)

def lista_familiares(request):
    familia = Familiares.objects.all()
    context={
        'familia': familia
    }
    return render (request,'lista-familiares.html',context=context)
