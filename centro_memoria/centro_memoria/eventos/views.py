from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, FotoEvento
from centro_memoria.instituicao.models import Instituicao

def eventos(request):
    instituicao = get_object_or_404(Instituicao)
    eventos = Evento.objects.all().filter(ativo=True).order_by('-criado_em')
    fotos_eventos_destaque = FotoEvento.objects.all().filter(evento__in=eventos, destaque=True)
    template_name = 'eventos.html'
    context = {
        'eventos': eventos,
        'fotos_eventos_destaque': fotos_eventos_destaque,
        'instituicao': instituicao
    }
    return render(request, template_name, context)

def evento_detalhes(request, titulo):
    instituicao = get_object_or_404(Instituicao)
    evento = get_object_or_404(Evento, nome__iexact=titulo)
    foto_evento = FotoEvento.objects.all().filter(evento=evento, destaque=True)

    outros_eventos = Evento.objects.all().filter(ativo=True, destaque=True).exclude(pk=evento.pk).order_by('-criado_em')
    if len(outros_eventos) > 0:
        outros_eventos = outros_eventos[:6]
    fotos_outros_eventos = FotoEvento.objects.all().filter(evento__in=outros_eventos, destaque=True)

    template_name = 'evento_detalhes.html'
    context = {
        'evento': evento,
        'foto_evento': foto_evento,
        'instituicao': instituicao,
        'outros_eventos': outros_eventos,
        'fotos_outros_eventos': fotos_outros_eventos
    }
    return render(request, template_name, context)