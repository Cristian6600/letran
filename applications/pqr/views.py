from dataclasses import field
from re import template
from django.shortcuts import render
from django.views.generic import CreateView
from . models import Pqr, Contacto

class PqrCreateView(CreateView):
    model = Pqr
    template_name = "publico/formulario/pqr.html"
    fields = ['fecha', 'tipo_do', 'n_documento','apellidos', 'nombre','email', 'n_contacto', 'direccion', 'n_guia','desc_pqr']
    success_url = '.'   

class ContactoCreateView(CreateView):
    template_name = "publico/formulario/contacto.html"
    model = Contacto
    fields = ['nombre', 'mail', 'ciudad', 'empresa', 'telefono', 'aceptar']
    success_url = '.'   


