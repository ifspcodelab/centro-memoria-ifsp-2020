from django.contrib import admin
from .models import Evento, FotoEvento

class EventoAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ativo', 'descricao', 'data', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'ativo', 'data', 'criado_em', 'atualizado_em']
    list_filter = ['titulo', 'ativo', 'data']

class FotoEventoAdmin(admin.ModelAdmin):

    list_display = ['evento', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['evento', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['evento', 'destaque']


admin.site.register(Evento, EventoAdmin)
admin.site.register(FotoEvento, FotoEventoAdmin)