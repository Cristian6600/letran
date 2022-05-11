from django.contrib import admin
from . models import Noticia, Home

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'titulo', 'articulo' )

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
