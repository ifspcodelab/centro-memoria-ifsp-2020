'''
from django import forms
from .models import CategoriaAcervo

class DateInput(forms.DateInput):
    input_type = 'date'

class PesquisaForm(forms.Form):

    parametro = forms.CharField(label='', widget=forms.TextInput(
                                            attrs={
                                                'placeholder': 'Digite o item do acervo',
                                                'class': 'form-control'
                                            }))

    def save(self, commit=True):
        return self.cleaned_data['parametro']

class PesquisaAvancadaForm(forms.Form):

    CATEGORIAS = (
        ('', 'Escolha uma categoria'),
    )

    for categoria in CategoriaAcervo.objects.all().filter(ativo=True):
        CATEGORIAS += ((categoria.nome, categoria.nome),)

    item = forms.CharField(required=False, label='Item do acervo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(required=False, label='Descrição do item', widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(required=False, label='Categoria do acervo', widget=forms.Select(choices=CATEGORIAS, attrs={'class': 'form-control'}))
    data = forms.DateField(required=False, label='Data', widget=DateInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        return {
            'item': self.cleaned_data['item'] if self.cleaned_data['item'] else 'none',
            'descricao': self.cleaned_data['descricao'] if self.cleaned_data['descricao'] else 'none',
            'categoria': self.cleaned_data['categoria'] if self.cleaned_data['categoria'] else 'none',
            'data': self.cleaned_data['data'] if self.cleaned_data['data'] else 'none'
        }
'''