from django.db import models
from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator

class CategoriaAcervoManager(models.Manager):
    pass

class CategoriaAcervo(models.Model):

    nome = models.CharField('Nome da Categoria', max_length=100)
    descricao_curta = models.TextField('Descrição Curta da Categoria')
    descricao_longa = RichTextField('Descrição Longa da Categoria')

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

class FundoColecaoManager(models.Manager):
    pass

class FundoColecao(models.Model):

    nome = models.CharField('Nome', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FundoColecaoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fundo/Coleção'
        verbose_name_plural = 'Fundos/Coleções'
        ordering = ['criado_em']

class AbordagemManager(models.Manager):
    pass

class Abordagem(models.Model):

    tipo = models.CharField('Tipo', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AbordagemManager()

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Abordagem'
        verbose_name_plural = 'Abordagens'
        ordering = ['criado_em']

class TecnicaRegistroManager(models.Manager):
    pass

class TecnicaRegistro(models.Model):

    nome = models.CharField('Nome', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = TecnicaRegistroManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Técnica de Registro'
        verbose_name_plural = 'Técnicas de Registro'
        ordering = ['criado_em']

class TipoSuporteManager(models.Manager):
    pass

class TipoSuporte(models.Model):

    nome = models.CharField('Nome', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = TipoSuporteManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Suporte'
        verbose_name_plural = 'Tipos de Suporte'
        ordering = ['criado_em']

class TipoFormatoManager(models.Manager):
    pass

class TipoFormato(models.Model):

    nome = models.CharField('Nome', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = TipoFormatoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Formato'
        verbose_name_plural = 'Tipos de Formato'
        ordering = ['criado_em']

class IdiomaManager(models.Manager):
    pass

class Idioma(models.Model):

    idioma = models.CharField('Idioma', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = IdiomaManager()

    def __str__(self):
        return self.idioma

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['criado_em']

class FormaDocumentoManager(models.Manager):
    pass

class FormaDocumento(models.Model):

    forma = models.CharField('Forma', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FormaDocumentoManager()

    def __str__(self):
        return self.forma

    class Meta:
        verbose_name = 'Forma de Documento'
        verbose_name_plural = 'Formas de Documento'
        ordering = ['criado_em']

class PeriodicidadeManager(models.Manager):
    pass

class Periodicidade(models.Model):

    periodo = models.CharField('Período', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = PeriodicidadeManager()

    def __str__(self):
        return self.periodo

    class Meta:
        verbose_name = 'Periodicidade'
        verbose_name_plural = 'Periodicidades'
        ordering = ['criado_em']

class TipoReproducaoManager(models.Manager):
    pass

class TipoReproducao(models.Model):

    tipo = models.CharField('Tipo', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = TipoReproducaoManager()

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Tipo de Reprodução'
        verbose_name_plural = 'Tipos de Reprodução'
        ordering = ['criado_em']

class ProblemaConservacaoManager(models.Manager):
    pass

class ProblemaConservacao(models.Model):

    problema = models.CharField('Problema', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ProblemaConservacaoManager()

    def __str__(self):
        return self.problema

    class Meta:
        verbose_name = 'Problema de Conservação'
        verbose_name_plural = 'Problemas de Conservação'
        ordering = ['criado_em']

class AtividadeEventoManager(models.Manager):
    pass

class AtividadeEvento(models.Model):

    atividade = models.CharField('Atividade/Evento', max_length=100)
    especificacao = RichTextField('Especificação da Atividade/Evento')
    local = models.CharField('Local do Evento', max_length=100)
    data_inicio = models.DateField('Data de Início do Evento')
    data_fim = models.DateField('Data de Fim do Evento', blank=True, null=True)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AtividadeEventoManager()

    def __str__(self):
        return self.atividade

    class Meta:
        verbose_name = 'Atividade/Evento'
        verbose_name_plural = 'Atividades/Eventos'
        ordering = ['criado_em']

class AutorManager(models.Manager):
    pass

class Autor(models.Model):

    nome = models.CharField('Nome do Autor', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AutorManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['criado_em']

class ProdutorInstituicaoManager(models.Manager):
    pass

class ProdutorInstituicao(models.Model):

    nome = models.CharField('Nome do Produtor/Instituição', max_length=100)
    sigla = models.CharField('Nome do Produtor/Instituição', max_length=5)
    fundo_colecao = models.ForeignKey(FundoColecao, on_delete=models.PROTECT, 
        verbose_name='Fundo/Coleção', related_name='produtores',
        null=True, blank=True
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ProdutorInstituicaoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produtor/Instituição'
        verbose_name_plural = 'Produtores/Instituições'
        ordering = ['criado_em']

class EditoraManager(models.Manager):
    pass

class Editora(models.Model):

    nome = models.CharField('Nome da Editora', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = EditoraManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['criado_em']

class ItemAcervoManager(models.Manager):
    pass

class ItemAcervo(models.Model):

    CROMIA = (
        ('1', 'Branco & Preto'),
        ('2', 'Cores'),
    )

    ACESSO = (
        ('1', 'Livre'),
        ('2', 'Restrito'),
    )

    nome = models.CharField('Nome', max_length=100)
    descricao_curta = models.TextField('Descrição Curta')
    descricao_longa = RichTextField('Descrição Longa')
    fundo_colecao = models.ForeignKey(FundoColecao, on_delete=models.PROTECT, 
        verbose_name='Fundo/Coleção', related_name='itens',
        null=True, blank=True
    )
    origem = RichTextField('Origem')
    abordagem = models.ForeignKey(Abordagem, on_delete=models.PROTECT, 
        verbose_name='Abordagem', related_name='itens',
        null=True, blank=True
    )
    tipo_documento = models.CharField('Tipo de Documento', max_length=100)
    local = models.CharField('Local de Produção', max_length=100, blank=True, null=True)
    data_inicio = models.DateField('Data de Produção do Item')
    data_fim = models.DateField('Data do Fim da Produção do Item', blank=True, null=True)
    autores = models.ManyToManyField(Autor, 
        verbose_name='Autores', related_name='itens',
        blank=True
    )
    produtor_instituicao = models.ForeignKey(ProdutorInstituicao, on_delete=models.PROTECT, 
        verbose_name='Produtor/Instituição', related_name='itens',
        null=True, blank=True
    )
    classificacao = models.CharField('Classificação', max_length=100, blank=True, null=True)
    tecnica_registro = models.ForeignKey(TecnicaRegistro, on_delete=models.PROTECT, 
        verbose_name='Técnica de Registro', related_name='itens',
        null=True, blank=True
    )
    suporte = models.ForeignKey(TipoSuporte, on_delete=models.PROTECT, 
        verbose_name='Suporte', related_name='itens',
        null=True, blank=True
    )
    formato = models.ForeignKey(TipoFormato, on_delete=models.PROTECT, 
        verbose_name='Formato', related_name='itens',
        null=True, blank=True
    )
    idiomas = models.ManyToManyField(Idioma, 
        verbose_name='Idioma', related_name='itens',
        blank=True
    )
    forma = models.ForeignKey(FormaDocumento, on_delete=models.PROTECT, 
        verbose_name='Forma do Documento', related_name='itens',
        null=True, blank=True
    )
    cromia = models.CharField('Cromia', max_length=2, blank=True, null=True, choices=CROMIA)
    periodicidade = models.ForeignKey(Periodicidade, on_delete=models.PROTECT, 
        verbose_name='Periodicidade', related_name='itens',
        null=True, blank=True
    )
    itens = models.PositiveIntegerField('Quantidade de itens', validators=[MinValueValidator(1)])
    exemplares = models.PositiveIntegerField('Quantidade de Exemplares', validators=[MinValueValidator(0)])
    reproducao = models.ForeignKey(TipoReproducao, on_delete=models.PROTECT, 
        verbose_name='Reprodução', related_name='itens',
        null=True, blank=True
    )
    problemas_conservacao = models.ManyToManyField(ProblemaConservacao, 
        verbose_name='Problema de Conservação', related_name='itens',
        blank=True
    )
    acesso = models.CharField('Acesso', max_length=2, choices=ACESSO)
    atividades_eventos = models.ManyToManyField(AtividadeEvento,
        verbose_name='Atividade/Evento', related_name='itens',
        blank=True
    )
    descritores = models.TextField('Descritores', help_text='Separar cada descritor usando ";"')
    referencia = RichTextField('Referência')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, 
        verbose_name='Editora', related_name='itens',
        null=True, blank=True
    )
    local_custodia = models.TextField('Local de Custódia')
    observacoes = RichTextField('Observações', blank=True, null=True)

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