from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Equipe, Vagas, Campeonato, Perfil
from users.models import User
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("pagelanding")

        if not request.user.nickname:
            return HttpResponseRedirect(reverse_lazy("editarPerfil", kwargs={"pk": request.user.pk}))

        return super(IndexView, self).dispatch(request, *args, **kwargs)


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


class CriarEquipeView(CreateView):
    model = Equipe
    template_name = 'equipe_form.html'
    fields = ['nome', 'descricao', 'senha']
    success_url = reverse_lazy('equipes')

    def form_valid(self, form):
        equipe = form.save(commit=False)
        equipe.dono = self.request.user
        equipe.save()
        eqp = form.cleaned_data["nome"]
        obj_eqp = Equipe.objects.get(nome=eqp)
        User.objects.filter(id=self.request.user.id).update(equipe_jogador=obj_eqp)
        User.objects.filter(id=self.request.user.id).update(is_dono=True)
        obj_member = Equipe.objects.get(id=equipe.id)
        obj_member.membros.add(self.request.user)
        return super(CriarEquipeView, self).form_valid(form)


class EditarPerfilView(UpdateView):
    model = User
    template_name = 'profile_form.html'
    fields = ['nome', 'dataNasc', 'nickname', 'patente', 'nivelHabilidade', 'steam', 'funcao_jogador']
    success_url = reverse_lazy('index')


class EquipeDetailview(DetailView):
    model = Equipe
    template_name = 'equipe.html'

    def get_context_data(self, **kwargs):
        context = super(EquipeDetailview, self).get_context_data(**kwargs)
        self.pk = self.kwargs.get(self.pk_url_kwarg)
        context['membros'] = Equipe.objects.filter(id=self.pk)

        return context


class EditarEquipeView(UpdateView):
    model = Equipe
    template_name = 'equipe_form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('index')


class CriarVagaView(CreateView):
    model = Vagas
    template_name = 'vaga_form.html'
    fields = ['vaga', 'funcao', 'descricao', 'nivel_habilidade']
    success_url = reverse_lazy('vagas')

    def form_valid(self, form):
        vaga = form.save(commit=False)
        vaga.equipe = self.request.user.equipe_jogador
        vaga.save()
        return super(CriarVagaView, self).form_valid(form)


class JogadorDetailView(DetailView):
    model = User
    template_name = 'jogador.html'


class CampeonatoDetailView(DetailView):
    model = Campeonato
    template_name = 'campeonato.html'

    def get_context_data(self, **kwargs):
        context = super(CampeonatoDetailView, self).get_context_data(**kwargs)
        self.pk = self.kwargs.get(self.pk_url_kwarg)
        context['equipes'] = Campeonato.objects.filter(id=self.pk)

        return context


class AddMembroTemplateView(TemplateView):
    template_name = 'addMembro.html'


class AddMembroView(TemplateView, View):
    template_name = "addMembro.html"

    def post(self, request):
        if request.user.is_dono:
            membro = request.POST["membro"]
            equipe = request.user.equipe_jogador_id
            membro_obj = User.objects.get(id=membro)
            equipe_obj = Equipe.objects.get(id=equipe)
            equipe_obj.membros.add(membro_obj)
            User.objects.filter(id=membro).update(equipe_jogador=equipe_obj)
            return render(request, 'addMembro.html')
        else:
            return render(request, 'index.html')


class InscreverEquipeCampeonatoView(DetailView, View):
    model = Campeonato
    template_name = "inscreverEquipe.html"

    def post(self, request, **kwargs):
        if request.user.is_dono:
            equipe = request.user.equipe_jogador_id
            campeonato = Campeonato.objects.get(id=kwargs["pk"])
            equipe_obj = Equipe.objects.get(id=equipe)
            campeonato.equipes_inscritas.add(equipe_obj)
            pk = kwargs["pk"]
            return HttpResponseRedirect(
                reverse_lazy("detailCampeonato", kwargs={"pk": pk})
            )
        else:
            return render(request, 'index.html')
