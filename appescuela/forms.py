from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length= 20)
    comision = forms.IntegerField()