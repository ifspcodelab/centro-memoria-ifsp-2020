from django.db import models
from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField

class NoticiaManager(models.Manager):
    pass

class Noticia(models.Model):

    titulo = models.CharField('Título', max_length=100)
    descricao = RichTextField('Descrição', max_length=350)
    corpo = RichTextField('Corpo')
    destaque = models.BooleanField('Destaque')
    periodo_destaque = models.IntegerField('Tempo em Destaque', null=True, blank=True)

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = NoticiaManager()

    def get_absolute_url(self):
        return reverse('noticias:noticia_detalhes', args=[str(self.titulo).lower()])

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['titulo']


class FotoNoticiaManager(models.Manager):
    pass

class FotoNoticia(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem da Notícia'
    )

    noticia = models.ForeignKey(Noticia, on_delete=models.PROTECT, 
        verbose_name='Notícia', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoNoticiaManager()

    def __str__(self):
        return self.noticia.__str__()

    class Meta:
        verbose_name = 'Foto da Notícia'
        verbose_name_plural = 'Fotos das Notícias'
        ordering = ['criado_em']