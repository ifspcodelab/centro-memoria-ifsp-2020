from django.shortcuts import render, redirect
from .models import Instituicao
from centro_memoria.acervo.models import CategoriaAcervo, ItemAcervo, FotoItemAcervo
from centro_memoria.galeria_diretores.models import Personalidade, Galeria, FotoPersonalidade
from centro_memoria.noticias.models import Noticia, FotoNoticia
from centro_memoria.linha_tempo.models import Evento, FotoEvento
from django.db.models import Q
from .forms import FormVisita, FormFaleConosco, PesquisaAvancadaForm

def agendamento(request):
    instituicao = Instituicao.objects.get()
    context = {}
    if request.method == 'POST':
        form = FormVisita(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.confirmarAgendamento(instituicao)
            form = FormVisita()
    else:
        form = FormVisita()
    context['form'] = form
    context['instituicao'] = instituicao
    template_name = 'agendamento_visita.html'
    return render(request, template_name, context)

def faleconosco(request):
    instituicao = Instituicao.objects.get()
    context = {}
    if request.method == 'POST':
        form = FormFaleConosco(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.enviarMensagem(instituicao)
            form = FormFaleConosco()
    else:
        form = FormFaleConosco()
    context['form'] = form
    context['instituicao'] = instituicao
    template_name = 'fale_conosco.html'
    return render(request, template_name, context)

def index(request):
    instituicao = Instituicao.objects.get()
    template_name = 'index.html'
    if request.method == 'POST':
        form = PesquisaAvancadaForm(request.POST)
        if form.is_valid():
            pesquisa = form.save()
            return redirect('instituicao:pesquisa', parametro=pesquisa.lower())
    else:
        form = PesquisaAvancadaForm()
    context = {
        'instituicao': instituicao,
        'form': form
    }
    return render(request, template_name, context)

def pesquisa_avancada(request, parametro):
    instituicao = Instituicao.objects.get()
 
    categorias_acervo = CategoriaAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro), ativo=True)
    itens_acervo = ItemAcervo.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro) | Q(fundo__unaccent__icontains=parametro) |
                    Q(data__icontains=parametro), ativo=True)
    fotos_itens_destaque = FotoItemAcervo.objects.all().filter(item_acervo__in=itens_acervo, destaque=True)

    galerias = Galeria.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro), ativo=True)
    personalidades = Personalidade.objects.all().filter(Q(nome__unaccent__icontains=parametro) |
                    Q(funcao__unaccent__icontains=parametro) | Q(sobre__unaccent__icontains=parametro) |
                    Q(inicio_servico__icontains=parametro) | Q(fim_servico__icontains=parametro), 
                    ativo=True)
    fotos_personalidades_destaque = FotoPersonalidade.objects.all().filter(personalidade__in=personalidades, destaque=True)

    eventos = Evento.objects.all().filter(Q(titulo__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro) | Q(data__icontains=parametro),
                    ativo=True)
    fotos_eventos_destaque = FotoEvento.objects.all().filter(evento__in=eventos, destaque=True)

    noticias = Noticia.objects.all().filter(Q(titulo__unaccent__icontains=parametro) |
                    Q(descricao__unaccent__icontains=parametro) | Q(corpo__unaccent__icontains=parametro),
                    ativo=True)
    fotos_noticias_destaque = FotoNoticia.objects.all().filter(noticia__in=noticias, destaque=True)
    context = {
        'instituicao': instituicao,
        'categorias_acervo': categorias_acervo,
        'itens_acervo': itens_acervo,
        'galerias': galerias,
        'personalidades': personalidades,
        'eventos': eventos,
        'noticias': noticias,
        'fotos_itens': fotos_itens_destaque,
        'fotos_personalidades': fotos_personalidades_destaque,
        'fotos_eventos': fotos_eventos_destaque,
        'fotos_noticias': fotos_noticias_destaque
    }
    template_name = 'resultado_pesquisa.html'
    return render(request, template_name, context)