from django.urls import path
from . import views

app_name = 'instituicao'

urlpatterns = [
    path('agendamento/', views.agendamento, name='agendamento'),
]