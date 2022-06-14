from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Noticia

class probando(ListView):
    template_name = "publico/index.html"

    def get_queryset(self):
        queryset = Noticia.objects.all()
        return queryset

#-----------Servicios---------------------------------
class mesa_docu(TemplateView):
    template_name = "publico/servicios/mensajeria_documentos.html"

class Paqueteo(TemplateView):
    template_name = "publico/servicios/paqueteo.html"

class Servicios_adicionales(TemplateView):
    template_name = "publico/servicios/serv_adi.html"

class Almacenamiento(TemplateView):
    template_name = "publico/servicios/almacenamiento.html"

#-------------------------------------------------------    

class Terminos_cond(TemplateView):
    template_name = "publico/terminos_condi.html"

class Docu_masiva(TemplateView):
    template_name = "publico/docu_masiva.html"

class politica_priva(TemplateView):
    template_name = "publico/polica_priva.html"

class politica_t_datos(TemplateView):
    template_name = "publico/general/polica_t_datos.html"

class Sedes(TemplateView):
    template_name = "publico/general/sedes.html"

class Quienes_somos(TemplateView):
    template_name = "publico/general/quienes-somos.html"

class Politica_SGC(TemplateView):
    template_name = "publico/politica_sgc.html"

class Cumplimiento(TemplateView):
    template_name = "publico/requerimientos/cumplimiento.html"

#---------------Noticias------------------------------
# class NoticiaDetailView(DetailView):
#     model: Noticia
#     template_name = "publico/index.html"

   
