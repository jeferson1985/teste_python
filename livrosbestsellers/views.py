from rest_framework import viewsets

from livrosbestsellers.models import LivrosBestSellers

from livrosbestsellers.models import LivrosTotal

from livrosbestsellers.serializer import LivroSerializer, LivroTotalSerializer


class LivrosViewSet(viewsets.ModelViewSet):
    queryset = LivrosBestSellers.objects.all()
    serializer_class = LivroSerializer

class LivroTotalViewSet(viewsets.ModelViewSet):
    queryset = LivrosTotal.objects.all()
    serializer_class = LivroTotalSerializer




