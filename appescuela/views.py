from django.shortcuts import render
from appescuela.forms_buscar import BuscaCursoForm
from appescuela.models import Curso
from appescuela.forms import CursoFormulario
from appescuela.models import Estudiante
from appescuela.formss import EstudianteFormulario
from appescuela.models import Profesor
from appescuela.formsss import ProfesorFormulario

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


def form_est(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Estudiante(nombre=informacion["curso"], apellido=informacion["apellido"])
            curso.save()

            return render(request, "appescuela/inicio.html")
    else:
        mi_formulario = EstudianteFormulario()

    return render(request, "appescuela/form_est.html", {"mi_formulario": mi_formulario})

def form_prof(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Profesor(nombre=informacion["curso"], apellido=informacion["apellido"])
            curso.save()

            return render(request, "appescuela/inicio.html")
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "appescuela/form_prof.html", {"mi_formulario": mi_formulario})




def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appescuela/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "appescuela/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
