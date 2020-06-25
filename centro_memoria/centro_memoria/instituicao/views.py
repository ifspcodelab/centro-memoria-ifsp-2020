from django.shortcuts import render
from .models import Instituicao
from .forms import FormVisita

def agendamento(request):
    instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
    context = {}
    if request.method == 'POST':
        form = FormVisita(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.confirmarAgendamento()
            form = FormVisita()
    else:
        form = FormVisita()
    context['form'] = form
    context['instituicao'] = instituicao
    template_name = 'agendamento_visita.html'
    return render(request, template_name, context)