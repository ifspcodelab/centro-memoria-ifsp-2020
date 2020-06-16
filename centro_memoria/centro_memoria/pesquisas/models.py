from django.db import models

class GrupoPesquisaManager(models.Manager):
    pass

class GrupoPesquisa(models.Model):

    nome = models.CharField('Nome do Grupo', max_length=100)
    descricao = models.CharField('Descrição do Grupo', max_length=255)
    texto_livre = models.TextField('Texto Livre')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = GrupoPesquisaManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Grupo de Pesquisa'
        verbose_name_plural = 'Grupos de Pesquisa'
        ordering = ['nome']

class FotoGrupoPesquisaManager(models.Manager):
    pass

class FotoGrupoPesquisa(models.Model):

    destaque = models.BooleanField('Destaque')

    imagem = models.ImageField(
        verbose_name='Imagem do Grupo de Pesquisa'
    )

    grupo_pesquisa = models.ForeignKey(GrupoPesquisa, on_delete=models.PROTECT, 
        verbose_name='Grupo de Pesquisa', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoGrupoPesquisaManager()

    def __str__(self):
        return self.grupo_pesquisa

    class Meta:
        verbose_name = 'Foto do Grupo de Pesquisa'
        verbose_name_plural = 'Fotos dos Grupos de Pesquisa'
        ordering = ['criado_em']

class MembroManager(models.Manager):
    pass

class Membro(models.Model):

    nome = models.CharField('Nome', max_length=100)
    funcao = models.CharField('Função', max_length=100, blank=True, null=True)
    descricao = models.CharField('Descrição do Trabalho do Membro', max_length=255, blank=True, null=True)

    image = models.ImageField(
        verbose_name='Foto do Membro do Grupo de Pesquisa', blank=True, null=True
    )

    grupo_pesquisa = models.ForeignKey(GrupoPesquisa, on_delete=models.PROTECT, 
        verbose_name='Grupo de Pesquisa', related_name='membros'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = MembroManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Membro do Grupo de Pesquisa'
        verbose_name_plural = 'Membros do Grupo de Pesquisa'
        ordering = ['nome']