from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


from django.db import models


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    nuit = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Certificado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_emissao = models.DateField()
    validade = models.DateField(blank=True, null=True)
    arquivos = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class ClienteCertificado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="certificados")
    certificado = models.ForeignKey(Certificado, on_delete=models.CASCADE, related_name="clientes")
    data_atribuicao = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("cliente", "certificado")  # evita duplicados

