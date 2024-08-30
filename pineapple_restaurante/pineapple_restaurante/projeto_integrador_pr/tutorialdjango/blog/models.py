from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
     

class Cliente(models.Model):
    cod_cliente = models.BigAutoField(primary_key=True, verbose_name="Código do Cliente")
    nome_cliente = models.CharField(max_length=200, verbose_name="Nome do Cliente")
    cpf_cliente = models.CharField(max_length=15, verbose_name="CPF do Cliente")
    telefone01_cliente = models.CharField(max_length=15, verbose_name="Telefone (01) do Cliente")
    telefone02_cliente = models.CharField(max_length=15, verbose_name="Telefone (02) do Cliente")
    email_cliente = models.EmailField(max_length=260, verbose_name="E-mail do Cliente")
    senha_cliente = models.CharField(max_length=20, verbose_name="Senha do Cliente")

    def __str__(self) -> str:
        return "{} ({})".format(self.cod_cliente, self.nome_cliente)


class Reserva(models.Model):
    cod_reserva = models.BigAutoField(primary_key=True, verbose_name="Código da Reserva")
    qtd_pessoas = models.IntegerField(verbose_name="Quantidade de Pessoas")
    data_reserva = models.DateField(verbose_name="Data da Reserva")
    horario_reserva = models.TimeField(verbose_name="Horário da Reserva")
    tempo_tolerancia = models.IntegerField(verbose_name="Tempo de Tolerância de Atraso")

    slug = models.SlugField(max_length=255, unique=True)
    
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return "Cód. R: {} ({})".format(self.cod_reserva, self.data_reserva)
        
    def get_absolute_url(self):
        return reverse("blog:dreserva", kwargs={"slug": self.slug})



class Mesa(models.Model):
    num_mesa = models.IntegerField(primary_key=True, verbose_name="Número da Mesa")
    capacidade_mesa = models.IntegerField(verbose_name="Capacidade de pessoas da Mesa")
    descricao_mesa = models.TextField(max_length=500, verbose_name="Descrição")

    def __str__(self) -> str:
        return "Mesa Nº{}".format(self.num_mesa)


class Possui(models.Model):
    qtd_mesas_reservadas = models.IntegerField(verbose_name="Quantidade de Mesas Reservadas")

    num_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cod_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - Mesas reservadas: {}".format(self.cod_reserva, self.qtd_mesas_reservadas)


class Cardapio(models.Model):
    cod_produto = models.BigAutoField(primary_key=True, verbose_name="Código do Produto")
    nome_produto = models.CharField(max_length=45, verbose_name="Nome do Produto")
    descricao_produto = models.TextField(max_length=600, verbose_name="Descrição do Produto")
    preco_produto = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    porc_desconto = models.IntegerField(verbose_name="Porcentagem de Desconto do Produto")

    def __str__(self) -> str:
        return "Cód.: {} ({})".format(self.cod_produto, self.nome_produto)
    
