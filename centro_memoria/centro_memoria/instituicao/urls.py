from django.urls import path
from . import views

app_name = 'instituicao'

urlpatterns = [
    path('', views.index, name='index'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('contato/', views.faleconosco, name='contato'),
    path('pesquisa/<str:parametro>/', views.pesquisa_avancada, name='pesquisa')
]