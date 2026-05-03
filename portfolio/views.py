
from .models import (Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao, MakingOf)
from .forms import ProjetoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


def is_gestor_portfolio(user):
    return user.is_authenticated and user.groups.filter(name="gestor-portfolio").exists()

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

@login_required
@user_passes_test(is_gestor_portfolio)
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("projetos")

    context = {"form": form}
    return render(request, "portfolio/novo_projeto.html", context)

def projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    return render(request, "portfolio/projeto.html", {"projeto": projeto})

@login_required
@user_passes_test(is_gestor_portfolio)
def edita_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = ProjetoForm(instance=projeto)

    context = {"form": form, "projeto": projeto}
    return render(request, "portfolio/edita_projeto.html", context)

@login_required
@user_passes_test(is_gestor_portfolio)
def apaga_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    projeto.delete()
    return redirect("projetos")
