from django.contrib import admin
from .models import Evento, FotoEvento

class EventoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'data_inicio', 'data_fim', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'ativo', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'data_inicio','ativo']

class FotoEventoAdmin(admin.ModelAdmin):

    list_display = ['evento', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['evento', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['evento__nome', 'destaque']
    autocomplete_fields = ['evento']


admin.site.register(Evento, EventoAdmin)
admin.site.register(FotoEvento, FotoEventoAdmin)