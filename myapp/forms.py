from django import forms
from .models import *

class bookform(forms.ModelForm):
    class Meta:
        model=bookinfo
        fields='__all__'