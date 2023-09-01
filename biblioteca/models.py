from django.db import models

class Titulo(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return f'Titulo: {self.titulo}'


class Livro(models.Model):
    preco = models.CharField(max_length=10)
    autor = models.CharField(max_length=100)
    titulo = models.ForeignKey(
        Titulo,
        max_length=100,
        on_delete=models.CASCADE
    )