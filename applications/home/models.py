from django.db import models

# Create your models here.
class Noticia(models.Model):
    articulo = models.TextField(max_length=800)