from distutils.text_file import TextFile
import email
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyexpat import model
from typing import Text
from django.db import models
from .managers import BdManager
# from applications.cliente.models import Departamento


class Pqr(models.Model):
    SOLICITUD = (
        ('PE', 'Petición'),
        ('QUEJA', 'Queja'),
        ('INDEM', 'Indemnización'),
        ('SUG', 'Sugerencia'), 
    )

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
    tipo_soli = models.CharField(
        max_length=10,
        choices=SOLICITUD)
    # otro_cual = models.CharField(max_length=30)
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
    archivo = models.FileField(
        upload_to='archivos_pqr',
        blank=True)

    objects = BdManager()

    def __str__(self):
        return str(self.n_guia)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()
    ciudad = models.CharField(max_length=40)
    empresa = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    aceptar = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Respuesta(models.Model):

    Tipo = (
        ('Abierto', 'Abierto'),
        ('Pendiente', 'Pendiente'),
        ('Cerrado', 'Cerrado'),
    )

    id = models.OneToOneField(
        Pqr, primary_key=True,
        on_delete=models.CASCADE,
        verbose_name= 'numero_pqr', 
        related_name= 'pqr_respuesta'
        )

    tipo = models.CharField(max_length=9, choices=Tipo, default='Abierto')

    respuesta = models.TextField(max_length=7500)

    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True,)

@receiver(post_save, sender=Pqr)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        Respuesta.objects.create(id=instance)