from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.categorias_acervo, name='categorias'),
    path('pesquisa/<str:parametro>/', views.acervo_pesquisa, name='pesquisa'),
    path('<str:nome_categoria>/', views.categoria_detalhes, name='itens'),
    path('<str:nome_categoria>/<str:nome_item>/', views.item_detalhes, name='item-detalhes')
]