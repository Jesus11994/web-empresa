from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    
    titulo = models.CharField(max_length=200)
    contenido = RichTextField(max_length=200)
    creado = models.DateField(auto_now_add=True)
    actualizado =models.DateField(auto_now=True)

    class Meta:
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo