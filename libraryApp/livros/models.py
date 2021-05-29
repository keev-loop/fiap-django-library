from django.db import models
from autores.models import Autor

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)
    capa = models.ImageField(upload_to='capas/%d/%m/%Y', blank=True)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
