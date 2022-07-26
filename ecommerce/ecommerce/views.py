import re
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render


def bienvenido_a (request):
    return HttpResponse('Bienvenid@ !!!!')

def saber_lista (request):
    return render (request, 'templates-saberlista.html',context={})



