from django.contrib import admin
from django.urls import path
from ecommerce.views import saludo_inicial,saber_lista

urlpatterns =[
    path('admin/', admin.site.urls),
    path ('saludo-inicial/', saludo_inicial, name='saludo-inicial'),
    path ('saber-lista', saber_lista, name='saber lista')
]
