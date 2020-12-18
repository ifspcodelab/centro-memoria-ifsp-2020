from django.contrib import admin
from .models import Instituicao, FotoInstituicao, Membro

class InstituicaoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'sobre', 'endereco', 'email']
    search_fields = ['nome', 'sobre', 'endereco', 'email', 'telefone']
    list_filter = ['nome', 'endereco', 'email']


class FotoInstituicaoAdmin(admin.ModelAdmin):

    list_display = ['instituicao', 'criado_em', 'atualizado_em']
    search_fields = ['instituicao', 'criado_em', 'atualizado_em']
    list_filter = ['instituicao__nome']
    autocomplete_fields = ['instituicao']


class MembroAdmin(admin.ModelAdmin):

    list_display = ['nome', 'funcao', 'instituicao']
    search_fields = ['nome', 'funcao', 'instituicao']
    list_filter = ['nome', 'instituicao__nome']
    autocomplete_fields = ['instituicao']


admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(FotoInstituicao, FotoInstituicaoAdmin)
admin.site.register(Membro, MembroAdmin)