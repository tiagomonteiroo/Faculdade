from django.db import models

# Create your models here.
class Plantel(models.Model):
    sigla = models.Choices("A","B")
    desporto = models.CharField(max_length=20)

class Jogadores(models.Model):
    numero = models.IntegerField
    nome = models.CharField(max_length=100)
    posicao = models.TextChoices("Avançado","Extermo", "Médio", "Central", "Lateral", "Guarda-Redes")
    idade = models.IntegerField

class Treinadores(models.Model):
    ID_Treinador = models.IntegerField
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    idade = models.IntegerField

class Principal(Treinadores):
    pass

class Auxiliares(Treinadores):
    pass

class Conta(models.Model):
    email = models.EmailField
    palavra_passe = models.CharField

class Utilizadores (Conta):
    pass
    N_Cliente = models.IntegerField
    nome = models.CharField(max_length=100)
    NIF = models.IntegerField
    nascimento = models.DateField

class Admin(Conta):
    pass
    N_Admin = models.IntegerField
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    ano_entrada = models.DateField

class Produtos (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=5)
    ID_prod = models.IntergerField


class Vendas(Utilizadores,Produtos):
    pass
    data = models.DateField









