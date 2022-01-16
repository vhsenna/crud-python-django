from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
