from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<str:titulo>/', views.noticia_detalhes, name='noticia_detalhes')
]