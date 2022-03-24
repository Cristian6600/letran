from django import forms
from .models import Pqr
from django.utils.safestring import mark_safe


class PqrForm(forms.ModelForm):
    
    class Meta:
        model = Pqr
        fields = (
            '__all__'    
        )

        