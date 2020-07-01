from django import forms
from django.core.mail import send_mail
from django.conf import settings
from localflavor.br.br_states import STATE_CHOICES
from .utils import GeoAPI, GeradorDinamico

class FormVisita(forms.Form):

    DATAS_VISITAS = GeradorDinamico.gerarDatasVisita()

    PERIODOS = GeradorDinamico.gerarPeriodoVisita()

    AREAS = GeradorDinamico.gerarAreasVisita()

    ESTADOS = GeoAPI.getEstado()

    CIDADES = (
        ('', 'Selecione um Estado'),
    )

    nome = forms.CharField(label='Nome do visitante ou do responsável*', max_length=50)
    instituicao = forms.CharField(required=False, label='Instituição', max_length=150)
    estado = forms.ChoiceField(label='Estado*', choices=ESTADOS, widget=forms.Select(attrs={"onChange": 'getCidade()'}))
    cidade = forms.ChoiceField(label='Cidade*', choices=CIDADES)
    email = forms.EmailField(label='Email para contato*')
    telefone = forms.CharField(label='Telefone para contato*', max_length=50)
    data_visita = forms.ChoiceField(label='Data da visita*', choices=DATAS_VISITAS)
    periodo = forms.ChoiceField(label='Período*', choices=PERIODOS)
    total_visitantes = forms.IntegerField(label='Total de visitantes*')
    areas_visita = forms.MultipleChoiceField(label='Áreas a serem visitadas*', choices=AREAS, widget=forms.CheckboxSelectMultiple)
    motivo = forms.CharField(label='Motivo da visita*', widget=forms.Textarea)
    informacoes_adicionais = forms.CharField(required=False, label='Informações adicionais', widget=forms.Textarea)

    def confirmarAgendamento(self):
        # e-mail para o cliente
        send_mail('Obrigado por Agendar uma Visita!',
        'Olá' + self.cleaned_data['nome'] + ', seu agendamento já foi enviado, e um e-mail de retorno será enviado em breve',
        'teste@gmail.com',
        [self.cleaned_data['email']],
        fail_silently=True)

        # e-mail para administração
        send_mail('Agendamento de Visita',
        'Novo agendamento de visita:' + self.cleaned_data['nome'] + self.cleaned_data['instituicao'] + 
        self.cleaned_data['estado'] + self.cleaned_data['cidade'] + self.cleaned_data['email'] + self.cleaned_data['telefone'] +
        self.cleaned_data['data_visita'] + self.cleaned_data['periodo'] + 
        str(self.cleaned_data['total_visitantes']) + str(self.cleaned_data['areas_visita']) + self.cleaned_data['motivo'] + self.cleaned_data['informacoes_adicionais'],
        'teste@gmail.com',
        ['teste@gmail.com'],
        fail_silently=True)


class FormFaleConosco(forms.Form):

    ESTADOS = GeoAPI.getEstado()

    CIDADES = (
        ('', 'Selecione um Estado'),
    )

    nome = forms.CharField(label='Nome do visitante ou do responsável*', max_length=50)
    email = forms.EmailField(label='Email para contato*')
    estado = forms.ChoiceField(label='Estado*', choices=ESTADOS, widget=forms.Select(attrs={"onChange": 'getCidade()'}))
    cidade = forms.ChoiceField(label='Cidade*', choices=CIDADES)
    mensagem = forms.CharField(label='Mensagem*', widget=forms.Textarea)

    def enviarMensagem(self):
        # e-mail para o cliente
        send_mail('Obrigado por enviar sua mensagem!',
        'Olá ' + self.cleaned_data['nome'] + ', sua mensagem já foi recebida, e um e-mail de retorno será enviado em breve',
        'teste@gmail.com',
        [self.cleaned_data['email']],
        fail_silently=True)

        # e-mail para administração
        send_mail('Fale Conosco',
        'Fale Conosco: ' + self.cleaned_data['nome'] + self.cleaned_data['estado'] +
        self.cleaned_data['cidade'] + self.cleaned_data['email'] + self.cleaned_data['mensagem'],
        'teste@gmail.com',
        ['teste@gmail.com'],
        fail_silently=True)