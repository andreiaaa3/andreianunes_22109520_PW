from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("licenciaturas/", views.licenciaturas_view, name="licenciaturas"),
    path("licenciaturas/<int:id>/", views.licenciatura_view, name="licenciatura"),
    path("docentes/", views.docentes_view, name="docentes"),
    path("ucs/", views.ucs_view, name="ucs"),
    path("projetos/", views.projetos_view, name="projetos"),
    path("projetos/novo/", views.novo_projeto_view, name="projeto_novo"),
    path("projetos/<int:id>/", views.projeto_view, name="projeto"),
    path("projetos/edita/<int:id>/", views.edita_projeto_view, name="edita_projeto"),
    path("tecnologias/", views.tecnologias_view, name="tecnologias"),5
    path("tfcs/", views.tfcs_view, name="tfcs"),
    path("competencias/", views.competencias_view, name="competencias"),
    path("formacoes/", views.formacoes_view, name="formacoes"),
    path("makingof/", views.makingof_view, name="makingof"),
]