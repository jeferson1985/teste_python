from django.db import models


class LivrosBestSellers(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    em_estoque = models.PositiveIntegerField(default=1)

def __str__(self):
        return self.nome

def disponivel(self):
        return bool(self.em_estoque)


class LivrosTotal(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    em_estoque = models.PositiveIntegerField(default=1)

def __str__(self):
        return self.nome

def disponivel(self):
        return bool(self.em_estoque)