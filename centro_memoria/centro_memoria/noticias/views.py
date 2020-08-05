from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, FotoNoticia
from centro_memoria.instituicao.models import Instituicao

def noticias(request):
    instituicao = get_object_or_404(Instituicao)
    noticias = Noticia.objects.all().filter(ativo=True).order_by('-criado_em')
    fotos_noticias_destaque = FotoNoticia.objects.all().filter(noticia__in=noticias, destaque=True)
    template_name = 'noticias.html'
    context = {
        'noticias': noticias,
        'fotos_noticias_destaque': fotos_noticias_destaque,
        'instituicao': instituicao
    }
    return render(request, template_name, context)

def noticia_detalhes(request, titulo):
    instituicao = get_object_or_404(Instituicao)
    noticia = get_object_or_404(Noticia, titulo__iexact=titulo)
    foto_noticia = FotoNoticia.objects.all().filter(noticia=noticia, destaque=True)

    outras_noticias = Noticia.objects.all().filter(ativo=True, destaque=True).exclude(pk=noticia.pk).order_by('-criado_em')
    if len(outras_noticias) > 0:
        outras_noticias = outras_noticias[:6]
    fotos_outras_noticias = FotoNoticia.objects.all().filter(noticia__in=outras_noticias, destaque=True)

    template_name = 'noticia_detalhes.html'
    context = {
        'noticia': noticia,
        'foto_noticia': foto_noticia,
        'instituicao': instituicao,
        'outras_noticias': outras_noticias,
        'fotos_outras_noticias': fotos_outras_noticias
    }
    return render(request, template_name, context)