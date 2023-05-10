from django import forms


class LectorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    apellido = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True)