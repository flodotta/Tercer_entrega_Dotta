from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "Hola Flopydu"
    pagina_html = HttpResponse(saludo)
    return pagina_html