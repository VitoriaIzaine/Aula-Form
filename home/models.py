from django.db import models
from stdimage import StdImageField

class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=30)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=1)
    foto = StdImageField(
        verbose_name='Foto',
        upload_to='foto-produto',
        variations={
            'pequeno': (150,150),
            'media':(300,300)
        })
