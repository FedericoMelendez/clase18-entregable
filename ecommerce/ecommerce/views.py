from django.http import HttpResponse

def saludo_inicial (request):
    return HttpResponse('Bienvenid@ !!!! Para poder saber la lista de los familiares coloque / lista-familiar')