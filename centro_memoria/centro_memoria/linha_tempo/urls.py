from django.urls import path
from . import views

app_name = 'linha_tempo'

urlpatterns = [
    path('', views.timeline, name='timeline'),
]