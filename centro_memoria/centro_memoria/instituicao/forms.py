from django import forms
from django.core.mail import send_mail
from django.conf import settings

class FormVisita(forms.Form):
    datas_visita =(
        ('', 'Selecione'),
        ("01-07-2020", "01/07/2020"), 
        ("02-07-2020", "02/07/2020"), 
        ("03-07-2020", "03/07/2020"), 
        ("04-07-2020", "04/07/2020"), 
        ("05-07-2020", "05/07/2020"), 
    )

    periodos =(
        ("manhã", "Manhã (das 09h às 12h)"), 
        ("tarde", "Tarde (das 14h às 17h)")
    )

    areas=(
        ('Acervo','Acervo'),
        ('Biblioteca','Biblioteca'),
        ('Coleção','Coleção'),
        ('Museu','Museu'),
    )

    nome = forms.CharField(label='Nome do visitante ou do responsável*', max_length=50)
    instituicao = forms.CharField(required=False, label='Instituição', max_length=150)
    estado = forms.ChoiceField(label='Estado*')
    cidade = forms.ChoiceField(label='Cidade*')
    email = forms.EmailField(label='Email para contato*')
    telefone = forms.CharField(label='Telefone para contato*', max_length=50)
    data_visita = forms.ChoiceField(label='Data da visita*', choices=datas_visita)
    periodo = forms.ChoiceField(label='Período*', choices=periodos)
    total_visitantes = forms.IntegerField(label='Total de visitantes*')
    areas_visita = forms.MultipleChoiceField(label='Áreas a serem visitadas*', choices=areas, widget=forms.CheckboxSelectMultiple)
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
    nome = forms.CharField(label='Nome do visitante ou do responsável*', max_length=50)
    email = forms.EmailField(label='Email para contato*')
    estado = forms.CharField(label='Estado*', max_length=50)
    cidade = forms.CharField(label='Cidade*', max_length=50)
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