from django.db import models

from django.db import models

class CategoriaAcervoManager(models.Manager):
    pass

class CategoriaAcervo(models.Model):

    nome = models.CharField('Nome da Categoria', max_length=100)
    descricao = models.TextField('Descrição da Categoria')

    image = models.ImageField(
        verbose_name='Imagem da Categoria'
    )

    categoria_pai = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, 
        verbose_name='Categoria Pai', related_name='categorias_filhas'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CategoriaAcervoManager()

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
    descricao = models.TextField('Descrição')
    data = models.DateField('Data do Item', blank=True, null=True)
    fundo = models.CharField('Fundo', blank=True, null=True, max_length=100)
    id_acervo = models.IntegerField('Identificador no Acervo', blank=True, null=True)
    url_documentacao_externa = models.CharField('URL da documentação externa', 
                                                blank=True, null=True, max_length=100)

    categorias = models.ManyToManyField(CategoriaAcervo)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ItemAcervoManager()

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
        return self.item_acervo

    class Meta:
        verbose_name = 'Foto do Item do Acervo'
        verbose_name_plural = 'Fotos dos Itens do Acervo'
        ordering = ['criado_em']