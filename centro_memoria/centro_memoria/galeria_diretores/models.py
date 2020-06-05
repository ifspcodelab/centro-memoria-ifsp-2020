from django.db import models

from django.db import models

class DiretorManager(models.Manager):
    pass

class Diretor(models.Model):

    nome = models.CharField('Nome', max_length=100)
    sobre = models.TextField('Sobre')
    inicio_direcao = models.DateField('Início da direçao')
    fim_direcao = models.DateField('Fim da direção')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = DiretorManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'
        ordering = ['nome']


class FotoDiretorManager(models.Manager):
    pass

class FotoDiretor(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem do Diretor'
    )

    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, 
        verbose_name='Diretor', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoDiretorManager()

    def __str__(self):
        return self.diretor

    class Meta:
        verbose_name = 'Foto do Diretor'
        verbose_name_plural = 'Fotos dos Diretores'
        ordering = ['criado_em']