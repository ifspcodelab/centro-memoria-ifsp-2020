from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import ItemAcervo, CategoriaAcervo, FotoItemAcervo

def categorias_acervo(request):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    categorias = CategoriaAcervo.objects.all().filter(categoria_pai__isnull=True)
    context = {
        'instituicao': instituicao,
        'categorias': categorias
    }
    template_name = 'categorias_acervo.html'
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

def item_detalhes(request, nome_categoria, nome_item):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    categoria = get_object_or_404(CategoriaAcervo, nome=nome_categoria)
    item = get_object_or_404(ItemAcervo, nome=nome_item)
    fotos_item = FotoItemAcervo.objects.all().filter(item_acervo=item)
    context = {
        'instituicao': instituicao,
        'categoria': categoria,
        'item': item,
        'fotos_item': fotos_item
    }
    template_name = 'info_item.html'
    return render(request, template_name, context)