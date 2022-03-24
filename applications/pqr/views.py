from dataclasses import field

from re import template
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from . models import Pqr, Contacto
from .forms import PqrForm

class PqrCreateView(CreateView):
    # model = Pqr
    template_name = "publico/formulario/pqr.html"
    form_class = PqrForm
    #fields = ['fecha', 'tipo_do', 'tipo_soli', 'aceptar', 'n_documento','apellidos', 'nombre','email', 'n_contacto', 'direccion', 'n_guia','desc_pqr', 'ciudad_radi', 'ciudad_env']
    success_url = '.'

class ContactoCreateView(CreateView):
    template_name = "publico/formulario/contacto.html"
    model = Contacto
    fields = ['nombre', 'mail', 'ciudad', 'empresa', 'telefono', 'aceptar']
    success_url = '.'   

class ConsultarListView(ListView):
    template_name = "publico/formulario/consulta-pqr.html"
    model = Pqr
    context_object_name = 'list'

    def get_queryset(self):
        return Pqr.objects.all()

    
    


