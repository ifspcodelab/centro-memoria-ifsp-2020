from django.contrib import admin
from .models import Personalidade, FotoPersonalidade, Galeria

class GaleriaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'descricao', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'ativo', 'descricao', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'ativo', 'descricao', 'criado_em', 'atualizado_em']

class PersonalidadeAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'funcao', 'sobre', 'inicio_servico', 'fim_servico', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'ativo', 'funcao', 'inicio_servico', 'fim_servico', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'ativo', 'inicio_servico', 'fim_servico']

class FotoPersonalidadeAdmin(admin.ModelAdmin):

    list_display = ['personalidade', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['personalidade', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['personalidade', 'destaque']


admin.site.register(Personalidade, PersonalidadeAdmin)
admin.site.register(FotoPersonalidade, FotoPersonalidadeAdmin)
admin.site.register(Galeria, GaleriaAdmin)