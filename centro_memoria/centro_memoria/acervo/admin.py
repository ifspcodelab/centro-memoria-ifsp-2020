from django.contrib import admin
from .models import ItemAcervo, FotoItemAcervo, CategoriaAcervo, Dimensao, DimensaoItemAcervo

class DimensaoItemAcervoAdmin(admin.TabularInline):
    model = DimensaoItemAcervo
    autocomplete_fields = ['dimensao']
    extra = 1

class ItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao', 'data', 'fundo', 'id_acervo']
    search_fields = ['nome', 'ativo', 'descricao', 'data', 'fundo', 'id_acervo', 'categorias__nome']
    list_filter = ['nome', 'ativo', 'data', 'fundo', 'id_acervo']
    autocomplete_fields = ['categorias']
    inlines = [DimensaoItemAcervoAdmin,]


class FotoItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['item_acervo', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['item_acervo__nome', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['item_acervo', 'destaque']
    autocomplete_fields = ['item_acervo']


class CategoriaAcervoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao', 'categoria_pai']
    search_fields = ['nome', 'ativo', 'descricao', 'categoria_pai__nome']
    list_filter = ['nome', 'ativo', 'categoria_pai']
    autocomplete_fields = ['categoria_pai']

class DimensaoAdmin(admin.ModelAdmin):

    list_display = ['tipo']
    search_fields = ['tipo']
    list_filter = ['tipo']


admin.site.register(ItemAcervo, ItemAcervoAdmin)
admin.site.register(FotoItemAcervo, FotoItemAcervoAdmin)
admin.site.register(CategoriaAcervo, CategoriaAcervoAdmin)
admin.site.register(Dimensao, DimensaoAdmin)