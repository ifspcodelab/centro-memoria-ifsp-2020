from django.urls import path
from . import views

app_name = 'linha_tempo'

urlpatterns = [
    path('', views.linha_do_tempo, name='linhas_do_tempo'),
    path('<str:titulo_linha_do_tempo>/', views.timeline, name='timeline'),
    path('<str:titulo_linha_do_tempo>/<str:titulo_acontecimento>/', views.acontecimento_detalhes, name='acontecimento_detalhe'),
    
]