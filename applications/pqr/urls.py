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
         views.Send.as_view(),
         name='contacto-letran',
    ),

    path(
        'consultar-pqr/',
         views.ConsultarListView.as_view(),
         name='consultar-pqr',
    ),

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
    # path('send/', views.Send.as_view(), name='send'),

    ]