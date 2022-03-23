from distutils.text_file import TextFile
import email
from pyexpat import model
from typing import Text
from django.db import models
# from applications.cliente.models import Departamento


class Pqr(models.Model):

    TIPOS = (
        ('C', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'Nit'),
        ('TDI', 'Tarjeta de identidad'),
        ('PSATE', 'Pasaporte'),
        ('P_P_P_T', 'Persmiso por proteccion temporal'),
        ('C_V', 'Cédula Venezolana'),
        ('P_E_D_P', 'Permsio especial de permanencia'),
    )
    ciudad_radi = models.CharField(
        max_length=80,
        verbose_name='Ciudad radicado'
        )
    fecha = models.DateField(blank=True, null=True)
    # tipo_pqr 
    # tipo_soli
    otro_cual = models.CharField(max_length=30)
    tipo_do = models.CharField(
        max_length=8,
        choices=TIPOS,)
    n_documento = models.CharField(max_length=12)
    apellidos = models.CharField(max_length=60)
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    n_contacto = models.CharField(max_length = 10)
    direccion = models.CharField(max_length=120)
    ciudad_env = models.CharField(
        max_length=80,
        verbose_name='Ciudad envio'
        )
    n_guia = models.IntegerField()
    desc_pqr = models.TextField()
    aceptar = models.BooleanField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()
    ciudad = models.CharField(max_length=40)
    empresa = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    aceptar = models.BooleanField()
    