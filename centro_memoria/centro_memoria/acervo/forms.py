from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class PesquisaForm(forms.Form):

    parametro = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Digite o item do acervo'}))

    def save(self, commit=True):
        return self.cleaned_data['parametro']

class PesquisaAvancadaForm(forms.Form):

    item = forms.CharField(label='Item do acervo')
    descricao = forms.CharField(label='Descrição do item')
    categoria = forms.CharField(label='Categoria do acervo')
    data = forms.DateField(label='Data', widget=DateInput)

    def save(self, commit=True):
        return self.cleaned_data['parametro']