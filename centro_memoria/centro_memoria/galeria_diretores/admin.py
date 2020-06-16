from django.contrib import admin
from .models import Personalidade, FotoPersonalidade, Galeria

class GaleriaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'descricao', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'descricao', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'descricao', 'criado_em', 'atualizado_em']

class PersonalidadeAdmin(admin.ModelAdmin):

    list_display = ['nome', 'funcao', 'sobre', 'inicio_servico', 'fim_servico', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'funcao', 'inicio_servico', 'fim_servico', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'inicio_servico', 'fim_servico']

class FotoPersonalidadeAdmin(admin.ModelAdmin):

    list_display = ['personalidade', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['personalidade', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['personalidade', 'destaque']


admin.site.register(Personalidade, PersonalidadeAdmin)
admin.site.register(FotoPersonalidade, FotoPersonalidadeAdmin)
admin.site.register(Galeria, GaleriaAdmin)