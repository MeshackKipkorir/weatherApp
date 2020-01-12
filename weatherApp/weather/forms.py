from django import forms
from django.forms import ModelForm,TextInput
from .models import weatherModel

class CityForm(forms.ModelForm):
    
    class Meta:
        model = weatherModel
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class':'form',
            'placeholder':'City Name',
            'size':25
        })}
