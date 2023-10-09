from django.db import models

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.TextField(max_length=255)
    nome = models.TextField(max_length=200)
    senha = models.TextField(max_length=255)
    
class Instrutor_Parceiro(models.Model):
    cpf = models.CharField(max_length=12)
    nome = models.CharField(max_length=50)
    dt_entrada = models.DateField()
    numero_alunos = models.IntegerField()

class Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    instrutor = models.ForeignKey(Instrutor_Parceiro, on_delete=models.CASCADE)
    aluno_vinculado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20)
    dt_created = models.DateField()
