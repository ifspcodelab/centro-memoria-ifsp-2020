from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('', views.acervo, name='acervo'),
    path('pesquisa/<str:parametro>/', views.acervo_pesquisa, name='pesquisa'),
    path('<str:nome_categoria>/', views.acervo_categoria, name='acervo_categoria'),
    path('item/<str:nome_item>/', views.item_detalhe, name='item_detalhe')
]