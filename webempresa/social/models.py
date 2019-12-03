from django.db import models

# Create your models here.
class Link(models.Model):
    Key = models.SlugField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    creado = models.DateField(auto_now_add=True)
    actualizado =models.DateField(auto_now=True)

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre