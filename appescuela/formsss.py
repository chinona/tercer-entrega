from django import forms

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length= 20)
    apellido = forms.CharField(max_length=30)