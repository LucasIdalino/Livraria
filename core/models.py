from email.policy import default
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descrição = models.CharField(max_length=255)

    def __str__(self):
        return self.descrição


class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(models.Model):
    class Meta:
        verbose_name_plural = 'Autores'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    título = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    preço = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self):
        return '%s  (%s)' %(self.título, self.editora)


class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


    