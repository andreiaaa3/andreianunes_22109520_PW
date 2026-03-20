from django.db import models

# Create your models here.
class Festival(models.Model):
    nome = models.CharField(max_length=100)
    #morada = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nome}: {self.morada}'



class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} {self.turma}'

class Banda(models.Model):
    ano = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name = "bandas") 
    festival = models.ManyToManyField(Festival, related_name = "bandas")
    def __str__(self):
        return f'{self.ano}: {self.escola}'