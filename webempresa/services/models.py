from django.db import models

# Create your models here.
class Service(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo =models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="services")
    creado = models.DateField(auto_now_add=True)
    actualizado =models.DateField(auto_now=True)

class Meta:
    ordering = ['-created']
