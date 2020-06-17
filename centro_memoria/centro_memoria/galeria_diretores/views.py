from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import Personalidade, Galeria, FotoPersonalidade

def galerias(request):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    galerias = Galeria.objects.all()
    context = {
        'instituicao': instituicao,
        'galerias': galerias
    }
    template_name = 'galeria_index.html'
    return render(request, template_name, context)

def personalidades_galeria(request, galeria):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    personalidades = get_object_or_404(Personalidade, galeria=galeria)
    fotos_personalidades_destaque = FotoPersonalidade.objects.filter(personalidade__in=personalidades, 
                                                                    destaque=True)
    context = {
        'instituicao': instituicao,
        'galeria': galeria,
        'personalidades': personalidades,
        'fotos_personalidades_destaque': fotos_personalidades_destaque
    }
    template_name = 'personalidades_galeria.html'
    return render(request, template_name, context)

def personalidade_detalhes(request, galeria, personalidade):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    fotos_personalidade = FotoPersonalidade.objects.filter(personalidade=personalidade)
    context = {
        'instituicao': instituicao,
        'galeria': galeria,
        'personalidade': personalidade,
        'fotos_personalidade': fotos_personalidade
    }
    template_name = 'info_personalidade.html'
    return render(request, template_name, context)
