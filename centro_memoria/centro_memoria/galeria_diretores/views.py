from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import Personalidade, Galeria, FotoPersonalidade

def galerias(request):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    galerias = Galeria.objects.all().filter(ativo=True)
    context = {
        'instituicao': instituicao,
        'galerias': galerias
    }
    template_name = 'galeria_index.html'
    return render(request, template_name, context)

def personalidades_galeria(request, nome_galeria):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    galeria = get_object_or_404(Galeria, nome=nome_galeria, ativo=True)
    personalidades = Personalidade.objects.all().filter(galerias=galeria, ativo=True)
    fotos_personalidades_destaque = FotoPersonalidade.objects.all().filter(personalidade__in=personalidades, 
                                                                    destaque=True)
    context = {
        'instituicao': instituicao,
        'galeria': galeria,
        'personalidades': personalidades,
        'fotos_personalidades_destaque': fotos_personalidades_destaque
    }
    template_name = 'personalidades_galeria.html'
    return render(request, template_name, context)

def personalidade_detalhes(request, nome_personalidade):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    personalidade = get_object_or_404(Personalidade, nome=nome_personalidade, ativo=True)
    fotos_personalidade = FotoPersonalidade.objects.all().filter(personalidade=personalidade)
    context = {
        'instituicao': instituicao,
        'personalidade': personalidade,
        'fotos_personalidade': fotos_personalidade
    }
    template_name = 'info_personalidade.html'
    return render(request, template_name, context)
