from django.shortcuts import render, get_object_or_404, redirect
from centro_memoria.instituicao.models import Instituicao
from .models import ItemAcervo, CategoriaAcervo, FotoItemAcervo
from django.db.models import Q
from .forms import PesquisaForm

def categorias_acervo(request):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    categorias = CategoriaAcervo.objects.all().filter(categoria_pai__isnull=True)
    template_name = 'categorias_acervo.html'
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            pesquisa = form.save()
            return redirect('acervo:pesquisa', parametro=pesquisa)
    else:
        form = PesquisaForm()
    context = {
        'instituicao': instituicao,
        'categorias': categorias,
        'form': form
    }
    return render(request, template_name, context)

def categoria_detalhes(request, nome_categoria):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    categoria = get_object_or_404(CategoriaAcervo, nome=nome_categoria)
    categorias_filhas = CategoriaAcervo.objects.all().filter(categoria_pai=categoria)
    itens_acervo = ItemAcervo.objects.all().filter(categorias=categoria)
    fotos_itens_destaque = FotoItemAcervo.objects.all().filter(item_acervo__in=itens_acervo, destaque=True)
    context = {
        'instituicao': instituicao,
        'categoria': categoria,
        'categorias_filhas': categorias_filhas,
        'itens_acervo': itens_acervo,
        'fotos_itens_destaque': fotos_itens_destaque
    }
    template_name = 'itens_categoria.html'
    return render(request, template_name, context)

def item_detalhes(request, nome_item):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    item = get_object_or_404(ItemAcervo, nome=nome_item)
    fotos_item = FotoItemAcervo.objects.all().filter(item_acervo=item)
    context = {
        'instituicao': instituicao,
        'item': item,
        'fotos_item': fotos_item
    }
    template_name = 'info_item.html'
    return render(request, template_name, context)

def acervo_pesquisa(request, parametro):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    categorias_acervo = CategoriaAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro))
    itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro) | Q(fundo__unaccent__icontains=parametro) |
                    Q(data__icontains=parametro))
    fotos_itens_destaque = FotoItemAcervo.objects.all().filter(item_acervo__in=itens_acervo, destaque=True)
    context = {
        'instituicao': instituicao,
        'categorias_acervo': categorias_acervo,
        'itens_acervo': itens_acervo,
        'fotos_itens_destaque': fotos_itens_destaque
    }
    template_name = 'itens_pesquisa.html'
    return render(request, template_name, context)