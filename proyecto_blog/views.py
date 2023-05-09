from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "Hola Flopydu"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto = {
        "usuario": "Flopydu"
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/base.html',
        context=contexto,
    )
    return http_response

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/index.html',
        context=contexto,
    )
    return http_response