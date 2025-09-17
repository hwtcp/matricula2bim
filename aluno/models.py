from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=11, unique=True)
    telefone2 = models.CharField(max_length=11, unique=True)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=250)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.BooleanField(default=True)
    matricula = models.CharField(max_length=30)
    curso = models.CharField(max_length=150)
    serie = models.CharField(max_length=150)
    ano = models.CharField(max_length=150)
    turno = models.CharField(max_length=150)
    obersvacoes = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    
