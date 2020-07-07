from django.contrib import admin
from .models import ItemAcervo, FotoItemAcervo, CategoriaAcervo

class ItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao', 'data', 'fundo', 'id_acervo']
    search_fields = ['nome', 'ativo', 'descricao', 'data', 'fundo', 'id_acervo']
    list_filter = ['nome', 'ativo', 'data', 'fundo', 'id_acervo']


class FotoItemAcervoAdmin(admin.ModelAdmin):

    list_display = ['item_acervo', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['item_acervo', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['item_acervo', 'destaque']


class CategoriaAcervoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao', 'categoria_pai']
    search_fields = ['nome', 'ativo', 'descricao', 'categoria_pai']
    list_filter = ['nome', 'ativo', 'categoria_pai']


admin.site.register(ItemAcervo, ItemAcervoAdmin)
admin.site.register(FotoItemAcervo, FotoItemAcervoAdmin)
admin.site.register(CategoriaAcervo, CategoriaAcervoAdmin)