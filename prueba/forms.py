from django import forms
from prueba.choices import *

class pruebaForms(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True)
    fecha_nacimiento=forms.DateTimeField(label="Fecha de nacimiento",required=True)
    habla_castellano=forms.ChoiceField( choices=CASTELLANO, label="Español",widget=forms.Select(),  required=True)
    genero=forms.ChoiceField(choices=GENERO, label="Genero",widget=forms.Select(),required=True)
