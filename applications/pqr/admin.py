from django.contrib import admin
from . models import Pqr, Contacto, Respuesta

@admin.register(Pqr)
class PqrAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'tipo_soli', 'n_guia', 'fecha')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'mail')

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'fecha')


