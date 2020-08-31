from django.urls import path
from . import views

app_name = 'instituicao'

urlpatterns = [
    path('', views.index, name='index'),
    #path('servico/visitas', views.agendamento, name='visitas'),
    #path('contato/', views.faleconosco, name='contato'),
    path('pesquisa/<str:parametro>/', views.pesquisa_avancada, name='pesquisa')
]