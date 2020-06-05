from django.contrib import admin
from .models import Diretor, FotoDiretor

class DiretorAdmin(admin.ModelAdmin):

    list_display = ['nome', 'sobre', 'inicio_direcao', 'fim_direcao', 'criado_em', 'atualizado_em']
    search_fields = ['nome', 'inicio_direcao', 'fim_direcao', 'criado_em', 'atualizado_em']
    list_filter = ['nome', 'inicio_direcao', 'fim_direcao']

class FotoDiretorAdmin(admin.ModelAdmin):

    list_display = ['diretor', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['diretor', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['diretor', 'destaque']


admin.site.register(Diretor, DiretorAdmin)
admin.site.register(FotoDiretor, FotoDiretorAdmin)