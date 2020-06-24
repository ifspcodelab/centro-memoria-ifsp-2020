from django import forms
from django.core.mail import send_mail
from django.conf import settings

class FormVisita(forms.Form):
    nome = forms.CharField(label='Nome do visitante ou do responsável*', max_length=50)
    instituicao = forms.CharField(required=False, label='Instituição', max_length=150)
    estado = forms.CharField(label='Estado*', max_length=50)
    cidade = forms.CharField(label='Cidade*', max_length=50)
    email= forms.EmailField(label='Email para contato*')
    telefone = forms.CharField(label='Telefone para contato*', max_length=50)
    data_visita = forms.CharField(label='Data da visita (somente às quarta-feiras)*', max_length=50)
    periodo = forms.CharField(label='Período*', max_length=50)
    total_visitantes = forms.IntegerField(label='Total de visitantes*')
    areas_visita = forms.CharField(label='Áreas a serem visitadas*', max_length=50)
    motivo = forms.CharField(label='Motivo da visita*', widget=forms.Textarea)
    informacoes_adicionais = forms.CharField(required=False, label='Informações adicionais', widget=forms.Textarea)
'''
    def send_mail(self, course):
        subject = '[%s] Contato' % course
        message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        template_name = 'contact_email.html'
        send_main_template(subject, template_name, context, [settings.CONTACT_EMAIL])
'''