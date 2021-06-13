from django.contrib import admin
from .models import Evento, Estado, Cidade, Server, Equipe, Funcao, Vagas, Campeonato

# Register your models here.


@admin.register(Evento)
class Evento(admin.ModelAdmin):
    list_display = ('nomeEvento', 'dataInicio', 'dataTermino', 'informacao', 'situacaoEvento'
                    )


@admin.register(Estado)
class Estado(admin.ModelAdmin):
    list_display = ('nome', 'sigla')


@admin.register(Cidade)
class Cidade(admin.ModelAdmin):
    list_display = ('nome', 'estado')


@admin.register(Server)
class Server(admin.ModelAdmin):
    list_display = ('nome', 'ip')


@admin.register(Equipe)
class Equipe(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'dono',)


@admin.register(Funcao)
class Funcao(admin.ModelAdmin):
    list_display = ('funcao',)


@admin.register(Vagas)
class Vagas(admin.ModelAdmin):
    list_display = ('vaga', 'funcao', 'equipe', 'descricao')


@admin.register(Campeonato)
class Campeonato(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_termino', 'premiacao')






