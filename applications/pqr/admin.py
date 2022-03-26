from django.contrib import admin
from . models import Pqr, Contacto

@admin.register(Pqr)
class PqrAdmin(admin.ModelAdmin):
    
    list_display = ('tipo_soli', 'n_guia', 'fecha')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'mail')


