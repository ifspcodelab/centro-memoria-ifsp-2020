from django.shortcuts import render, get_object_or_404
from .models import Acontecimento, FotoAcontecimento, LinhaDoTempo
from centro_memoria.instituicao.models import Instituicao
from django.template.defaulttags import register

def timeline(request, titulo_linha_do_tempo):
    instituicao = get_object_or_404(Instituicao)
    linhaDoTempo = get_object_or_404(LinhaDoTempo, titulo__iexact=titulo_linha_do_tempo, ativo=True)
    acontecimentos = Acontecimento.objects.all().filter(linha_do_tempo=linhaDoTempo, ativo=True)
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
        'instituicao': instituicao,
        'linha_do_tempo':linhaDoTempo
    }
    return render(request, template_name, context)

def linha_do_tempo(request):
    instituicao = get_object_or_404(Instituicao)
    linhasDoTempo = LinhaDoTempo.objects.all().filter(ativo=True)
    context = {
        'linhasDoTempo':linhasDoTempo,
        'instituicao':instituicao
    }
    template_name = 'linhas-do-tempo.html'

    return render(request, template_name, context)

def acontecimento_detalhes(request, titulo_linha_do_tempo, titulo_acontecimento):
    instituicao = get_object_or_404(Instituicao)
    linhaDoTempo = get_object_or_404(LinhaDoTempo, titulo__iexact=titulo_linha_do_tempo, ativo=True)
    acontecimento = get_object_or_404(Acontecimento, titulo__iexact=titulo_acontecimento, ativo=True)
    images = FotoAcontecimento.objects.all().filter(acontecimento=acontecimento)
    fotoDestaque = FotoAcontecimento
    if len(images) > 0:
        fotoDestaque = images[0]
    else:
        images = None
        fotoDestaque = None

    context = {
        'instituicao': instituicao,
        'linhaDoTempo': linhaDoTempo,
        'acontecimento': acontecimento,
        'fotos': images,
        'fotoDestaque':fotoDestaque
    }
    template_name = 'timeline-saiba-mais.html'

    return render(request, template_name, context)