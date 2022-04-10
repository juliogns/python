from django.db import models

# Create your models here.
class Dados(models.Model):
    cpf = models.CharField(max_length=14)
    pis = models.CharField(max_length=14)

class Adr(models.Model):
    pais = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    rua = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    num = models.CharField(max_length=10)
    compl = models.CharField(max_length=20)
