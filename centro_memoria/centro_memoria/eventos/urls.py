from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('<str:titulo>/', views.evento_detalhes, name='evento_detalhes')
]