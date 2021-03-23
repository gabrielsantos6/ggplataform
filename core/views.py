from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def jogadores(request):
    return render(request, 'jogadores.html')


def campeonatos(request):
    return render(request, 'campeonatos.html')


def equipes(request):
    return render(request, 'equipes.html')


def eventos(request):
    return render(request, 'eventos.html')
