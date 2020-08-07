from django.shortcuts import render, get_object_or_404
from .models import Acontecimento, FotoAcontecimento
from centro_memoria.instituicao.models import Instituicao
from django.template.defaulttags import register

def timeline(request):
    instituicao = get_object_or_404(Instituicao)
    acontecimentos = Acontecimento.objects.all().filter(ativo=True).order_by('data')
    marcos = {}
    for acontecimento in acontecimentos:
        foto_acontecimento = FotoAcontecimento.objects.all().filter(acontecimento=acontecimento, destaque=True)
        if len(foto_acontecimento) > 0:
            foto_acontecimento = foto_acontecimento[0]
        else:
            foto_acontecimento = None
        if acontecimento.data in marcos:
            lista_marcos = []
            lista_marcos = marcos[acontecimento.data].copy()
            lista_marcos.append({acontecimento: foto_acontecimento})
            marcos[acontecimento.data] = lista_marcos
        else:
            marcos[acontecimento.data] = [{acontecimento: foto_acontecimento}]
    template_name = 'timeline.html'
    context = {
        'marcos': marcos,
        'instituicao': instituicao
    }
    return render(request, template_name, context)