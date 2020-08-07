from django.db import models

class AcontecimentoManager(models.Manager):
    pass

class Acontecimento(models.Model):

    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição')
    data = models.DateField('Data do acontecimento')

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AcontecimentoManager()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Acontecimento da Linha do Tempo'
        verbose_name_plural = 'Acontecimentos da Linha do Tempo'
        ordering = ['titulo']


class FotoAcontecimentoManager(models.Manager):
    pass

class FotoAcontecimento(models.Model):

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
        ordering = ['criado_em']