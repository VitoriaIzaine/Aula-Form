from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class detProduto(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco','foto')