from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class LinhaDoTempoManage(models.Manager):
    pass

class LinhaDoTempo(models.Model):
    titulo = models.CharField('Título da linha do tempo', max_length=100)
    descricao = RichTextField('Descrição curta', max_length=500)
    descricao_longa = RichTextField('Descrição longa')
    inicio_periodo = models.DateField('Inicío dessa linha do tempo')
    fim_periodo = models.DateField('Fim dessa linha do tempo', null=True, blank=True)

    image = models.ImageField(verbose_name='Imagem capa')

    ativo = models.BooleanField('Registro ativo?',
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = LinhaDoTempoManage()

    def get_absolute_url(self):
        return reverse('linha_tempo:timeline', args=[str(self.titulo).lower()])

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Linha do Tempo'
        verbose_name_plural = 'Linhas do tempo'
        ordering = ['inicio_periodo']

class AcontecimentoManager(models.Manager):
    pass

class Acontecimento(models.Model):

    titulo = models.CharField('Título do acontecimento', max_length=100)
    descricao = RichTextField('Descrição ', max_length=500)
    sobre = RichTextField('Descrição longa')
    data = models.DateField('Data do acontecimento')

    linha_do_tempo = models.ForeignKey(LinhaDoTempo, on_delete=models.PROTECT, 
        verbose_name='Linha do Tempo', related_name='acontecimento')

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AcontecimentoManager()

    def get_absolute_url(self):
        return reverse('linha_tempo:acontecimento_detalhe', args=[str(self.linha_do_tempo).lower(), str(self.titulo).lower()])

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Acontecimento da Linha do Tempo'
        verbose_name_plural = 'Acontecimentos da Linha do Tempo'
        ordering = ['data']


class FotoAcontecimentoManager(models.Manager):
    pass

class FotoAcontecimento(models.Model):
    nome = models.CharField('nome da imagem', max_length=100)
    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem do Acontecimento'
    )

    acontecimento = models.ForeignKey(Acontecimento, on_delete=models.PROTECT, 
        verbose_name='Acontecimento', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoAcontecimentoManager()

    def __str__(self):
        return self.acontecimento.__str__()

    class Meta:
        verbose_name = 'Foto do Acontecimento'
        verbose_name_plural = 'Fotos dos Acontecimentos'
        ordering = ['nome']