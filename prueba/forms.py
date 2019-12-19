from django import forms
from prueba.choices import CASTELLANO,GENERO

class pruebaForms(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True)
    fecha_nacimiento=forms.DateField(label="Fecha de nacimiento",required=True)
    #fecha_nacimiento=forms.DateInput(format=('%d-%m-%Y'))
    habla_castellano=forms.ChoiceField( choices=CASTELLANO, label="Español",widget=forms.Select(),  required=True)
    genero=forms.ChoiceField(choices=GENERO, label="Genero",widget=forms.Select(),required=True)

class formPreguntas(forms.Form):
    p1_p1 = forms.CharField(label="bla",required=False)