from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('', views.galerias, name='galerias'),
    path('<str:nome_galeria>/', views.galeria_detalhes, name='galeria_detalhes'),
    path('<str:nome_galeria>/<str:nome_personalidade>/', views.personalidade_detalhes, name='personalidade-detalhes')
]