from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [

    path(
        '', 
        views.probando.as_view(),
        name='publico',
    ),
    #----------Servicios------------------
    path(
        'mensajeria-documentos/', 
        views.mesa_docu.as_view(),
        name='mensajeria-documentos',
    ),
    
    path(
        'paqueteo/', 
        views.Paqueteo.as_view(),
        name='paqueteo',
    ),
    
    path(
        'servicios-adicionales/', 
        views.Servicios_adicionales.as_view(),
        name='servicios-adicionales',
    ),
    #----------------------------------------
     path(
        'terminos-condiciones/', 
        views.Terminos_cond.as_view(),
        name='terminos-condiciones',
    ),

    path(
        'documentacion-masiva/', 
        views.Docu_masiva.as_view(),
        name='documentacion-masiva',
    ),
    
    path(
        'politica-t-datos/', 
        views.politica_t_datos.as_view(),
        name='politica-t-datos',
    ),
    path(
        'sedes/', 
        views.Sedes.as_view(),
        name='sedes',
    ),
    
    path(
        'quienes-somos/', 
        views.Quienes_somos.as_view(),
        name='quienes-somos',
    ),
    
    path(
        'politica-sgc/', 
        views.Politica_SGC.as_view(),
        name='politica-sgc',
    ),
    
    path(
        'cumplimiento/', 
        views.Cumplimiento.as_view(),
        name='cumplimiento',
    ),
]