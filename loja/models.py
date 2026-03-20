from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'
    
class Loja(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'    

class Morada(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = "moradas")  
    #loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name = "moradas")
    def __str__(self):
        return f'{self.rua} {self.numero} '

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    morada = models.ForeignKey(Morada, on_delete=models.CASCADE, related_name= "clientes")

    def __str__(self):
        return f'{self.nome} {self.apelido}' 

class Pedido(models.Model):
    numeroPedido = models.IntegerField()
    dataHora = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = "pedidos") 
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name = "pedidos")
    morada = models.ForeignKey(Morada, on_delete=models.CASCADE, related_query_name="pedidos")
    def __str__(self):
        return f'{self.cliente} {self.dataHora}'

  
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name = "produtos")  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name = "produtos")  
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name = "produtos")  

    def __str__(self):
        return f'{self.nome}'


