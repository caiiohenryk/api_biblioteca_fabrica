from rest_framework import viewsets # importa as viewsets
from .models import Livro, Titulo #importa a classe que criamos
from .serializers import LivroSerializer, TituloSerializer #importa a classe serializada pra json

class TituloViewSet(viewsets.ModelViewSet):
    queryset = Titulo.objects.all()

    serializer_class = TituloSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()

    serializer_class = LivroSerializer