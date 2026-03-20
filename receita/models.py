from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=100)
        
    def __str__(self):
        return f'{self.nome}'


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    receita = models.ManyToManyField(Receita, related_name = "ingredientes")  
    
    def __str__(self):
        return f'{self.receita} {self.ingredientes}'

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    receita = models.ManyToManyField(Receita, related_name = "utilizadores")  
    
    def __str__(self):
        return f'{self.nome} {self.receita}'

