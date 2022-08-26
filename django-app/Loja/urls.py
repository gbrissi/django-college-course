from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('busca/', views.busca, name='busca'),
    path('adicionar/', views.adicionar, name='adicionar')
]