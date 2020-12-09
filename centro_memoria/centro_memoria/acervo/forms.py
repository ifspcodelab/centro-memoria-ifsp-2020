from django import forms
from .models import CategoriaAcervo, FundoColecao, Autor

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

    FUNDOS_COLECOES = (
        ('', 'Escolha...'),
    )

    AUTORES = (
        ('', 'Escolha...'),
    )

    for categoria in CategoriaAcervo.objects.all().filter(ativo=True):
        CATEGORIAS += ((categoria.nome, categoria.nome),)

    for fundo in FundoColecao.objects.all():
        FUNDOS_COLECOES += ((fundo.nome, fundo.nome),)

    for autor in Autor.objects.all():
        AUTORES += ((autor.nome, autor.nome),)

    categoria = forms.CharField(required=False, label='Categoria do acervo', widget=forms.Select(choices=CATEGORIAS, attrs={'class': 'form-control'}))
    fundo_colecao = forms.CharField(required=False, label='Fundo/Coleção', widget=forms.Select(choices=FUNDOS_COLECOES, attrs={'class': 'form-control'}))
    autor = forms.CharField(required=False, label='Autor', widget=forms.Select(choices=AUTORES, attrs={'class': 'form-control'}))
    titulo = forms.CharField(required=False, label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    item = forms.CharField(required=False, label='Item do acervo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data = forms.DateField(required=False, label='Data', widget=DateInput(attrs={'class': 'form-control'}))
    periodo_inicio = forms.DateField(required=False, label='De', widget=DateInput(attrs={'class': 'form-control'}))
    periodo_fim = forms.DateField(required=False, label='até', widget=DateInput(attrs={'class': 'form-control'}))

    field_order = ['categoria', 'fundo_colecao', 'autor', 'titulo', 'item', 'data', 'periodo_inicio', 'periodo_fim']
    
    def save(self, commit=True):
        return {
            'categoria': self.cleaned_data['categoria'] if self.cleaned_data['categoria'] else 'none',
            'fundo_colecao': self.cleaned_data['fundo_colecao'] if self.cleaned_data['fundo_colecao'] else 'none',
            'autor': self.cleaned_data['autor'] if self.cleaned_data['autor'] else 'none',
            'titulo': self.cleaned_data['titulo'] if self.cleaned_data['titulo'] else 'none',
            'item': self.cleaned_data['item'] if self.cleaned_data['item'] else 'none',
            'data': self.cleaned_data['data'] if self.cleaned_data['data'] else 'none',
            'periodo_inicio': self.cleaned_data['periodo_inicio'] if self.cleaned_data['periodo_inicio'] else 'none',
            'periodo_fim': self.cleaned_data['periodo_fim'] if self.cleaned_data['periodo_fim'] else 'none'
        }
