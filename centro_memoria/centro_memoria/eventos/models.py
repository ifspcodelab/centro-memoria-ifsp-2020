from django.db import models
from django.urls import reverse
from django.db import models

class EventoManager(models.Manager):
    pass

class Evento(models.Model):

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=250)
    texto = models.TextField('Texto sobre evento')
    destaque = models.BooleanField('Destaque')

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = EventoManager()

    def get_absolute_url(self):
        return reverse('eventos:evento_detalhes', args=[str(self.nome).lower()])

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['nome']


class FotoEventoManager(models.Manager):
    pass

class FotoEvento(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem do Evento'
    )

    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, 
        verbose_name='Evento', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoEventoManager()

    def __str__(self):
        return self.evento.__str__()

    class Meta:
        verbose_name = 'Foto do Evento'
        verbose_name_plural = 'Fotos dos Eventos'
        ordering = ['criado_em']