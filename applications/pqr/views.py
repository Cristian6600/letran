from dataclasses import field
from pyexpat import model
from django.template import loader
from re import template
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.views import generic
from . models import Pqr, Contacto, Respuesta
from .forms import PqrForm
from django.http import HttpResponse
from .utils import render_to_pdf

class PqrCreateView(CreateView):

    template_name = "publico/formulario/pqr.html"
    form_class = PqrForm
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
        print('*******')
        palabra_clave = self.request.GET.get("kword")
        lista = Pqr.objects.filter(
            id = palabra_clave
        )
        return lista

def index(request):
    latest_question_list = Pqr.objects.all()
    
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return render(request, 'publico/prueba-eliminar.html', context)

class IndexView(generic.DetailView):
    model = Pqr
    template_name = 'publico/prueba-eliminar.html'
    context_object_name = 'latest_question_list'

class RespuestaPdf(DetailView):
    
    def get(self, request, *args, **kwargs):
        
        nombre = self.kwargs['full_name']
               
        respuesta = Respuesta.objects.get(id = nombre)
        data = {
            'respuesta': respuesta,
                                    
        }
        pdf = render_to_pdf('publico/formulario/pdf_respuestas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    


    
    


