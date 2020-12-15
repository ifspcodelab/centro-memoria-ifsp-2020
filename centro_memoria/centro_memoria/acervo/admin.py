from django.contrib import admin
from .models import (ItemAcervo, FotoItemAcervo, CategoriaAcervo, Dimensao,
                    DimensaoItemAcervo, Abordagem, TipoFormato, TipoSuporte,
                    TecnicaRegistro, FundoColecao, Idioma,
                    FormaDocumento, Periodicidade, TipoReproducao,
                    ProblemaConservacao, AtividadeEvento, Autor,
                    ProdutorInstituicao, Editora, TipoDocumento)

class DimensaoItemAcervoAdmin(admin.TabularInline):
    model = DimensaoItemAcervo
    autocomplete_fields = ['dimensao']
    extra = 1

class ItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ativo', 'descricao_curta', 'data_inicio', 'notacao']
    search_fields = ['titulo', 'ativo', 'descricao_curta', 'data_inicio',
                    'notacao', 'categorias__nome', 'fundo_colecao__nome', 'abordagem__tipo',
                    'autores__nome', 'produtor_instituicao__nome', 'tecnica_registro__nome',
                    'suporte__nome', 'formato__nome', 'idiomas__idioma', 'forma__forma',
                    'periodicidade__periodo', 'reproducao__tipo', 'problemas_conservacao__problema',
                    'atividades_eventos__atividade', 'editora__nome', 'tipo_documento__tipo']
    list_filter = ['titulo', 'ativo', 'data_inicio', 'notacao']
    autocomplete_fields = ['categorias', 'fundo_colecao', 'abordagem', 'produtor_instituicao', 'autores',
                            'tecnica_registro', 'suporte', 'formato', 'idiomas', 'forma', 'periodicidade',
                            'reproducao', 'problemas_conservacao', 'atividades_eventos', 'editora', 'tipo_documento']
    inlines = [DimensaoItemAcervoAdmin,]


class FotoItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['item_acervo', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['item_acervo__nome', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['item_acervo', 'destaque']
    autocomplete_fields = ['item_acervo']


class CategoriaAcervoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao_curta', 'categoria_pai']
    search_fields = ['nome', 'ativo', 'descricao_curta', 'categoria_pai__nome']
    list_filter = ['nome', 'ativo', 'categoria_pai']
    autocomplete_fields = ['categoria_pai']

class DimensaoAdmin(admin.ModelAdmin):

    list_display = ['tipo']
    search_fields = ['tipo']
    list_filter = ['tipo']

class AbordagemAdmin(admin.ModelAdmin):

    list_display = ['tipo']
    search_fields = ['tipo']
    list_filter = ['tipo']

class TipoDocumentoAdmin(admin.ModelAdmin):

    list_display = ['tipo']
    search_fields = ['tipo']
    list_filter = ['tipo']

class TipoFormatoAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class TipoSuporteAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class TecnicaRegistroAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class FundoColecaoAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class IdiomaAdmin(admin.ModelAdmin):

    list_display = ['idioma']
    search_fields = ['idioma']
    list_filter = ['idioma']

class FormaDocumentoAdmin(admin.ModelAdmin):

    list_display = ['forma']
    search_fields = ['forma']
    list_filter = ['forma']

class PeriodicidadeAdmin(admin.ModelAdmin):

    list_display = ['periodo']
    search_fields = ['periodo']
    list_filter = ['periodo']

class TipoReproducaoAdmin(admin.ModelAdmin):

    list_display = ['tipo']
    search_fields = ['tipo']
    list_filter = ['tipo']

class ProblemaConservacaoAdmin(admin.ModelAdmin):

    list_display = ['problema']
    search_fields = ['problema']
    list_filter = ['problema']

class AtividadeEventoAdmin(admin.ModelAdmin):

    list_display = ['atividade', 'local', 'data_inicio', 'data_fim']
    search_fields = ['atividade', 'local', 'data_inicio', 'data_fim']
    list_filter = ['atividade', 'local', 'data_inicio', 'data_fim']

class AutorAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class ProdutorInstituicaoAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

class EditoraAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

admin.site.register(ItemAcervo, ItemAcervoAdmin)
admin.site.register(FotoItemAcervo, FotoItemAcervoAdmin)
admin.site.register(CategoriaAcervo, CategoriaAcervoAdmin)
admin.site.register(Dimensao, DimensaoAdmin)
admin.site.register(Abordagem, AbordagemAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(TipoFormato, TipoFormatoAdmin)
admin.site.register(TipoSuporte, TipoSuporteAdmin)
admin.site.register(TecnicaRegistro, TecnicaRegistroAdmin)
admin.site.register(FundoColecao, FundoColecaoAdmin)
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(FormaDocumento, FormaDocumentoAdmin)
admin.site.register(Periodicidade, PeriodicidadeAdmin)
admin.site.register(TipoReproducao, TipoReproducaoAdmin)
admin.site.register(ProblemaConservacao, ProblemaConservacaoAdmin)
admin.site.register(AtividadeEvento, AtividadeEventoAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(ProdutorInstituicao, ProdutorInstituicaoAdmin)
admin.site.register(Editora, EditoraAdmin)