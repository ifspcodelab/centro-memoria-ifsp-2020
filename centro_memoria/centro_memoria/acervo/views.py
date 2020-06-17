from django.shortcuts import render, get_object_or_404
from centro_memoria.instituicao.models import Instituicao
from .models import ItemAcervo, CategoriaAcervo, FotoItemAcervo

def categorias_acervo(request):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    categorias = CategoriaAcervo.objects.filter(categoria_pai__isnull=True)
    context = {
        'instituicao': instituicao,
        'categorias': categorias
    }
    template_name = 'categorias_acervo.html'
    return render(request, template_name, context)

def categoria_detalhes(request, categoria):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    categorias_filhas = get_object_or_404(CategoriaAcervo, categoria_pai=categoria)
    itens_acervo = get_object_or_404(ItemAcervo, categorias__in=categoria)
    fotos_itens_destaque = FotoItemAcervo.objects.filter(item_acervo__in=itens_acervo, destaque=True)
    context = {
        'instituicao': instituicao,
        'categoria': categoria,
        'categorias_filhas': categorias_filhas,
        'itens_acervo': itens_acervo,
        'fotos_itens_destaque': fotos_itens_destaque
    }
    template_name = 'personalidades_galeria.html'
    return render(request, template_name, context)

def item_detalhes(request, categoria, item):
    instituicao = Instituicao.objects.all().order_by('-created_at')[0]
    fotos_item = FotoItemAcervo.objects.filter(item_acervo=item)
    context = {
        'instituicao': instituicao,
        'categoria': categoria,
        'item': item,
        'fotos_item': fotos_item
    }
    template_name = 'info_item.html'
    return render(request, template_name, context)