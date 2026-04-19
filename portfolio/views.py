from django.shortcuts import render
from .models import (Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao, MakingOf)

def home(request):
    return render(request, "portfolio/home.html")

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, "portfolio/licenciaturas.html", {"licenciaturas": licenciaturas})

def licenciatura_view(request, id):
    licenciatura = Licenciatura.objects.get(id=id)
    return render(request, "portfolio/licenciatura.html", {"licenciatura": licenciatura})

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, "portfolio/docentes.html", {"docentes": docentes})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.all()
    return render(request, "portfolio/ucs.html", {"ucs": ucs})

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, "portfolio/projetos.html", {"projetos": projetos})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, "portfolio/tecnologias.html", {"tecnologias": tecnologias})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, "portfolio/tfcs.html", {"tfcs": tfcs})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, "portfolio/competencias.html", {"competencias": competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, "portfolio/formacoes.html", {"formacoes": formacoes})

def makingof_view(request):
    makingofs = MakingOf.objects.all()
    return render(request, "portfolio/makingof.html", {"makingofs": makingofs})