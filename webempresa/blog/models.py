from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateField(auto_now_add=True)
    actualizado =models.DateField(auto_now=True)

    class Meta:
        ordering = ['-creado']

class Post(models.Model):
    titulo =models.CharField(max_length=200)
    contenido = models.TextField()
    fechapublicacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-creado']





