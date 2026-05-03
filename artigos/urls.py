from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('<int:id>/', views.artigo_view, name='artigo'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('<int:id>/editar/', views.edita_artigo_view, name='edita_artigo'),
    path('<int:id>/like/', views.like_artigo_view, name='like_artigo'),
    path('<int:id>/comentario/', views.comentario_artigo_view, name='comentario_artigo'),
]