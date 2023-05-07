from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel" , "apellido": "Dautel"} ,
            {"nombre": "Flo" , "apellido": "Dotta"} ,
            {"nombre": "carlos" , "apellido": "perez"}, 
        ]
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


# Create your views here.
def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Python" , "comision": "1000"} ,
            {"nombre": "Frontend" , "comision": "1001"} ,
            {"nombre": "diseño" , "comision": "1002"}, 
        ]
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_cursos.html',
        context=contexto,
    )
    return http_response