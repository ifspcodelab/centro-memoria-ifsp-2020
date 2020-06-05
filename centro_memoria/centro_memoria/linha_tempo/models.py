from django.db import models

class EventoManager(models.Manager):
    pass

class Evento(models.Model):

    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição')
    data = models.DateField('Data do Evento')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = EventoManager()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Evento da Linha do Tempo'
        verbose_name_plural = 'Eventos da Linha do Tempo'
        ordering = ['titulo']


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
        return self.evento

    class Meta:
        verbose_name = 'Foto do Evento'
        verbose_name_plural = 'Fotos dos Eventos'
        ordering = ['criado_em']