from django.urls import path
from . import views
app_name = "pqr_app"

urlpatterns = [
    path(
        'pqr-letran/',
         views.PqrCreateView.as_view(),
         name='pqr',
    ),
    
    path(
        'contacto-letran/',
         views.ContactoCreateView.as_view(),
         name='contacto-letran',
    ),

    path(
        'consultar-pqr/',
         views.ConsultarListView.as_view(),
         name='consultar-pqr',
    ),

    path('prueba', views.index, name='index'),

    path(
        'prueba-vista/',
         views.IndexView.as_view(),
         name='prueba-vista',
    ),

    path(
        'respuesta-pdf/<full_name>/',
        views.RespuestaPdf.as_view(),
        name = 'respuesta-pdf',
    ),

    ]