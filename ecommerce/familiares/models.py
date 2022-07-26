from django.db import models


class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    hobbie=models.CharField(max_length=500,null=True,blank=True)
    edad=models.IntegerField()
    is_active= models.BooleanField(default=True)
    ultimo_mensaje_enviado= models.DateField(auto_now_add=True, null=True, blank=True)
