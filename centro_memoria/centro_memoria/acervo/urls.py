from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('', views.acervo, name='acervo'),
    path('pesquisa/?pesquisa=<str:parametro>/', views.acervo_pesquisa, name='pesquisa'),
    path('pesquisa/?categoria=<str:categoria>&fundo_colecao=<str:fundo_colecao>&autor=<str:autor>&titulo=<str:titulo>&item=<str:item>&data=<str:data>&periodo_inicio=<str:periodo_inicio>&periodo_fim=<str:periodo_fim>&/', views.acervo_pesquisa_avancada, name='pesquisa_avancada'),
    path('<str:nome_categoria>/', views.acervo_categoria, name='acervo_categoria'),
    path('<str:nome_categoria>/<str:nome_item>/', views.item_detalhe, name='item_detalhe')
]