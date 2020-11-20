from django.contrib import admin
from .models import GrupoPesquisa, FotoGrupoPesquisa, Membro

class GrupoPesquisaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'descricao', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'descricao', 'texto_livre']
    list_filter = ['nome', 'descricao', 'criado_em', 'atualizado_em']


class FotoGrupoPesquisaAdmin(admin.ModelAdmin):

    list_display = ['grupo_pesquisa', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['grupo_pesquisa', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['grupo_pesquisa__nome']
    autocomplete_fields = ['grupo_pesquisa']


class MembroManagerAdmin(admin.ModelAdmin):

    list_display = ['nome', 'funcao', 'descricao', 'grupo_pesquisa']
    search_fields = ['nome', 'funcao', 'descricao', 'grupo_pesquisa']
    list_filter = ['nome', 'grupo_pesquisa__nome']
    autocomplete_fields = ['grupo_pesquisa']

admin.site.register(GrupoPesquisa, GrupoPesquisaAdmin)
admin.site.register(FotoGrupoPesquisa, FotoGrupoPesquisaAdmin)
admin.site.register(Membro, MembroManagerAdmin)