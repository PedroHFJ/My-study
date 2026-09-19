from django.db import models
from django.contrib.auth.models import User

class PerfilMEI(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20)
    categoria_MEI = models.CharField(max_length=20, choices=[
        ('comercio', 'Comércio'),
        ('servico', 'Serviço'),
        ('industria', 'Indústria'),
    ])

    def __str__(self):
        return f"{self.usuario.username} ({self.categoria_MEI})"


class Despesas(models.Model):
    TIPO_CHOICE = [("fixa", "Fixa"),("variavel","Variável")]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    tipo = models.CharField(max_length=120, choices=TIPO_CHOICE)

    def __str__(self):
        return self.descricao

class TabelaDAS(models.Model):
    categoria = models.CharField(max_length=30)
    ano_vigente = models.IntegerField()
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.categoria} - {self.ano_vigente}"

class Imposto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mes_referencia = models.CharField(max_length=7)
    valor_das = models.DecimalField(max_digits=10, decimal_places=2)
    faturamento_bruto_mes = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.usuario.username}-{self.mes_referencia}"

class DreMensal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mes_referencia = models.CharField(max_length=7)
    receita_bruta = models.DecimalField(max_digits=10, decimal_places=2)
    custos_variaveis = models.DecimalField(max_digits=10, decimal_places=2)
    despesas_fixas = models.DecimalField(max_digits=10, decimal_places=2)
    lucro_liquido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DRE{self.usuario.username}- {self.mes_referencia}"


class Receita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_vendida = models.IntegerField(default=1)
    data = models.DateField()

    def __str__(self):
        return self.descricao




# Create your models here.
