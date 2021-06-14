
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    PATENTE_CHOICES = (
        ("Prata 1", "Prata 1"),
        ("Prata 2", "Prata 2"),
        ("Prata 3", "Prata 3"),
        ("Prata 4", "Prata 4"),
        ("Prata de Elite", "Prata de Elite"),
        ("Prata de Elite Mester", "Prata de Elite Mester"),
        ("Ouro 1", "Ouro 1"),
        ("Ouro 2", "Ouro 2"),
        ("Ouro 3", "Ouro 3"),
        ("Ouro Mestre", "Ouro Mestre"),
        ("AK 1", "AK 1"),
        ("AK 2", "AK1"),
        ("AK Cruzada", "AK Cruzada"),
        ("Xerife", "Xerife"),
        ("Águia 1", "Águia 1"),
        ("Águia 2", "Águia 2"),
        ("Supremo", "Supremo"),
        ("Global", "Global"),
        ("Sem Patente", "Sem Patente"),
        ("Expirado", "Expirado"),
    )

    NIVELHABILIDADE_CHOICES = (
        ("Iniciante", "Iniciante"),
        ("Amador", "Amador"),
        ("Semi Profissional", "Semi Profissional"),
        ("Profissional", "Profissional"),
    )

    FUNCAO_CHOICES = (
        ("Capitão", "Capitão"),
        ("AWP", "Awper"),
        ("Entry fragger", "Entry fragger"),
        ("Suporte", "Suporte"),
        ("Lurker", "Lurker"),
    )

    nome = models.CharField('Nome', max_length=100)
    dataNasc = models.DateField('Data de nascimento', blank=True, null=True)
    situacao = models.CharField('Situação', max_length=50)
    nickname = models.CharField('Nickname', max_length=25)
    patente = models.CharField('Patente', max_length=25, choices=PATENTE_CHOICES)
    nivelHabilidade = models.CharField('Nivel de Habilidade', max_length=17, choices=NIVELHABILIDADE_CHOICES)
    steam = models.CharField('Steam Url', max_length=200)
    is_dono = models.BooleanField(default=False)
    is_jogador = models.BooleanField(default=True)
    funcao_jogador = models.CharField('Funçao', max_length=20, default="", choices=FUNCAO_CHOICES)
    equipe_jogador = models.ForeignKey('core.Equipe', on_delete=models.CASCADE, null=True)


