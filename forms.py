from django import forms
from home.models import Produto

class Contato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    email = forms.EmailField(label='E-mail', max_length=50)
    msg = forms.CharField(label='Mensagem', max_length=100)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao','preco','quantidade','foto']