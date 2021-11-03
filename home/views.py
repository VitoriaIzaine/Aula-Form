from django.db.models.signals import pre_delete
from django.shortcuts import render
from django.contrib import messages
from forms import Contato
from forms import ProdutoForm
from django.dispatch import receiver
from django.db.models import signals

from home.models import Produto


def index(request):
    form = Contato(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome_ = form.cleaned_data['nome']
            email_ = form.cleaned_data['email']
            msg_ = form.cleaned_data['msg']
            messages.sucess(request, 'Legal')
        else:
            messages.error(request, 'Não legal')
    contexto = {
        'form': form
    }

    return render(request, 'home/index.html', contexto)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Salvo')
        else:
            messages.error(request, 'Erro')
            form = ProdutoForm()
            return render(request, 'home/produto.html', {'form': form})
    else:
        form = ProdutoForm()
    dados = Produto.objects.all()
    contexto = {
        'form': form,
        'dados': dados,
    }
    return render(request, 'home/produto.html', contexto)


@receiver(pre_delete, sender=Produto)
def deletaImagem(sender, instance, **kwargs):
    instance.foto.delete(False)
