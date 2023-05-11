from django import forms


class LectorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    apellido = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True)

class EscritorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    apellido = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True, max_length=20)    
    dni = forms.CharField(required=True, max_length=32)    
    fecha_nacimiento = forms.DateField(required=True)    

class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    codigo = forms.CharField(required=True, max_length=20)
    categoria = forms.CharField(required=True, max_length=256)
    fecha_publicacion = forms.DateField(required=True)    
