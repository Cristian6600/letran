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

    
    ]