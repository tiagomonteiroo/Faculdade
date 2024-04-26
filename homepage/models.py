from django.db import models

# Create your models here.

class Plantel(models.Model):
    SIGLA_CHOICES = (
        ("A", "A"),
        ("B", "B")
    )
    sigla = models.CharField(max_length=1, choices=SIGLA_CHOICES)
    desporto = models.CharField(max_length=20)

class Jogadores(models.Model):
    POSICAO_CHOICES = (
        ("Avançado", "Avançado"),
        ("Extermo", "Extermo"),
        ("Médio", "Médio"),
        ("Central", "Central"),
        ("Lateral", "Lateral"),
        ("Guarda-Redes", "Guarda-Redes")
    )
    numero = models.IntegerField()
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=20, choices=POSICAO_CHOICES)
    idade = models.IntegerField()

class Treinadores(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    idade = models.IntegerField()

class Principal(Treinadores):
    pass

class Auxiliares(Treinadores):
    pass

class Conta(models.Model):
    email = models.EmailField()
    palavra_passe = models.CharField(max_length=100)

class Utilizadores(Conta):
    N_Cliente = models.IntegerField()
    nome = models.CharField(max_length=100)
    NIF = models.IntegerField()
    nascimento = models.DateField()

class Admin(Conta):
    N_Admin = models.IntegerField()
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    ano_entrada = models.DateField()

class Socio(Utilizadores):
    N_Socio = models.IntegerField()
    is_socio = models.BooleanField()

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=5)
    ID_prod = models.IntegerField()

class Vendas(models.Model):
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    data = models.DateField()

class Bilhete(Produtos):
    data = models.DateField()
    lugar = models.IntegerField()
    N_Emissao = models.IntegerField()

class Merchadising(Produtos):
    tipo = models.CharField(max_length=100)








