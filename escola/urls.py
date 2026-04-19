## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos_view, name="cursos"),
    path('professores/', views.professor_view, name="professores"),
    path('alunos/', views.alunos_view, name="alunos"),


]