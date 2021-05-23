from django.views.generic import TemplateView
from .models import Equipe, Vagas, Campeonato
from users.models import User


class IndexView(TemplateView):
    template_name = 'index.html'


class JogadoresView(TemplateView):
    template_name = 'jogadores.html'

    def get_context_data(self, **kwargs):
        context = super(JogadoresView, self).get_context_data(**kwargs)
        context['jogadores'] = User.objects.order_by('?').all()
        return context


class CampeonatosView(TemplateView):
    template_name = 'campeonatos.html'

    def get_context_data(self, **kwargs):
        context = super(CampeonatosView, self).get_context_data(**kwargs)
        context['campeonatos'] = Campeonato.objects.order_by('?').all()
        return context


class EquipesView(TemplateView):
    template_name = 'equipes.html'

    def get_context_data(self, **kwargs):
        context = super(EquipesView, self).get_context_data(**kwargs)
        context['equipes'] = Equipe.objects.order_by('?').all()
        return context


class EventosView(TemplateView):
    template_name = 'eventos.html'


class PagelandingView(TemplateView):
    template_name = 'pagelanding.html'


class VagasView(TemplateView):
    template_name = 'vagas.html'

    def get_context_data(self, **kwargs):
        context = super(VagasView, self).get_context_data(**kwargs)
        context['vagas'] = Vagas.objects.order_by('?').all()

        return context


class PlayerView(TemplateView):
    template_name = 'player.html'


class EquipeView(TemplateView):
    template_name = 'equipe.html'
