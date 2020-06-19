from django import forms

class PesquisaForm(forms.Form):

    parametro = forms.CharField(label='Pesquisar um item no acervo')

    def save(self, commit=True):
        return self.cleaned_data['parametro']