from django import forms
from .models import Core

class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = ['text', 'photo']