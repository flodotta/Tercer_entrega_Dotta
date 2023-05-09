from django.shortcuts import render

# Create your views Lectores here.
def listar_lectores(request):
    contexto = {
        "lectores": [
            {"nombre": "Cata" , "comision": "1000"} ,
            {"nombre": "Flo" , "comision": "1001"} ,
            {"nombre": "Mahia" , "comision": "1002"}, 
        ]
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_lectores.html',
        context=contexto,
    )
    return http_response

# Create your views Escritores here.
def listar_escritores(request):
    contexto = {
        "escritores": [
            {"nombre": "Emanuel" , "apellido": "Dautel"} ,
            {"nombre": "Flo" , "apellido": "Dotta"} ,
            {"nombre": "carlos" , "apellido": "perez"}, 
        ]
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_escritores.html',
        context=contexto,
    )
    return http_response

# Create your views Articulos here.
def listar_articulos(request):
    contexto = {
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_articulos.html',
        context=contexto,
    )
    return http_response