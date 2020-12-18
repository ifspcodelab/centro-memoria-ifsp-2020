from django.contrib import admin
from .models import Acontecimento, FotoAcontecimento, LinhaDoTempo

class AcontecimentoAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ativo', 'descricao', 'data', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'ativo', 'data', 'criado_em', 'atualizado_em']
    list_filter = ['titulo', 'ativo', 'data']

class FotoAcontecimentoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'acontecimento', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['acontecimento', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['acontecimento__titulo', 'destaque']
    autocomplete_fields = ['acontecimento']

class LinhaDoTempoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ativo', 'inicio_periodo', 'fim_periodo', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'ativo',  'inicio_periodo', 'fim_periodo', 'criado_em', 'atualizado_em']
    list_filter = ['titulo', 'ativo', 'inicio_periodo', 'fim_periodo']
    
admin.site.register(Acontecimento, AcontecimentoAdmin)
admin.site.register(FotoAcontecimento, FotoAcontecimentoAdmin)
admin.site.register(LinhaDoTempo, LinhaDoTempoAdmin)