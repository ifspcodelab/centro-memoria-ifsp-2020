from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, FotoNoticia
from centro_memoria.instituicao.models import Instituicao

def noticias(request):
    instituicao = get_object_or_404(Instituicao)
    noticias = []

    for noticia in Noticia.objects.all().filter(ativo=True).order_by('-criado_em'):
        fotos = FotoNoticia.objects.all().filter(noticia=noticia, destaque=True)
        if len(fotos) > 0:
            foto_noticia = fotos[0]
        else:
            foto_noticia = None
        
        noticia_detalhes = {
            'noticia': noticia,
             'foto': foto_noticia
             }        
        noticias.append(noticia_detalhes.copy())

    template_name = 'noticias.html'
    context = {
        'noticias': noticias,
        'instituicao': instituicao
    }
    return render(request, template_name, context)

def noticia_detalhes(request, titulo):
    instituicao = get_object_or_404(Instituicao)
    noticia = get_object_or_404(Noticia, titulo__iexact=titulo)
    foto_noticia = FotoNoticia.objects.all().filter(noticia=noticia, destaque=True)
    outras_noticias = Noticia.objects.all().filter(ativo=True, destaque=True).exclude(pk=noticia.pk).order_by('-criado_em')
    foto_noticias = FotoNoticia.objects.all().filter(noticia=noticia)
    if (len(foto_noticia) > 0 ):
        foto_noticia = foto_noticia[0]
    else:
        foto_noticia = None

    outras_noticas = []
    for outra_noticia in outras_noticias:
        fotos_outras_noticias = FotoNoticia.objects.all().filter(noticia=outra_noticia, destaque=True)
        if len(fotos_outras_noticias) > 0:
            fotos_outras_noticias = fotos_outras_noticias[0]
        else:
            fotos_outras_noticias = None

        outras_noticas_detalhes = {
            'noticia': outra_noticia,
            'foto': fotos_outras_noticias
            }
        outras_noticas.append(outras_noticas_detalhes.copy())

    if len(outras_noticias) > 0:
        outras_noticias = outras_noticias[:6]

    template_name = 'noticia_detalhes.html'
    context = {
        'noticia': noticia,
        'foto_noticia': foto_noticia,
        'outras_fotos': foto_noticias,
        'instituicao': instituicao,
        'outras_noticias': outras_noticas
    }
    return render(request, template_name, context)