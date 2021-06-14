from django.urls import path, re_path
from .views import IndexView, JogadoresView, EquipesView, EventosView, CampeonatosView, PagelandingView, VagasView, \
    PlayerView, EquipeView, CriarEquipeView, EditarPerfilView, EquipeDetailview, CriarVagaView, JogadorDetailView, \
    CampeonatoDetailView, AddMembroView, EditarEquipeView, InscreverEquipeCampeonatoView, DeleteMembroView, AwpPlayers

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jogadores/', JogadoresView.as_view(), name="jogadores"),
    path('jogadores/<int:pk>/', JogadorDetailView.as_view(), name='detailJogador'),
    path('equipes/', EquipesView.as_view(), name="equipes"),
    path('equipes/<int:pk>/', EquipeDetailview.as_view(), name='detailEquipe'),
    path('eventos/', EventosView.as_view(), name="eventos"),
    path('campeonatos/', CampeonatosView.as_view(), name="campeonatos"),
    path('campeonatos/<int:pk>/', CampeonatoDetailView.as_view(), name="detailCampeonato"),
    path('pagelanding/', PagelandingView.as_view(), name='pagelanding'),
    path('vagas/', VagasView.as_view(), name='vagas'),
    path('player/', PlayerView.as_view(), name='player'),
    path('equipe/', EquipeView.as_view(), name='equipe'),
    path('criarEquipe/', CriarEquipeView.as_view(), name='criarEquipe'),
    path('editarPerfil/<int:pk>/', EditarPerfilView.as_view(), name='editarPerfil'),
    path('jogadores/<int:pk>/', JogadorDetailView.as_view(), name='detailJogador'),
    path('adicionarMembro/', AddMembroView.as_view(), name='addMembro'),
    path('criarVaga/', CriarVagaView.as_view(), name='criarVaga'),
    path('editarEquipe/<int:pk>/', EditarEquipeView.as_view(), name='editarEquipe'),
    path('inscreverEquipe/<int:pk>/', InscreverEquipeCampeonatoView.as_view(), name='inscreverEquipe'),
    path('RemoverMembro/<int:pk>/', DeleteMembroView.as_view(), name='removerMembro'),
    path('Jogadores/Awps/', AwpPlayers.as_view(), name='awpPlayers'),

]
