from django.urls import path
from .views import IndexView, JogadoresView, EquipesView, EventosView, CampeonatosView, PagelandingView, VagasView, PlayerView, EquipeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jogadores/', JogadoresView.as_view(), name="jogadores"),
    path('equipes/', EquipesView.as_view(), name="equipes"),
    path('eventos/', EventosView.as_view(), name="eventos"),
    path('campeonatos/', CampeonatosView.as_view(), name="campeonatos"),
    path('pagelanding/', PagelandingView.as_view(), name='pagelanding'),
    path('vagas/', VagasView.as_view(), name='vagas'),
    path('player/', PlayerView.as_view(), name='player'),
    path('equipe/', EquipeView.as_view(), name='equipe'),
]
