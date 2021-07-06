from django.contrib import admin

from livrosbestsellers.models import LivrosBestSellers
from livrosbestsellers.models import LivrosTotal

class Livros(admin.ModelAdmin):
    list_display = ('nome','categoria', 'autor', 'em_estoque')
    list_display_links = ('nome', 'categoria')
    search_fields = ('nome',)

class LivrosGeral(admin.ModelAdmin):
    list_display = ('nome','categoria', 'autor', 'em_estoque')
    list_display_links = ('nome', 'categoria')
    search_fields = ('nome',)

admin.site.register(LivrosBestSellers, Livros)
admin.site.register(LivrosTotal, LivrosGeral)
