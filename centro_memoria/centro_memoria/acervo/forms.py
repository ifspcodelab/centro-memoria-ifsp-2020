from django import forms
from .models import CategoriaAcervo, FundoColecao, Autor, AtividadeEvento, TipoDocumento, TipoSuporte

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

    categoria = forms.CharField(required=False, label='Categoria do acervo', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'categoriaDataList'}))
    fundo_colecao = forms.CharField(required=False, label='Fundo/Coleção', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'fundoDataList'}))
    autor = forms.CharField(required=False, label='Autor', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'autorDataList'}))
    titulo = forms.CharField(required=False, label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descritores = forms.CharField(required=False, label='Descritores', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_inicio = forms.IntegerField(required=False, label='Ano de edição', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ano_fim = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    periodo_inicio = forms.DateField(required=False, label='Data ou período', widget=DateInput(attrs={'class': 'form-control'}))
    periodo_fim = forms.DateField(required=False, widget=DateInput(attrs={'class': 'form-control'}))
    tipo_documento = forms.CharField(required=False, label='Tipo de Documento', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'documentoDataList'}))
    atividade = forms.CharField(required=False, label='Atividade/Evento', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'atividadeDataList'}))
    suporte = forms.CharField(required=False, label='Suporte', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'suporteDataList'}))

    field_order = ['categoria', 'fundo_colecao', 'autor', 'titulo', 'descritores', 'periodo_inicio', 'periodo_fim',
                    'ano_inicio', 'ano_fim', 'tipo_documento', 'atividade', 'suporte']
    
    def save(self, commit=True):
        return {
            'categoria': self.cleaned_data['categoria'] if self.cleaned_data['categoria'] else 'none',
            'fundo_colecao': self.cleaned_data['fundo_colecao'] if self.cleaned_data['fundo_colecao'] else 'none',
            'autor': self.cleaned_data['autor'] if self.cleaned_data['autor'] else 'none',
            'titulo': self.cleaned_data['titulo'] if self.cleaned_data['titulo'] else 'none',
            'descritores': self.cleaned_data['descritores'] if self.cleaned_data['descritores'] else 'none',
            'ano_inicio': self.cleaned_data['ano_inicio'] if self.cleaned_data['ano_inicio'] else 'none',
            'ano_fim': self.cleaned_data['ano_fim'] if self.cleaned_data['ano_fim'] else 'none',
            'periodo_inicio': self.cleaned_data['periodo_inicio'] if self.cleaned_data['periodo_inicio'] else 'none',
            'periodo_fim': self.cleaned_data['periodo_fim'] if self.cleaned_data['periodo_fim'] else 'none',
            'tipo_documento': self.cleaned_data['tipo_documento'] if self.cleaned_data['tipo_documento'] else 'none',
            'atividade': self.cleaned_data['atividade'] if self.cleaned_data['atividade'] else 'none',
            'suporte': self.cleaned_data['suporte'] if self.cleaned_data['suporte'] else 'none'
        }
