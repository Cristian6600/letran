from dataclasses import field
from pyexpat import model
from django import http
from django.template import loader
from re import template
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, View
from django.views import generic
from . models import Pqr, Contacto, Respuesta
from .forms import PqrForm, ContactForm
from django.http import HttpResponse
from .utils import render_to_pdf
from django.db.models import Q

class PqrCreateView(CreateView):

    template_name = "publico/formulario/pqr.html"
    form_class = PqrForm
    success_url = '.'

# class ContactoCreateView(CreateView):
#     template_name = "publico/formulario/contacto.html"
#     model = Contacto
#     fields = ['nombre', 'mail', 'ciudad', 'empresa', 'telefono', 'aceptar', 'observacion']
#     success_url = '.'   

class ConsultarListView(ListView):
    template_name = "publico/formulario/consulta-pqr.html"
    model = Pqr
    context_object_name = 'list'

    def get_queryset(self):
        print('*******')
        palabra_clave = self.request.GET.get("kword")
        lista = Pqr.objects.filter(Q(id = palabra_clave)| Q(n_documento = palabra_clave)
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

from django.conf import settings
from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class Send(View):
    form_class = ContactForm
    template_name = 'publico/formulario/contacto.html'

    def get(self, request):
        mail = request.GET.get('mail')
        form = self.form_class()
        data = {
            'form': form,
            'mail':mail
        }
        return render(request, self.template_name, data)
    
    def post(self, request):
        mail = request.POST.get('mail')
        form = self.form_class(request.POST)
        datas = {
            'form': form,
            'mail':mail
        }
        if form.is_valid():
            self.object = form.save(commit=False)
            
            form.save()

            # return HttpResponse('<h1>Su registro se realizo correctamente</h1>')
            
        print(mail)

        template = get_template('publico/formulario/email-order-success.html')

        # Se renderiza el template y se envias parametros
        content = template.render({'mail': mail})

        # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives(
            'Esto es una prueba',
            'Se puede eliminar',
            settings.EMAIL_HOST_USER,
            [mail]
        )

        msg.attach_alternative(content, 'text/html')
        msg.send()

        return render(request, self.template_name, datas)
        
    
    


