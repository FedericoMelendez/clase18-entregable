from django.contrib import admin
from django.urls import path
from ecommerce.ecommerce.views import bienvenido
from ecommerce.views import bienvenido_a,saber_lista

urlpatterns =[
    path('admin/', admin.site.urls),
    path ('bienvenido-a/', bienvenido_a, name='bienvenido-a'),
    path ('saber-lista', saber_lista, name='saber lista')
]
