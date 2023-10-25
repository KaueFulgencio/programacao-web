from django.db import models

# Create your models here.

class Integrante(models.Model):
    nome = models.CharField(max_length=100)
    TIPO_CHOICES = (
        ('Iniciação Científica', 'Iniciação Científica'),
        ('Mestrando', 'Mestrando'),
        ('Doutorando', 'Doutorando'),
        ('Pós-doutorando', 'Pós-doutorando'),
        ('Professor', 'Professor'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    foto = models.ImageField(upload_to='fotos/')

class Publicacao(models.Model):
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    onde_publicado = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
