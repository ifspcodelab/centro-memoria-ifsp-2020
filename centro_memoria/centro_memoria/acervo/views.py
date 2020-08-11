from django.shortcuts import render, get_object_or_404, redirect
from centro_memoria.instituicao.models import Instituicao
from .models import ItemAcervo, CategoriaAcervo, FotoItemAcervo
from django.db.models import Q
from .forms import PesquisaForm, PesquisaAvancadaForm

def acervo(request):
    instituicao = get_object_or_404(Instituicao)
    categorias = CategoriaAcervo.objects.all().filter(categoria_pai__isnull=True, ativo=True)
    template_name = 'acervo.html'
    if request.method == 'POST':
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
                                item=pesquisa['item'].lower(), desc=pesquisa['descricao'].lower(), data=pesquisa['data'])
    else:
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
    categorias_filhas = CategoriaAcervo.objects.all().filter(categoria_pai=categoria, ativo=True)
    itens_acervo = ItemAcervo.objects.all().filter(categorias=categoria, ativo=True)
    fotos_itens_destaque = FotoItemAcervo.objects.all().filter(item_acervo__in=itens_acervo, destaque=True)
    context = {
        'categoria': categoria,
        'categorias_filhas': categorias_filhas,
        'itens_acervo': itens_acervo,
        'fotos_itens_destaque': fotos_itens_destaque,
        'instituicao': instituicao
    }
    template_name = 'acervo_categoria.html'
    return render(request, template_name, context)

def item_detalhe(request, nome_item):
    instituicao = get_object_or_404(Instituicao)
    item = get_object_or_404(ItemAcervo, nome__iexact=nome_item, ativo=True)
    foto_destaque = get_object_or_404(FotoItemAcervo, item_acervo=item, destaque=True)
    fotos_item = FotoItemAcervo.objects.all().filter(item_acervo=item)
    context = {
        'item': item,
        'foto_destaque': foto_destaque,
        'fotos_item': fotos_item,
        'instituicao': instituicao
    }
    template_name = 'acervo_item_detalhe.html'
    return render(request, template_name, context)

def acervo_pesquisa(request, parametro):
    instituicao = Instituicao.objects.get()
    itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro) | Q(fundo__unaccent__icontains=parametro) |
                    Q(data__icontains=parametro), ativo=True)
    if request.method == 'POST':
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
                                item=pesquisa['item'].lower(), desc=pesquisa['descricao'].lower(), data=pesquisa['data'])
    else:
        form = PesquisaForm()
        formAvancado = PesquisaAvancadaForm()
    context = {
        'instituicao': instituicao,
        'itens_acervo': itens_acervo,
        'form': form,
        'formAvancado': formAvancado
    }
    template_name = 'acervo_resultado_busca.html'
    return render(request, template_name, context)

def acervo_pesquisa_avancada(request, categoria, item, desc, data):
    instituicao = Instituicao.objects.get()
    itens_acervo = []
    if categoria != 'none':
        categoria = CategoriaAcervo.objects.all().filter(nome__unaccent__icontains=categoria, ativo=True)
        if len(categoria) > 0:
            itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=item) |
                            Q(descricao__unaccent__icontains=desc) | Q(fundo__unaccent__icontains=item) |
                            Q(data__icontains=data) | Q(ativo=True), categorias=categoria[0], ativo=True)
    else:
        itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=item) |
                        Q(descricao__unaccent__icontains=desc) | Q(fundo__unaccent__icontains=item) |
                        Q(data__icontains=data), ativo=True)
    if request.method == 'POST':
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
                                item=pesquisa['item'].lower(), desc=pesquisa['descricao'].lower(), data=pesquisa['data'])
    else:
        form = PesquisaForm()
        formAvancado = PesquisaAvancadaForm()
    context = {
        'instituicao': instituicao,
        'itens_acervo': itens_acervo,
        'form': form,
        'formAvancado': formAvancado
    }
    template_name = 'acervo_resultado_busca.html'
    return render(request, template_name, context)
