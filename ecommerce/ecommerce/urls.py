from django.contrib import admin
from django.urls import path
from ecommerce.views import bienvenido_a,saber_lista
from familiares.views import create_familiares,lista_familiares

urlpatterns =[
    path('admin/', admin.site.urls),
    path ('bienvenido-a/', bienvenido_a, name='bienvenido-a'),
    path ('saber-lista', saber_lista, name='saber lista'),
    path('create_familiares/', create_familiares,name='create_familiares'),
    path('lista-familiares/', lista_familiares, name='lista-familiares')
]
