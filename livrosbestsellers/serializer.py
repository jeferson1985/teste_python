from rest_framework import serializers

from livrosbestsellers.models import LivrosBestSellers

from livrosbestsellers.models import LivrosTotal


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivrosBestSellers
        fields = ['nome', 'categoria', 'autor', 'em_estoque']

class LivroTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivrosTotal
        fields = ['nome', 'categoria', 'autor', 'em_estoque']
