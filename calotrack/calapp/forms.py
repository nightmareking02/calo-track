from django import forms
from .models import calmodel,savemodel

class caloform(forms.ModelForm):
    class Meta:
        model=calmodel
        fields="__all__"

class saveform(forms.ModelForm):
    class Meta:
        model=savemodel
        fields=['consumedfood','quantity']