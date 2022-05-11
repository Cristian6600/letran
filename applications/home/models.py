from django.db import models

# Create your models here.

class Home(models.Model):
    titulo = models.CharField(max_length=30, verbose_name='Titulo pagina')

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    articulo = models.TextField(max_length=800)
    imagen = models.ImageField(upload_to='imagen_home')