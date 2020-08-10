from django import forms

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

    item = forms.CharField(label='Item do acervo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição do item', widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(label='Categoria do acervo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data = forms.DateField(label='Data', widget=DateInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        return self.cleaned_data['item', 'descricao', 'categoria', 'data']