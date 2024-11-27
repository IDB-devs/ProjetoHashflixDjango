from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

#(armazenar_no_banco_de_dados, aparecer_pro_usuario)
LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros')
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100) #campo de texto pequeno
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000) #campo de texto grande
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self): #mostra o que será exibido quando der um print na classe
        return self.titulo
    

# criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE) #oq conecta com a classe filme, cascade deleta tudo q for relativo ao Filme q foi deletado
    titulo = models.CharField(max_length=100)
    videos = models.URLField()
    
    def __str__(self): #mostra o que será exibido quando der um print na classe
        return self.filme.titulo + ' - ' + self.titulo
    
    
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')