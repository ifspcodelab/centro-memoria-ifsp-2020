from django.shortcuts import render, get_object_or_404, redirect
from centro_memoria.instituicao.models import Instituicao
from .models import ItemAcervo, CategoriaAcervo, FotoItemAcervo, DimensaoItemAcervo, Autor
from django.db.models import Q

import sys
if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from .forms import PesquisaForm, PesquisaAvancadaForm

def generateBreadcrumb(categoria):
    breadcrumb = [categoria]
    i = 0
    cat = categoria
    while i == 0:
        if cat.categoria_pai is not None:
            cat_pai = CategoriaAcervo.objects.all().filter(pk=cat.categoria_pai.pk, ativo=True)[0]
            breadcrumb.insert(0, cat_pai)
            cat =  cat_pai
            continue
        i = 1
    return breadcrumb

def getCategoriasPai(itens_acervo):
    categorias_pai = []
    for item in itens_acervo:
        categoria = CategoriaAcervo.objects.all().filter(pk__in=item.categorias.all(), ativo=True)[0]
        categorias_pai.append(categoria)
    return categorias_pai

def redirectPesquisa(request):
    if 'simples' in request.POST:
            form = PesquisaForm(request.POST)
            if form.is_valid():
                pesquisa = form.save()
                return redirect('acervo:pesquisa', parametro=pesquisa.lower())
    elif 'avancado' in request.POST:
        form = PesquisaAvancadaForm(request.POST)
        if form.is_valid():
            pesquisa = form.save()
            return redirect('acervo:pesquisa_avancada', categoria=pesquisa['categoria'].lower(),
                            fundo_colecao=pesquisa['fundo_colecao'].lower(), autor=pesquisa['autor'].lower(),
                            titulo=pesquisa['titulo'].lower(), item=pesquisa['item'].lower(),
                            data=pesquisa['data'], periodo_inicio=pesquisa['periodo_inicio'], periodo_fim=pesquisa['periodo_fim'])


def acervo(request):
    instituicao = get_object_or_404(Instituicao)
    categorias = CategoriaAcervo.objects.all().filter(categoria_pai__isnull=True, ativo=True).order_by('nome')
    template_name = 'acervo.html'
    if request.method == 'POST':
        return redirectPesquisa(request)

    form = PesquisaForm()
    formAvancado = PesquisaAvancadaForm()
    context = {
        'categorias': categorias,
        'form': form,
        'formAvancado': formAvancado,
        'instituicao': instituicao
    }
    return render(request, template_name, context)

def acervo_categoria(request, nome_categoria):
    instituicao = get_object_or_404(Instituicao)
    categoria = get_object_or_404(CategoriaAcervo, nome__iexact=nome_categoria, ativo=True)
    categorias_filhas = CategoriaAcervo.objects.all().filter(categoria_pai=categoria, ativo=True).order_by('nome')
    itens_acervo = ItemAcervo.objects.all().filter(categorias=categoria, ativo=True).order_by('tipo_documento', 'data_inicio')
    fotos_itens_destaque = FotoItemAcervo.objects.order_by('item_acervo__pk').filter(item_acervo__in=itens_acervo, destaque=True).distinct('item_acervo')

    breadcrumb = generateBreadcrumb(categoria)

    context = {
        'categoria': categoria,
        'categorias_filhas': categorias_filhas,
        'itens_acervo': itens_acervo,
        'fotos_itens_destaque': fotos_itens_destaque,
        'instituicao': instituicao,
        'breadcrumb': breadcrumb
    }
    template_name = 'acervo_categoria.html'
    return render(request, template_name, context)

def item_detalhe(request, nome_categoria, nome_item):
    instituicao = get_object_or_404(Instituicao)
    categoria = get_object_or_404(CategoriaAcervo, nome__iexact=nome_categoria)
    item = get_object_or_404(ItemAcervo, nome__iexact=nome_item, categorias=categoria, ativo=True)
    foto_destaque = FotoItemAcervo.objects.order_by('item_acervo__pk').filter(item_acervo=item, destaque=True).distinct('item_acervo')
    fotos_item = FotoItemAcervo.objects.all().filter(item_acervo=item)
    dimensoes = DimensaoItemAcervo.objects.all().filter(item_acervo=item)

    breadcrumb = generateBreadcrumb(categoria)

    context = {
        'item': item,
        'foto_destaque': foto_destaque,
        'fotos_item': fotos_item,
        'instituicao': instituicao,
        'breadcrumb': breadcrumb,
        'dimensoes': dimensoes
    }
    template_name = 'acervo_item_detalhe.html'
    return render(request, template_name, context)

def acervo_pesquisa(request, parametro):
    if request.method == 'POST':
        return redirectPesquisa(request)

    form = PesquisaForm()
    formAvancado = PesquisaAvancadaForm()
    instituicao = Instituicao.objects.get()
    categorias = CategoriaAcervo.objects.all().filter(nome__unaccent__icontains=parametro, ativo=True)
    itens_acervo = []
    if len(categorias) > 0:
        itens_acervo += ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                Q(descricao_curta__unaccent__icontains=parametro) | Q(descricao_longa__unaccent__icontains=parametro) |
                Q(titulo__unaccent__icontains=parametro) | Q(fundo_colecao__nome__unaccent__icontains=parametro) |
                Q(data_inicio__icontains=parametro) | Q(categorias__in=categorias), ativo=True)
    else:
        itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                        Q(descricao_curta__unaccent__icontains=parametro) | Q(descricao_longa__unaccent__icontains=parametro) |
                        Q(titulo__unaccent__icontains=parametro) | Q(fundo_colecao__nome__unaccent__icontains=parametro) |
                        Q(data_inicio__icontains=parametro), ativo=True)

    categorias_pai = getCategoriasPai(itens_acervo)

    breadcrumbs = []
    for categoria in categorias_pai:
        breadcrumbs.append(generateBreadcrumb(categoria))

    context = {
        'instituicao': instituicao,
        'itens_acervo': itens_acervo,
        'form': form,
        'formAvancado': formAvancado,
        'categorias_pai': categorias_pai,
        'breadcrumbs': breadcrumbs
    }
    template_name = 'acervo_resultado_busca.html'
    return render(request, template_name, context)

def acervo_pesquisa_avancada(request, categoria, fundo_colecao, autor, titulo, item, data, periodo_inicio, periodo_fim):
    if request.method == 'POST':
        return redirectPesquisa(request)

    form = PesquisaForm()
    formAvancado = PesquisaAvancadaForm()
    instituicao = Instituicao.objects.get()
    if ((categoria == 'none' and autor == 'none' and fundo_colecao == 'none'and titulo == 'none') and
            (item == 'none' and data == 'none' and periodo_inicio == 'none' and periodo_fim == 'none')):
        itens_acervo = []
    else:
        itens_acervo = ItemAcervo.objects.all().filter(ativo=True)
        if categoria != 'none':
            categoria = CategoriaAcervo.objects.all().filter(nome__unaccent__icontains = categoria, ativo=True)
            if len(categoria) > 0:
                itens_acervo = itens_acervo.filter(categorias__in = categoria)
        if autor != 'none':
            autores = Autor.objects.all().filter(nome__unaccent__icontains = autor)
            if len(autores) > 0:
                itens_acervo = itens_acervo.filter(autores__in = autores)
        if fundo_colecao != 'none':
            itens_acervo = itens_acervo.filter(fundo_colecao__nome__unaccent__icontains = fundo_colecao)
        if titulo != 'none':
            itens_acervo = itens_acervo.filter(titulo__unaccent__icontains = titulo)
        if item != 'none':
            itens_acervo = itens_acervo.filter(nome__unaccent__icontains = item)
        if data != 'none':
            itens_acervo = itens_acervo.filter(data_inicio__icontains = data)
        if periodo_inicio != 'none':
            itens_acervo = itens_acervo.filter(data_inicio__range = [periodo_inicio, '9999-12-31'])
        if periodo_fim != 'none':
            itens_acervo = itens_acervo.filter(data_inicio__range = ['0001-01-01', periodo_fim])

    categorias_pai = getCategoriasPai(itens_acervo)

    breadcrumbs = []
    for categoria in categorias_pai:
        breadcrumbs.append(generateBreadcrumb(categoria))

    context = {
        'instituicao': instituicao,
        'itens_acervo': itens_acervo,
        'categoria': categoria,
        'form': form,
        'formAvancado': formAvancado,
        'categorias_pai': categorias_pai,
        'breadcrumbs': breadcrumbs
    }
    template_name = 'acervo_resultado_busca.html'
    return render(request, template_name, context)
