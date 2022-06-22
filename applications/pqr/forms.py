from django import forms
from .models import Pqr, Contacto
from django.utils.safestring import mark_safe


class PqrForm(forms.ModelForm):
    
    class Meta:
        model = Pqr
        fields = (
            '__all__'    
        )

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = (
            '__all__'    
        )