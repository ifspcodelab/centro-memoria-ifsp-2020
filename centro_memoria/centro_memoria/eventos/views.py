from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, FotoEvento
from centro_memoria.instituicao.models import Instituicao

def eventos(request):
    instituicao = get_object_or_404(Instituicao)
    template_name = 'eventos.html'

    eventos = []
    for evento in Evento.objects.all().filter(ativo=True).order_by('-criado_em'):
        fotos_eventos_destaque = FotoEvento.objects.all().filter(evento=evento, destaque=True)
        if len(fotos_eventos_destaque) > 0:
            fotos_eventos_destaque = fotos_eventos_destaque[0]
        else:
            fotos_eventos_destaque = None

        evento_detalhes = {
            "evento": evento,
            "foto":fotos_eventos_destaque
        }
        eventos.append(evento_detalhes.copy())

    context = {
        'eventos': eventos,
        'instituicao': instituicao
    }
    return render(request, template_name, context)

def evento_detalhes(request, titulo):
    instituicao = get_object_or_404(Instituicao)
    evento = get_object_or_404(Evento, nome__iexact=titulo)
    foto_evento = FotoEvento.objects.all().filter(evento=evento, destaque=True)
    if len(foto_evento) > 0:
        foto_evento = foto_evento[0]
    else:
        foto_evento = None

    outras_fotos = FotoEvento.objects.all().filter(evento=evento)

    outros_eventos_detalhes= []
    for eventos in Evento.objects.all().filter(ativo=True, destaque=True).exclude(pk=evento.pk).order_by('-criado_em'):
        fotos_outros_eventos = FotoEvento.objects.all().filter(evento=eventos, destaque=True)

        if len(fotos_outros_eventos) > 0:
            fotos_outros_eventos = fotos_outros_eventos[0]
        else:
            fotos_outros_eventos = None
        
        outros_eventos_dicionario= {
            'foto':fotos_outros_eventos,
            'outros_eventos': eventos
        }
        outros_eventos_detalhes.append(outros_eventos_dicionario.copy())

    if len(outros_eventos_detalhes) > 0:
        outros_eventos_detalhes = outros_eventos_detalhes[:6]
    
    template_name = 'evento_detalhes.html'
    context = {
        'evento': evento,
        'fotos': outras_fotos,
        'foto_evento': foto_evento,
        'instituicao': instituicao,
        'outros_eventos': outros_eventos_detalhes,
    }
    return render(request, template_name, context)