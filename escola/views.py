##  ficheiro escola/views.py

from django.shortcuts import render
from .models import Escola, Curso, Professor, Aluno

def escola_view(request):
    return render(request, "escola/home.html")

def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professor_view(request):

    professores = Professor.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/professor.html', {'professores': professores})

def alunos_view(request):

    alunos = Aluno.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/alunos.html', {'alunos': alunos})