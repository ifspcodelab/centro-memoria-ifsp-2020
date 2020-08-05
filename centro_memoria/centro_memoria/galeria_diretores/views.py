from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import Personalidade, Galeria, FotoPersonalidade

def galerias(request):
    instituicao = get_object_or_404(Instituicao)
    galerias = Galeria.objects.all().filter(ativo=True)
    context = {
        'galerias': galerias,
        'instituicao': instituicao
    }
    template_name = 'galerias.html'
    return render(request, template_name, context)

def galeria_detalhes(request, nome_galeria):
    instituicao = get_object_or_404(Instituicao)
    galeria = get_object_or_404(Galeria, nome__iexact=nome_galeria, ativo=True)
    personalidades = Personalidade.objects.all().filter(galerias=galeria, ativo=True)
    fotos_personalidades_destaque = FotoPersonalidade.objects.all().filter(personalidade__in=personalidades, 
                                                                    destaque=True)
    context = {
        'galeria': galeria,
        'personalidades': personalidades,
        'fotos_personalidades_destaque': fotos_personalidades_destaque,
        'instituicao': instituicao
    }
    template_name = 'galeria_detalhes.html'
    return render(request, template_name, context)

def personalidade_detalhes(request, nome_galeria, nome_personalidade):
    instituicao = get_object_or_404(Instituicao)
    personalidade = get_object_or_404(Personalidade, nome__iexact=nome_personalidade, ativo=True)
    fotos_personalidade = FotoPersonalidade.objects.all().filter(personalidade=personalidade)
    foto_destaque = get_object_or_404(FotoPersonalidade, personalidade=personalidade, destaque=True)
    context = {
        'personalidade': personalidade,
        'fotos_personalidade': fotos_personalidade,
        'foto_destaque': foto_destaque,
        'instituicao': instituicao
    }
    template_name = 'personalidade_detalhes.html'
    return render(request, template_name, context)
