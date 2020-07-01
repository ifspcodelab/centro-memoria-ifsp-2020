from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import Personalidade, Galeria, FotoPersonalidade

def galerias(request):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    galerias = Galeria.objects.all()
    context = {
        'instituicao': instituicao,
        'galerias': galerias
    }
    template_name = 'galeria_index.html'
    return render(request, template_name, context)

def personalidades_galeria(request, nome_galeria):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    galeria = get_object_or_404(Galeria, nome=nome_galeria)
    personalidades = Personalidade.objects.all().filter(galerias=galeria)
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

def personalidade_detalhes(request, nome_galeria, nome_personalidade):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    galeria = get_object_or_404(Galeria, nome=nome_galeria)
    personalidade = get_object_or_404(Personalidade, nome=nome_personalidade)
    fotos_personalidade = FotoPersonalidade.objects.all().filter(personalidade=personalidade)
    context = {
        'instituicao': instituicao,
        'galeria': galeria,
        'personalidade': personalidade,
        'fotos_personalidade': fotos_personalidade
    }
    template_name = 'info_personalidade.html'
    return render(request, template_name, context)