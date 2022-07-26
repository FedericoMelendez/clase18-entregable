from django.contrib import admin
from django.urls import path
from ecommerce.views import saludo_inicial

urlpatterns =[
    path('admin/', admin.site.urls),
    path ('saludo-inicial/', saludo_inicial, name='saludo-inicial')
]
