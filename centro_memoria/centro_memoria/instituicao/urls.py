from django.urls import path
from . import views

app_name = 'instituicao'

urlpatterns = [
    path('', views.index, name='index'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('faleconosco/', views.faleconosco, name='faleconosco'),
    path('pesquisa/<str:parametro>/', views.pesquisa_avancada, name='pesquisa')
]