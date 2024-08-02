from django.shortcuts import render
from appescuela.models import Curso
from appescuela.forms import CursoFormulario

def inicio(request):
    return render (request, "appescuela/inicio.html")

def cursos(request):
    return render (request, "appescuela/cursos.html")

def estudiantes(request):
    return render (request, "appescuela/estudiantes.html")

def profesores(request):
    return render (request, "appescuela/profesores.html")

def entregables(request):
    return render (request, "appescuela/entregables.html")



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()

            return render(request, "appescuela/inicio.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "appescuela/form_con_api.html", {"mi_formulario": mi_formulario})

