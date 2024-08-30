from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("cod_cliente", "nome_cliente", "cpf_cliente", "telefone01_cliente", "telefone02_cliente", "email_cliente", "senha_cliente")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cod_reserva", "qtd_pessoas", "data_reserva", "horario_reserva", "tempo_tolerancia", "cod_cliente")

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ("num_mesa", "capacidade_mesa", "descricao_mesa")

@admin.register(Possui)
class PossuiAdmin(admin.ModelAdmin):
    list_display = ("qtd_mesas_reservadas", "num_mesa", "cod_reserva")

@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ("cod_produto", "nome_produto", "descricao_produto", "preco_produto", "porc_desconto")

