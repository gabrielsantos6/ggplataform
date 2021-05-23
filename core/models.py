import uuid
from django.db import models
from users.models import User

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Estado(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=2)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome


class Server(models.Model):
    nome = models.CharField('Nome', max_length=100)
    ip = models.CharField('Ip ', max_length=100)

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField('Nome', max_length=100)
    senha = models.CharField('Senha', max_length=25)
    descricao = models.CharField('Descrição', max_length=255)
    numeroMembros = models.IntegerField('Numero de membros', blank=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Dono')
    membros = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nomeEvento = models.CharField('Nome', max_length=100)
    dataInicio = models.DateTimeField('Data de inicio', blank=True, null=True)
    dataTermino = models.DateTimeField('Data de termino', blank=True, null=True)
    informacao = models.TextField('Informação', blank=True)
    situacaoEvento = models.CharField('Situação', max_length=30)
    usuarios = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nomeEvento


class Funcao(models.Model):
    FUNCAO_CHOICES = (
        ("Capitão", "Capitão"),
        ("AWP", "Awper"),
        ("Entry fragger", "Entry fragger"),
        ("Suporte", "Suporte"),
        ("Lurker", "Lurker"),
    )

    funcao = models.CharField('Funçao', max_length=20, choices=FUNCAO_CHOICES)

    class Meta:
        verbose_name = 'Funcao'
        verbose_name_plural = 'Funcoes'

    def __str__(self):
        return self.funcao


class Vagas(models.Model):
    VAGAS_CHOICES = (
        ("Capitão", "Vaga para Capitão"),
        ("AWP", "Vaga para Awper"),
        ("Entry Fragger", "Vaga para Entry fragger"),
        ("Suporte", "Vaga para  Suporte"),
        ("Lurker", "Vaga para Lurker"),
    )

    NIVELHABILIDADE_CHOICES = (
        ("Iniciante", "Iniciante"),
        ("Amador", "Amador"),
        ("Semi Profissional", "Semi Profissional"),
        ("Profissional", "Profissional"),
    )
    vaga = models.CharField('Vaga', max_length=50, choices=VAGAS_CHOICES)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name="Funcoes")
    equipe = models.OneToOneField("Equipe", on_delete=models.CASCADE)
    descricao = models.TextField("Descrição", blank=True)
    nivel_habilidade = models.CharField('Nivel de Habilidade', max_length=17, choices=NIVELHABILIDADE_CHOICES,blank=True)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.vaga


class Campeonato(models.Model):
    nome = models.CharField('Nome', max_length=200)
    data_inicio = models.DateField('Data de Inicio', blank=True, null=True)
    data_termino = models.DateField('Data de Termino', blank=True, null=True)
    equipes_inscritas = models.ManyToManyField(Equipe, blank=True)
    premiacao = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'

    def __str__(self):
        return self.nome
