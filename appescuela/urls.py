from django.urls import path
from appescuela import views
from appescuela.views import cursos, estudiantes, profesores, inicio, entregables

urlpatterns=[
    path("",inicio, name="inicio"),
    path("pag-cursos",cursos, name="cursos"),
    path("pag-estudiantes", estudiantes, name="estudiantes"),
    path("pag-profesores", profesores, name="profesores"),
    path("pag-entregables", entregables, name= "entregables"),
]

clase_21= [
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    ] 

urlpatterns += clase_21