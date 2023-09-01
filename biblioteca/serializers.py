from rest_framework import serializers
from .models import Livro, Titulo

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'