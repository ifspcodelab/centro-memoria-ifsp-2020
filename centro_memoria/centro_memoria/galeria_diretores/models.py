from django.db import models
from django.urls import reverse
from django.db import models

class GaleriaManager(models.Manager):
    pass

class Galeria(models.Model):

    nome = models.CharField('Nome da Galeria', max_length=100)
    descricao = models.TextField('Descrição da Galeria')

    imagem = models.ImageField(
        verbose_name='Imagem da Galeria'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = GaleriaManager()

    def get_absolute_url(self):
        return reverse('galeria:personalidades', args=[self.nome])

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ['nome']

class PersonalidadeManager(models.Manager):
    pass

class Personalidade(models.Model):

    nome = models.CharField('Nome', max_length=100)
    funcao = models.CharField('Função', max_length=100, blank=True, null=True)
    sobre = models.TextField('Sobre')
    inicio_servico = models.DateField('Início dos serviços prestados')
    fim_servico = models.DateField('Fim dos serviços prestados')

    galerias = models.ManyToManyField(Galeria, related_name='galerias')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = PersonalidadeManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Personalidade'
        verbose_name_plural = 'Personalidades'
        ordering = ['nome']


class FotoPersonalidadeManager(models.Manager):
    pass

class FotoPersonalidade(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem da Personalidade'
    )

    personalidade = models.ForeignKey(Personalidade, on_delete=models.PROTECT, 
        verbose_name='Personalidade', related_name='personalidade'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoPersonalidadeManager()

    def __str__(self):
        return self.personalidade.__str__()

    class Meta:
        verbose_name = 'Foto da Personalidade'
        verbose_name_plural = 'Fotos das Personalidades'
        ordering = ['criado_em']