from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = [
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
    ]
    
    UF_CHOICES = [
        ("RN", "Rio Grande do Norte"),
        ("CE", "Ceará"),
        ("PB", "Paraíba"),
    ]

    CURSO_CHOICES = [
        ("Alimentos", "Alimentos"),
        ("Apicultura", "Apicultura"),
        ("Informática", "Informática"),
    ]

    SERIE_CHOICES = [
        ("1º Ano", "1º Ano"),
        ("2º Ano", "2º Ano"),
        ("3º Ano", "3º Ano"),
        ("4º Ano", "4º Ano"),
    ]

    TURNO_CHOICES = [
        ("Manhã", "Manhã"),
        ("Tarde", "Tarde"),
        ("Noite", "Noite"),
        ("Integral", "Integral"),
    ]

    nome = models.CharField(max_length=150)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=10,  choices=SEXO_CHOICES)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    telefone2 = models.CharField(max_length=11, blank=True, null=True)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=250)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=80, choices=UF_CHOICES)
    matricula = models.CharField(max_length=30, unique=True)
    curso = models.CharField(max_length=150, choices=CURSO_CHOICES)
    serie = models.CharField(max_length=6, choices=SERIE_CHOICES)
    turno = models.CharField(max_length=15, choices=TURNO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"

    
