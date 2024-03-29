from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15, unique=True)
    rg = models.CharField(max_length=15, unique=True)
    sexo = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome


class Relato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=50)
    detalhes_pedido = models.TextField(max_length=200)


    def __str__(self):
        return self.pedido

class Endereco(models.Model):
    ecliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)

    def __str__(self):
        return self.rua
