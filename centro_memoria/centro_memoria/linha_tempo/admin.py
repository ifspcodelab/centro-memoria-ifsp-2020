from django.contrib import admin
from .models import Acontecimento, FotoAcontecimento

class AcontecimentoAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ativo', 'descricao', 'data', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'ativo', 'data', 'criado_em', 'atualizado_em']
    list_filter = ['titulo', 'ativo', 'data']

class FotoAcontecimentoAdmin(admin.ModelAdmin):

    list_display = ['acontecimento', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['acontecimento', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['acontecimento__titulo', 'destaque']
    autocomplete_fields = ['acontecimento']


admin.site.register(Acontecimento, AcontecimentoAdmin)
admin.site.register(FotoAcontecimento, FotoAcontecimentoAdmin)