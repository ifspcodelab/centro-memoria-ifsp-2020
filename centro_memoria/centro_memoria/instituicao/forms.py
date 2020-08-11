from django import forms
from django.core.mail import send_mail
from django.conf import settings
from localflavor.br.br_states import STATE_CHOICES
from .utils import GeoAPI, GeradorDinamico
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class PesquisaAvancadaForm(forms.Form):

    parametro = forms.CharField(label='Pesquisar um item no Centro de Memória')

    def save(self, commit=True):
        return self.cleaned_data['parametro']

class FormVisita(forms.Form):

    PERIODOS = GeradorDinamico.gerarPeriodoVisita()

    ESTADOS = GeoAPI.getEstado()

    CIDADES = (
        ('', 'Selecione um Estado'),
    )

    nome = forms.CharField(label='Nome completo do visitante',
                            widget=forms.TextInput(attrs={'placeholder': 'Maria Aparecida da Silva'}),max_length=50)
    email = forms.EmailField(label='E-mail para contato',
                            widget=forms.TextInput(attrs={'placeholder': 'maria.cida@email.com'}))
    estado = forms.ChoiceField(label='Estado', choices=ESTADOS, widget=forms.Select(attrs={"onChange": 'getCidade()'}))
    cidade = forms.CharField(label='Cidade', widget=forms.Select(choices=CIDADES))
    data_visita = forms.DateField(label='Data da visita', widget=DateInput)
    instituicao = forms.CharField(label='Instituição', max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': 'Colégio Nossa Senhora das Graças'}))
    periodo = forms.ChoiceField(label='Período', choices=PERIODOS, widget=forms.RadioSelect)
    total_visitantes = forms.IntegerField(label='Total de visitantes')
    motivo = forms.CharField(label='Motivo da visita',
                            widget=forms.Textarea(attrs={'placeholder': 'Coloque aqui porque você gostaria de visitar o Instituito Federal'}))

    def confirmarAgendamento(self, instituicao):

        # e-mail para o cliente
        send_mail('Obrigado por Agendar uma Visita!',
        'Olá ' + self.cleaned_data['nome'].split()[0] + ', seu agendamento já foi enviado, e um e-mail de retorno será enviado em breve',
        instituicao.email_agendamento,
        [self.cleaned_data['email']],
        fail_silently=True)

        # e-mail para administração
        send_mail('Agendamento de Visita',
        'Novo agendamento de visita: ' + self.cleaned_data['nome'] + ' - ' + self.cleaned_data['instituicao'] + ' - ' + 
        self.cleaned_data['estado'] + ' - ' + self.cleaned_data['cidade'] + ' - ' + self.cleaned_data['email'] + ' - ' + 
        str(self.cleaned_data['data_visita']) + ' - ' + self.cleaned_data['periodo'] + ' - ' +
        str(self.cleaned_data['total_visitantes']) + ' - ' + self.cleaned_data['motivo'],
        instituicao.email_agendamento,
        [instituicao.email_agendamento],
        fail_silently=True)


class FormFaleConosco(forms.Form):

    nome = forms.CharField(label='', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='', max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control form-control-lg'}))
    mensagem = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Deixe aqui sua mensagem', 'class': 'mensagem', 'rows': '2', 'cols': '20'}))

    def enviarMensagem(self, instituicao):
        # e-mail para o cliente
        send_mail('Obrigado por enviar sua mensagem!',
        'Olá ' + self.cleaned_data['nome'] + ', sua mensagem já foi recebida, e um e-mail de retorno será enviado em breve',
        instituicao.email_faleconosco,
        [self.cleaned_data['email']],
        fail_silently=True)

        # e-mail para administração
        send_mail('Fale Conosco',
        'Fale Conosco: ' + self.cleaned_data['nome'] + ' - ' + self.cleaned_data['sobrenome'] + ' - ' +
        self.cleaned_data['email'] + ' - ' + self.cleaned_data['mensagem'],
        instituicao.email_faleconosco,
        [instituicao.email_faleconosco],
        fail_silently=True)