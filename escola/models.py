from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    #morada = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nome}: {self.morada}'

class Turma(models.Model):
    ano = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name = "turmas") 

    def __str__(self):
        return f'{self.ano}: {self.escola}'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name = "professores") 
   # escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name = "professores") 

    def __str__(self):
        return f'{self.nome} {self.turma}'


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name = "alunos") 
    #escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return f'{self.nome} {self.idade}'
