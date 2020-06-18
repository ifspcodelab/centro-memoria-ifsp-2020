from django.db import models

class InstituicaoManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
                models.Q(about__icontains=query) | \
                models.Q(name__icontains=query)
            )

class Instituicao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobre = models.TextField('Sobre')
    missao = models.TextField('Missão')
    visao = models.TextField('Visão')
    endereco = models.CharField('Endereço', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    email_agendamento = models.CharField('E-mail para envio de Agendamento', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    patrono = models.TextField('Informações sobre Patrono')
    atividade = models.TextField('Atividade')
    policia_acervo = models.TextField('Políticas de Acervo')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = InstituicaoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Instituição e Site'
        verbose_name_plural = 'Instituição e Site'
        ordering = ['criado_em']


class FotoInstituicaoManager(models.Manager):
    pass

class FotoInstituicao(models.Model):

    POSICAO_CHOICES = (
        ('R', 'Rodapé'),
        ('I', 'Index'),
    )

    posicao = models.CharField('Posição', max_length=1, choices=POSICAO_CHOICES)

    imagem = models.ImageField(
        verbose_name='Imagem da Instituição'
    )

    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, 
        verbose_name='Instituição', related_name='fotos'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FotoInstituicaoManager()

    def __str__(self):
        return self.posicao

    class Meta:
        verbose_name = 'Foto da Instituição/Site'
        verbose_name_plural = 'Fotos da Instituição/Site'
        ordering = ['criado_em']


class MembroManager(models.Manager):
    pass

class Membro(models.Model):

    nome = models.CharField('Nome', max_length=100)
    funcao = models.CharField('Função', max_length=100)

    imagem = models.ImageField(
        verbose_name='Foto do Membro da Equipe'
    )

    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, 
        verbose_name='Instituição', related_name='membros'
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    objects = MembroManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Membros da Equipe'
        ordering = ['nome']
