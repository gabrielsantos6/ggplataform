from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, View, ListView
from .models import Equipe, Vagas, Campeonato, Perfil, Evento
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


class JogadoresView(ListView):
    model = User
    template_name = 'jogadores.html'
    paginate_by = 9


class CampeonatosView(ListView):
    model = Campeonato
    template_name = 'campeonatos.html'
    paginate_by = 9


class EquipesView(ListView):
    model = Equipe
    template_name = 'equipes.html'
    paginate_by = 9


class EventosView(ListView):
    model = Evento
    template_name = 'eventos.html'
    paginate_by = 9


class PagelandingView(TemplateView):
    template_name = 'pagelanding.html'


class VagasView(ListView):
    model = Vagas
    template_name = 'vagas.html'
    paginate_by = 9


class PlayerView(TemplateView):
    template_name = 'player.html'


class EquipeView(TemplateView):
    template_name = 'equipe.html'


class CriarEquipeView(CreateView):
    model = Equipe
    template_name = 'equipe_form.html'
    fields = ['nome', 'descricao', 'senha']

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
        return HttpResponseRedirect(
            reverse_lazy("detailEquipe", kwargs={"pk": obj_eqp.id})
        )


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

    def get_success_url(self):
        id_equipe = self.kwargs['pk']
        return reverse_lazy('detailEquipe', kwargs={'pk': id_equipe})


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
            return HttpResponseRedirect(
                reverse_lazy("detailEquipe", kwargs={"pk": equipe_obj.id})
            )
        else:
            return render(request, 'index.html')


class DeleteMembroView(DeleteView):
    model = Equipe
    template_name = "deleteMembro.html"

    def post(self, request, pk):
        membro = request.POST["membro"]
        equipe = request.user.equipe_jogador_id
        membro_obj = User.objects.get(id=pk)
        equipe_obj = Equipe.objects.get(id=equipe)
        equipe_obj.membros.remove(membro_obj)
        User.objects.filter(id=pk).update(equipe_jogador=None)

        return HttpResponseRedirect(
            reverse_lazy("detailEquipe", kwargs={"pk": equipe_obj.id})
        )


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


class AwpPlayers(ListView):
    model = User
    template_name = 'jogadores.html'

    def get_queryset(self, **kwargs):
        return User.objects.filter(funcao_jogador='AWP')