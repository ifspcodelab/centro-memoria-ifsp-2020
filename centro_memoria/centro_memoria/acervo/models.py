from django.db import models
from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField

class CategoriaAcervoManager(models.Manager):
    pass

class CategoriaAcervo(models.Model):

    nome = models.CharField('Nome da Categoria', max_length=100)
    descricao = RichTextField('Descrição da Categoria')

    imagem = models.ImageField(
        verbose_name='Imagem da Categoria'
    )

    categoria_pai = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, 
        verbose_name='Categoria Pai', related_name='categorias_filhas'
    )

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CategoriaAcervoManager()

    def get_absolute_url(self):
        return reverse('acervo:acervo_categoria', args=[str(self.nome).lower()])

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria do Acervo'
        verbose_name_plural = 'Categorias do Acervo'
        ordering = ['nome']


class ItemAcervoManager(models.Manager):
    pass

class ItemAcervo(models.Model):

    nome = models.CharField('Nome', max_length=100)
    descricao = RichTextField('Descrição')
    data = models.DateField('Data do Item', blank=True, null=True)
    fundo = models.CharField('Fundo', blank=True, null=True, max_length=100)
    id_acervo = models.IntegerField('Identificador no Acervo', blank=True, null=True)

    categorias = models.ManyToManyField(CategoriaAcervo)

    ativo = models.BooleanField('Registro ativo?', 
        help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ItemAcervoManager()

    def get_absolute_url(self):
        return reverse('acervo:item_detalhe', args=[str(self.nome).lower()])

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Item do Acervo'
        verbose_name_plural = 'Itens do Acervo'
        ordering = ['nome']

class FotoItemAcervoManager(models.Manager):
    pass

class FotoItemAcervo(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem do Item do Acervo'
    )

    item_acervo = models.ForeignKey(ItemAcervo, on_delete=models.PROTECT, 
        verbose_name='Item do Acervo', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoItemAcervoManager()

    def __str__(self):
        return self.item_acervo.__str__()

    class Meta:
        verbose_name = 'Foto do Item do Acervo'
        verbose_name_plural = 'Fotos dos Itens do Acervo'
        ordering = ['criado_em']

class DimensaoManager(models.Manager):
    pass

class Dimensao(models.Model):

    tipo = models.CharField('Tipo', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = DimensaoManager()

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Dimensão'
        verbose_name_plural = 'Dimensões'
        ordering = ['criado_em']

class DimensaoItemAcervoManager(models.Manager):
    pass

class DimensaoItemAcervo(models.Model):

    dimensao = models.ForeignKey(Dimensao, on_delete=models.PROTECT, 
        verbose_name='Dimensão', related_name='dimensoes'
    )

    quantidade = models.CharField('Quantidade', max_length=50)

    item_acervo = models.ForeignKey(ItemAcervo, on_delete=models.PROTECT, 
        verbose_name='Item do Acervo', related_name='item_acervo'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = DimensaoItemAcervoManager()

    def __str__(self):
        return self.dimensao.__str__()

    class Meta:
        verbose_name = 'Dimensão do Item'
        verbose_name_plural = 'Dimensões do Item'
        ordering = ['criado_em']