from django.urls import path
from .views import index, jogadores, equipes, eventos, campeonatos

urlpatterns = [
    path('', index),
    path('jogadores', jogadores),
    path('equipes', equipes),
    path('eventos', eventos),
    path('campeonatos', campeonatos)
]
